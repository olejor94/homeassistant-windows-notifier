# Home Assistant Windows Notifier Addon

Dette er et Home Assistant-tillegg som sender varsler til Windows.

## 📌 Installasjon
1. Legg til følgende repository i Home Assistant:
https://github.com/olejor94/homeassistant-windows-notifier

2. Installer addonen fra Home Assistant.
3. Start addonen.

## 🚀 Bruk
For å sende varsler, bruk en **REST-kommando** i Home Assistant:

```yaml
rest_command:
windows_notify:
 url: "http://homeassistant-ip:5000/notify"
 method: "post"
 content_type: "application/json"
 payload: '{"title": "Test", "message": "Dette er en test!"}'
