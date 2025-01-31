from __future__ import annotations

from databases import DatabaseURL
from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings
from starlette.datastructures import Secret

config = Config(".env")

SERVER_ADDR = config("SERVER_ADDR")
SERVER_PORT = int(v) if (v := config("SERVER_PORT", default=None)) else None

DB_DSN = config("DB_DSN", cast=DatabaseURL)
REDIS_DSN = config("REDIS_DSN")

OSU_API_KEY = config("OSU_API_KEY", cast=Secret)

DOMAIN = config("DOMAIN")

INGAME_REGISTRATION_ENABLED = config("INGAME_REGISTRATION_ENABLED", cast=bool)

COMMAND_PREFIX = config("COMMAND_PREFIX")

SEASONAL_BGS = config("SEASONAL_BGS", cast=CommaSeparatedStrings)

MENU_ICON_URL = config("MENU_ICON_URL")
MENU_ONCLICK_URL = config("MENU_ONCLICK_URL")

DATADOG_API_KEY = config("DATADOG_API_KEY", cast=Secret)
DATADOG_APP_KEY = config("DATADOG_APP_KEY", cast=Secret)

DEBUG = config("DEBUG", cast=bool)
REDIRECT_OSU_URLS = config("REDIRECT_OSU_URLS", cast=bool)

PP_CACHED_ACCURACIES = [
    int(acc) for acc in config("PP_CACHED_ACCS", cast=CommaSeparatedStrings)
]

PP_CACHED_SCORES = [
    int(score)
    for score in config(
        "PP_CACHED_SCORES",
        cast=CommaSeparatedStrings,
    )
]

AUTOFREEZE_PP = [
    int(pp)
    for pp in config(
        "AUTOFREEZE_PP",
        cast=CommaSeparatedStrings,
    )
]

AUTOBAN_PP = [
    int(pp)
    for pp in config(
        "AUTOBAN_PP",
        cast=CommaSeparatedStrings,
    )
]

DISALLOWED_NAMES: CommaSeparatedStrings = config(
    "DISALLOWED_NAMES",
    cast=CommaSeparatedStrings,
)
DISALLOWED_PASSWORDS: CommaSeparatedStrings = config(
    "DISALLOWED_PASSWORDS",
    cast=CommaSeparatedStrings,
)

PP_CACHED_SCORES = [
    int(score) for score in config("PP_CACHED_SCORES", cast=CommaSeparatedStrings)
]

DISALLOWED_NAMES = config("DISALLOWED_NAMES", cast=CommaSeparatedStrings)
DISALLOWED_PASSWORDS = config("DISALLOWED_PASSWORDS", cast=CommaSeparatedStrings)
DISALLOW_OLD_CLIENTS = config("DISALLOW_OLD_CLIENTS", cast=bool)

DISCORD_AUDIT_LOG_WEBHOOK = config("DISCORD_AUDIT_LOG_WEBHOOK")

DISCORD_OSU_CHANNEL_WEBHOOK: str = config("DISCORD_OSU_CHANNEL_WEBHOOK")

DISCORD_NOW_RANKED_WEBHOOK: str = config("DISCORD_NOW_RANKED_WEBHOOK")

DISCORD_REQUESTS_WEBHOOK: str = config("DISCORD_REQUESTS_WEBHOOK")

BOT_PREFIX: str = config("BOT_PREFIX")

BOT_TOKEN: str = config("BOT_TOKEN")

AUTOMATICALLY_REPORT_PROBLEMS = config("AUTOMATICALLY_REPORT_PROBLEMS", cast=bool)

# advanced dev settings

## WARNING touch this once you've
##          read through what it enables.
##          you could put your server at risk.
DEVELOPER_MODE = config("DEVELOPER_MODE", cast=bool)

## WARNING touch this if you know how
##          the migrations system works.
##          you'll regret it.
VERSION = "4.5.6"
