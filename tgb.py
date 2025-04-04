import argparse
import asyncio
import logging
import sys
from os import getenv, path

from dotenv import load_dotenv
from telegram import Bot
from telegram.error import NetworkError, TelegramError


def check_files_exists(*files_paths: str):
    for file_path in files_paths:
        logging.info(f'Checking {file_path}')

        if not path.exists(file_path):
            logging.error(f'{file_path}: not found')
            exit(2)


async def send_files(token: str, chat_id: int, files_paths: list[str]):
    bot = Bot(token=token)

    for file_path in files_paths:
        logging.info(f'Sending {file_path}')

        try:
            with open(file_path, 'rb') as file:
                await bot.send_document(chat_id=chat_id, document=file)
                logging.info(f'{file_path}: sent!')
        except NetworkError as e:
            print(f'Network error ({file_path}): {e}')
        except TelegramError as e:
            print(f'Telegram API error ({file_path}): {e}')
        except Exception as e:
            print(f'Unexpected error ({file_path}): {e}')


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        stream=sys.stdout
    )

    parser = argparse.ArgumentParser(description='Can send any file(s) via Telegram Bot')
    parser.add_argument('-e', '--env-path', type=str, default='.env',
                        help='Path to configuration environment file (default: .env)')

    parser.add_argument('files_paths', metavar='FILE', nargs='+', type=str,
                        help="Path(s) to target file(s)")

    args = parser.parse_args()
    check_files_exists(*args.files_paths, args.env_path)

    load_dotenv(dotenv_path=args.env_path)
    logging.info('Environment loaded!')

    asyncio.run(send_files(getenv("BOT_TOKEN"), int(getenv("CHAT_ID")), args.files_paths))
