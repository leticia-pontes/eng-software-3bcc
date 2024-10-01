from unittest import TestCase
from palavra.termo import Termo, Feedback, InvalidAttempt


class TermoTest(TestCase):

    def test_run(self):
        self.assertTrue(True)

    def test_special_characters(self):
        termo = Termo('áéíóú', {'áéíóú'})
        result = termo.test_guess('aeiou')
        expected = [
            ('á', Feedback.CORRECT_POSITION),
            ('é', Feedback.CORRECT_POSITION),
            ('í', Feedback.CORRECT_POSITION),
            ('ó', Feedback.CORRECT_POSITION),
            ('ú', Feedback.CORRECT_POSITION),
        ]
        self.assertTrue(result.win)
        self.assertListEqual(result.feedback, expected)

    def test_all_right(self):
        termo = Termo('casa', {'casa'})
        result = termo.test_guess('casa')
        expected = [
            ('c', Feedback.CORRECT_POSITION),
            ('a', Feedback.CORRECT_POSITION),
            ('s', Feedback.CORRECT_POSITION),
            ('a', Feedback.CORRECT_POSITION),
        ]
        self.assertTrue(result.win)
        self.assertListEqual(result.feedback, expected)

    def test_all_WRONG_POSITION(self):
        termo = Termo('abc', {'abc', 'cab'})
        result = termo.test_guess('cab')
        expected = [
            ('c', Feedback.WRONG_POSITION),
            ('a', Feedback.WRONG_POSITION),
            ('b', Feedback.WRONG_POSITION),
        ]
        self.assertFalse(result.win)
        self.assertListEqual(result.feedback, expected)

    def test_all_wrong(self):
        termo = Termo('casa', {'casa', 'pent'})
        result = termo.test_guess('pent')
        expected = [
            ('p', Feedback.INCORRECT),
            ('e', Feedback.INCORRECT),
            ('n', Feedback.INCORRECT),
            ('t', Feedback.INCORRECT),
        ]
        self.assertFalse(result.win)
        self.assertListEqual(result.feedback, expected)

    def test_invalid_attempt(self):
        termo = Termo('casa', {'casa', 'abc'})
        with self.assertRaises(InvalidAttempt):
            termo.test_guess('abc')

    def test_duplicated(self):
        termo = Termo('teste', {'teste', 'eeeee'})
        result = termo.test_guess('eeeee')
        expected = [
            ('e', Feedback.INCORRECT),
            ('e', Feedback.CORRECT_POSITION),
            ('e', Feedback.INCORRECT),
            ('e', Feedback.INCORRECT),
            ('e', Feedback.CORRECT_POSITION),
        ]
        self.assertEqual(result.feedback, expected)
