# 🧹 Telegram Bot Manager — Bulk Channel Post Cleaner

### ⚡ Lightning-fast bulk deletion for Telegram channels — Android + Termux optimized

> Delete **100,000+ posts** from your own Telegram channels safely — with automatic resume, FloodWait handling, and live progress tracking. No PC, no server, no Docker required.

---

## 📌 Overview

**tg_bot_manager** is a lightweight Python toolkit built on [Telethon](https://github.com/LonamiWebs/Telethon) for bulk-deleting posts from Telegram channels you own or manage.

It ships with **two separate scripts** for two separate use cases:

| Script | Use case |
|---|---|
| `private_channel_cleaner.py` | Clean **private** channels (identified by numeric channel IDs) |
| `public_channel_cleaner.py` | Clean **public** channels (identified by `@username`) |

Both scripts delete in batches of 100 messages per request, auto-resume if interrupted, and handle Telegram's rate limits (FloodWait) automatically. Built and tested for **Android + Termux**, but works on any machine with Python 3.

---

## ✨ Features

- ⚡ **Batch deletion** — 100 messages per API call instead of one-by-one
- 📂 **Multi-channel support** — process a whole list of channels in one run
- 🔄 **Automatic resume** — safe to stop and restart; already-deleted messages are tracked and skipped
- 🛡 **Smart FloodWait handling** — auto-detects rate limits, waits the required time, and continues without crashing
- 📊 **Live progress** — real-time percentage and count printed to the terminal per channel
- 📱 **Android/Termux friendly** — no laptop, no root, no external server needed
- 💾 **Zero database** — just Telethon + two plain text state files

---

## 📁 Repository Structure

```
tg_bot_manager/
├── private_channel_cleaner.py   # For private channels (numeric IDs, e.g. -1001234567890)
├── public_channel_cleaner.py    # For public channels (@username)
├── LICENSE                      # MIT License
├── .github/ISSUE_TEMPLATE/      # Bug report / feature request templates
└── README.md
```

> Note: each script generates its own state file at runtime (`multi_deleted_ids.txt` for the private script, `public_deleted_ids.txt` for the public script) — these are not part of the repo, they're created on first run.

---

## 📦 Requirements

- Python 3.7+
- A Telegram account
- [Telethon](https://pypi.org/project/Telethon/) library
- Your own Telegram **API ID** and **API Hash**

Only one external dependency:

```bash
pip install telethon
```

---

## 🔑 Getting Your Telegram API ID & Hash

Both scripts need your personal `API_ID` and `API_HASH` — these identify *your app*, not your account password.

1. Go to **[my.telegram.org](https://my.telegram.org)** and log in with your phone number.
2. Click **API Development Tools**.
3. Fill the short form (App title / Short name — anything works).
4. You'll get an **`api_id`** (number) and **`api_hash`** (string). Copy both.

⚠️ Keep these private — don't commit them to a public repo.

---

## 🛠 Installation

### Option A — Android (Termux)

```bash
# 1. Install Termux (from F-Droid, recommended over Play Store version)

# 2. Allow storage access
termux-setup-storage

# 3. Update packages
pkg update && pkg upgrade -y

# 4. Install Python & Git
pkg install python git -y

# 5. Install Telethon
pip install telethon

# 6. Clone this repo
git clone https://github.com/erpriyanshu58/tg_bot_manager.git
cd tg_bot_manager
```

### Option B — Linux / Windows / macOS (Desktop)

```bash
git clone https://github.com/erpriyanshu58/tg_bot_manager.git
cd tg_bot_manager
pip install telethon
```

---

## ⚙ Configuration

Open the script relevant to your case and edit the config block at the top.

### For Private Channels → `private_channel_cleaner.py`

```python
API_ID = 12345678
API_HASH = 'your_api_hash_here'

CHANNELS_LIST = [
    -1001111111111,
    -1002222222222,
    -1003333333333,
]
```

**Important:**
- Private channel IDs must start with `-100`.
- Do **not** wrap them in quotes — they're integers, not strings.
- ✅ Correct: `-1001234567890` — ❌ Wrong: `"-1001234567890"`

> Not sure how to find a private channel's ID? Forward any message from that channel to **[@userinfobot](https://t.me/userinfobot)** or use a similar ID-lookup bot.

### For Public Channels → `public_channel_cleaner.py`

```python
API_ID = 12345678
API_HASH = 'your_api_hash_here'

CHANNELS_LIST = [
    'my_public_channel_username_1',
    'my_public_channel_username_2',
]
```

- Usernames can be given with or without `@` — the script strips it automatically.

---

## ▶ Usage

Run whichever script matches your channel type:

```bash
# For private channels
python private_channel_cleaner.py

# For public channels
python public_channel_cleaner.py
```

---

## 🔐 First-Time Login

On the first run, Telethon needs to authenticate your account:

1. **Phone number** — enter with country code, e.g. `+919876543210`
2. **OTP code** — Telegram sends a login code; type it and press Enter (nothing will visibly appear on screen while typing — this is normal)
3. **Two-Step Verification** — if enabled on your account, enter your password when prompted

After the first successful login, a `.session` file is created and you won't need to log in again on that device.

⚠️ **Never share or commit your `.session` file** — it grants full access to your Telegram account, just like your password.

---

## 🔄 How It Works

1. The script fetches all message IDs from each channel in your list.
2. It cross-checks against the state file to skip messages already deleted in a previous run.
3. Remaining messages are deleted in batches of **100 per request**.
4. After each successful batch, the batch is logged to the state file and the script sleeps **5 seconds** before the next batch (safety buffer against rate limits).
5. If Telegram throws a `FloodWaitError`, the script automatically sleeps for the exact required duration and resumes — no manual restart needed.
6. Once a channel is fully cleaned, it moves to the next one in your list.
7. When **all** channels are done, the state file is deleted automatically.

This means you can safely close Termux, lose internet, or restart your phone mid-run — just re-run the same script and it picks up where it left off.

| Capability | Supported |
|---|:---:|
| Multi-channel processing | ✅ |
| Batch deletion (100/request) | ✅ |
| Auto-resume after interruption | ✅ |
| FloodWait auto-recovery | ✅ |
| Live progress tracking | ✅ |
| Android / Termux support | ✅ |

---

## 🔋 Keeping Termux Alive During Long Runs

Cleaning 100K+ posts can take hours. To stop Android from killing the process:

1. Start the script.
2. Pull down the notification panel.
3. Tap **Acquire Wakelock** inside the Termux notification.

The script will keep running even with the screen locked.

---

## ⚠ Important Notes & Safety

- Only run this on channels **you own or administer** — deletion is permanent and cannot be undone.
- Your Telegram credentials and session never leave your device — everything runs locally, no external server involved.
- Keep `API_ID`, `API_HASH`, and your `.session` file private — add them to `.gitignore` if you fork/modify this repo.
- Telegram's own rate limits still apply regardless of this script's batching — extremely large channels may still take significant time.
- Don't edit or delete the state file (`multi_deleted_ids.txt` / `public_deleted_ids.txt`) while a script is running.

Suggested `.gitignore` additions if you're customizing this repo:
```
*.session
*.session-journal
multi_deleted_ids.txt
public_deleted_ids.txt
```

---

## 🩺 Troubleshooting

| Issue | Likely Cause | Fix |
|---|---|---|
| `Skipping: ID ... valid nahi hai` | Wrong channel ID format | Ensure private IDs start with `-100` and are not quoted |
| `Channel nahi mila` | Wrong/misspelled public username | Double-check the `@username`, remove typos |
| Script stuck on rate limit | Telegram FloodWait triggered | This is automatic — just let it wait, don't kill the script |
| Login code not appearing while typing | Normal Termux/terminal behavior | Type the code blindly and press Enter |
| Termux killed mid-run | Android background restrictions | Use **Acquire Wakelock** (see above) |

---

## ❤️ Contributing

Pull requests are welcome! Bug report and feature request templates are already set up under `.github/ISSUE_TEMPLATE/` — use them when opening an issue.

Ideas especially welcome for:
- Faster deletion strategies
- Better CLI/progress UI
- Config via `.env` instead of hardcoded values
- Adding a `requirements.txt`

---

## 📜 License

Released under the **MIT License** — see [`LICENSE`](./LICENSE) for details.

Use responsibly and in compliance with Telegram's [Terms of Service](https://telegram.org/tos).

---

## 👤 Author

**Priyanshu Kumar**
GitHub: [@erpriyanshu58](https://github.com/erpriyanshu58)

---

### Made with ❤️ for the Telegram community
