# ©AKBOTZ

import re
import aiohttp

from os import environ
from pyrogram import Client, filters
from pyrogram.types import *

API_ID = environ.get('API_ID')
API_HASH = environ.get('API_HASH')
BOT_TOKEN = environ.get('BOT_TOKEN')
API_KEY = environ.get('API_KEY')
API_URL = environ.get('API_URL')

akbotz = Client('link shortener bot',
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             workers=100)

print("Developer: @itzAbhixD , Join & Share Channel")
print("Bot is Started Now")

@akbotz.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    await message.reply(
        f"**Hi {message.chat.first_name}!**\n\n"
        "➣𝗜'𝗺 𝗘𝗮𝘀𝘆𝘀𝗸𝘆 𝗦𝗵𝗼𝗿𝘁𝗲𝗻𝗲𝗿 𝗯𝗼𝘁.\n\n ➤𝗝𝘂𝘀𝘁 𝗦𝗲𝗻𝗱 𝗠𝗲 𝗟𝗼𝗻𝗴 𝗨𝗿𝗹 𝗔𝗻𝗱 𝗚𝗲𝘁 𝗦𝗵𝗼𝗿𝘁 𝗟𝗶𝗻𝗸 \n\n**🧑‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿:** @itzAbhixD 🇮🇳")


@akbotz.on_message(filters.private & filters.text & filters.incoming)
async def link_handler(bot, message):
    link_pattern = re.compile('https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,}', re.DOTALL)
    links = re.findall(link_pattern, message.text)
    if len(links) <1:
        await message.reply("No links Found in this text",quote=True)
        return
    for link in links:
        try:
            short_link = await get_shortlink(link)
            await message.reply(f"➣ 𝗛𝗲𝗿𝗲 𝗶𝘀 𝗬𝗼𝘂𝗿 𝗦𝗵𝗼𝗿𝘁𝗲𝗻𝗲𝗱 𝗟𝗶𝗻𝗸\n\n➣ 𝗢𝗿𝗶𝗴𝗶𝗻𝗮𝗹 𝗟𝗶𝗻𝗸 : {link}\n\n➤ 𝗦𝗵𝗼𝗿𝘁𝗲𝗻𝗲𝗱 𝗟𝗶𝗻𝗸: `{short_link}`",quote=True,disable_web_page_preview=True)
        except Exception as e:
            await message.reply(f'𝐄𝐫𝐫𝐨𝐫: `{e}`', quote=True)


async def get_shortlink(link):
    url = API_URL
    params = {'api': API_KEY, 'url': link}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params, raise_for_status=True) as response:
            data = await response.json()
            return data["shortenedUrl"]


akbotz.run()
