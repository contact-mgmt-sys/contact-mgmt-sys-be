from rest_framework import serializers as sz

from contacts.models import Contact

class ContactSerializer(sz.ModelSerializer):
    class Meta:
        model = Contact
        fields = ["id", "name", "address", "email", "mobile"]