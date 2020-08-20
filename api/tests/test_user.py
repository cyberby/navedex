from django.test import TestCase
import json
class TestUser(TestCase):
    fixtures = ['User']



    def test_add_correct(self):
        """
        Testa adicionar um usuário corretamente
        :return:
        """
        data = {
            'username': 'joao',
            'password': '123456'
        }
        response = self.client.post("/users/", data)
        r = json.loads(response.content)
        self.assertEqual("joao", r['username'])
        self.assertEqual(response.status_code, 201)

    def test_add_correct_without_username(self):
        """
        Testa adicionar um usuário sem o username, esperando o erro
        :return:
        """
        data = {
            'password': '123456'
        }
        response = self.client.post("/users/", data)
        self.assertEqual(400, response.status_code)

    def test_add_correct_without_password(self):
        """
        Testa adicionar um usuário sem o password, esperando o erro
        :return:
        """
        data = {
            'username': 'pedro'
        }
        response = self.client.post("/users/", data)
        self.assertEqual(400, response.status_code)

    def test_login_correct(self):
        """
        Teste para fazer o login corretamente
        :return:
        """
        data = {
            'username': 'root',
            'password': '123456'
        }
        response = self.client.post("/accounts/login/", data)
        r = json.loads(response.content)
        self.assertNotEqual("", r['token'])
        self.assertEqual(response.status_code, 200)

    def test_login_incorrect(self):
        """
        Teste para fazer um login com erro
        :return:
        """
        data = {
            'username': 'root',
            'password': '1234567'
        }
        response = self.client.post("/accounts/login/", data)
        self.assertEqual(400, response.status_code)
