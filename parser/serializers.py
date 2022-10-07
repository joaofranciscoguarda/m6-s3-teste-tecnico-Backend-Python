from rest_framework import serializers
from rest_framework.serializers import (FileField, ModelSerializer,
                                        PrimaryKeyRelatedField, Serializer,
                                        SlugRelatedField)

from .models import Transaction, Type


class TypeSerializer(ModelSerializer):
  class Meta:
    model= Type
    fields = '__all__'

class TransactionSerializer(ModelSerializer):
  class Meta:
    model= Transaction
    fields= ['transaction_type', 'date', 'amount', 'cpf', 'card', 'shop_owner', 'shop_name',]

  # transaction_type = TypeSerializer(read_only=True)

class UploadSerializer(Serializer):
    file_uploaded = FileField()
    class Meta:
        fields = ['file_uploaded']

 