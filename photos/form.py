# -*_ coding: utf8 -*-
from django.core.exceptions import ValidationError

from photos.models import Photo
from django import forms

BADWORDS = ("meapilas", "aparcabicis", "abollao", "abrazafarolas", "afinabanjos", "diseñata")

class PhotoForm (forms.ModelForm):

    class Meta:
        model = Photo
        exclude = ['owner']

    def clean(self):
        """
        Valida que la descripción no contiene ninguna palabrota
        :return: diccionario con los datos limpios y validados
        """
        cleaner_data = super().clean()
        description = cleaner_data.get('description','')
        for badword in BADWORDS:
            if badword in description:
                raise ValidationError("la palabra {0} no esta permitida".format(badword))
        return cleaner_data