from django.test import TestCase
from .models import Audios


class TestModels(TestCase):
    def setUp(self):
        self.audios = Audios.objects.create(
            category = "suicidal",
            title = "suicide attempt",
            audio = "suicide.mp3"
        )
        
    def test_project_is_assigned_slug_on_creation(self):
        self.assertEqual(self.audios.__str__(), 'audio/suicide.mp3')
