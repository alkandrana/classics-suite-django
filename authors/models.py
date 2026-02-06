from django.db import models
class Language(models.TextChoices):
    LATIN = 'LAT', 'Latin'
    GREEK = 'GRK', 'Greek'
    HEBREW = 'HEB', 'Hebrew'
    ENGLISH = 'ENG', 'English'
    SANSKRIT = 'SKR', 'Sanskrit'

# Create your models here.
class Author(models.Model):
    abbreviation = models.CharField(unique=True, max_length=5)
    name = models.CharField(max_length=50, blank=False)
    praenomen = models.CharField(max_length=50, blank=True)
    nomen = models.CharField(max_length=50, blank=True)
    cognomen = models.CharField(max_length=50, blank=True)
    language = models.CharField(max_length=3, blank=True, choices=Language.choices)

    def __str__(self):
        return self.name
class Opus(models.Model):
    abbreviation = models.CharField(max_length=10, null=False)
    title = models.CharField(max_length=255, null=False)
    dialect = models.CharField(max_length=3, blank=True, choices=Language.choices)
    author = models.ForeignKey(
        Author,
        on_delete=models.PROTECT,
        related_name='opera',
        null=True
    )
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['abbreviation', 'author'],
                name='unique_work'
            )
        ]
    def __str__(self):
        return f"{self.author.name}: {self.title}"
