from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.shortcuts import render, redirect
from django.views import View

from users.form import LoginForm


class LoginView(View):

    def get(self, request):
        """
        Presenta el formulario de login y gestiona el login de un usuario
        :param request: objeto HttpRequest con los datos de la petición
        :return: objeto HttpResponse con los datos de la respuesta
        """
        error_message = ""
        login_form = LoginForm()
        context = {
            'errors': error_message,
            'login_form': login_form
        }
        return render(request, 'users/login.html', context)

    def post(self, request):
        """
        Presenta el formulario de login y gestiona el login de un usuario
        :param request: objeto HttpRequest con los datos de la petición
        :return: objeto HttpResponse con los datos de la respuesta
        """
        #cambiar el post de la vista
        error_message = ""
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('pwd')
            user = authenticate(username=username, password=password)
            if user is None:
                error_message = "Usuario o contraseña incorrecto"
            else:
                if user.is_active:
                    django_login(request, user)
                    return redirect(request.GET.get('next', 'photos_home'))
                else:
                    error_message = "Cuenta de usuario inactiva"
        context = {
            'errors': error_message,
            'login_form': login_form
        }
        return render(request, 'users/login.html', context)


class LogoutView(View):

    def get(self, request):
        """
        Hace el logout de un usuario y redirige al login
        :param request: objeto HttpRequest con los datos de la petición
        :return: objeto HttpResponse con los datos de la respuesta
        """
        if request.user.is_authenticated():
            django_logout(request)
        return redirect('photos_home')