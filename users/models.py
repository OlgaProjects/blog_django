from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name='Логин', on_delete=models.CASCADE) # юзер импортировали, если удалится юзер - удалится профиль - on_delete для этого
    avatar = models.ImageField('Аватар', default='avatar.jpg', upload_to='avatars/')

    def __str__(self): #будет возвращать объект
        return f'{self.user.username}'

    def save(self,*args, **kwargs): # для обрезки фото
        super().save(*args, **kwargs)

        image = Image.open(self.avatar.path)

        if image.height > 250 or image.width > 250:
            resize = (250,250)
            image.thumbnail(resize)
            image.save(self.avatar.path)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


