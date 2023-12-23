# captchas

Uma biblioteca não oficial que une e simplifica as funcionalidades de resolução de CAPTCHAs das bibliotecas [anticaptchaofficial](https://pypi.org/project/anticaptchaofficial/) e [capmonster_python](https://pypi.org/project/capmonster-python/), facilitando sua utilização em projetos ao proporcionar uma interface única para acesso a esses serviços.

## Instalação da biblioteca

```bash
pip install captchas
```

## Configuração da Chave de API

Na primeira execução do seu arquivo que faz uso desta biblioteca, será solicitada a inserção da sua chave de API para poder utilizá-la. Conforme o exemplo   abaixo:

![image](https://github.com/Douglas-MRM/captchas/assets/63890669/dab877ba-ce55-43f4-a0a0-d45a04fdd26b)

Uma vez inserida, a chave será armazenada automaticamente, dispensando a necessidade de informá-la novamente posteriormente.


## Exemplo de uso

```python
from captchas.wrapper_anticaptchaofficial import imagecaptcha

captcha_text = imagecaptcha('PATH_DO_CAPTCHA')
print(captcha_text)
```

