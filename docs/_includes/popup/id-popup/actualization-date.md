
Дата актуализации. Соответствует времени последней актуализации данных. Используется для того, чтобы не скачивалась информация, полученная при предыдущей проверке. Содержимое может быть указано в формате:
- `ДД.ММ.ГГГГ`;
- {% if tld == "ru" or tld == "kz" or tld == "uz" %}[UNIX‑time](https://ru.wikipedia.org/wiki/Unix-время){% endif %}{% if tld == "com" %}[UNIX‑time](https://en.wikipedia.org/wiki/Unix_time){% endif %}{% if tld == 'com.tr' %}[UNIX‑time](https://tr.wikipedia.org/wiki/Unix_zaman){% endif %} — указывается в миллисекундах от `00:00:00.000 01.01.1970`.
