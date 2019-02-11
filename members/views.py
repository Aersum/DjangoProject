from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from datetime import datetime
from django.views.generic import (
    ListView, DetailView, FormView, View, CreateView, UpdateView
    )
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib import messages
from .models import Event
from members.forms import (
    RegistrationForm, EditUserForm, EditProfileForm, NewEventForm
    )


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
        user_form = EditUserForm(
            request.POST,
            request.FILES,
            instance=request.user
            )
        profile_form = EditProfileForm(
            request.POST, request.FILES,
            instance=request.user.profile
            )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('/profile')
    user_form = EditUserForm(instance=request.user)
    profile_form = EditProfileForm(instance=request.user.profile)
    args = {'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'members/edit_profile.html', args)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('members:profile'))
        else:
            redirect(reverse('members:profile'))
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'members/change_password.html', args)


def hello_there(request, name):
    return render(
        request,
        'members/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )


class EventCreateView(CreateView):
    model = Event
    template_name = 'members/add_event.html'
    form_class = NewEventForm

    def get_success_url(self):
        return reverse('members:event', args=(self.object.id, ))

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(EventCreateView, self).get_context_data()
        context['hobby'] = self.request.user.profile.hobby.all()
        return context


class EventUpdateView(UpdateView):
    model = Event
    template_name = 'members/update_event.html'
    form_class = NewEventForm

    def get_success_url(self):
        return reverse('members:event', args=(self.object.id, ))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(EventUpdateView, self).get_context_data()
        context['hobby'] = self.request.user.profile.hobby.all()
        return context
