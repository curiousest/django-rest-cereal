import unittest
import json

from rest_framework.test import (
    APIClient, APIRequestFactory, APITestCase,
    force_authenticate
)

from .testapp.models import (A, B, C)
from .testapp.serializers import (
    ASerializer, BSerializer, CSerializer
)


class CerealMixinTest(unittest.TestCase):

    request_factory = APIRequestFactory()
    request_data = {}

    def setUp(self):
        self.client = APIClient()

        self.a = A.objects.create(title="aaa")
        self.b = B.objects.create(title="bbb")
        self.c = C.objects.create(title="ccc", b=self.b)
        self.a.b = self.b
        self.a.save()
        self.b.c = self.c
        self.b.save()

        self.url = '/as/{0}/'.format(self.a.id)

    def test_no_request_serializer(self):
        serializer = ASerializer(self.a)
        self.assertEqual(serializer.data['title'], 'aaa')
        self.assertEqual(serializer.data['b'], self.b.id)

    def test_no_fields_requested(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200, response.content)
        result = response.json()

        self.assertEqual(result['title'], 'aaa')

    def test_single_normal_field(self):
        fields_string = 'title'
        response = self.client.get(
            self.url + '?fields=title',
            params={'fields': fields_string}
        )
        self.assertEqual(response.status_code, 200, response.content)
        result = response.json()

        self.assertEqual(result['title'], 'aaa')
        self.assertNotIn('b', result)
