# Home Assistant Add-on: Telegram Replicator

## Mi ez?

Ez a Home Assistant kiegészítő lehetővé teszi a Telegram üzenetek automatikus másolását egyik csatornából a másikba. A kiegészítő teljesen integrálódik a Home Assistant-be, ami lehetővé teszi a könnyű konfigurációt a Home Assistant felhasználói felületén keresztül.

## Előfeltételek

A kiegészítő használatához a következőkre lesz szükséged:

1. Telegram API kulcsok (api_id és api_hash), amelyeket a [Telegram API Development](https://my.telegram.org/apps) oldalon igényelhetsz.
2. A forrás csatorna azonosítója, ahonnan az üzeneteket másolni szeretnéd.
3. A cél csatorna azonosítója, ahová az üzeneteket másolni szeretnéd.
4. A Telegram fiókoddal társított telefonszám.

## Konfiguráció

A kiegészítőt a telepítés után konfigurálnod kell:

1. Navigálj a **Supervisor** > **Telegram Replicator** oldalra.
2. Kattints a **Configuration** fülre.
3. Add meg a következő paramétereket:
   - `api_id`: A Telegram API ID-d.
   - `api_hash`: A Telegram API Hash-ed.
   - `source_channel`: A forrás csatorna azonosítója vagy felhasználóneve.
   - `target_channel`: A cél csatorna azonosítója vagy felhasználóneve.
   - `phone_number`: A Telegram fiókodhoz társított telefonszám teljes formátumban (pl. +36201234567).
4. Kattints a **SAVE** gombra.
5. Kattints a **START** gombra.

## Első indítás és hitelesítés

Amikor először indítod el a kiegészítőt, a Telegram hitelesítést fog kérni:

1. Ellenőrizd a kiegészítő naplóit a **Log** fülön.
2. Kövesd a naplóban megjelenő utasításokat a Telegram hitelesítéshez.
3. Ha telefonszámot kér, add meg az ellenőrző kódot, amit a Telegramtól kapsz.

A sikeres hitelesítés után a kiegészítő automatikusan elkezdi másolni az üzeneteket a forrás csatornából a cél csatornába.

## Hibaelhárítás

Ha problémákba ütközöl, ellenőrizd a következőket:

1. Biztosítsd, hogy a megadott API ID és API Hash helyes.
2. Ellenőrizd, hogy a csatorna azonosítók helyesek. Ezeket általában a `-100` előtaggal együtt kell megadni.
3. Ellenőrizd, hogy van-e jogosultságod üzeneteket küldeni a cél csatornába.
4. Nézd meg a kiegészítő naplóit a részletes hibaüzenetekért. 