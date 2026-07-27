from datetime import datetime, timedelta

import config


def current_time():
    """
    Returns current system time.
    """
    return datetime.now().time()


def is_market_open():
    """
    Returns True if current time is between
    market open and market close.
    """

    now = datetime.now().strftime("%H:%M")

    return config.MARKET_OPEN <= now <= config.MARKET_CLOSE


def is_entry_time():
    """
    Returns True after the entry time.
    """

    now = datetime.now().strftime("%H:%M")

    return now >= config.ENTRY_TIME and now <= "14:00"


def is_exit_time():
    """
    Returns True after exit time.
    """

    now = datetime.now().strftime("%H:%M")

    return now >= config.EXIT_TIME

def is_expiry_day():
    """
    Returns True if today is betbeen monday and thursday.
    """

    return datetime.now().weekday() >= 0 and datetime.now().weekday() <= 4

def round_to_strike(price):
    """
    Rounds the spot price to the nearest strike.
    """

    step = config.STRIKE_STEP

    return round(price / step) * step


def today():
    return datetime.now().strftime("%d-%m-%Y")


def yesterday():
    return (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")

print(today())