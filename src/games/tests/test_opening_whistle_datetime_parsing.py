from datetime import datetime

from django.test import TestCase

from base.parsing import parse_opening_whistle


class OpeningWhistleParseTest(TestCase):
    def test_date_not_null(self):
        datetime_text = 'Sa, 09.09.17, 19:30h'

        actual = parse_opening_whistle(datetime_text)

        self.assertNotEqual(None, actual)

    def test_fixed_date(self):
        datetime_text = 'Sa, 09.09.17, 19:30h'

        actual = parse_opening_whistle(datetime_text)

        expected = datetime(2017, 9, 9, 19, 30, 0)

        self.assertEqual(expected, actual)

    def test_dynamic_date(self):
        datetime_text = 'Di, 06.03.18, 03:54h'

        actual = parse_opening_whistle(datetime_text)

        expected = datetime(2018, 3, 6, 3, 54, 0)

        self.assertEqual(expected, actual)
