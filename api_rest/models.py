from django.db import models

# Create your models here.
class User(models.Model):
    user_nickname = models.CharField('nickname', primary_key = True, max_length = 100, default = '')
    name = models.CharField('name', max_length = 100, default = '')
    email = models.EmailField('email', default = '')
    age = models.IntegerField('age', default = 0)

    def __str__(self):
        return f'Nickname: {self.user_nickname}\nEmail:{self.email}'