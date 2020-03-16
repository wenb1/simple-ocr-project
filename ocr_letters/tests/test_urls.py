from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ocr_letters.views import add


class TestUrls(SimpleTestCase):

    # 测试url
    def test_add_url_is_resolved(self):
        url = reverse('ocr_letters:add')
        self.assertEquals(resolve(url).func, add)
