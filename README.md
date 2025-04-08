# Papercept Manuscript Decision Monitor

This script monitors the status of a Papercept/EMBS paper submission and sends a Telegram notification when the status changes to avoid manually checking it.

## Features

- Logs into paper submission portal.
- Scrapes and checks the current paper status.
- Sends Telegram alerts on change
- Headless browser operation (no GUI needed).

## Quick Start

### 1. Clone and Install
```bash
git clone https://github.com/yiannislevy/PaperDecisionMonitor.git
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
