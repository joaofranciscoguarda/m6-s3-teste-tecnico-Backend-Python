
from parser.models import Transaction, Type
from unittest import TestCase

from parser.serializers import TransactionSerializer


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

  # def test_create_cnab(self):
  #   line = '3201903010000014200096206760174753****3153153453JOÃO MACEDO   BAR DO JOÃO       '
  
  #   # dict format: {transaction_type: ,date: ,amount: ,cpf: ,card: ,shop_owner: ,shop_name: ,} 
  #   obj = {
  #     'transaction_type': line[:1],
  #     'date': line[1:5] + '-' +
  #             line[5:7] + '-' +
  #             line[7:9] + 'T' +
  #             line[42:44] + ':' +
  #             line[44:46] + ':' +
  #             line[46:48],
  #     'amount': float(line[9:19])/100,
  #     'cpf': line[19:30],
  #     'card': line[30:42],
  #     'shop_owner': line[48:62].strip(),
  #     'shop_name': line[62:81].strip(),
  #   }

  #   serializer = TransactionSerializer(data=obj)

  #   serializer.is_valid(raise_exception=True)

  #   serializer.save()
    
  #   self.assertEquals(serializer.data, Transaction.objects.all()[-1])