from django import forms
from .models import MyModel, Profile, Feedback


class MyForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = '__all__'


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class DataUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = MyModel
        fields = ['email', 'birth_date']


class NameUpdateForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ['first_name', 'last_name']


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['text_area']