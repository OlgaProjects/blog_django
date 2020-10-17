from django.contrib.auth.models import User
from .models import Profile
from django.db.models.signals import post_save
from django.dispatch import receiver # декоратор

@receiver(post_save, sender=User) # отслеживаем есть ли пост сэйв, сохранился ли пост. В sender передаем user и если изменения произошли, то передаем в функцию
def create_profile(sender, instance, created, **kwargs): # sender таблица, instance новый объект который создался,created на самом деле это создалось или нет,**kwargs словарь
    if created:
        Profile.objects.create(user=instance) # подвязываем в профиль изменения, которые были в таблице юзеров

@receiver(post_save, sender=User) # отслеживает новые изменения в таблице User. Чтобы сигналы работали - ихх надо подвязать в apps.py
def save_profile(sender, instance, **kwargs):
    instance.profile.save() # если произошли изменения пересохраняем данные изменения
