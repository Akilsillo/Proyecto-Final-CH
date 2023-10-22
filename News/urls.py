from django.urls import path
from News.views import *


urlpatterns = [
    path('news/', NewsListView.as_view(), name="News"),
    path('news-detail/<int:pk>', NewsDetailView.as_view(), name="NewsDetail"),
    path('news-form/', NewsFormView.as_view(), name="NewsForm"),
    path('news-delete/<int:pk>', NewsDeleteView.as_view(), name="NewsDelete"),
]