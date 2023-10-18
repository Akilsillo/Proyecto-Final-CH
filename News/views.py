from django.shortcuts import render
from News.models import NewsItem

# Class views
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class NewsListView(ListView):
    model = NewsItem
    template_name = "News/news_list.html"
    
class NewsFormView(LoginRequiredMixin ,CreateView):
    model = NewsItem
    template_name = "News/news_form.html"
    success_url = reverse_lazy("NewsForm")
    fields = ["title", "date", "preview", "full_view", "image"]