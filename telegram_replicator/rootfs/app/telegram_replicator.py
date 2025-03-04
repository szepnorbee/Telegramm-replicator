#!/usr/bin/env python3
import os
import json
import logging
from telethon import TelegramClient, events
import asyncio

# Beállítjuk a naplózást
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Konfiguráció betöltése a Home Assistant options.json fájlból
def load_config():
    with open('/data/options.json', 'r') as f:
        return json.load(f)

# Fő funkció a kliens futtatásához
async def main():
    # Konfiguráció betöltése
    config = load_config()
    
    # Telegram API adatok
    api_id = int(config.get('api_id', ''))
    api_hash = config.get('api_hash', '')
    source_channel = config.get('source_channel', '')
    target_channel = config.get('target_channel', '')
    phone_number = config.get('phone_number', '')
    
    if not api_id or not api_hash or not source_channel or not target_channel:
        logger.error("Hiányzó konfiguráció! Ellenőrizd az API ID, API Hash, forrás és cél csatorna beállításokat.")
        return
    
    # Session fájl a /data könyvtárban (ez megmarad a konténer újraindításakor is)
    session_file = '/data/telegram_session'
    
    # TelegramClient létrehozása
    client = TelegramClient(session_file, api_id, api_hash)
    
    # Üzenet kezelő a forrás csatornához
    @client.on(events.NewMessage(chats=source_channel))
    async def new_message_handler(event):
        try:
            logger.info(f"Új üzenet érkezett a forrás csatornából: {event.message.id}")
            
            # Szöveges tartalom kezelése
            message_text = event.message.message if event.message.message else ""
            
            # Média tartalom kezelése
            if event.message.media:
                logger.info("Az üzenet médiát tartalmaz, letöltés...")
                # Letöltjük a médiát egy ideiglenes fájlba
                file_path = await event.message.download_media('/tmp/')
                # Elküldjük a médiát a cél csatornába a szöveggel együtt
                await client.send_file(target_channel, file_path, caption=message_text)
                # Törölhetjük a temp fájlt
                if os.path.exists(file_path):
                    os.remove(file_path)
                logger.info(f"Média sikeresen továbbítva a cél csatornába")
            elif message_text:
                # Ha csak szöveg van, azt küldjük el
                await client.send_message(target_channel, message_text)
                logger.info(f"Szöveg sikeresen továbbítva a cél csatornába")
        
        except Exception as e:
            logger.error(f"Hiba az üzenet kezelése közben: {str(e)}")
    
    # Kapcsolódás a Telegramhoz
    await client.start(phone=phone_number)
    
    # Információs üzenet
    if await client.is_user_authorized():
        logger.info("Telegram fiók hitelesítve, a replikátor aktív!")
    else:
        logger.error("Sikertelen Telegram hitelesítés. Kérjük, ellenőrizd a beállításokat.")
        return
    
    # Futtatás a megszakításig
    await client.run_until_disconnected()

if __name__ == "__main__":
    try:
        # Event loop létrehozása és futtatása
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Telegram Replicator leállítva a felhasználó által")
    except Exception as e:
        logger.error(f"Váratlan hiba történt: {str(e)}")
        raise 