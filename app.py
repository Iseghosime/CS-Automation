import falcon
import enum
import json
from googletrans import Translator, constants


app = falcon.App()


class Language (enum.Enum):
    ENG = 1
    IGB = 2
    YRB = 3
    HSA = 4

def choose_language(lang):
    translator = Translator()
    text = ''
    print(Language.ENG.value)

    if lang == Language.ENG.value:
        # specify source language
        text = translator.translate("Hello World", dest='en').text
    elif lang == Language.IGB.value:
        text = translator.translate("Hello World", dest='ig').text
    elif lang == Language.YRB.value:
        text = translator.translate("Hello World", dest='yo').text
    elif lang == Language.HSA.value:
        text = translator.translate("Hello World", dest='ha').text
    else:
        raise falcon.HTTPBadRequest('Language is not available')

    return text

class LanguageResource:
    def on_post(self, req, res):
        body  = json.loads(req.stream.read().decode('utf-8'))
        lang = body.get('lang')
        text = choose_language(lang)
        res.body = json.dumps({"Message": text})
        res.status = falcon.HTTP_200

app.add_route('/translate', LanguageResource())