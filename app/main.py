from telegram.ext import Updater, CommandHandler, Application
from commands import start
from db import create_db_and_tables


DB_PATH = 'dnd_db.db'

TOKEN = '7339800372:AAEGGLMbT_z8f4t70uKCWqnzHzBV8vvNksE'


def main() -> None:
    create_db_and_tables()
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    # application.add_handler(CallbackQueryHandler(show_users, pattern='show_users'))
    application.run_polling()


if __name__ == '__main__':
    main()