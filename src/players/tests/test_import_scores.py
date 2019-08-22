from unittest.mock import Mock, patch

from django.core.management import call_command

from base.tests.model_test_case import ModelTestCase


class Forfeit(ModelTestCase):

    def test(self):
        return_code = call_command('setup', '-a', 3, '-d', 10, '-s', 2018, '-l', 35537)
        self.assertEqual(return_code, None)

        return_code = call_command('import_games', '-g', 60201)
        self.assertEqual(return_code, None)

        mock: Mock
        with patch('players.management.commands.import_reports.import_report') as mock:
            return_code = call_command('import_reports')
            self.assertEqual(return_code, None)
            mock.assert_not_called()