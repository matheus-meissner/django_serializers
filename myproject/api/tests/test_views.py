from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Post

class PostViewSetTest(APITestCase):
    
    def setUp(self):
        self.post = Post.objects.create(title='Post de teste', content='Este é um post de teste.')

    def test_list_posts(self):
        url = reverse('post-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_post(self):
        url = reverse('post-list')
        data = {
            'title': 'Novo Post',
            'content': 'Conteúdo do novo post'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_post(self):
        url = reverse('post-detail', args=[self.post.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_post(self):
        url = reverse('post-detail', args=[self.post.id])
        data = {
            'title': 'Post atualizado',
            'content': 'Conteúdo atualizado'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_post(self):
        url = reverse('post-detail', args=[self.post.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
