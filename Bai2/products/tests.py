from django.test import TestCase, Client
from django.urls import reverse
from products.models import product  
import json

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse('product_list')
        self.detail_url = reverse('product_detail', args=['1'])
        self.product1 = product.objects.create(  # Corrected model name
            title='product1',
            description='description1',
            category='category1',
            price=100.0
        )

    def test_product_list_GET(self):
        """Kiểm tra trạng thái thành công (200) khi truy vấn danh sách sản phẩm bằng phương thức GET."""
        response = self.client.get(self.list_url)

        self.assertEquals(response.status_code, 200)

    def test_product_detail_GET(self):
        """Kiểm tra trạng thái thành công (200) khi truy vấn chi tiết sản phẩm bằng phương thức GET."""
        response = self.client.get(self.detail_url)

        self.assertEquals(response.status_code, 200)

    def test_product_list_POST(self):
        """Kiểm tra trạng thái tạo mới thành công (201) khi gửi dữ liệu sản phẩm mới bằng phương thức POST."""
        product_data = {
            'title': 'product2',
            'description': 'description2',
            'category': 'category2',
            'price': 200.0
        }

        response = self.client.post(self.list_url, product_data, content_type='application/json')

        self.assertEquals(response.status_code, 201)

    def test_product_detail_PUT(self):
        """Kiểm tra trạng thái cập nhật thành công (200) khi gửi dữ liệu cập nhật sản phẩm bằng phương thức PUT."""
        product_data = {
            'title': 'product1 updated',
            'description': 'description1 updated',
            'category': 'category1 updated',
            'price': 150.0
        }

        response = self.client.put(self.detail_url, json.dumps(product_data), content_type='application/json')

        self.assertEquals(response.status_code, 200)

    def test_product_detail_DELETE(self):
        """Kiểm tra trạng thái xóa thành công (204) khi gửi yêu cầu xóa sản phẩm bằng phương thức DELETE."""
        response = self.client.delete(self.detail_url)

        self.assertEquals(response.status_code, 204)
