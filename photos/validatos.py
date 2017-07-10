from django.core.exceptions import ValidationError

BADWORDS = ("meapilas", "aparcabicis", "abollao", "abrazafarolas", "afinabanjos", "diseñata")

def badwords(description):
    """
    Valida que la descripción no contiene ninguna palabrota
    :return: diccionario con los datos limpios y validados
    """
    for badword in BADWORDS:
        if badword in description:
            raise ValidationError("la palabra {0} no esta permitida".format(badword))
    return True