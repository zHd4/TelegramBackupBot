# Telegram Backup Bot
Script for sending files via Telegram Bot, can be used for backing (for example with cron).

## Configuration

Install requirements:

```shell
pip install -r requirements.txt
```

Create environment file (.env) with the following variables:

```dotenv
BOT_TOKEN='<your Telegram Bot token>'
CHAT_ID='<your chat id>'
```

## Usage

```texta
usage: tgb.py [-h] [-e ENV_PATH] FILE [FILE ...]

Can send any file(s) via Telegram Bot

positional arguments:
  FILE                  Path(s) to target file(s)

options:
  -h, --help            show this help message and exit
  -e ENV_PATH, --env-path ENV_PATH
                        Path to configuration environment file (default: .env)
```

## Example

```shell
python tgb.py image.jpg text.txt archive.zip database.db -e config.env
```