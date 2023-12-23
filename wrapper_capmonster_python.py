from .controller import get_key # TODO remove it "." to run locally
from capmonster_python import HCaptchaTask
from capmonstercloudclient.requests import HcaptchaProxylessRequest, RecaptchaV2ProxylessRequest
from capmonstercloudclient import ClientOptions, CapMonsterClient
from asyncio import run


KEY_NAME = 'CAPMONSTER_PYTHON'
API_KEY  = get_key(KEY_NAME)

def hcaptcha(url: str, sitekey: str, invisible: bool = False) -> str | None:
    capmonster = HCaptchaTask(API_KEY)
    task = capmonster.create_task(url, sitekey, is_invisible=invisible)

    return capmonster.join_task_result(task).get('gRecaptchaResponse')

def hcaptcha2(url: str, sitekey: str) -> str | None:
    hcaptcha2request = HcaptchaProxylessRequest(websiteUrl=url, websiteKey=sitekey)

    client_options = ClientOptions(api_key=API_KEY)
    client = CapMonsterClient(options=client_options)

    async def solve_captcha():
        return await client.solve_captcha(hcaptcha2request)

    return run(solve_captcha()).get('gRecaptchaResponse')

def recaptcha_v2(url: str, sitekey: str) -> str | None:
    recaptcha2request = RecaptchaV2ProxylessRequest(websiteUrl=url, websiteKey=sitekey)

    client_options = ClientOptions(api_key=API_KEY)
    client = CapMonsterClient(options=client_options)

    async def solve_captcha():
        return await client.solve_captcha(recaptcha2request)

    return run(solve_captcha()).get('gRecaptchaResponse')
