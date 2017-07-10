from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView
from django.urls import reverse

from photos.form import PhotoForm
from photos.models import Photo, PUBLIC


# Create your views here.

class HomeView (View):

    def get(self, request):
        """
        Rederiza el home con un listado de fotos
        :param request: objeto HttpRequest con los datos de la petición
        :return: objeto HttpResponse con los datos de la respuesta
        """
        # Recupera todas las fotos de la base de datos
        photos = Photo.objects.filter(visibility=PUBLIC).order_by('-create_at')
        context = {'photos_list': photos[:4]}
        return render(request, 'photos/home.html', context)


class PhotosQueryset(object):

    def get_photo_by_user(user):
        possible_phtotos = Photo.objects.all().select_related("owner")


class PhotoDetailView (View):

    def get(self, request, pk):
        """
        Rederiza del detalle de imagen
        :param request: objeto HttpRequest con los datos de la peticion
        :param pk: clave primaria de la foto que se recupera
        :return: un objeto HttpResponse con los datos de respuesta
        """
        possible_photo = Photo.objects.filter(pk=pk).select_related('owner')
        if len(possible_photo) == 0:
            return HttpResponseNotFound("La imagen no existe")
        elif len(possible_photo) > 1:
            return HttpResponse("Multiples opciones", status=300)

        photo = possible_photo[0]
        context = {'photo': photo}
        return render(request, 'photos/detail.html', context)


class PhotoCreationView (View):

    @method_decorator(login_required())
    def get(self, request):
        """
        Presenta el formulario para crear una foto
        :param request: objeto HttpRequest con los datos de la peticion
        :return: un objeto HttpResponse con los datos de respuesta
        """
        message = None
        photo_form = PhotoForm()
        context ={
            'form': photo_form,
            'message': message
        }
        return render(request, 'photos/photo_creation.html', context)

    @method_decorator(login_required())
    def post(self, request):
        """
        Presenta el formulario para crear una foto y en caso de que la peticion sea POST la
        valida y la creat en caso de ser valida
        :param request: objeto HttpRequest con los datos de la peticion
        :return: un objeto HttpResponse con los datos de respuesta
        """
        message = None
        photo_with_user = Photo(owner=request.user)
        photo_form = PhotoForm(request.POST, instance=photo_with_user)
        if photo_form.is_valid():
            new_photo = photo_form.save()
            photo_form = PhotoForm()
            message = 'Foto creada satisfactoriamente <a href="{0}">Ver foto</a>'.format(
                reverse('photos_detail', args=[new_photo.pk])
            )
        context = {
            'form': photo_form,
            'message': message
        }
        return render(request, 'photos/photo_creation.html', context)


class PhotosListView(LoginRequiredMixin, ListView):

    model = Photo
    template_name = 'photos/photo_list.html'

    def get_queryset(self):
        return super().get_queryset().filter(owner=self.request.user)