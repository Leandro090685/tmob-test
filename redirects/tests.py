from django.test import TestCase
from django.test import Client
from .models import Redirect


class YourTestClass(TestCase):
    def setUp(self):
        self.redirect_1 = Redirect.objects.create(key=1, url="http://test_1.com", active=True)
        self.redirect_2 = Redirect.objects.create(key=2, url="http://test_3.com")
        
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
    
    # test para get_redirect_db
    def test_get_redirect_db(self):
        result_1 = self.redirect_1.get_redirect_db
        result_2 = self.redirect_2.get_redirect_db

        # Verificar que los resultados son los esperados
        self.assertIsNotNone(result_1)
        self.assertEquals(result_1["key"], "1")
        self.assertEquals(result_1["url"], "http://test_1.com")
        self.assertEquals(result_1["location"], "database")