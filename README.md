# 🚀 Telegram Multi-Channel Bulk Post Cleaner
### ⚡ Lightning Fast Bulk Telegram Channel Cleaner (Android + Termux Optimized)

> Delete **100,000+ Telegram channel posts** safely with automatic resume, flood-wait handling, live progress tracking, and zero PC requirement.

---

## 📌 Overview

Telegram Multi-Channel Bulk Post Cleaner is a lightweight yet powerful Python utility built using **Telethon**.

It is specially designed for **Android users running Termux**, allowing you to clean multiple Telegram channels without using a computer.

Whether you have **10,000 posts or 1,000,000 posts**, the script automatically deletes them in optimized batches while respecting Telegram rate limits.

---

# ✨ Features

## ⚡ Ultra Fast Bulk Deletion

- Deletes **100 messages per API request**
- Up to **100x faster** than deleting messages one by one
- Easily handles **100K+ posts**

---

## 📂 Multi-Channel Support

Delete posts from multiple Telegram channels in a single run.

Example:

- Channel 1
- Channel 2
- Channel 3
- ...
- Channel 16

No need to restart the script for every channel.

---

## 🔄 Automatic Resume

Internet disconnected?

Phone restarted?

Termux closed accidentally?

No problem.

The script automatically saves progress inside:

```
multi_deleted_ids.txt
```

When started again it continues exactly from where it stopped.

---

## 🛡 Smart FloodWait Protection

Telegram may temporarily rate-limit deletion requests.

Instead of crashing, the script:

- Detects FloodWait automatically
- Waits required seconds
- Continues automatically

No manual work required.

---

## 📊 Live Progress Monitor

Real-time terminal display:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Current Channel
██████████████░░░░░ 72%

Deleted:
72,400

Remaining:
27,600

Speed:
100 Messages / Batch

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 📱 Android Optimized

Designed specifically for

- ✅ Android
- ✅ Termux
- ✅ Python 3

No laptop required.

---

## 💾 Lightweight

Only one dependency:

- Telethon

No database.

No Docker.

No complicated setup.

---

# 📦 Requirements

- Android Phone
- Internet Connection
- Telegram Account
- Python 3
- Termux

---

# 🛠 Installation Guide

## Step 1

Install Termux.

---

## Step 2

Allow storage permission.

```bash
termux-setup-storage
```

Press **Allow** when Android asks for permission.

---

## Step 3

Update packages.

```bash
pkg update && pkg upgrade -y
```

---

## Step 4

Install Git and Python.

```bash
pkg install git python -y
```

---

## Step 5

Install Telethon.

```bash
pip install telethon
```

---

# 📥 Clone Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>

cd <YOUR_REPOSITORY_NAME>
```

---

# ▶ Run Script

```bash
python multi_cleaner.py
```

---

# 🔐 First Login

The first launch requires Telegram authentication.

### Enter Phone Number

Example

```
+919876543210
```

---

### Enter Telegram Login Code

Telegram will send an OTP.

While typing, **nothing will appear on screen**.

This is completely normal.

Simply type the code and press Enter.

---

### Two-Step Verification

If your Telegram account has a password,

enter it when prompted.

---

# 🔋 Prevent Android From Sleeping

Large deletions may take several hours.

To prevent Android from killing Termux:

1. Start the script.

2. Pull down Notification Panel.

3. Tap

```
Acquire Wakelock
```

inside the Termux notification.

Now the script keeps running even if the screen is locked.

---

# ⚙ Configuration

Open:

```
multi_cleaner.py
```

Edit:

```python
API_ID = 12345678

API_HASH = "xxxxxxxxxxxxxxxxxxxxxxxx"

CHANNELS_LIST = [

    -1001111111111,

    -1002222222222,

    -1003333333333

]
```

### Important

Private channel IDs must begin with

```
-100
```

Do not wrap IDs in quotes.

Correct:

```python
-1001234567890
```

Wrong:

```python
"-1001234567890"
```

---

# 📁 Generated Files

During execution the script automatically creates

```
multi_deleted_ids.txt
```

Stores deleted message IDs.

Used for automatic resume.

---

# 📈 Performance

| Feature | Supported |
|----------|-----------|
| Multi Channel | ✅ |
| Batch Delete | ✅ |
| Resume | ✅ |
| FloodWait Recovery | ✅ |
| Android | ✅ |
| Termux | ✅ |
| Live Progress | ✅ |
| Auto Retry | ✅ |

---

# ⚠ Important Notes

- Only delete messages from channels you own or manage.
- Telegram API rate limits still apply.
- Do not modify the saved state file while the script is running.
- Keep your API_ID and API_HASH private.

---

# 🔒 Security

Your Telegram credentials are **never uploaded anywhere**.

Everything runs locally on your Android device.

No external servers are used.

---

# ❤️ Contributing

Pull Requests are welcome.

If you have ideas for:

- Faster deletion
- Better UI
- Performance improvements
- Bug fixes

feel free to contribute.

---

# ⭐ Support

If this project saves you hours of manual work,

please consider giving the repository a ⭐ on GitHub.

It motivates future development.

---

# 📜 License

This project is released under the MIT License.

Use responsibly and comply with Telegram's Terms of Service.

---

## 🚀 Built With

- Python
- Telethon
- Termux
- Telegram API

---

### Made with ❤️ for the Telegram Community
