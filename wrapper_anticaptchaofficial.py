from .controller import get_key # TODO remove it "." to run locally
from anticaptchaofficial import (
    imagecaptcha,
)


KEY_NAME = 'ANTI_CAPTCHA_OFFICIAL'
API_KEY  = get_key(KEY_NAME)

def imgcaptcha(img: str) -> str | None:
    solver = imagecaptcha.imagecaptcha()
    solver.set_key(API_KEY)

    captcha_text = solver.solve_and_return_solution(img)
    if captcha_text != 0:
        return captcha_text

    return None
