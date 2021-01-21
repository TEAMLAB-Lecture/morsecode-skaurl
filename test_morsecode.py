# -*- coding: utf8 -*-

import unittest
import morsecode as mc

from mock import patch
from io import StringIO

class TestMorseCode(unittest.TestCase):

    def test_is_help_command(self):
        self.assertTrue(mc.is_help_command("H"))
        self.assertTrue(mc.is_help_command("h"))
        self.assertTrue(mc.is_help_command("Help"))
        self.assertTrue(mc.is_help_command("heLp"))

        self.assertFalse(mc.is_help_command("xxx"))
        self.assertFalse(mc.is_help_command("gelp"))

    def test_is_validated_english_sentence(self):
        self.assertFalse(mc.is_validated_english_sentence("!_X_!"))
        self.assertFalse(mc.is_validated_english_sentence(".$."))
        self.assertFalse(mc.is_validated_english_sentence("Base_ball"))
        self.assertFalse(mc.is_validated_english_sentence("def main()"))
        self.assertFalse(mc.is_validated_english_sentence("..."))
        self.assertFalse(mc.is_validated_english_sentence(""))
        self.assertFalse(mc.is_validated_english_sentence("   "))
        self.assertFalse(mc.is_validated_english_sentence("Hello 123"))

        self.assertTrue(mc.is_validated_english_sentence("Hello World!"))
        self.assertTrue(mc.is_validated_english_sentence("!X!"))
        self.assertTrue(mc.is_validated_english_sentence("Testing started at "))
        self.assertTrue(mc.is_validated_english_sentence("Process finished with exit code"))

    def test_is_validated_morse_code(self):
        self.assertTrue(mc.is_validated_morse_code("-"))
        self.assertTrue(mc.is_validated_morse_code("-."))
        self.assertTrue(mc.is_validated_morse_code('... --- ...'))
        self.assertTrue(mc.is_validated_morse_code('.... . .-.. .-.. ---'))
        self.assertTrue(mc.is_validated_morse_code('.... ..'))

        self.assertFalse(mc.is_validated_morse_code('....... .. '))
        self.assertFalse(mc.is_validated_morse_code('lfef'))
        self.assertFalse(mc.is_validated_morse_code('.-.---.-- .---. ----'))

    def test_get_cleaned_english_sentence(self):
        test_sentence = "This is CS50."
        self.assertEqual(
            mc.get_cleaned_english_sentence(test_sentence),
            self.get_cleaned_english_sentence(test_sentence),
        )

        test_sentence = "This is CS50!!!"
        self.assertEqual(
            mc.get_cleaned_english_sentence(test_sentence),
            "This is CS50",
        )

        test_sentence = "Hello, My name is CS50?"
        self.assertEqual(
            mc.get_cleaned_english_sentence(test_sentence),
            "Hello My name is CS50",
        )

    def test_decoding_character(self):
        self.assertEqual(mc.decoding_character("-"), "T")
        self.assertEqual(mc.decoding_character(".-"), "A")
        self.assertEqual(mc.decoding_character(".-."), "R")
        self.assertEqual(mc.decoding_character("-.-"), "K")
        self.assertEqual(mc.decoding_character("..-."), "F")
        self.assertEqual(mc.decoding_character(".--."), "P")

    def test_encoding_character(self):
        self.assertEqual(mc.encoding_character("T"), "-")
        self.assertEqual(mc.encoding_character("A"), ".-")
        self.assertEqual(mc.encoding_character("R"), ".-.")
        self.assertEqual(mc.encoding_character("K"), "-.-")
        self.assertEqual(mc.encoding_character("F"), "..-.")
        self.assertEqual(mc.encoding_character("P"), ".--.")

    def test_decoding_sentence(self):
        self.assertEqual(mc.decoding_sentence("... --- ..."), "SOS")
        self.assertEqual(mc.decoding_sentence(".... . .-.. .-.. ---"), "HELLO")
        self.assertEqual(mc.decoding_sentence("--. .- -.-. .... --- -."), "GACHON")
        self.assertEqual(mc.decoding_sentence(".. -- ."), "IME")

    def test_encoding_sentence(self):
        self.assertEqual((mc.encoding_sentence("Sungchul    CHOI") ).strip(), "... ..- -. --. -.-. .... ..- .-..  -.-. .... --- ..")
        self.assertEqual((mc.encoding_sentence("GACHON UNIV.!")).strip(), "--. .- -.-. .... --- -.  ..- -. .. ...-")
        self.assertEqual((mc.encoding_sentence("HI! Fine Thank, you.")).strip(), ".... ..  ..-. .. -. .  - .... .- -. -.-  -.-- --- ..-")
        self.assertEqual((mc.encoding_sentence("WHERE ARE YOU GOING?")).strip(), ".-- .... . .-. .  .- .-. .  -.-- --- ..-  --. --- .. -. --.")

    def test_main(self):
        for x in range(50):
            with patch('builtins.input', side_effect=["0"]):
                with patch('sys.stdout', new=StringIO()) as fakeOutput:
                    mc.main()
                    console = fakeOutput.getvalue().strip().split("\n")
                    self.assertIn(console[1].upper(), "GOOD BYE")

        input_list = ["woesds.l;", "_e_we", "12434cscs21", "545caacas", "--------", "0"]
        with patch('builtins.input', side_effect=input_list):
            with patch('sys.stdout', new=StringIO()) as fakeOutput:
                mc.main()
                console = fakeOutput.getvalue().strip().split("\n")
                self.assertIn("WRONG", console[1].upper())
                self.assertIn("WRONG", console[2].upper())
                self.assertIn("WRONG", console[3].upper())
                self.assertIn("WRONG", console[4].upper())
                self.assertIn("WRONG", console[5].upper())

        print(console)

        input_list = ["Hello!!", "Hi, Gachon", "This is,! CS50", "WTF!", "--. --", "--. --.  --. -  -  -  - . . . .",
                      "::helo::", "0"]
        with patch('builtins.input', side_effect=input_list):
            with patch('sys.stdout', new=StringIO()) as fakeOutput:
                mc.main()
                console = fakeOutput.getvalue().strip().split("\n")
                self.assertIn(".... . .-.. .-.. ---", console[1].upper())
                self.assertIn(".... ..  --. .- -.-. .... --- -.", console[2].upper())
                self.assertIn("WRONG", console[3].upper())
                self.assertIn(".-- - ..-.", console[4].upper())
                self.assertIn("GM", console[5].upper())
                self.assertIn("GG GT T T TEEEE", console[6].upper())
                self.assertIn("WRONG", console[7].upper())


    def get_cleaned_english_sentence(self, raw_english_sentence):
        english_sentence = "".join([character for character in raw_english_sentence if character not in ".,!?"])
        return english_sentence

    def decoding_character(self, morse_character):
        morse_code_dict = self.get_morse_code_dict()
        for k, v in morse_code_dict.items():
            if v == morse_character:
                return k

    def encoding_character(self, english_character):
        morse_code_dict = self.get_morse_code_dict()
        return morse_code_dict[english_character.upper()]

    def decoding_sentence(self, morse_sentence):
        result = []
        for character in morse_sentence.split(" "):
            if character is not "":
                result.append(self.decoding_character(character))
            else:
                result.append("-")
        return " ".join(result).replace(" ", "").replace("-", " ")

    def encoding_sentence(self, english_sentence):
        english_sentence = self.get_cleaned_english_sentence(english_sentence)
        sentence_list = english_sentence.split()
        result = []
        for word in sentence_list:
            for character in word:
                result.append(self.encoding_character(character))
            result.append("T")
        return " ".join(result).replace("T", "")

    def get_morse_code_dict(self):
        morse_code = {
            "A": ".-", "N": "-.", "B": "-...", "O": "---", "C": "-.-.", "P": ".--.", "D": "-..", "Q": "--.-", "E": ".",
            "R": ".-.", "F": "..-.", "S": "...", "G": "--.", "T": "-", "H": "....", "U": "..-", "I": "..", "V": "...-",
            "K": "-.-", "X": "-..-", "J": ".---", "W": ".--", "L": ".-..", "Y": "-.--", "M": "--", "Z": "--.."
        }
        return morse_code
