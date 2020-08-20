from django.test import TestCase
import json
from rest_framework.test import APIClient
from django.test import tag
class TestNaver(TestCase):
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

    def test_add_correct_without_projects(self):
        """
        Teste para adicionar um naver corretamente sem navers
        :return:
        """
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token)
        data = {
            "name": "Pedro",
            "job_role": "Developer",
            "birthdate": "1999-01-01",
            "admission_date": "2020-01-01",
        }
        response = client.post('/navers/', data)
        r = json.loads(response.content)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['name'], r["name"])
        self.assertEqual(data['job_role'], r["job_role"])
        self.assertEqual(data['birthdate'], r["birthdate"])
        self.assertEqual(data['admission_date'], r["admission_date"])


    def test_add_correct_with_projects(self):
        """
        Teste para adicionar um naver corretamente com projects
        :return:
        """
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token)
        data = {
            "name": "Pedro",
            "job_role": "Developer",
            "birthdate": "1999-01-01",
            "admission_date": "2020-01-01",
            "projects": [1,2]
        }
        response = client.post('/navers/', data)
        r = json.loads(response.content)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['name'], r["name"])
        self.assertEqual(data['job_role'], r["job_role"])
        self.assertEqual(data['birthdate'], r["birthdate"])
        self.assertEqual(data['admission_date'], r["admission_date"])
        self.assertEqual(data['admission_date'], r["admission_date"])
        self.assertEqual(data['projects'][0], 1)
        self.assertEqual(data['projects'][1], 2)

    def test_add_incorrect_without_name(self):
        """
        Teste para adicionar um naver incorretamente
        :return:
        """
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token)
        data = {
            "job_role": "Developer",
            "birthdate": "1999-01-01",
            "admission_date": "2020-01-01",
        }
        response = client.post('/navers/', data)
        r = json.loads(response.content)

        self.assertEqual(response.status_code, 400)


    def test_list_correct(self):
        """
        Teste para listar os navers corretamente
        :return:
        """
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token)
        response = client.get('/navers/')
        r = json.loads(response.content)
        self.assertGreater(len(r), 0)
        self.assertEqual(10, r[0]['id'])
        self.assertEqual("Naver 1", r[0]['name'])
        self.assertEqual("1999-01-01", r[0]['birthdate'])
        self.assertEqual('2020-01-01', r[0]['admission_date'])
        self.assertEqual('Developer', r[0]['job_role'])
        self.assertEqual(response.status_code, 200)


    def test_view_correct(self):
        """
        Teste para ver um naver corretamente
        :return:
        """
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token)
        response = client.get('/navers/10/')
        r = json.loads(response.content)
        self.assertGreater(len(r), 0)
        self.assertEqual(10, r['id'])
        self.assertEqual("Naver 1", r['name'])
        self.assertEqual("1999-01-01", r['birthdate'])
        self.assertEqual('2020-01-01', r['admission_date'])
        self.assertEqual('Developer', r['job_role'])
        self.assertEqual(1, r['projects'][0]['id'])
        self.assertEqual("Projeto 1", r['projects'][0]['name'])
        self.assertEqual(2, r['projects'][1]['id'])
        self.assertEqual("Projeto 2", r['projects'][1]['name'])

        self.assertEqual(response.status_code, 200)

    def test_edit_correct(self):
        """
        Teste para editar um naver corretamente
        :return:
        """
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token)
        data = {
            "name": "Jose",
        }
        response = client.patch('/navers/10/', data)
        r = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['name'], r["name"])


    def test_delete_correct(self):
        """
        Teste para deletar um naver corretamente
        :return:
        """
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token)
        response = client.get('/navers/10/')
        r = json.loads(response.content)
        self.assertEqual(response.status_code, 200)