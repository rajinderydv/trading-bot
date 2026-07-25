"""
from neo_api_client import NeoAPI
import pyotp
import config
import inspect

totp = pyotp.TOTP(config.TOTP_SECRET).now()

client = NeoAPI(
    consumer_key=config.ACCESS_TOKEN,
    environment="prod"
)

print("Current TOTP:", totp)

print(inspect.signature(client.quotes))
# print(inspect.signature(client.place_order))


print("NeoAPI object created successfully")
print("Current TOTP:", totp)

try:
    response = client.totp_login(
        mobile_number=config.MOBILE_NUMBER,
        ucc=config.CLIENT_ID,
        totp=totp
    )

    print("Login Response:")
    print(response['data']['token'])
except Exception as e:
    print("❌ Login Failed")
    print(e)

"""


