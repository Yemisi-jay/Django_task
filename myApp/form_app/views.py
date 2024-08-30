from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

from .forms import MyForm, DataUpdateForm, NameUpdateForm, ProfileUpdateForm
from .models import MyModel
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView


# Create your views here.

class MyView(ListView):
    queryset = MyModel.objects.all()
    template_name = 'index.html'
    context_object_name = 'contact'
    # success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class FormCreateView(CreateView):
    model = MyModel
    template_name = 'my_form.html'
    context_object_name = 'form_'
    fields = '__all__'
    success_url = '/'

    # def get(self, request):
    #     self.form()
    #     form_ = MyModel.objects.all()


class FormUpdateView(UpdateView):
    model = MyModel
    form_class = MyForm
    # data_update = DataUpdateForm
    # name_update_form = NameUpdateForm
    template_name = 'form_update.html'
    context_object_name = 'contact'
    pk_url_kwarg = 'person_id'
    success_url = reverse_lazy('home')

    def get_forms(self):
        user_form = self.get_form()
        profile_form = ProfileUpdateForm(self.request.POST or None)
        return profile_form, user_form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile_form, user_form = self.get_forms()
        context['u_form'] = user_form
        context['p_form'] = profile_form
        context['person'] = self.object
        return context

    def post(self, request, *args, **kwargs):
        user_form, profile_form = self.get_forms()
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect(self.get_success_url())
        else:
            return self.form_invalid(user_form, profile_form)

    def form_invalid(self, user_form, profile_form):
        return self.render_to_response(
            self.get_context_data(user_form=user_form, profile_form=profile_form)
        )