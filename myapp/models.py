from django.db import models

class Article(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="Article/image")

    def __str__(self) -> str:
        return f"{self.title}"