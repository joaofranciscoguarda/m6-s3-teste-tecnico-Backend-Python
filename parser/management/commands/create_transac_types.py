
from parser.models import Type

from django.core.management.base import BaseCommand


class Command(BaseCommand):
  help = 'Create Transaction Types'
  
  def handle(self, *args, **kwargs):
    Type.objects.create(description='Débito', nature='Entrada', sinal='+')
    Type.objects.create(description='Boleto', nature='Saída', sinal='-')
    Type.objects.create(description='Financiamento', nature='Saída', sinal='-')
    Type.objects.create(description='Crédito', nature='Entrada', sinal='+')
    Type.objects.create(description='Recebimento Empréstimo', nature='Entrada', sinal='+')
    Type.objects.create(description='Vendas', nature='Entrada', sinal='+')
    Type.objects.create(description='Recebimento TED', nature='Entrada', sinal='+')
    Type.objects.create(description='Recebimento DOC', nature='Entrada', sinal='+')
    Type.objects.create(description='Aluguel', nature='Saída', sinal='-')

    return 'Done!'
