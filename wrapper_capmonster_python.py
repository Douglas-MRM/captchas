from .controller import get_key # TODO remove it "." to run locally
from capmonster_python import HCaptchaTask


KEY_NAME = 'CAPMONSTER_PYTHON'
API_KEY  = get_key(KEY_NAME)

def hcaptcha(url: str, sitekey: str, invisible: bool = False) -> str | None:
    capmonster = HCaptchaTask(API_KEY)
    task = capmonster.create_task(url, sitekey, is_invisible=invisible)

    return capmonster.join_task_result(task).get('gRecaptchaResponse')
