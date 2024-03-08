from django.db import models

# Create your models here.
class User(models.Model):
    user_nickname = models.CharField('nickname', max_length = 100, primary_key = True, default = '')
    name = models.CharField('name', max_length = 100, default = ''),
    email = models.EmailField('email', default = ''),
    age = models.IntegerField('age', default = 0),