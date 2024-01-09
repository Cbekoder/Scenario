from django.db import models
from django.contrib.auth.models import User, AbstractUser

# class Owner(AbstractUser):
#     name = models.CharField(max_length=40)
#     company = models.CharField(max_length=50)
#     type = models.CharField(max_length=20)
#
#     first_name = None
#     last_name = None
#
#     def __str__(self):
#         return self.company

class Profile(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField()
    name = models.CharField(max_length=30)
    company = models.CharField(max_length=40)
    location = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    type = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Keywords(models.Model):
    word = models.CharField(max_length=40)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.word

class Answers(models.Model):
    answer_text = models.TextField()
    audio_link = models.URLField(blank=True)
    key_id = models.ForeignKey(Keywords, on_delete=models.CASCADE, related_name='answers')

    def __str__(self):
        return self.answer_text



