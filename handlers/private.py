from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    
    await message.reply_text(
        f"""**
HEY๐ I AM A ๐๐ฑ๐๐ฎ๐ป๐ฐ๐ฒ ๐ง๐ฒ๐น๐ฒ๐ด๐ฟ๐ฎ๐บ ๐ ๐๐๐ถ๐ฐ ๐๐ผ๐ \n๐บ๐ฅ๐๐ป ๐ข๐ป ๐ฃ๐ฟ๐ถ๐๐ฎ๐๐ฒ ๐ฉ๐ฃ๐ฆ ๐ฆ๐ฒ๐ฟ๐๐ฒ๐ฟ \n๐ผ๐๐ฒ๐ฒ๐น ๐๐ถ๐ด๐ต ๐ค๐๐ฎ๐น๐ถ๐๐ ๐ ๐๐๐ถ๐ฐ ๐๐ป ๐ฉ๐ \nโญ๐๐ฒ๐๐ฒ๐น๐ผ๐ฝ๐ฒ๐ฑ ๐๐ [Lallu](https://t.me/pro_editor_tg)**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "โฐDevโฑ", url="https://t.me/pro_editor_tg")
                  ],[
                    InlineKeyboardButton(
                        "โฐupdatesโฑ", url="https://t.me/team_annaben"
                    ),
                    InlineKeyboardButton(
                        "โฐGroupโฑ", url="https://t.me/EDIT_REPO"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "โฐSourceโฑ", url="https://github.com/Lallu-lallus/anna_music_bot"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("hexor") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**๐ ๐๐๐ถ๐ฐ ๐๐ผ๐ ๐ข๐ป๐น๐ถ๐ป๐ฒ ๐ก๐ผ๐\n๐ Lallu_tg <3**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ผ๐ฆ๐๐ฝ๐ฝ๐ผ๐ฟ๐", url="https://t.me/EDIT_REPO")
                ]
            ]
        )
   )
