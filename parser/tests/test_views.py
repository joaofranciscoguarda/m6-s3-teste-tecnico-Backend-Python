from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from rest_framework.views import Response, status


class CnabViewTest(APITestCase):
  @classmethod
  def setUpTestData(cls) -> None:
    
    pass

  # def test_send_CNAB_example_file(self):

  #   with open('CNAB_example_file.txt', mode='r') as file:
      
  #     response = self.client.post('/upload/', file, format='json')
  #     expected_status_code = status.HTTP_200_OK
  #     result_status_code = response.status_code
  #     self.assertEqual(expected_status_code, result_status_code)
