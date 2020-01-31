from django.core.management.base import BaseCommand

from zipcodeSearcher.zipcode.models import Address


# BaseCommandを継承して作成
class Command(BaseCommand):
    # python manage.py help count_entryで表示されるメッセージ
    help = 'Display the number of blog articles'

    # コマンドライン引数を指定します。(argparseモジュール https://docs.python.org/2.7/library/argparse.html)
    # 今回はblog_idという名前で取得する。（引数は最低でも1個, int型）
    def add_arguments(self, parser):
        pass

    # コマンドが実行された際に呼ばれるメソッド
    def handle(self, *args, **options):
        pass