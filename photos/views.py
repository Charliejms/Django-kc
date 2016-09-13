from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView

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


class PhotoDetailView (View):

    def get(self, request, pk):
        """
        Rederiza del detalle de imagen
        :param request:
        :param pk:
        :return:
        """
        possible_photo = Photo.objects.filter(pk=pk)
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
        Presenta el formulario para crear una foto y en caso de que la peticion sea POST la
        valida y la creat en caso de ser valida
        :param request:
        :return:
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
        :param request:
        :return:
        """
        message = None
        photo_with_user = Photo(owner=request.user)
        photo_form = PhotoForm(request.POST, instance=photo_with_user)
        if photo_form.is_valid():
            new_photo = photo_form.save()
            photo_form = PhotoForm()
        context = {
            'form': photo_form,
            'message': message
        }
        return render(request, 'photos/photo_creation.html', context)


class PhotosListView(ListView):

    model = Photo
    template_name = 'photos/photo_list.html'