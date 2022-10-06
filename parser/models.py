from django.db import models


class TransactionNatureChoices(models.TextChoices):
  INFLOW  = 'Entrada'
  OUTFLOW = 'Saída'

class TransactionSinalChoices(models.TextChoices):
  INFLOW  = '+'
  OUTFLOW = '-'

class Type(models.Model):
  class Meta:
    ordering = ['-kind']

  kind = models.BigAutoField(primary_key=True)
  description = models.CharField(max_length=50)
  nature = models.CharField(max_length=50, choices=TransactionNatureChoices.choices)
  sinal = models.CharField(max_length=50, choices=TransactionSinalChoices.choices)

class Transaction(models.Model):
  class Meta:
    ordering = ['-id']

  transaction_type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='transactions')
  date = models.DateTimeField()
  amount = models.FloatField()
  cpf = models.CharField(max_length=11)
  card = models.CharField(max_length=12)
  shop_owner = models.CharField(max_length=14)
  shop_name = models.CharField(max_length=19)

