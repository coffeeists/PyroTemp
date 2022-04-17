from pyrogram import Client
from pyrogram.types import Message

import filters
import utils


app = Client(utils.BASE_DIR('configs/bot.app'),
			config_file= utils.BASE_DIR('configs/bot.ini'))


@app.on_message(filters.start_private)
async def main(cli: app, msg: Message):
	await msg.reply_text('Hello world!') # NOTE : remove this line , it's just for test bot
