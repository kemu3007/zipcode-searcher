from django.db import models

# Create your models here.
class Address(models.Model):
    code = models.CharField('全国地方公共団体コード', max_length=20)
    old_zipcode = models.CharField('（旧）郵便番号', max_length=5)
    zipcode = models.CharField('郵便番号', max_length=7)
    prefecture = models.CharField('都道府県', max_length=128)
    city = models.CharField('市区町村名', max_length=128)
    town_area = models.CharField('町域名', max_length=128)
    prefecture_kana = models.CharField('都道府県カナ', max_length=128)
    city_kana = models.CharField('市区町村名カナ', max_length=128)
    town_area_kana = models.CharField('町域名カナ', max_length=128)