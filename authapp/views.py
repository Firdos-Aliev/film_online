from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView, View, UpdateView
from django.contrib import auth

from authapp.forms import UserRegisterForm, UserLoginForm, UserChangeForm, UserProfileForm


class PageMainTitleMixin:
    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(object_list=None, **kwargs)
        data['main_title'] = self.main_title
        return data


class Registration(PageMainTitleMixin, FormView):
    form_class = UserRegisterForm
    template_name = 'authapp/registration.html'
    success_url = reverse_lazy('film:movies_list')
    main_title = "Регистрация"

    def form_valid(self, form):
        form.save()
        # отпарвка на почту письмо
        # логика при правильной отправке формы
        return super().form_valid(form)


class Login(PageMainTitleMixin, FormView):
    form_class = UserLoginForm
    template_name = 'authapp/login.html'
    success_url = reverse_lazy('film:movies_list')
    main_title = "Авторизация"

    def form_valid(self, form):
        username = self.request.POST['username']  # берем данные
        password = self.request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
        return super().form_valid(form)


class Profile(PageMainTitleMixin, UpdateView):
    form_class = UserProfileForm
    template_name = 'authapp/profile.html'
    success_url = reverse_lazy('film:movies_list')
    main_title = "Профиль"

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('film:movies_list'))
