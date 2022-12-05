"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import json
from graphene_django.utils.testing import GraphQLTestCase
from seed.util.test_util import fill_test_database
from rest_auth.models import TokenModel
from app.models import User

class TestGraphql(GraphQLTestCase):
    GRAPHQL_URL = "/graphql"

    def setUp(self):
        fill_test_database()
        user = User.objects.all().first()
        token, created = TokenModel.objects.get_or_create(user=user)
        self.headers = {"HTTP_AUTHORIZATION": 'Token ' + token.key}
    
    def test_query_contacts(self):
        response_01 = self.query(
            '''
            {
                contacts(query: "id=1", orderBy: "id", limit: 1){
                    id
                    business
                    comment
                    lastname
                    name
                    position
                    email
                    user {
                      id
                    }
                }
            }
            ''', headers=self.headers)
        res_01 = json.loads(response_01.content)["data"]
        self.assertResponseNoErrors(response_01)
        with self.subTest():
            self.assertEqual(res_01["contacts"][0]["id"], 1)

        response_02 = self.query(
            '''
            {
                contacts{ id }
            }
            ''', headers=self.headers)
        res_02 = json.loads(response_02.content)["data"]
        self.assertResponseNoErrors(response_02)
        with self.subTest():
            self.assertEqual(res_02["contacts"][0]["id"], 1)

        response_03 = self.query(
            '''
            {
                contactPagination(pageNum: 1, pageSize: 1){
                    pageNum
                    pageSize
                    totalPages
                    totalCount
                    contacts { id }
                }
            }
            ''', headers=self.headers)
        res_03 = json.loads(response_03.content)["data"]
        self.assertResponseNoErrors(response_03)
        with self.subTest():
            self.assertEqual(res_03["contactPagination"]["totalPages"], 1)
            self.assertEqual(res_03["contactPagination"]["totalCount"], 1)
            self.assertEqual(res_03["contactPagination"]["contacts"][0]["id"], 1)

        response_04 = self.query(
            '''
            {
                contactCount(query: "id=1"){ count }
            }
            ''', headers=self.headers)
        res_04 = json.loads(response_04.content)["data"]
        self.assertResponseNoErrors(response_04)
        with self.subTest():
            self.assertEqual(res_04["contactCount"]["count"], 1)

        response_05 = self.query(
            '''
            {
                contactCount { count }
            }
            ''', headers=self.headers)
        res_05 = json.loads(response_05.content)["data"]
        self.assertResponseNoErrors(response_05)
        with self.subTest():
            self.assertEqual(res_05["contactCount"]["count"], 1)

    def test_query_contact(self):
        response = self.query(
            '''
            {
                contact(id: 1){
                    id
                    business
                    comment
                    lastname
                    name
                    position
                    email
                    user {
                      id
                    }
                }
            }
            ''', headers=self.headers)
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["contact"]["id"], 1)
    
    def test_save_contact(self):
        response = self.query(
            '''
            mutation {
                saveContact(
                    user:  1,
                    business: "",
                    comment: "",
                    lastname: "",
                    name: "",
                    position: "",
                    email: "",
                ) {
                    contact {
                        id
                        business
                        comment
                        lastname
                        name
                        position
                        email
                        user {
                          id
                        }
                    }
                }
            }
            ''', headers=self.headers)
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["saveContact"]["contact"]["id"], 2)
    
    def test_set_contact(self):
        response = self.query(
            '''
            mutation {
                setContact(id:1
                    user:  1,
                    business: "",
                    comment: "",
                    lastname: "",
                    name: "",
                    position: "",
                    email: "",

                ) {
                    contact {
                        id
                        business
                        comment
                        lastname
                        name
                        position
                        email
                        user {
                          id
                        }
                    }
                }
            }
            ''', headers=self.headers)
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["setContact"]["contact"]["id"], 1)
    
    def test_delete_contact(self):
        response = self.query(
            '''
            mutation {
                deleteContact(id:1) { id }
            }
            ''', headers=self.headers)
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["deleteContact"]["id"], 1)

    def test_query_users(self):
        response_01 = self.query(
            '''
            {
                users(query: "id=1", orderBy: "id", limit: 1){
                    id
                    username
                    firstName
                    lastName
                    email
                    isActive
                }
            }
            ''', headers=self.headers)
        res_01 = json.loads(response_01.content)["data"]
        self.assertResponseNoErrors(response_01)
        with self.subTest():
            self.assertEqual(res_01["users"][0]["id"], 1)

        response_02 = self.query(
            '''
            {
                users{ id }
            }
            ''', headers=self.headers)
        res_02 = json.loads(response_02.content)["data"]
        self.assertResponseNoErrors(response_02)
        with self.subTest():
            self.assertEqual(res_02["users"][0]["id"], 1)

        response_03 = self.query(
            '''
            {
                userPagination(pageNum: 1, pageSize: 1){
                    pageNum
                    pageSize
                    totalPages
                    totalCount
                    users { id }
                }
            }
            ''', headers=self.headers)
        res_03 = json.loads(response_03.content)["data"]
        self.assertResponseNoErrors(response_03)
        with self.subTest():
            self.assertEqual(res_03["userPagination"]["totalPages"], 1)
            self.assertEqual(res_03["userPagination"]["totalCount"], 1)
            self.assertEqual(res_03["userPagination"]["users"][0]["id"], 1)

        response_04 = self.query(
            '''
            {
                userCount(query: "id=1"){ count }
            }
            ''', headers=self.headers)
        res_04 = json.loads(response_04.content)["data"]
        self.assertResponseNoErrors(response_04)
        with self.subTest():
            self.assertEqual(res_04["userCount"]["count"], 1)

        response_05 = self.query(
            '''
            {
                userCount { count }
            }
            ''', headers=self.headers)
        res_05 = json.loads(response_05.content)["data"]
        self.assertResponseNoErrors(response_05)
        with self.subTest():
            self.assertEqual(res_05["userCount"]["count"], 1)

    def test_query_user(self):
        response = self.query(
            '''
            {
                user(id: 1){
                    id
                    username
                    firstName
                    lastName
                    email
                    isActive
                }
            }
            ''', headers=self.headers)
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["user"]["id"], 1)
    
    def test_save_user(self):
        response = self.query(
            '''
            mutation {
                saveUser(
                    username: "email@test.com",
                    firstName: "FirstName",
                    lastName: "LastName",
                    email: "email@test.com",
                    password: "pbkdf2_sha256$150000$jMOqkdOUpor5$kU/QofjBsopM+CdCnU2+pROhtnxd5CZc7NhUiXNTMc0=",
                    isActive: true,
                ) {
                    user {
                        id
                        username
                        firstName
                        lastName
                        email
                        isActive
                    }
                }
            }
            ''', headers=self.headers)
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["saveUser"]["user"]["id"], 2)
    
    def test_set_user(self):
        response = self.query(
            '''
            mutation {
                setUser(id:1
                    username: "email_1@test.com",
                    firstName: "FirstName",
                    lastName: "LastName",
                    email: "email_1@test.com",
                    password: "pbkdf2_sha256$150000$jMOqkdOUpor5$kU/QofjBsopM+CdCnU2+pROhtnxd5CZc7NhUiXNTMc0=",
                    isActive: true,

                ) {
                    user {
                        id
                        username
                        firstName
                        lastName
                        email
                        isActive
                    }
                }
            }
            ''', headers=self.headers)
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["setUser"]["user"]["id"], 1)
    
    def test_delete_user(self):
        response = self.query(
            '''
            mutation {
                deleteUser(id:1) { id }
            }
            ''', headers=self.headers)
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["deleteUser"]["id"], 1)