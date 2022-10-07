
from parser.models import Type
from unittest import TestCase


class TypeModelTets(TestCase):
  @classmethod
  def setUpTestData(cls) -> None:
    cls.type1 = {'description': 'Débito', 'nature':'Entrada', 'sinal':'+'}
    
    Type.objects.create(**cls.type1)
    cls.type2 = Type.objects.create(description='Boleto', nature='Saída', sinal='-')
    cls.type3 = Type.objects.create(description='Financiamento', nature='Saída', sinal='-')
    cls.type4 = Type.objects.create(description='Crédito', nature='Entrada', sinal='+')
    cls.type5 = Type.objects.create(description='Recebimento Empréstimo', nature='Entrada', sinal='+')
    cls.type6 = Type.objects.create(description='Vendas', nature='Entrada', sinal='+')
    cls.type7 = Type.objects.create(description='Recebimento TED', nature='Entrada', sinal='+')
    cls.type8 = Type.objects.create(description='Recebimento DOC', nature='Entrada', sinal='+')
    cls.type9 = Type.objects.create(description='Aluguel', nature='Saída', sinal='-')
    
  def test_create_type_model(self):
    length = Type.objects.all().count()
    self.assertEquals(length, 9)
  
  def test_created_currectly(self):
    obj = Type.objects.filter(kind=1)[0]
    type1 = {'description': 'Débito', 'nature':'Entrada', 'sinal':'+'}
    self.assertEquals(type1['description'], obj.description)

