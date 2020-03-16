from django.test import TestCase

from ocr_letters.models import mysqlImage


class TestModels(TestCase):

    def setUp(self):
        self.mysqlimage = mysqlImage.objects.create(
            name='bill',
            letters='dsldcvds',
        )
        self.invalidmysqlimage = mysqlImage.objects.create(
            name='',
            letters='dsldcvds',
        )

    # 测试用户名是否正确
    def test_mysqlimage_name(self):
        self.assertEquals(self.mysqlimage.name, 'bill')

    # 测试用户识别后的字母是否正确
    def test_mysqlimage_letters(self):
        self.assertEquals(self.mysqlimage.letters, 'dsldcvds')
