import os
import re

import tabula as tabula
from django.conf import settings
from django.core.management import BaseCommand

from scorers.models import Score, Team, Player

REPORTS_DIR = settings.BASE_DIR + "/reports/"


def parse_penalty_data(text: str) -> (int, int):
    match = re.match("([0-9]+)/([0-9]+)", text)
    if match:
        return match.group(1), match.group(2)
    return 0, 0


def parse_team_names(text: str) -> (int, int):
    match = re.match("(.+) - (.+)", text)
    return match.group(1), match.group(2)


class Command(BaseCommand):
    def handle(self, *args, **options):
        Score.objects.all().delete()

        file_names = os.listdir(REPORTS_DIR)
        for file_name in file_names:
            file_path = REPORTS_DIR + file_name
            teams_pdf = tabula.read_pdf(file_path, output_format='json', encoding='cp1252',
                                        **{'pages': 1, 'lattice': True})
            team_names = teams_pdf[0]['data'][3][1]['text']
            home_team_name, guest_team_name = parse_team_names(team_names)
            scores_pdf = tabula.read_pdf(file_path, output_format='json', encoding='cp1252',
                                         **{'pages': 2, 'lattice': True})

            add_scores(scores_pdf[0], team_name=home_team_name)
            add_scores(scores_pdf[1], team_name=guest_team_name)


def add_scores(table, team_name):
    team = Team.objects.get_or_create(name=team_name)[0]
    table_rows = table['data']
    for table_row in table_rows[2:]:
        row_data = [cell['text'] for cell in table_row]
        # player_number = row_data[0]
        player_name = row_data[1]
        # player_year_of_birth = row_data[2]
        goals_total = row_data[5] or 0
        penalty_tries, penalty_goals = parse_penalty_data(row_data[6])
        # warning_time = row_data[7]
        # first_suspension_time = row_data[8]
        # second_suspension_time = row_data[9]
        # third_suspension_time = row_data[10]
        # disqualification_time = row_data[11]
        # report_time = row_data[12]
        # team_suspension_time = row_data[13]

        if not player_name:
            continue

        player = Player.objects.get_or_create(name=player_name, team=team)[0]

        Score(
            player=player,
            goals=goals_total,
            penalty_goals=penalty_goals,
        ).save()