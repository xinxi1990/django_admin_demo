

"""
批量倒入数据
"""


import csv

from django.core.management import BaseCommand
from interview.models import Candidate

class Commands(BaseCommand):
    help = '从一个CSV文件的内容中读取候选人列表，导入到数据库中'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self, *args, **options):
        path = options['path']
        with open(path,'rt') as f:
            reader = csv.reader(f, dialect='excel', delimiter=';')
            # dialect，编码风格，默认为excel的风格




