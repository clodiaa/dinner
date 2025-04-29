# import requests

# BOT_TOKEN = "7994330393:AAGdVFaEI1Ey4MTQvCJfvk4_v1BuqxCy-tM"
# CHAT_ID = "-4762617003"
# MESSAGE = "Hello! This is your daily message."

# url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
# payload = {"chat_id": CHAT_ID, "text": MESSAGE}

# response = requests.post(url, data=payload)
# print("Status:", response.status_code)
# print("Response:", response.text)


from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from datetime import date

BOT_TOKEN = "7994330393:AAGdVFaEI1Ey4MTQvCJfvk4_v1BuqxCy-tM"

def start(update: Update, context):
    today = date.today().strftime("%A, %d %B %Y")  # e.g., Monday, 29 April 2025
    person_a = "Alice"
    person_b = "Bob"
    
    # Inline buttons for Yes/No options
    keyboard = [
        [InlineKeyboardButton("✅ Yes", callback_data="person_a_yes"), InlineKeyboardButton("❌ No", callback_data="person_a_no")],
        [InlineKeyboardButton("✅ Yes", callback_data="person_b_yes"), InlineKeyboardButton("❌ No", callback_data="person_b_no")]
    ]

    # Create the markup for the inline keyboard
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Send the message with inline buttons
    update.message.reply_text(
        f"Eating dinner tonight? ({today})\n\n"
        f"{person_a}: ✅ Yes / ❌ No\n"
        f"{person_b}: ✅ Yes / ❌ No",
        reply_markup=reply_markup
    )

def button(update: Update, context):
    query = update.callback_query
    query.answer()  # Acknowledge the button click
    
    # Handle different responses
    if query.data == "person_a_yes":
        query.edit_message_text(text="Alice is having dinner tonight. ✅")
    elif query.data == "person_a_no":
        query.edit_message_text(text="Alice is not having dinner tonight. ❌")
    elif query.data == "person_b_yes":
        query.edit_message_text(text="Bob is having dinner tonight. ✅")
    elif query.data == "person_b_no":
        query.edit_message_text(text="Bob is not having dinner tonight. ❌")

def main():
    # Set up the Updater with the bot's token
    updater = Updater(BOT_TOKEN)

    # Add handlers
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
