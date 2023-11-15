from django.db import models


class Audios(models.Model):
    category = models.CharField(max_length=255)
    title = models.CharField(max_length=255, unique=True)
    audio = models.FileField(upload_to='audio/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"audio/{self.audio}"