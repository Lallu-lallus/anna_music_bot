import os
import requests
import aiohttp
import yt_dlp

from pyrogram import filters, Client
from youtube_search import YoutubeSearch

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(':'))))


@Client.on_message(filters.command('song') & ~filters.private & ~filters.channel)
def song(client, message):

    user_id = message.from_user.id 
    user_name = message.from_user.first_name 
    rpk = "["+user_name+"](tg://user?id="+str(user_id)+")"

    query = ''
    for i in message.command[1:]:
        query += ' ' + str(i)
    print(query)
    m = message.reply('๐๐ข๐ง๐๐ข๐ง๐  ๐ซ ๐๐ก๐ ๐๐จ๐ง๐  ๐ง ๐๐ซ๐จ๐ฆ Ma โค๏ธ ๐๐๐ซ๐ฏ๐๐ซ ๐...')
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        #print(results)
        title = results[0]["title"][:40]       
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f'thumb{title}.jpg'
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, 'wb').write(thumb.content)


        duration = results[0]["duration"]
        url_suffix = results[0]["url_suffix"]
        views = results[0]["views"]

    except Exception as e:
        m.edit(
            "๐๐จ๐ง๐  ๐ฅ ๐๐จ๐ญ ๐ ๐๐จ๐ฎ๐ง๐."
        )
        print(str(e))
        return
    m.edit("๐๐จ๐ฐ๐ง๐ฅ๐จ๐๐ โจ ๐๐จ๐ง๐  ๐ผ ๐๐ซ๐จ๐ฆ codes only ๐ฅ ๐๐๐ซ๐ฏ๐๐ซ ๐...")
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = '**๐ต ๐๐ฉ๐ฅ๐จ๐๐๐๐ ๐๐ฒ :- โจ @Edit_repoโค๏ธ**'
        secmul, dur, dur_arr = 1, 0, duration.split(':')
        for i in range(len(dur_arr)-1, -1, -1):
            dur += (int(dur_arr[i]) * secmul)
            secmul *= 60
        message.reply_audio(audio_file, caption=rep, thumb=thumb_name, parse_mode='md', title=title, duration=dur)
        m.delete()
    except Exception as e:
        m.edit('๐๐จ๐ฎ๐ญ๐ฎ๐๐  ๐๐ซ๐ซ๐จ๐ซ โ ๐๐จ๐ง๐ญ๐๐๐ญ ๐๐ฐ๐ง๐๐ซ ๐ฅ @pro_editor_tg โค๏ธ')
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)
