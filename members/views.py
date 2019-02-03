from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from datetime import datetime
from django.views.generic import ListView, DetailView, FormView, View
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib import messages
from .models import Event
from members.forms import RegistrationForm


class IndexView(ListView):
    model = Event
    template_name = 'members/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data()
        context['page_title'] = "All events"
        return context


class EventDetailView(DetailView):
    model = Event
    template_name = 'members/event.html'


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = 'members/login.html'
    success_url = '/'

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        messages.info(self.request, f'Hi {form.get_user()}!')
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')


class RegisterFormView(FormView):
    form_class = RegistrationForm
    template_name = 'members/register.html'
    success_url = '/login/'

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegisterFormView, self).form_invalid(form)


def view_profile(request):
    args = {'user': request.user}
    return render(request, 'members/profile.html', args)


def edit_profile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/profile')
    else:
        form = UserChangeForm(instance=request.user)
        args = {'form': form}
        return render(request, 'members/edit_profile.html', args)


def hello_there(request, name):
    return render(
        request,
        'members/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )
