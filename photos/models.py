from django.db import models
from django.contrib.auth.models import User


# Create your models here.
from photos.validatos import badwords

COPYRIGTH = 'RIG'
COPYLEFT = 'LEF'
CREATIVE_COMMONS = 'CC'

LICENSES = (
    (COPYRIGTH, 'Copyrigth'),
    (COPYLEFT, 'Copyleft'),
    (CREATIVE_COMMONS, 'Creative Commons')
)


PUBLIC = 'PUB'
PRIVATE = 'PRI'

VISIBILITY = (
    (PUBLIC, 'Pública'),
    (PRIVATE, 'Privado')
)

class Photo(models.Model):
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=150)
    url = models.URLField()
    description = models.TextField(blank=True, null=True, default="", validators=[badwords])
    license = models.CharField(max_length=3, choices=LICENSES, default=CREATIVE_COMMONS)
    create_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    visibility = models.CharField(max_length=3, choices=VISIBILITY, default=PUBLIC)

    def __str__(self):
        return self.name
