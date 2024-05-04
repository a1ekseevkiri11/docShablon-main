from django.db import models
from django.contrib.auth.models import User

from .declination import (
    get_str_genitive
)



class Profile(models.Model):


    user = models.OneToOneField(
        User, on_delete=models.CASCADE,
    )
    first_name = models.CharField(max_length=64, null=True)
    last_name = models.CharField(max_length=64, null=True)
    patronymic = models.CharField(max_length=64, null=True)



    class Meta:
        abstract = True

    # flag for inflect
    # Именительный падеж: 'nomn'
    # Родительный падеж: 'gent'
    # Дательный падеж: 'datv'
    # Винительный падеж: 'accs'
    # Творительный падеж: 'ablt'
    # Предложный падеж: 'loct'
    
    def get_fio(self, inflect=None):
        fio = self.last_name + " " + self.first_name + " " + self.patronymic
        if inflect:
            return get_str_genitive(fio, inflect)
        return fio
    

    def get_short_fio(self, inflect=None):
        short_fio = self.last_name + " " + self.first_name[0] + ". " + self.patronymic[0] + "."
        if inflect:
            return get_str_genitive(short_fio, inflect)
        return short_fio
    

    def __str__(self):
        return self.user.username

