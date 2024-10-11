import os
from django.test import TestCase
from api.models import Post
from api.serializers import PostSerializer

# Definindo o ambiente de configuração do Django para os testes
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

class PostSerializerTest(TestCase):
    def setUp(self):
        # Criando um objeto Post para ser usado nos testes
        self.post = Post.objects.create(title='Test Post', content='This is a test.')

    def test_post_serializer(self):
        # Serializando o objeto Post
        serializer = PostSerializer(self.post)
        data = serializer.data

        # Verificando se todos os campos estão presentes no dicionário serializado
        expected_keys = set(['id', 'title', 'content', 'created_at'])
        self.assertEqual(set(data.keys()), expected_keys)

        # Verificando o conteúdo dos campos serializados
        self.assertEqual(data['title'], 'Test Post')
        self.assertEqual(data['content'], 'This is a test.')
