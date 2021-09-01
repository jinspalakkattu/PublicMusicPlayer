import os
import re
from youtube_dl import YoutubeDL

ydl_opts = {
    "geo-bypass": True,
    "nocheckcertificate": True
}
ydl = YoutubeDL(ydl_opts)
links = []
finalurl = ""
C_PLAY = False
Y_PLAY = False
STREAM = os.environ.get("STREAM_URL", "https://youtu.be/zcrUCvBD16k")
regex = r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+"
match = re.match(regex, STREAM)
regex_ = r"http.*"
match_ = re.match(regex_, STREAM)
if match:
    meta = ydl.extract_info(STREAM, download=False)
    formats = meta.get('formats', [meta])
    for f in formats:
        links.append(f['url'])
    finalurl = links[-1]
elif STREAM.startswith("https://t.me/DumpPlaylist"):
    try:
        msg_id = STREAM.split("/", 4)[4]
        finalurl = int(msg_id)
        Y_PLAY = True
    except:
        finalurl = "https://eu10.fastcast4u.com/clubfmuae"
        print("Unable to fetch youtube playlist, starting CLUB FM")
        pass
elif match_:
    finalurl = STREAM
else:
    C_PLAY = True
    finalurl = STREAM


class Config:
    ADMIN = os.environ.get("ADMINS", '631110062')
    ADMINS = [int(admin) if re.search('^\d+$', admin) else admin for admin in (ADMIN).split()]
    API_ID = int(os.environ.get("API_ID", '3607361'))
    CHAT = int(os.environ.get("CHAT", "-1001492474364"))
    LOG_GROUP = os.environ.get("LOG_GROUP", "")
    if LOG_GROUP:
        LOG_GROUP = int(LOG_GROUP)
    else:
        LOG_GROUP = None
    STREAM_URL = finalurl
    CPLAY = C_PLAY
    YPLAY = Y_PLAY
    SHUFFLE = bool(os.environ.get("SHUFFLE", True))
    DELETE_HISTORY = bool(os.environ.get("DELETE_HISTORY", True))
    LIMIT = int(os.environ.get("LIMIT", 1500))
    ADMIN_ONLY = os.environ.get("ADMIN_ONLY", "N")
    REPLY_MESSAGE = os.environ.get("REPLY_MESSAGE", None)
    if REPLY_MESSAGE:
        REPLY_MESSAGE = REPLY_MESSAGE
    else:
        REPLY_MESSAGE = None
    EDIT_TITLE = os.environ.get("EDIT_TITLE", True)
    if EDIT_TITLE == "NO":
        EDIT_TITLE = None
    DURATION_LIMIT = int(os.environ.get("MAXIMUM_DURATION", 15))
    DELAY = int(os.environ.get("DELAY", 10))
    API_HASH = os.environ.get("API_HASH", "c57bcc4b09591db4f90f60b469e8870f")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "1992112183:AAFMs4xbUCY96P8j5yAKdeIYCUPev8PGt0c")
    SESSION = os.environ.get("SESSION_STRING", "")
    playlist = []
    msg = {}
    CONV = {}
