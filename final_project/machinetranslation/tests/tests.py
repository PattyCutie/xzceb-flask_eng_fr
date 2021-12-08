'''
This is Final Assignment - Python Web Application
'''
import unittest
from translator import english_to_french # pylint: disable=import-error
from translator import french_to_english # pylint: disable=import-error
#Write at least 2 tests in tests.py for each method
class TestEnglishToFrench(unittest.TestCase):
    ''' Class 1 '''
    def test_e2f1(self):
        ''' def 1 '''
        self.assertEqual(english_to_french('Are you hungry?'),
        'As-tu faim?')
        # test case 1.
    def test_e2f2(self):
        ''' def 2 '''
        self.assertEqual(english_to_french('I have 10 euros in my pocket'),
        'J\'ai 10 euros dans ma poche')
        # test case 2.
    def test_e2f3(self):
        ''' def 3 '''
        self.assertNotEqual(english_to_french('None'), '')
        #Test for null input for english_to_french.
    def test_e2f4(self):
        ''' def 4 '''
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        #Test for the translation of the word 'Hello' and 'Bonjour'.

class TestFrenchToEnglish(unittest.TestCase):
    ''' Class 2 '''
    def test_f2e1(self):
        ''' def 5 '''
        self.assertEqual(french_to_english('As-tu faim?'),
        'Are you hungry?')
        # test case 1.
    def test_f2e2(self):
        ''' def 6 '''
        self.assertEqual(french_to_english('J\'ai 10 euros dans ma poche'),
        'I have 10 euros in my pocket')
        # test case 2
    def test_f2e3(self):
        ''' def 7 '''
        self.assertNotEqual(french_to_english('None'), '')
        # Test for null input for french_to_english
    def test_f2e4(self):
        ''' def 8 '''
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        #Test for the translation of the word 'Bonjour' and 'Hello'.

unittest.main()
