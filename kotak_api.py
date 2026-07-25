
import pyotp,config
from neo_api_client import NeoAPI

class KotakAPI:
    
    def __init__(self):
        self.client = NeoAPI(
            consumer_key=config.ACCESS_TOKEN,
            environment="prod"
        )

    def login(self):
        try:
            totp = pyotp.TOTP(config.TOTP_SECRET).now()
            response = self.client.totp_login(
                mobile_number=config.MOBILE_NUMBER,
                ucc=config.CLIENT_ID,
                totp=totp
            )
            # print("Login response:", response)
            totp_validation = self.client.totp_validate(mpin=config.MPIN)
            # print("totp validation response:", totp_validation)

            return totp_validation
        except Exception as e:
            print("❌ Login Failed")
            return e
    def get_spot_price(self):

        try:
            instrument = [{
                "exchange_segment" : config.EXCHANGE_SEGMENT,
                "instrument_token" : config.INSTRUMENT_TOKEN
                }]            
            # instrument = [config.EXCHANGE_SEGMENT,]
            responce = self.client.quotes(instrument_tokens=instrument,quote_type="ltp")
            return responce
        except Exception as e:
            return e
    def get_script_master(self,exchange_segment="none"):
        responce = self.client.scrip_master(exchange_segment=exchange_segment)
        return responce
        
    def get_client(self):
        return self.client