from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from tweets.models import Tweet

User = get_user_model()


class TweetAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.other_user = User.objects.create_user(username="other", password="pass")
        self.tweet = Tweet.objects.create(user=self.user, payload="Hello world!")
        self.base_url = "/api/v1/tweets/"

    # ----------- [GET /api/v1/tweets/] -----------
    def test_get_all_tweets(self):
        response = self.client.get(self.base_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # ----------- [POST /api/v1/tweets/] -----------
    def test_create_tweet_authenticated(self):
        self.client.login(username="testuser", password="testpass")
        data = {"payload": "New tweet!"}
        response = self.client.post(self.base_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["payload"], data["payload"])

    def test_create_tweet_unauthenticated(self):
        data = {"payload": "Should fail"}
        response = self.client.post(self.base_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # ----------- [GET /api/v1/tweets/<pk>/] -----------
    def test_get_single_tweet(self):
        url = f"{self.base_url}{self.tweet.pk}/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["payload"], self.tweet.payload)

    # ----------- [PUT /api/v1/tweets/<pk>/] -----------
    def test_update_tweet(self):
        self.client.login(username="testuser", password="testpass")
        url = f"{self.base_url}{self.tweet.pk}/"
        data = {"payload": "Updated tweet"}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["payload"], data["payload"])

    def test_update_tweet_unauthorized(self):
        self.client.login(username="other", password="pass")
        url = f"{self.base_url}{self.tweet.pk}/"
        data = {"payload": "Hacked!"}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # ----------- [DELETE /api/v1/tweets/<pk>/] -----------
    def test_delete_tweet(self):
        self.client.login(username="testuser", password="testpass")
        url = f"{self.base_url}{self.tweet.pk}/"
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_tweet_unauthorized(self):
        self.client.login(username="other", password="pass")
        url = f"{self.base_url}{self.tweet.pk}/"
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
