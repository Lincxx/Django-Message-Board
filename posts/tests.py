from django.test import TestCase
from .models import Post

# Create your tests here.
class PostModelTest(TestCase):

    def setUp(self):
        Post.objects.create(text='just a test')

    def text

