from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from photos.models import Photo
from photos.seriealizers import PhotoSerializer, PhotoListSerializer


class PhotoListAPI(ListCreateAPIView):
    """
    EndPoint de listado y creacion de fotos
    """
    queryset = Photo.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_serializer_class(self):
        return PhotoSerializer if self.request.method =='POST' else PhotoSerializer

class PhotoDetailAPI(RetrieveUpdateDestroyAPIView):
    """
    EndPoint de detalle de foto
    """
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)