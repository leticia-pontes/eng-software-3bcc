from unittest import TestCase
from termo import Termo, Feedback, InvalidAttempt


class TermoTest(TestCase):

    def test_run(self):
        self.assertTrue(True)

    def test_special_characters(self):
        termo = Termo('áéíóú', {'áéíóú'})
        result = termo.test('aeiou')
        expected = [
            ('á', Feedback.RIGHT_PLACE),
            ('é', Feedback.RIGHT_PLACE),
            ('í', Feedback.RIGHT_PLACE),
            ('ó', Feedback.RIGHT_PLACE),
            ('ú', Feedback.RIGHT_PLACE),
        ]
        self.assertTrue(result.win)
        self.assertListEqual(result.feedback, expected)

    def test_all_right(self):
        termo = Termo('casa', {'casa'})
        result = termo.test('casa')
        expected = [
            ('c', Feedback.RIGHT_PLACE),
            ('a', Feedback.RIGHT_PLACE),
            ('s', Feedback.RIGHT_PLACE),
            ('a', Feedback.RIGHT_PLACE),
        ]
        self.assertTrue(result.win)
        self.assertListEqual(result.feedback, expected)

    def test_all_wrong_place(self):
        termo = Termo('abc', {'abc', 'cab'})
        result = termo.test('cab')
        expected = [
            ('c', Feedback.WRONG_PLACE),
            ('a', Feedback.WRONG_PLACE),
            ('b', Feedback.WRONG_PLACE),
        ]
        self.assertFalse(result.win)
        self.assertListEqual(result.feedback, expected)

    def test_all_wrong(self):
        termo = Termo('casa', {'casa', 'pent'})
        result = termo.test('pent')
        expected = [
            ('p', Feedback.WRONG),
            ('e', Feedback.WRONG),
            ('n', Feedback.WRONG),
            ('t', Feedback.WRONG),
        ]
        self.assertFalse(result.win)
        self.assertListEqual(result.feedback, expected)

    def test_invalid_attempt(self):
        termo = Termo('casa', {'casa', 'abc'})
        with self.assertRaises(InvalidAttempt):
            termo.test('abc')

    def test_duplicated(self):
        termo = Termo('teste', {'teste', 'eeeee'})
        result = termo.test('eeeee')
        expected = [
            ('e', Feedback.WRONG),
            ('e', Feedback.RIGHT_PLACE),
            ('e', Feedback.WRONG),
            ('e', Feedback.WRONG),
            ('e', Feedback.RIGHT_PLACE),
        ]
        self.assertEqual(result.feedback, expected)
