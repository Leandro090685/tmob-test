from django.test import TestCase
from django.test import Client
from .models import Redirect

class YourTestClass(TestCase):

    def setUp(self):
        Redirect.objects.create(key=1, url="http://test_1.com", active=True)
        Redirect.objects.create(key=2, url="http://test_3.com")
        
    #test del modelo
    def test_get_redirect_ok(self):
        r1 = Redirect(key=1)
        self.assertEquals(r1.get_redirect.get("url"), "http://test_1.com")

    def test_get_redirect_is_one(self):
        r2 = Redirect(key=2)
        self.assertIsNone(r2.get_redirect)

    #test de la api
    def test_view_200(self):
        c = Client()
        response = c.get("/redirect/1")
        self.assertEquals(response.status_code, 200)

    def test_view_404(self):
        c = Client()
        response = c.get("/redirect/2")
        self.assertEquals(response.status_code, 404)