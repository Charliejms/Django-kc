# -*_ coding: utf8 -*-
from django.core.exceptions import ValidationError

from photos.models import Photo
from django import forms

BADWORDS = ("meapilas", "aparcabicis", "abollao", "abrazafarolas", "afinabanjos", "diseñata")

class PhotoForm (forms.ModelForm):

    class Meta:
        model = Photo
        exclude = ['owner']
        fields =['name', 'license', 'visibility', 'url', 'description']