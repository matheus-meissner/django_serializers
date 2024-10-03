from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from api.models import Post

class PostViewSetTest(APITestCase):

    def setUp(self):
        # Criando um post com caracteres sem acentos
        self.post = Post.objects.create(title='Post de teste', content='Este e um post de teste.')

    def test_list_posts(self):
        url = reverse('post-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_post(self):
        url = reverse('post-list')
        data = {
            'title': 'Novo Post',
            'content': 'Conteudo do novo post'
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
            'content': 'Conteudo atualizado'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_post(self):
        url = reverse('post-detail', args=[self.post.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class PostPaginationTest(APITestCase):
    def setUp(self):
        # Criar 15 posts para testar a paginacao
        for i in range(15):
            Post.objects.create(title=f'Post {i}', content=f'Conteudo do post {i}')

    def test_post_pagination(self):
        url = reverse('post-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 10)  # Verifica se apenas 10 itens sao retornados na primeira pagina
        self.assertIn('next', response.data)  # Verifica se existe um link para a proxima pagina
        self.assertIn('previous', response.data)  # Verifica se existe um link para a pagina anterior (neste caso deve ser None)

    def test_post_pagination_page_2(self):
        url = reverse('post-list') + '?page=2'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 5)  # Como criamos 15 posts, a segunda pagina deve ter 5 itens
