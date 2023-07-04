from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from contacts import views

app_name = "contacts"
urlpatterns = [
    path("", views.contacts, name="list"),
    path("<int:pk>/", views.contact, name="view")
]
urlpatterns = format_suffix_patterns(urlpatterns)