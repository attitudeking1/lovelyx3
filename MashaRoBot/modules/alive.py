from telethon import events, Button, custom
import re, os
from MashaRoBot.events import register
from MashaRoBot import telethn as love
from MashaRoBot import telethn as tgbot
PHOTO = "https://telegra.ph/file/63ec234e1be1f16345e69.jpg"
@register(pattern=("/alive"))
async def awake(event):
  LOVELY = event.sender.first_name
  LOVELY = "**ðªðð¢ ðð  ð ð¥ºâ** \n\n"
  LOVELY += "**I'á´ Lá´á´ á´ÊÊð, Yá´á´Ê Há´á´Êá´Êá´á´á´â¤ï¸ð*\n\n"
  LOVELY += "**I'á´ Wá´Êá´ÉªÉ´É¢ OÉ´ Lá´á´ á´ ð**\n\n"
  LOVELY += "**MÊ Lá´á´ á´ ð¥° :**  [ ð· ÃÎÎÅÅ¦IÄâ¤ï¸ ð¸ Ä¦ÎÂ¥ÎÅ ð¹ á»®ÅÄ¦ÎÅ](t.me/TUSHAR204)\n\n"
  LOVELY += "**AÊá´á´á´ MÊ Lá´á´ á´ ð¤© :** [ãÆ¬Æ²ÖÓÆÆ¦ â Ô¼Æ êªÐÔ¼Æ³ãð®ð³](t.me/ABOUTVEDMAT)\n\n"
  BUTTON = [[Button.url("ð¦ð¨ð£ð£ð¢ð¥ð§ð", "https://t.me/LOVELYAPPEAL"), Button.url("ð¨ð£ððð§ð", "https://t.me/LOVELY_ROBOTS")]]
  await love.send_file(event.chat_id, PHOTO, caption=LOVELY,  buttons=BUTTON)
