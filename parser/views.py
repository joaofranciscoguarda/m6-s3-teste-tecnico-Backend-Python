from parser import serializers
from parser.models import Transaction

from rest_framework import generics, viewsets
from rest_framework.parsers import (BaseParser, FileUploadParser,
                                    MultiPartParser)
from rest_framework.views import Response, View, status

from .serializers import TransactionSerializer, UploadSerializer


class PlainTextParser(BaseParser):
    """
    Plain text parser.
    """
    media_type = 'text/plain'

    def parse(self, stream, media_type=None, parser_context=None):
        """
        Simply return a string representing the body of the request.
        """
        return stream.read()

class UploadViewSet(viewsets.ViewSet):
    serializer_class = UploadSerializer

    def create(self, request):
        file_uploaded = request.FILES.get('file_uploaded')
        
        # line.decode('utf-8') or
        # str(line, 'utf-8')

        raw_lines = [line.decode('utf-8') for line in file_uploaded]
        
        #objeto para ser serializado a partir da leitura

        obj_response = []
    
        for line in raw_lines:
        # dict format: {transaction_type: ,date: ,amount: ,cpf: ,card: ,shop_owner: ,shop_name: ,} 
          obj = {
            'transaction_type': line[:1],
            'date': line[1:5] + '-' +
                    line[5:7] + '-' +
                    line[7:9] + 'T' +
                    line[42:44] + ':' +
                    line[44:46] + ':' +
                    line[46:48],
            'amount': float(line[9:19])/100,
            'cpf': line[19:30],
            'card': line[30:42],
            'shop_owner': line[48:62].strip(),
            'shop_name': line[62:81].strip(),
          }

          serializer = TransactionSerializer(data=obj)

          serializer.is_valid(raise_exception=True)

          serializer.save()
          
          obj_response.append(serializer.data)
  
        return Response({'detail': 'Information from file where uploaded to the database with success','objects':obj_response}, status.HTTP_201_CREATED)
    
    
    
    
    