from rest_framework.test import APITestCase, APIRequestFactory
from .views import PostListCreateView
from django.urls import reverse
from rest_framework import status
from django.contrib.auth import get_user_model


User = get_user_model()

class HelloworldTestCase(APITestCase):
    def test_hello_world(self):
        response = self.client.get(reverse('posts_home'))

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.data["message"], "Hello world")


class PostListCreateTestCase(APITestCase):


    def setUp(self):
        self.url = reverse('list_posts')


    def authenticate(self):
        self.client.post(reverse('signup'), {
            "email": "jonathan@app.com",
            "password": "password##!123",
            "username": "jonathan"
        })

        response = self.client.post(reverse('login'), {
            "email": "jonathan@app.com",
            "password": "password##!123",
        })

        # print(response.data)

        token = response.data['tokens']['access']
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")


    def test_list_posts(self):
        response = self.client.get(self.url)


        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.data['count'], 0)
        self.assertEquals(response.data['results'], [])


    def test_post_created(self):
        self.authenticate()

        sample_data = {
            "title": "Sample title",
            "content": "Sample content"
        }
        response = self.client.post(reverse('list_posts'), sample_data)

        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(response.data["title"], sample_data["title"])


        # sample_post = {
        #     "title": "Sample post",
        #     "content": "Sample content"
        # }
        #
        # request = self.factory.post(self.url, sample_post)
        #
        # request.user = self.user
        #
        # response = self.view(request)
        #
        # self.assertEquals(response.status_code, status.HTTP_201_CREATED)