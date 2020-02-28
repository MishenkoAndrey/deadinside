from django.db import models


# Create your models here.


class Post(models.Model):
    """Модель поста."""

    content = models.TextField()
    tags = models.ManyToManyField(
        'grantfatherinside.Tag'
    )

    @property
    def tags_display(self):
        return ', '.join(self.tags.values_list('name', flat=True).all())

    def __str__(self):
        return f"{self.content}: {self.tags_display}"


class Tag(models.Model):
    """Модель тега."""

    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name
