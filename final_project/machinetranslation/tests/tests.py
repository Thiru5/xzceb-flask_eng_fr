""" Unit tests """
import unittest
from translator import english_to_french, french_to_english

class TestEnToFr(unittest.TestCase):
    def test1(self):
        """ Unit test for English to French function"""
        self.assertIsNotNone(english_to_french("Hello")) # when non empty list of strings is sent into function should return translation and not null
        self.assertEqual(english_to_french("Hello"), "Bonjour") # should be equal


class TestFrToEn(unittest.TestCase):
    def test1(self):
        """ Unit test for French to English function"""
        self.assertIsNotNone(french_to_english("Bonjour")) # when non empty list of strings is sent into function should return translation and not null
        self.assertEqual(french_to_english("Bonjour"), "Hello") # should be equal


unittest.main()
