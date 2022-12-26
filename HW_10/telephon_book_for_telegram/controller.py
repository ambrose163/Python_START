import view
import model
import bot_token
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


def start():
    """Стартовая функция"""

    app = ApplicationBuilder().token(bot_token.token).build()
    app.add_handler(CommandHandler("start", view.greetings))
    app.add_handler(CommandHandler("show", view.show_book))
    app.add_handler(CommandHandler("add", view.add_contact))

    app.run_polling()

    # while True:
    #     match view.menu():
    #         case 0:
    #             break
    #         case 1:
    #             view.print_book(model.get_data())
    #         case 2:
    #             model.add_data(view.add_record())
    #         case 3:
    #             model.add_data(view.editor(model.get_data_id(view.request_id())))
    #         case 4:
    #             view.print_book(model.get_data_last_name(view.request_last_name()))