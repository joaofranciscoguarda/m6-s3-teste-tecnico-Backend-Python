from rest_framework import serializers
from rest_framework.serializers import Serializer, FileField, ModelSerializer
from .models import Transaction


class TransactionSerializer(ModelSerializer):
  class Meta:
    model= Transaction
    fields= '__all__'

class UploadSerializer(Serializer):
    file_uploaded = FileField()
    class Meta:
        fields = ['file_uploaded']
