from django.contrib.auth.views import LoginView as AuthLoginView
from django.contrib.auth.views import LogoutView as AuthLogoutView


class LoginView(AuthLoginView):
    template_name = 'accounts/login.html'


class LogoutView(AuthLogoutView):
    template_name = 'accounts/logged_out.html'


login = LoginView.as_view()
logout = LogoutView.as_view()
