from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters
from utils import USERNAME, mp
from config import Config

U = USERNAME
CHAT = Config.CHAT
msg = Config.msg
HOME_TEXT = "<b>Helo, [{}](tg://user?id={})\n\nIam MusicPlayer 2.0 which plays music in Channels and Groups " \
            "24*7.\n\nI can even Stream Youtube Live in Your Voicechat.\n\nDeploy Your Own bot from source code " \
            "below.\n\nHit /help to know about available commands.</b> "
HELP = """
<b>
Use /play <song name> or use /play as a reply to an audio file or youtube link.
Use /yplay to play all the songs of a youtube playlist.
You can also use <code>/splay song name</code> to play a song from Jio Saavn or <code>/splay -a album name</code> 
to play all the songs from a jiosaavn album or /cplay <channel username or channel id> to play music from a telegram channel.</b>
**Common Commands**:
**/play**  Reply to an audio file or YouTube link to play it or use /play <song name>.
**/splay** Play music from Jio Saavn, Use /splay <song name> or <code>/splay -a album name</code> to play all the songs from that album.
**/player**  Show current playing song.
**/upload** Uploads current playing song as audio file.
**/help** Show help for commands
**/playlist** Shows the playlist.
**Admin Commands**:
**/skip** [n] ...  Skip current or n where n >= 2.
**/cplay** Play music from a channel's music files.
**/yplay** Play music from a youtube playlist.
**/join**  Join voice chat.
**/leave**  Leave current voice chat
**/shuffle** Shuffle Playlist.
**/vc**  Check which VC is joined.
**/stop**  Stop playing.
**/radio** Start Radio.
**/stopradio** Stops Radio Stream.
**/clearplaylist** Clear the playlist.
**/export** Export current playlist for future use.
**/import** Import a previously exported playlist.
**/replay**  Play from the beginning.
**/clean** Remove unused RAW PCM files.
**/pause** Pause playing.
**/resume** Resume playing.
**/volume** Change volume(0-200).
**/mute**  Mute in VC.
**/unmute**  Unmute in VC.
**/restart**  Update and restarts the Bot.
"""


@Client.on_message(filters.command(['start', f'start@{U}']))
async def start(client, message):
    buttons = [
        [
            InlineKeyboardButton('⚙️ Update Channel', url='https://t.me/subin_works'),
            InlineKeyboardButton('🧩 Source', url='https://github.com/subinps/MusicPlayer'),
        ],
        [
            InlineKeyboardButton('👨🏼‍🦯 Help', callback_data='help'),

        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    m = await message.reply(HOME_TEXT.format(message.from_user.first_name, message.from_user.id),
                            reply_markup=reply_markup)
    await mp.delete(m)
    await mp.delete(message)


@Client.on_message(filters.command(["help", f"help@{U}"]))
async def show_help(client, message):
    buttons = [
        [
            InlineKeyboardButton('⚙️ Update Channel', url='https://t.me/subin_works'),
            InlineKeyboardButton('🧩 Source', url='https://github.com/subinps/MusicPlayer'),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    if msg.get('help') is not None:
        await msg['help'].delete()
    msg['help'] = await message.reply_text(
        HELP,
        reply_markup=reply_markup
    )
    await mp.delete(message)
