<h1>Telegram Backup Bot</h1>
<p>Script for sending files via Telegram Bot, can be used for backing (for example with cron).</p>

<h2>Usage</h2>

```text
usage: tgb.py [-h] [-e ENV_PATH] FILE [FILE ...]

Can send any file(s) via Telegram Bot

positional arguments:
  FILE                  Path(s) to target file(s)

options:
  -h, --help            show this help message and exit
  -e ENV_PATH, --env-path ENV_PATH
                        Path to configuration environment file (default: .env)
```

<h2>Example</h2>

```shell
python tgb.py image.jpg text.txt archive.zip database.db -e config.env
```