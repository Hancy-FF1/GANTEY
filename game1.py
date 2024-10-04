from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

Token: Final = '8046485121:AAEHzZGOyhESPeLbqyYivpFwqrbmVzpNdNs'
BOT_USERNAME: Final = '@Gantroxx_bot'

# Commands for telegram bot

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! Thanks for chatting with me! I am GANTROX.')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Type something, and I will respond!')

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a custom command :)')

# Responses
def handle_responses(text: str) -> str:
    processed: str = text.lower()

    if 'hello' in processed:
        return 'Hello! K Xa Khabar?'

    if 'thik xa' in processed:
        return 'Aaah'
        
    if 'GANTROX' in processed:
        return 'Kina Bolako Mero Channel Subscribe Gara Na La '
        
    if 'oee' in processed:
        return 'Kina'
        
    if 'game khelna aaija' in processed:
        return 'lala'
    
    if 'muji' in processed:
        return 'k bhan nix randi ko ban'
        
    if 'youtube name' in processed:
        return 'youtube name GANTROX ani like share and subscribe gara la'
    
    if 'can i join your guild' in processed:
        return 'yes guild id 3065361913'

    if 'topup' in processed:
        return ('PAUDEL STORE UID LIST CHEAPEST AND ROCKET SPEED✨\n'
                '25💎=25💸\n'
                '50💎=50💸\n'
                '115💎=85💸\n'
                '240💎=170💸\n'
                '355💎=255💸\n'
                '480💎=340💸\n'
                '505💎=365💸\n'
                '610💎=425💸\n'
                '725💎=510💸\n'
                '850💎=595💸\n'
                '1090💎=765💸\n'
                '1240💎=850💸\n'
                '1850💎=1275💸\n'
                '2530💎=1700💸\n'
                'WEEKLY MEMBERSHIP (450💎)=170💸\n'
                'LEVEL UP PASS (800💎)=170💸\n'
                'MONTHLY MEMBERSHIP (2400💎)=850💸\n'
                'COMBO (3050💎)=1030💸\n'
                'ALL ARE FIXED RATE💥\n'
                'NO BARGAINING❌\n'
                'NOTE: CREDIT NOT AVAILABLE ❌⚠️')
        

    return "Sorry, I didn't understand that."

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'user({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_responses(new_text)
        else:
            return  # Ignore messages that don't mention the bot
    else:
        response: str = handle_responses(text)

    print('Bot:', response)
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


if __name__ == '__main__':
    print('Starting bot...')
    app = Application.builder().token(Token).build()

    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    # Message handler
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Error handler
    app.add_error_handler(error)

    # Polling the bot
    print('Polling...')
    app.run_polling(poll_interval=3)
