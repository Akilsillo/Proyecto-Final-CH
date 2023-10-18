from django.urls import path
from News.views import *


urlpatterns = [
    path('news/', NewsListView.as_view(), name="News"),
    path('news-form/', NewsFormView.as_view(), name="NewsForm"),
]