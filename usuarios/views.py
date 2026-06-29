from django.contrib.auth.views import LoginView


class LoginUsuarioView(LoginView):
    template_name = "usuarios/login.html"

