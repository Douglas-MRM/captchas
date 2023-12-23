from .controller import get_key # TODO remove it "." to run locally
from anticaptchaofficial import (
    imagecaptcha,
    hcaptchaproxyless,
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

def hcaptcha(url: str, sitekey: str, invisible: bool = False) -> str | None:
    solver = hcaptchaproxyless.hCaptchaProxyless()
    solver.set_key(API_KEY)
    solver.set_website_url(url)
    solver.set_website_key(sitekey)
    solver.set_is_invisible(invisible)

    g_response = solver.solve_and_return_solution()
    if g_response != 0:
        return g_response

    return None
