from pyrogram import Client
from pyrogram.types import Message

import filters
import utils


app = Client( session_file = utils.BASE_DIR / 'configs/bot.ini',
              config_file  = utils.BASE_DIR / 'configs/bot.app')

@app.on_message(filters.private_start)
async def main(cli: app, msg: Message):
    await msg.reply_text('Hello world!') # NOTE : remove this line , it's just for test bot


if __name__ == "__main__":
    app.run()