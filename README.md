# Papercept Manuscript Decision Monitor

This script monitors the status of a Papercept/EMBS paper submission and sends a Telegram notification when the status changes to avoid manually checking it.

## Features

- Logs into paper submission portal
- Scrapes and checks the current paper status
- Sends Telegram alerts on change
- Runs headless (no GUI/browser window)

## Quick Start

### 1. Clone and Install
```bash
git clone git@github.com:yiannislevy/PaperDecisionMonitor.git
cd PaperDecisionMonitor
pip3 install -r requirements.txt
```

### 2. Set up your .env file

USERNAME=your_login_username
PASSWORD=your_login_password
START_URL=https://embs.papercept.net/conferences/scripts/start.pl <!-- Developed only for this -->
PAPER_ID=YourPaperID

BOT_TOKEN=your_telegram_bot_token
CHAT_IDS=["ID1", "ID2"]

## Telegram Bot Setup

1. Open Telegram and search for `@BotFather`.
2. Send `/start` and then` /newbot`.
3. Follow the prompts: give your bot a name and a unique username.
4. BotFather will give you a Bot Token – **copy** this.
5. Send a message to your new bot in Telegram.
6. Visit: https://api.telegram.org/bot<`YourBotToken`>/getUpdates
7. Look for "chat":{"id":123456789,...} — this is your `chat_id`.
8. Add your `BOT_TOKEN` and `CHAT_IDS` to the `.env`.

## Running the script

Simply run on your terminal:

```bash
python3 monitor.py
```

The script will start the process:

- Launch a headless chrome session.
- Log in with your credentials.
- Check the paper status every 5 minutes
- Notify you via Telegram when the status changes
- Sleep in between all steps to avoid harming the website's functionality and flagging the user.

Use responsibly.