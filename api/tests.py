from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User

# Create your tests here.


class CountryTests(APITestCase):
    def setUp(self):
        # Create superuser
        user = User.objects.create_superuser('admin', 'admin@admin.com', 'admin')
        # self.client.force_authenticate(user=user)
        self.client.login(username='admin', password='admin')

        # Create countries

    def test_country_list(self):
        """
        Ensure that the database is seeded with the primary countries
        :return:
        """
        test_data = {}

        # self.client.credentials(HTTP_AUTHORIZATION='Basic admin:admin')
        # self.client.login(username='admin', password='admin')
        url = reverse('country-list')
        response = self.client.get(url)
        print response.data
        self.assertEqual(response.status_code, status.HTTP_200_OK)