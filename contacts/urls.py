from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from contacts import views

app_name = "contacts"
urlpatterns = [
    path(f"{app_name}/", views.contacts, name="list"),
    path(f"{app_name}/<int:pk>/", views.contact, name="view")
]
urlpatterns = format_suffix_patterns(urlpatterns)