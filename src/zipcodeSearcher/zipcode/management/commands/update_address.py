import pandas as pd

from django.core.management.base import BaseCommand

from zipcodeSearcher.settings import BASE_DIR
from zipcodeSearcher.zipcode.models import Address


# BaseCommandを継承して作成
class Command(BaseCommand):
    # python manage.py help count_entryで表示されるメッセージ
    help = 'reload address data from csv'

    def handle(self, *args, **options):
        df = pd.read_csv(f'{BASE_DIR}/address_data/KEN_ALL.CSV', encoding='SHIFT_JIS')
        for index, row in df.iterrows():
            Address.objects.get_or_create(
                code = row[0],
                old_zipcode = row[1],
                zipcode = row[2],
                prefecture_kana = row[3],
                city_kana = row[4],
                town_area_kana = row[5],
                prefecture = row[6],
                city = row[7],
                town_area = row[8]
            )
            print(f'\r{index}/{len(df)}', end='')
