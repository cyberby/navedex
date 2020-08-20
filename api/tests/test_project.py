from django.test import TestCase
import json
from rest_framework.test import APIClient
from django.test import tag
class TestProject(TestCase):
    fixtures = ['User', 'Project', 'Naver']

    token = ''
    def setUp(self):
        data = {
            'username': 'root',
            'password': '123456'
        }
        response = self.client.post("/accounts/login/", data)
        r = json.loads(response.content)
        self.token = r['token']


    def test_add_correct_without_navers(self):
        """
        Teste para adicionar um projeto corretamente sem navers
        :return:
        """
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token)
        data = {
            "name": "Projeto 3",
        }
        response = client.post('/projects/', data)
        r = json.loads(response.content)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['name'], r["name"])


    def test_add_correct_with_navers(self):
        """
        Teste para adicionar um projeto corretamente com navers
        :return:
        """
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token)
        data = {
            "name": "Projeto 4",
            "navers": [10,11]
        }
        response = client.post('/projects/', data)
        r = json.loads(response.content)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['name'], r["name"])
        self.assertEqual(data['navers'][0], 10)
        self.assertEqual(data['navers'][1], 11)


    def test_add_incorrect_without_name(self):
        """
        Teste para adicionar um projeto incorretamente
        :return:
        """
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token)
        data = {
            "navers": [10, 11]
        }
        response = client.post('/projects/', data)
        r = json.loads(response.content)

        self.assertEqual(response.status_code, 400)


    def test_list_correct(self):
        """
        Teste para listar os projetos corretamente
        :return:
        """
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token)
        response = client.get('/projects/')
        r = json.loads(response.content)
        self.assertGreater(len(r), 0)
        self.assertEqual(1, r[0]['id'])
        self.assertEqual("Projeto 1", r[0]['name'])
        self.assertEqual(2, r[1]['id'])
        self.assertEqual("Projeto 2", r[1]['name'])
        self.assertEqual(response.status_code, 200)


    def test_view_correct(self):
        """
        Teste para ver um projeto corretamente
        :return:
        """
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token)
        response = client.get('/projects/1/')
        r = json.loads(response.content)
        self.assertGreater(len(r), 0)
        self.assertEqual(1, r['id'])
        self.assertEqual("Projeto 1", r['name'])
        self.assertEqual(10, r['navers'][0]['id'])
        self.assertEqual("Naver 1", r['navers'][0]['name'])
        self.assertEqual("1999-01-01", r['navers'][0]['birthdate'])
        self.assertEqual("2020-01-01", r['navers'][0]['admission_date'])
        self.assertEqual("Developer", r['navers'][0]['job_role'])
        self.assertEqual(response.status_code, 200)


    def test_edit_correct(self):
        """
        Teste para editar um projeto corretamente
        :return:
        """
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token)
        data = {
            "name": "Projeto 20",
        }
        response = client.patch('/projects/1/', data)
        r = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['name'], r["name"])

    @tag('atual')
    def test_delete_correct(self):
        """
        Teste para deletar um projeto corretamente
        :return:
        """
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token)
        response = client.get('/projects/1/')
        r = json.loads(response.content)
        self.assertEqual(response.status_code, 200)