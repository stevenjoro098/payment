__author__ = 'Da Vinci'
from mpesa.api.auth import MpesaBase
def access_token():
    env = 'sandbox'
    app_key = 'cHnkwYIgBbrxlgBoneczmIJFXVm0oHky'
    app_secret = '2nHEyWSD4VjpNh2g'
    sandbox_url = 'https://sandbox.safaricom.co.ke'
    live_url = 'https://safaricom.co.ke'
    access_token = MpesaBase.authenticate(env=env,app_key=app_key,app_secret=app_secret,sandbox_url=sandbox_url,live_url=live_url)
    return print(access_token)
access_token()