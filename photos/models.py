from django.db import models

# Create your models here.

class Photo(models.Model):

    COPYRIGTH = 'RIG'
    COPYLEFT = 'LEF'
    CREATIVE_COMMONS = 'CC'

    LICENSES = (
        (COPYRIGTH, 'Copyrigth'),
        (COPYLEFT, 'Copyleft'),
        (CREATIVE_COMMONS, 'Creative Commons')
    )

    name = models.CharField(max_length=150)
    url = models.URLField()
    description = models.TextField()
    license = models.CharField(max_length=3, choices=LICENSES)
    create_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_created=True)