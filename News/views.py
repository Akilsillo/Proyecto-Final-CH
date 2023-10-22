from django.shortcuts import render, redirect
from News.models import NewsItem

# Class views
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class SuperuserRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return redirect(reverse_lazy('admin:login'))
        return super(SuperuserRequiredMixin, self).dispatch(request, *args, **kwargs)

class NewsListView(ListView):
    model = NewsItem
    template_name = "News/news_list.html"
    context_object_name = "objects"
    
class NewsDetailView(DetailView):
    model = NewsItem
    template_name = "News/news_detail.html"
    context_object_name = "objects"
    
class NewsDeleteView(SuperuserRequiredMixin, DeleteView):
    model = NewsItem
    success_url = reverse_lazy("News")
    template_name = "News/news_delete.html"
    
class NewsFormView(LoginRequiredMixin ,CreateView):
    model = NewsItem
    template_name = "News/news_form.html"
    success_url = reverse_lazy("NewsForm")
    fields = ["title", "date", "preview", "full_view", "image"]
    
    def form_valid(self, form):
        form.instance.image = self.request.FILES.get('image')
        return super().form_valid(form)
    
