if (
    spot_price > r1
    and supertrend == "Bullish"
    and not position_open
):
    # Sell ATM+50 PE

if (
    spot_price < s1
    and supertrend == "Bearish"
    and not position_open
)