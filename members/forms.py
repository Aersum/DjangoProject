from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from members import models


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class EditUserForm(UserChangeForm):

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            # 'password'
        )


class EditProfileForm(forms.ModelForm):

    class Meta:
        model = models.Profile
        fields = (
            'city',
            'birth_date',
            'image',
            'hobby'
        )
    birth_date = forms.DateField(
        widget=forms.TextInput(attrs={'type': 'date'})
        )
    hobby = forms.ModelMultipleChoiceField(
            widget=forms.CheckboxSelectMultiple,
            queryset=models.Hobby.objects.all(),
            required=True)


class NewEventForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.TextInput(attrs={'type': 'date'})
        )
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'rows': 4, 'cols': 40})
        )

    class Meta:
        model = models.Event
        exclude = ('author', )
