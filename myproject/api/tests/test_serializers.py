from django.test import TestCase
from api.models import Post
from api.serializers import PostSerializer

class PostSerializerTest(TestCase):
    def setUp(self):
        self.post = Post.objects.create(title='Test Post', content='This is a test.')

    def test_post_serializer(self):
        serializer = PostSerializer(self.post)
        data = serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'title', 'content', 'created_at']))
        self.assertEqual(data['title'], 'Test Post')
