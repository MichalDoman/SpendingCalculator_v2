from django.views.generic import TemplateView, FormView
from django.contrib.auth import login
from django.contrib.auth.models import User

from app.forms import RegisterForm


# SORTING_NAMES = ["item", "-item", "price", "-price", "producer", "-producer", "room", "-room", "date", "-date"]


class HomeView(TemplateView):
    template_name = 'base.html'


class RegisterView(FormView):
    """A View that enables users to register via a form, and access all functionalities."""
    form_class = RegisterForm
    template_name = "registration/register.html"

    def form_valid(self, form):
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        password_repeated = form.cleaned_data['password_repeated']

        if User.objects.filter(email=email).exists():
            form.add_error(None, 'This e-mail address is already taken!')
            return super().form_invalid(form)

        if password != password_repeated:
            form.add_error(None, 'Passwords did not match!')
            return super().form_invalid(form)

        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
        )

        login(self.request, user)
        return super().form_valid(form)
