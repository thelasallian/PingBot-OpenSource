#Currently running on: https://www.pythonanywhere.com/user/TheLasallian/files/home/TheLasallian/Pingloi_bot.py?edit


from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

import pandas as pd
import re

# ------------------- BOT DETAILS ------------------ #
TOKEN: Final = os.getenv("TOKEN")
BOT_USERNAME: Final = os.getenv("BOT_USERNAME") 
SHEET_ID: Final = os.getenv("SHEET_ID")     
#----------------------------------------------------#

df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv")

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome! Glee says hi")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("You may edit the tags at https://docs.google.com/spreadsheets/d/1DbHfbIKEaUGtZnraOgp24gv5o2wMYrynP-Tpm3xqIrU/edit?pli=1#gid=0. This bot is a work in progress. Please send feedbacks to @gleezelluy")

async def setup_tag_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Setup Tag is already done and will be coded to the official bot.")

async def kasyaba_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if (update.message.reply_to_message.text) or (update.message.reply_to_message.caption):
        if update.message.reply_to_message.text:
            text: str = update.message.reply_to_message.text
        else:
            text: str = update.message.reply_to_message.caption
        reply: str = ""

        paragraphs = text.split("\n\n")

        for i in range(0, len(paragraphs), 1):
            reply += get_count(paragraphs[i], i+1) + " \n"
    else:
        reply = "beh i-reply mo sa tweet"

    await update.message.reply_text(reply)

def extract_words_with_at_symbol(text):
    pattern = r'(?<=@)\w+'
    words = re.findall(pattern, text)

    return words

def get_count(text, num) -> str:
    text_len = len(text)

    link_pattern = r'\b((?:https?://)?(?:(?:www\.)?(?:[\da-z\.-]+)\.(?:[a-z]{2,6})|(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)|(?:(?:[0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,7}:|(?:[0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,5}(?::[0-9a-fA-F]{1,4}){1,2}|(?:[0-9a-fA-F]{1,4}:){1,4}(?::[0-9a-fA-F]{1,4}){1,3}|(?:[0-9a-fA-F]{1,4}:){1,3}(?::[0-9a-fA-F]{1,4}){1,4}|(?:[0-9a-fA-F]{1,4}:){1,2}(?::[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:(?:(?::[0-9a-fA-F]{1,4}){1,6})|:(?:(?::[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(?::[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(?:ffff(?::0{1,4}){0,1}:){0,1}(?:(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])|(?:[0-9a-fA-F]{1,4}:){1,4}:(?:(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])))(?::[0-9]{1,4}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])?(?:/[\w\.-]*)*/?)\b'

    # Replace links with a fixed-length placeholder
    def replace_links(match):
        return "*" * (23)

    text_no_links = re.sub(link_pattern, replace_links, text)

    # Count the remaining characters
    character_count = len(text_no_links)

    text_len = character_count


    if (text_len <= 280):
        reply: str = "[T" + str(num) + "] " + str(text_len)
    else:
        reply: str = "[T" + str(num) + "] -" + str(text_len - 280)

    return reply

# Responses

def handle_response(text: str) -> str:
    processed_text: str = text.lower()

    if ('@' in processed_text):
        tags = extract_words_with_at_symbol(text)
        people = set()

        for tag in tags:
            if tag in df.columns:
                people.update(df[tag].dropna().astype(str))

        return ' '.join(people)

    return 'I do not understand what you wrote'

    '''
     if ('@merrs' in processed_text):
        regs = ' '.join(df['Regs'].dropna().astype(str))
        return regs
    '''

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    #check whether user is in group chat or private chat
    message_type: str = update.message.chat.type
    if (update.message.text):
        text: str = update.message.text
    else:
        text: str = update.message.caption

    print(f'User ({update.message.chat.id}) in {message_type}: "text"')

    #NOTE: if commented, bot does not have to be mentioned to work in a group
    '''
    if (message_type == 'group'):
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
    '''
    if ("@" in text):
        response: str = handle_response(text)

    print('Bot', response)
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()

    #Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('setup_tag', setup_tag_command))
    app.add_handler(CommandHandler('kasyaba', kasyaba_command))

    #Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    app.add_handler(MessageHandler(filters.PHOTO, handle_message))

    #Errors
    app.add_error_handler(error)

    #Polls the bot
    print('Polling...')
    app.run_polling(poll_interval=3)