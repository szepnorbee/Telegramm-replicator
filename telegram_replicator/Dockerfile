ARG BUILD_FROM=ghcr.io/home-assistant/amd64-base:latest
FROM ${BUILD_FROM}

ENV LANG C.UTF-8

# Telepítjük a szükséges csomagokat
RUN apk add --no-cache python3 py3-pip

# Python függőségek telepítése
RUN pip3 install --no-cache-dir telethon cryptg pillow

# Script fájlok másolása
COPY rootfs /

# Jogosultságok beállítása
RUN chmod a+x /etc/services.d/telegram_replicator/run
RUN chmod a+x /etc/services.d/telegram_replicator/finish 