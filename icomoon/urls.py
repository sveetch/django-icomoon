from django.urls import path

from .views import WebfontIconListView


app_name = "icomoon"


urlpatterns = [
    path("", WebfontIconListView.as_view(), name="index"),
]
