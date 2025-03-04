ARG BUILD_FROM=ghcr.io/hassio-addons/base:12.0.0

# Alap kép beállítása
FROM ${BUILD_FROM}

# Szükséges csomagok telepítése
RUN apk add --no-cache \
    python3 \
    py3-pip \
    py3-wheel \
    gcc \
    python3-dev \
    musl-dev \
    libffi-dev \
    openssl-dev

# Python csomagok telepítése
RUN pip3 install --no-cache-dir telethon cryptg pillow

# Munkamappa beállítása
WORKDIR /app

# Scriptek másolása
COPY rootfs /

# Futtatási engedély az entrypoint scriptnek
RUN chmod a+x /etc/services.d/telegram_replicator/run

# Build argumentumok
ARG BUILD_ARCH
ARG BUILD_DATE
ARG BUILD_DESCRIPTION
ARG BUILD_NAME
ARG BUILD_REF
ARG BUILD_REPOSITORY
ARG BUILD_VERSION

# Címkék
LABEL \
    io.hass.name="${BUILD_NAME}" \
    io.hass.description="${BUILD_DESCRIPTION}" \
    io.hass.arch="${BUILD_ARCH}" \
    io.hass.type="addon" \
    io.hass.version=${BUILD_VERSION} \
    maintainer="Szép Norbert" \
    org.opencontainers.image.title="${BUILD_NAME}" \
    org.opencontainers.image.description="${BUILD_DESCRIPTION}" \
    org.opencontainers.image.vendor="Home Assistant Community Add-ons" \
    org.opencontainers.image.authors="Szép Norbert" \
    org.opencontainers.image.licenses="MIT" \
    org.opencontainers.image.url="https://github.com/szepnorbee/Telegramm-replicator" \
    org.opencontainers.image.source="https://github.com/${BUILD_REPOSITORY}" \
    org.opencontainers.image.documentation="https://github.com/${BUILD_REPOSITORY}/blob/main/README.md" \
    org.opencontainers.image.created=${BUILD_DATE} \
    org.opencontainers.image.revision=${BUILD_REF} \
    org.opencontainers.image.version=${BUILD_VERSION} 