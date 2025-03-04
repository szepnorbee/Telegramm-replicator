from telethon import TelegramClient, events
import os
import sys

# Telegram API adatok konfigurációból
api_id = int(os.environ.get('API_ID'))
api_hash = os.environ.get('API_HASH')
source_channel = os.environ.get('SOURCE_CHANNEL')
target_channel = os.environ.get('TARGET_CHANNEL')
phone_number = os.environ.get('PHONE_NUMBER')

print(f"API ID: {api_id}")
print(f"Source Channel: {source_channel}")
print(f"Target Channel: {target_channel}")

# Klienst létrehozunk
client = TelegramClient('/data/telegram_session', api_id, api_hash)

@client.on(events.NewMessage(chats=source_channel))
async def new_message_handler(event):
    # Szöveges tartalom másolása
    if event.message.message:
        await client.send_message(target_channel, event.message.message)
    
    # Ha az üzenet médiát is tartalmaz (pl. kép, videó stb.)
    if event.message.media:
        # Letöltjük a médiát egy ideiglenes fájlba
        file_path = await event.message.download_media()
        # Elküldjük a médiát a cél csatornába, opcionálisan a szövegét is mellékelve
        await client.send_file(target_channel, file_path, caption=event.message.message if event.message.message else '')

print("A script fut, figyeljük a forrás csatornát...")

# Kapcsolódunk a Telegramhoz és futtatjuk a klienst
client.start(phone=phone_number)
client.run_until_disconnected()
