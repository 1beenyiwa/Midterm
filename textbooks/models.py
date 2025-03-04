from django.db import models

class Textbook(models.Model):
    CONDITION_CHOICES = [
        ('new', 'New'),
        ('written', 'Written'),
        ('old', 'Old'),
    ]

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    edition = models.CharField(max_length=50, blank=True, null=True)
    year = models.IntegerField(null=True, blank=True)
    course_code = models.CharField(max_length=20)
    availability = models.BooleanField(default=True)
    condition = models.CharField(max_length=10, choices=CONDITION_CHOICES)

    def __str__(self):
        return self.title


