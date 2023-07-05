from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = "contacts"
urlpatterns = [
    path(f"{app_name}/", views.Contacts.as_view(), name="list"),
    path(f"{app_name}/<int:pk>/", views.Contact.as_view(), name="view")
]
urlpatterns = format_suffix_patterns(urlpatterns)