import asyncio
import os
import sys
from telethon import TelegramClient
from telethon.errors import FloodWaitError, SessionPasswordNeededError
from telethon.tl.types import Channel

# --- CONFIGURATION ---
API_ID = 12345678
API_HASH = 'xxxxxxxxxxxxxxxxxxxxx'

CHANNELS_LIST = [
    -100xxxxxxxxxx, -100xxxxxxxxxx, -100xxxxxxxxxx, -100xxxxxxxxxx,
    -100xxxxxxxxxx, -100xxxxxxxxxx, -100xxxxxxxxxx, -100xxxxxxxxxx,
    -100xxxxxxxxxx, -100xxxxxxxxxx, -100xxxxxxxxxx, -100xxxxxxxxxx,
    -100xxxxxxxxxx, -100xxxxxxxxxx, -100xxxxxxxxxx, -100xxxxxxxxxx
]
# ----------------------------------------

STATE_FILE = "multi_deleted_ids.txt"

def load_deleted_ids():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as f:
            return set(line.strip() for line in f if line.strip())
    return set()

def save_deleted_batch(channel_id, batch_ids):
    with open(STATE_FILE, "a") as f:
        for msg_id in batch_ids:
            f.write(f"{channel_id}:{msg_id}\n")

async def main():
    client = TelegramClient('multi_cleaner_session', API_ID, API_HASH)
    
    print("[*] Telegram se connect ho raha hai...")
    try:
        await client.connect()
    except Exception as e:
        print(f"[-] Network Error: {e}")
        return

    if not await client.is_user_authorized():
        phone = input("[+] Phone Number dalein (with country code): ")
        try:
            await client.send_code_request(phone)
            code = input("[+] Telegram OTP dalein: ")
            await client.sign_in(phone, code)
        except SessionPasswordNeededError:
            password = input("[+] Two-Step Verification Password: ")
            await client.sign_in(password=password)
        except Exception as e:
            print(f"[-] Auth Error: {e}")
            return

    print("[+] Login Successful!\n")
    
    already_deleted_pairs = load_deleted_ids()
    total_channels = len(CHANNELS_LIST)

    for index, target_channel in enumerate(CHANNELS_LIST, 1):
        print("="*50)
        print(f"[*] Processing Channel {index}/{total_channels} (ID: {target_channel})")
        print("="*50)

        try:
            channel = await client.get_entity(target_channel)
            if not isinstance(channel, Channel):
                print(f"[-] Skipping: ID {target_channel} valid nahi hai.")
                continue
        except Exception as e:
            print(f"[-] Skipping: Permission issue ya invalid ID. Error: {e}")
            continue

        print("[*] Posts fetch ki ja rahi hain...")
        all_messages = []
        async for message in client.iter_messages(channel):
            all_messages.append(message.id)

        total_posts = len(all_messages)
        if total_posts == 0:
            print("[+] Is channel me koi post nahi hai.")
            continue

        to_delete = [mid for mid in all_messages if f"{target_channel}:{mid}" not in already_deleted_pairs]
        
        deleted_count = total_posts - len(to_delete)
        remaining_count = len(to_delete)

        print(f"[+] Total: {total_posts} | Pehle se Deleted: {deleted_count} | Bachi hui: {remaining_count}")

        if remaining_count == 0:
            print("[+] Is channel ki saari posts deleted hain.")
            continue

        print("[*] Bulk Deletion shuru ho rahi hai (100 posts per batch)...")
        
        BATCH_SIZE = 100
        batches = [to_delete[i:i + BATCH_SIZE] for i in range(0, len(to_delete), BATCH_SIZE)]

        for batch in batches:
            while True:
                try:
                    await client.delete_messages(channel, batch)
                    save_deleted_batch(target_channel, batch)
                    
                    deleted_count += len(batch)
                    remaining_count -= len(batch)
                    
                    percentage = (deleted_count / total_posts) * 100
                    sys.stdout.write(
                        f"\rChannel {index} Progress: {percentage:.2f}% | Deleted: {deleted_count}/{total_posts}"
                    )
                    sys.stdout.flush()
                    
                    # 100 messages ke liye ek safe smart delay (5 seconds)
                    await asyncio.sleep(5.0)
                    break
                    
                except FloodWaitError as e:
                    print(f"\n[!] Rate Limit! {e.seconds} seconds ke liye ruk rahe hain...")
                    await asyncio.sleep(e.seconds)
                except Exception as e:
                    print(f"\n[-] Batch delete karne me error: {e}")
                    break
        print(f"\n\n[+] Channel {index} clean ho gaya!\n")

    print("[+++] SABHI CHANNELS SUCCESSFULLY CLEAN HO GAYE HAIN! [+++]")
    if os.path.exists(STATE_FILE):
        os.remove(STATE_FILE)

if __name__ == '__main__':
    asyncio.run(main())
