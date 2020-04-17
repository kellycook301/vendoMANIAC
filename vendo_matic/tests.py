from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Beverage
from .serializers import BeverageSerializer

# Test creation for GET request

class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_beverage(name="", price="", quantity=""):
        if name != "" and price != "" and quantity != "":
            Beverage.objects.create(name=name, price=price, quantity=quantity)

    def setUp(self):
        # add test data
        self.create_beverage("Mirinda", 4, 10)
        self.create_beverage("Mr. Pibb", 2, 6)
        self.create_beverage("Blueberry Faygo", 1, 3)


class GetAllBeveragesTest(BaseViewTest):

    def test_get_all_beveragess(self):
        # hit the API endpoint
        response = self.client.get(
            reverse("beverages-all", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = Beverage.objects.all()
        serialized = BeverageSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
