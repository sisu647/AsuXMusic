from os import getenv
from dotenv import load_dotenv

load_dotenv()

get_queue = {}


API_ID = int(getenv("API_ID", "20583077")) 
API_HASH = getenv("API_HASH", "c6a1fabd1994a2aa81e90bb5f6d896c0")
ASS_HANDLER = list(getenv("ASS_HANDLER", ".").split())
BOT_TOKEN = getenv("BOT_TOKEN", "5796457197:AAG2SGPFD0-vym3WwZHhN1C2Fjq8dz_F8xY")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "150"))
LOGGER_ID = int(getenv("LOGGER_ID", "-1001701768647"))
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Trx:trx1234@cluster0.wmgka37.mongodb.net/?retryWrites=true&w=majority")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5905205047").split()))
PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/c5952790fa8235f499749.jpg")
START_IMG = getenv("START_IMG","https://te.legra.ph/file/238d26f5188c9056b307b.jpg")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/AbishnoiMF")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Abishnoi_bots")
STRING_SESSION = getenv("STRING_SESSION", "BQCm1o1gF0UKto24m8wAVY_hBo5rICM8a3TS5yYLomjeHvLWSFsOihFGgo7S3NZWVtwuJK8LqvDNn2pno75ncwx1sKu9_0NMlgFZV85psZ6WGUoXaoTkg2HQ_k9pp4AZeUZTAfKUOqmiOpidQht8u-go4Jpc4fAibDtZ6IT8Hs8zJJOsw9v2hQB-qbQeta0g97W9gnJW6FF58P3O10PSwURPfYfRbAspKcdsjHiCSa_j-TWCPWU24kpO3_tchJ5qSavvnwberzpu6wLXbN13j2sheX6Hl0id5jz_OQUSFfFekuxlqDFAHkK-kzPi40I0FvY3gie6QhJboSsWnDO7XJ5RePEpQgA")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5905205047").split()))
