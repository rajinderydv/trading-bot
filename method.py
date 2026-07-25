from neo_api_client import NeoAPI
import config

client = NeoAPI(
    consumer_key=config.ACCESS_TOKEN,
    environment="prod"
)

for method in dir(client):
    if not method.startswith("_"):
        print(method)