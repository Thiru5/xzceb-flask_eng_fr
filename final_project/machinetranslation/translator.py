"""Module providing Function to translate english-french"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']



authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)



def english_to_french(english_text):
    """To Translate English to French"""
    if english_text != "\n":
        french_text = language_translator.translate(
        text = english_text,
        model_id = "en-fr",
        source= "en",
        target = "fr",
        ).get_result()

    return french_text["translations"][0]["translation"]

print(english_to_french("Hello"))



def french_to_english(french_text):
    """To Translate French to English """
    if french_text != "\n":
        english_text = language_translator.translate(
        text = french_text,
        model_id= "fr-en",
        source = "fr",
        target = "en",
        ).get_result()

    return english_text["translations"][0]["translation"]

print(french_to_english("Bonjour"))
