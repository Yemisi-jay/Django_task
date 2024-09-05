from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, FormView

from .forms import MyForm, DataUpdateForm, NameUpdateForm, ProfileUpdateForm, FeedbackForm
from .models import MyModel, Profile, Feedback
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
        user_form = MyForm
        profile_form = ProfileUpdateForm
        return profile_form, user_form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile_form, user_form = self.get_forms()
        context['person'] = self.object
        if self.request.POST:
            context['u_form'] = user_form(self.request.POST, instance=self.object)

            context['p_form'] = profile_form(self.request.POST, instance=self.get_or_create_profile())
        else:
            context['u_form'] = user_form(instance=self.object)
            context['p_form'] = profile_form(instance=self.get_or_create_profile())
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        profile_form, user_form = self.get_forms()
        print(self.request.POST)

        u_form = user_form(self.request.POST, instance=self.object)
        p_form = profile_form(self.request.POST, instance=self.get_or_create_profile())
        if u_form.is_valid() and p_form.is_valid():
            print(111)
            u_form.save()
            p_form.save()
            return redirect(self.get_success_url())
        else:
            print("error")
            return self.form_invalid(u_form, p_form)

    def form_invalid(self, user_form, profile_form):
        return self.render_to_response(
            self.get_context_data(u_form=user_form, p_form=profile_form)
        )

    def get_or_create_profile(self):
        if hasattr(self.object, "profile"):
            # return Profile.objects.get(user=self.object)
            return self.object.profile
        else:
            profile = Profile.objects.create(user=self.object)
            return profile


class ProfileDetailView(DetailView):
    model = MyModel
    template_name = 'profile_detail.html'
    context_object_name = 'contact'

    # def get_forms(self):
    #     feedback_form = FeedbackForm
    #     return feedback_form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['feedback_form'] = FeedbackForm()
        context['feedback'] = Feedback.objects.all()
        # user_title = "my title"
        # blogs = Blog.objects.filter(title=user_title)
        # first_blog_post = blogs.first()
        # last_blog_post = blogs.last()
        # latest_blog_post = blogs.latest('id')
        # http://localhost:8000/index?idx=23
        return context

    def post(self, request, *args, **kwargs):
        contact = self.get_object()
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('detail', contact.pk)
        else:
            context = self.get_context_data(feedback_form=form)
            return self.render_to_response(context)


# class ListObjectView(ListView):
#     queryset = MyModel.objects.all()
#     template_name = 'profile_detail'
#     context_object_name = 'contact'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context
