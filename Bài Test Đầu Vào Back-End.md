---
type: article
date: 
year: 2024
month: March
day: 30
creation date: 2024-03-30 22:02
modification date: Saturday 30th March 2024 22:02:07
---

# I: Kiến thức lý thuyết 

## 1. Sự khác biệt giữa Flask và Django là gì?

- **Django:**
    - Khung MVC (Model-View-Controller) đầy đủ chức năng.
    - Cung cấp nhiều tiện ích tích hợp sẵn cho các tác vụ phổ biến.
    - Phù hợp cho các dự án lớn, phức tạp.
- **Flask:**
    - Khung vi mô (microframework) với cấu trúc đơn giản.
    - Cung cấp API tối giản để xây dựng web app.
    - Tự do lựa chọn thư viện và công cụ cho dự án.
    - Phù hợp cho các dự án nhỏ, đơn giản.

**2. Mức độ phức tạp:**

- **Django:**
    - Cấu trúc thư mục và tập tin phức tạp hơn.
    - Đường cong học tập dốc hơn.
    - Phù hợp cho các nhà phát triển có kinh nghiệm.
- **Flask:**
    - Cấu trúc đơn giản, dễ hiểu.
    - Dễ dàng học và sử dụng cho người mới bắt đầu.

**3. Tính năng:**

- **Django:**
    - Cung cấp nhiều tính năng tích hợp sẵn như:
        - Hệ thống quản trị nội dung (CMS)
        - Xác thực người dùng
        - Quản lý cơ sở dữ liệu
        - Hệ thống cache
        - Hỗ trợ đa ngôn ngữ
    - Có thể mở rộng thêm tính năng bằng thư viện bên thứ ba.
- **Flask:**
    - Ít tính năng tích hợp sẵn.
    - Cần sử dụng thư viện bên thứ ba cho hầu hết các chức năng.

**4. Tốc độ:**

- **Django:**
    - Có thể chậm hơn do cấu trúc phức tạp và nhiều tính năng.
    - Phù hợp cho các dự án không yêu cầu tốc độ cao.
- **Flask:**
    - Nhẹ và nhanh hơn do cấu trúc đơn giản.
    - Phù hợp cho các dự án yêu cầu tốc độ cao.

**5. Khả năng mở rộng:**

- **Django:**
    - Khả năng mở rộng tốt nhờ cấu trúc MVC và hệ thống ORM.
    - Phù hợp cho các dự án có thể phát triển lớn trong tương lai.
- **Flask:**
    - Khả năng mở rộng thấp hơn so với Django.
    - Cần thiết kế cẩn thận để đảm bảo khả năng mở rộng cho dự án lớn.

**6. Cộng đồng:**

- **Django:**
    - Cộng đồng lớn và mạnh mẽ với nhiều tài liệu và hỗ trợ.
    - Nhiều thư viện và công cụ được phát triển bởi cộng đồng.
- **Flask:**
    - Cộng đồng nhỏ hơn nhưng đang phát triển nhanh.
    - Ít tài liệu và hỗ trợ hơn so với Django.

**7. Lựa chọn:**

- **Django:** Phù hợp cho các dự án lớn, cần nhiều tính năng và khả năng mở rộng cao.
- **Flask:** Phù hợp cho các dự án nhỏ, đơn giản và cần tốc độ nhanh.

**Ví dụ:**

**Django:**

```python
from django.contrib.auth.models import User
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
```


**Flask:**

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
```
    
## 2. Các kiểu dữ liệu cơ bản trong Python là gì?

**1. Số:**

- **Số nguyên (Integer):**
    - Ví dụ: 1, 2, 3, -10, 0
    - Không có phần thập phân.
    - Có thể sử dụng các ký hiệu `+`, `-`, `*`, `/`, `//`, `%` cho phép toán.
- **Số thực (Float):**
    - Ví dụ: 1.5, 3.14, -2.718
    - Có phần thập phân.
    - Có thể sử dụng các ký hiệu `+`, `-`, `*`, `/`, `//`, `%` cho phép toán.
- **Số phức (Complex):**
    - Ví dụ: 1+2j, 3-4j, 5j
    - Bao gồm phần thực và phần ảo.
    - Có thể sử dụng các ký hiệu `+`, `-`, `*`, `/` cho phép toán.

**2. Chuỗi (String):**

- **Là tập hợp các ký tự Unicode.**
- Ví dụ: "Hello", "World!", "12345"
- Có thể sử dụng các toán tử `+`, `*`, `in`, `not in` cho phép toán.
- Có thể truy cập từng ký tự bằng chỉ mục.

**3. Danh sách (List):**

- **Là tập hợp các giá trị có thứ tự.**
- Ví dụ: `[1, 2, 3]`, ["a", "b", "c"], [True, False, None]
- Có thể thêm, xóa, sửa đổi các phần tử trong danh sách.
- Có thể sử dụng các toán tử `+`, `*`, `in`, `not in` cho phép toán.

**4. Tuple:**

- **Tương tự như danh sách nhưng không thể thay đổi.**
- Ví dụ: `(1, 2, 3)`, ("a", "b", "c"), (True, False, None)
- Có thể truy cập từng phần tử bằng chỉ mục.
- Có thể sử dụng các toán tử `+`, `*`, `in`, `not in` cho phép toán.

**5. Bộ (Set):**

- **Là tập hợp các giá trị không có thứ tự và không trùng lặp.**
- Ví dụ: `{1, 2, 3}`, {"a", "b", "c"}, {True, False}
- Có thể thêm, xóa, kiểm tra phần tử trong bộ.
- Có thể sử dụng các toán tử `&`, `|`, `-`, `^` cho phép toán.

**6. Từ điển (Dictionary):**

- **Là tập hợp các cặp key-value.**
- Ví dụ: `{"name": "John", "age": 30, "city": "Hanoi"}`
- Có thể thêm, xóa, sửa đổi các cặp key-value trong từ điển.
- Có thể truy cập giá trị bằng key.

**7. None:**

- **Kiểu dữ liệu đặc biệt biểu thị giá trị rỗng.**
- Ví dụ: `x = None`

**8. Boolean:**

- **Có hai giá trị True và False.**
- Ví dụ: `x = True`, `y = False`

- Python là ngôn ngữ gõ động, không cần khai báo kiểu dữ liệu khi tạo biến.
- Kiểu dữ liệu của biến được xác định dựa trên giá trị được gán cho nó.
    
## 3.  Sự khác biệt giữa list và tuple trong Python?

**1. Khả năng thay đổi:**

- **List:** Có thể thay đổi, thêm, xóa, sửa đổi các phần tử sau khi tạo.
- **Tuple:** Không thể thay đổi sau khi tạo.

**Ví dụ:**

```python
# List
my_list = [1, 2, 3]
my_list.append(4)
my_list[1] = 5
print(my_list)  # Output: [1, 5, 3, 4]

# Tuple
my_tuple = (1, 2, 3)
# my_tuple.append(4)  # Lỗi: 'tuple' object does not support item assignment
# my_tuple[1] = 5  # Lỗi: 'tuple' object does not support item assignment
print(my_tuple)  # Output: (1, 2, 3)
```


**2. Hiệu suất:**

- **List:** Tốn bộ nhớ hơn và truy cập phần tử chậm hơn tuple do tính linh hoạt.
- **Tuple:** Tiết kiệm bộ nhớ hơn và truy cập phần tử nhanh hơn do cấu trúc cố định.

**Ví dụ:**

```python
import time

# List
list_time = time.time()
my_list = list(range(1000000))
list_time = time.time() - list_time

# Tuple
tuple_time = time.time()
my_tuple = tuple(range(1000000))
tuple_time = time.time() - tuple_time

print(f"Thời gian tạo List: {list_time}")
print(f"Thời gian tạo Tuple: {tuple_time}")

# Truy cập phần tử thứ 500000
list_access_time = time.time()
my_list[500000]
list_access_time = time.time() - list_access_time

tuple_access_time = time.time()
my_tuple[500000]
tuple_access_time = time.time() - tuple_access_time

print(f"Thời gian truy cập List: {list_access_time}")
print(f"Thời gian truy cập Tuple: {tuple_access_time}")
```


**3. Mức độ sử dụng:**

- **List:** Phù hợp cho các trường hợp cần thay đổi dữ liệu thường xuyên, ví dụ: lưu trữ dữ liệu tạm thời, danh sách mua sắm.
- **Tuple:** Phù hợp cho các trường hợp dữ liệu không thay đổi, ví dụ: tọa độ điểm, thông tin cá nhân.

**4. Ví dụ về trường hợp ưu tiên:**

- **List:**
    - Lưu trữ dữ liệu cần cập nhật thường xuyên.
    - Thực hiện các phép toán trên danh sách như sắp xếp, lọc, v.v.
    - Truy cập phần tử theo vị trí.
- **Tuple:**
    - Lưu trữ dữ liệu không thay đổi.
    - Sử dụng làm key cho dictionary.
    - Truy cập phần tử theo giá trị.

**5. Mức độ low-level:**

- **List:** Được triển khai bằng C, sử dụng cấu trúc dữ liệu dynamic array.
- **Tuple:** Được triển khai bằng C, sử dụng cấu trúc dữ liệu struct.
    
## 4. Middleware trong Django:

### 4.1 Câu hỏi lý thuyết: Middleware trong Django là gì? Giải thích cách middleware hoạt động.

Middleware là một lớp phần mềm trung gian hoạt động như một cầu nối giữa request và view trong Django. Nó cho phép thực hiện các tác vụ trước khi request đến view và sau khi view trả về response.

**Cách middleware hoạt động:**

1. Khi một request đến Django, nó sẽ đi qua middleware theo thứ tự được định nghĩa trong file `settings.py`.
2. Mỗi middleware có thể thực hiện các tác vụ như:
    - Xử lý request
    - Chỉnh sửa request
    - Chặn request
    - Trả về response
3. Sau khi tất cả middleware được thực thi, request sẽ được chuyển đến view tương ứng.
4. Sau khi view trả về response, response sẽ đi qua middleware theo thứ tự ngược lại.
5. Mỗi middleware có thể thực hiện các tác vụ như:
    - Xử lý response
    - Chỉnh sửa response
    - Chặn response

**Ví dụ:**

- Middleware xác thực: Kiểm tra xem người dùng có đăng nhập hay không trước khi cho phép họ truy cập vào view.
- Middleware ghi log: Ghi lại thông tin về request và response vào file log.
- Middleware nén: Nén response để tiết kiệm băng thông.

**Lợi ích:**

- Middleware giúp ‎  tách biệt các phần logic trong Django.
- Middleware giúp ‎  dễ dàng thực hiện các tác vụ chung cho nhiều view.
- Middleware giúp ‎  tăng hiệu suất và bảo mật cho ứng dụng Django.
   
### 4.2. Ví dụ mã code  Hãy viết một middleware đơn giản để ghi lại thông tin về mỗi request đến ứng dụng Django.
    
Dưới đây là ví dụ mã code về một middleware đơn giản để ghi lại thông tin về mỗi request đến ứng dụng Django:

**1. File `myapp/middleware.py`:**

Python

```python
from django.utils.deprecation import MiddlewareMixin
from django.conf import settings

class RequestLoggerMiddleware(MiddlewareMixin):

    def process_request(self, request):
        """
        Ghi lại thông tin về request vào log.
        """
        logger = settings.LOGGING['loggers']['django']['handlers']['console']['logger']
        logger.info(
            f"Request: {request.method} {request.path} {request.META['REMOTE_ADDR']}"
        )

```

**2. Cấu hình middleware:**

Thêm middleware vào file `settings.py`:

Python

```
MIDDLEWARE = [
    ...
    'myapp.middleware.RequestLoggerMiddleware',
]
```

**Giải thích:**

- Middleware này kế thừa từ `MiddlewareMixin`.
- Phương thức `process_request` được gọi trước khi view xử lý request.
- Phương thức này sử dụng logger được cấu hình trong `settings.py` để ghi thông tin về request vào log.
- Thông tin ghi log bao gồm:
    - Phương thức HTTP
    - URL
    - Địa chỉ IP của client

## 5. ORM (Object-Relational Mapping) trong Django:
###  5.1 ORM trong Django là gì

ORM là viết tắt của Object-Relational Mapping. Nó là một kỹ thuật giúp ‎  ánh xạ các đối tượng trong Python sang các bảng trong cơ sở dữ liệu. ORM trong Django được xây dựng dựa trên thư viện SQLAlchemy và cung cấp một API đơn giản để truy cập và thao tác dữ liệu.

- ORM giúp tách biệt logic ứng dụng khỏi logic truy cập cơ sở dữ liệu.
- ORM giúp viết code đơn giản và dễ hiểu hơn.
- ORM giúp tăng hiệu suất truy cập cơ sở dữ liệu.

###  5.2 Làm thế nào để tạo một model và thực hiện truy vấn dữ liệu?

**Làm thế nào để tạo một model và thực hiện truy vấn dữ liệu?**

**Tạo model:**

1. Sử dụng `models.Model` để tạo một class cho model.
2. Định nghĩa các thuộc tính của model bằng các field types như `CharField`, `IntegerField`, `BooleanField`, v.v.
3. Sử dụng `models.Manager` để quản lý các instance của model.

**Ví dụ:**

```python
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    objects = models.Manager()
```

**Truy vấn dữ liệu:**

- Sử dụng các phương thức của `models.Manager` để truy vấn dữ liệu.
- Ví dụ:
    - `Book.objects.all()` lấy tất cả các instance của model `Book`.
    - `Book.objects.filter(title='Đắc Nhân Tâm')` lấy tất cả các instance của model `Book` có `title` là "Đắc Nhân Tâm".
    - `Book.objects.get(id=1)` lấy instance của model `Book` có `id` là 1.

**Ví dụ:**

```python
# Lấy tất cả các sách
books = Book.objects.all()

# Lấy các sách có giá cao hơn 100
expensive_books = Book.objects.filter(price__gt=100)

# Lấy sách có id là 1
book = Book.objects.get(id=1)
```


### 5.3. Ví dụ mã code: Viết một model đơn giản và thực hiện truy vấn để lấy danh sách các bài viết từ database.

**File `myapp/models.py`:**

```python
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=255)
    published_date = models.DateField()

    objects = models.Manager()
```

**2. File `myapp/views.py`:**

```python
from django.shortcuts import render

def blog_view(request):
    # Lấy danh sách bài viết
    posts = Post.objects.all()

    # Sắp xếp theo ngày đăng mới nhất
    posts = posts.order_by('-published_date')

    # Lấy 5 bài viết mới nhất
    # posts = posts[:5]

    return render(request, 'blog.html', {'posts': posts})
```

**3. File `myapp/templates/blog.html`:**

```HTML
{% for post in posts %}
    <h2>{{ post.title }}</h2>
    <p>{{ post.content }}</p>
    <p>Tác giả: {{ post.author }}</p>
    <p>Ngày đăng: {{ post.published_date }}</p>
{% endfor %}
```

## 6. RESTful API trong Django:

### 6.1 RESTful API là gì?

RESTful API là một kiến trúc phần mềm cho phép các ứng dụng web giao tiếp với nhau thông qua HTTP. RESTful API sử dụng các phương thức HTTP như GET, POST, PUT, DELETE để thực hiện các thao tác CRUD (Create, Read, Update, Delete) trên dữ liệu.

**Đặc điểm của RESTful API:**

- **Tài nguyên:** Dữ liệu được biểu diễn dưới dạng các tài nguyên.
- **URI:** Mỗi tài nguyên được xác định bởi một Uniform Resource Identifier (URI).
- **Phương thức HTTP:** Các phương thức HTTP được sử dụng để thực hiện các thao tác CRUD trên tài nguyên.
- **MIME types:** Các MIME types được sử dụng để định dạng dữ liệu được trả về bởi API.
- **Hypermedia:** API sử dụng hypermedia để liên kết các tài nguyên với nhau.

**Lợi ích của RESTful API:**

- **Dễ sử dụng:** RESTful API dễ hiểu và dễ sử dụng cho các nhà phát triển.
- **Khả năng mở rộng:** RESTful API có thể được mở rộng để hỗ trợ nhiều tài nguyên và thao tác hơn.
- **Hiệu suất:** RESTful API có thể được tối ưu hóa để có hiệu suất cao.
- **Bảo mật:** RESTful API có thể được bảo mật bằng các phương thức xác thực và ủy quyền.
### 6.2. Làm thế nào để xây dựng RESTful API bằng Django Rest Framework?

**. Cài đặt DRF:**

```python
pip install djangorestframework
```

**2. Thêm DRF vào settings.py:**

```Python
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

**3. Tạo model:**

```python
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    objects = models.Manager()
```

**4. Tạo serializer:**

```python
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'price')
```

**5. Tạo viewset:**

```python
from rest_framework import viewsets

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
```

**6. Thêm URL vào urls.py:**

```python
from django.urls import path, include

urlpatterns = [
    ...
    path('api/', include('myapp.urls')),
]

# myapp/urls.py
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('books', BookViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
```

**7. Chạy ứng dụng:**

```python
python manage.py runserver
```

**8. Truy cập API:**
```
- GET /api/books/ - Lấy danh sách tất cả sách.
- GET /api/books/<id>/ - Lấy thông tin chi tiết của sách có id là <id>.
- POST /api/books/ - Tạo một sách mới.
- PUT /api/books/<id>/ - Cập nhật thông tin sách có id là <id>.
- DELETE /api/books/<id>/ - Xóa sách có id là <id>.
```

### 6.3. Ví dụ mã code: Tạo một API endpoint để lấy danh sách người dùng.

**1. Cài đặt DRF:**

```python
pip install djangorestframework
```

**2. Thêm DRF vào settings.py:**

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

**3. Tạo model:**

```python
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    is_active = models.BooleanField(default=True)

    objects = models.Manager()
```

**4. Tạo serializer:**

```python
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_active')
```

**5. Tạo viewset:**

```python
from rest_framework import viewsets

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
```

**Thêm URL vào urls.py:**

```python
from django.urls import path, include

urlpatterns = [
    ...
    path('api/', include('myapp.urls')),
]

# myapp/urls.py
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
```

## 7. Testing trong Django:

### 7.1. Tại sao việc viết unit test và integration test quan trọng? 

Việc viết unit test và integration test quan trọng vì những lý do sau:

**1. Phát hiện lỗi:**

- Unit test giúp phát hiện lỗi trong code.
- Integration test giúp phát hiện lỗi trong cách các module khác nhau tương tác với nhau.

**2. Đảm bảo chất lượng:**

- Unit test và integration test giúp đảm bảo chất lượng code của ‎ .
- Việc chạy test thường xuyên giúp ‎  đảm bảo code của ‎  không bị lỗi sau khi thay đổi.

**3. Tiết kiệm thời gian:**

- Việc phát hiện lỗi sớm giúp ‎  tiết kiệm thời gian và công sức.
- Việc chạy test tự động giúp ‎  tiết kiệm thời gian so với việc test thủ công.

**4. Tăng độ tin cậy:**

- Việc viết test giúp tăng độ tin cậy của code của ‎ .
- Code được test tốt sẽ hoạt động ổn định và ít lỗi hơn.

**5. Dễ dàng refactor code:**

- Việc viết test giúp ‎  dễ dàng refactor code.
- Test giúp ‎  đảm bảo code refactor vẫn hoạt động chính xác.
### 7.2 Làm thế nào để viết các test case cho ứng dụng Django?

**Cài đặt thư viện test:**

```python
pip install unittest
```

**2. Tạo file test:**

Tạo file `tests.py` trong thư mục app.

**3. Viết unit test:**

```python
from django.test import TestCase

class MyTest(TestCase):
    def test_my_function(self):
        # ...
```

**4. Chạy test:**

```python
python manage.py test
```
    
### 7.3. Ví dụ mã code: Viết một test case kiểm tra tính hợp lệ của form đăng ký người dùng.

```python
from django.test import TestCase

class UserRegistrationTest(TestCase):
    def test_valid_username(self):
        data = {'username': 'hoangnhat', 'email': 'hoangnhat@gmail.com', 'password': 'Hoang12345'}
        response = self.client.post('/register/', data=data)
        self.assertEqual(response.status_code, 302)

    def test_invalid_username(self):
        data = {'username': '123', 'email': 'hoangnhat@gmail.com', 'password': 'Hoang12345'}
        response = self.client.post('/register/', data=data)
        self.assertFormError(response, 'username', 'Username không hợp lệ.')
```

**Mục tiêu:** Kiểm tra tính hợp lệ của các trường dữ liệu trong form đăng ký người dùng.

**Dữ liệu đầu vào:**

- **Username:**
    - Hợp lệ:
        - `hoangnhat`
        - `nhathoang`
        - `_nhat123`
    - Không hợp lệ:
        - `123` (chỉ số)
        - `hoang nhat` (khoảng trắng)
        - `hoang@gmail.com` (email)
- **Email:**
    - Hợp lệ:
        - `hoangnhat@gmail.com`
        - `nguyen.hoang@example.com`
    - Không hợp lệ:
        - `hoangnhat` (không có @)
        - `hoang@gmail` (thiếu đuôi)
        - `123@gmail.com` (username không hợp lệ)
- **Password:**
    - Hợp lệ:
        - `Hoang12345` (mật khẩu mạnh)
        - `hoangnhat123` (kết hợp chữ hoa và thường)
    - Không hợp lệ:
        - `123456` (mật khẩu yếu)
        - `hoangnhat` (quá ngắn)
        - `hoang nhat` (khoảng trắng)

**Test cases:**

| **STT** | **Trường dữ liệu** | **Giá trị đầu vào** | **Kết quả mong đợi**                           |
| ------- | ------------------ | ------------------- | ---------------------------------------------- |
| 1       | Username           | Hợp lệ              | Hiển thị thông báo đăng ký thành công          |
| 2       | Username           | Không hợp lệ        | Hiển thị thông báo lỗi (username không hợp lệ) |
| 3       | Email              | Hợp lệ              | Hiển thị thông báo đăng ký thành công          |
| 4       | Email              | Không hợp lệ        | Hiển thị thông báo lỗi (email không hợp lệ)    |
| 5       | Password           | Hợp lệ              | Hiển thị thông báo đăng ký thành công          |
| 6       | Password           | Không hợp lệ        | Hiển thị thông báo lỗi (mật khẩu không hợp lệ) |
## 8. Authentication và Authorization trong Django:

### 8.1. So sánh giữa authentication và authorization. 

**Authentication:**

- Là quá trình xác định danh tính của người dùng.
- Xác minh xem người dùng có phải là ai họ nói họ là.
- Thường sử dụng username, password, token, v.v.

**Authorization:**

- Là quá trình xác định quyền truy cập của người dùng.
- Xác định những gì người dùng được phép làm trong hệ thống.
- Dựa trên roles, permissions, v.v.

**Ví dụ:**

- **Authentication:** Khi bạn đăng nhập vào website, bạn cần cung cấp username và password để xác minh danh tính.
- **Authorization:** Sau khi đăng nhập, bạn chỉ có thể truy cập những trang web và chức năng mà bạn được phép truy cập dựa trên role của bạn.
### 8.2. Làm thế nào để xác thực người dùng và kiểm tra quyền truy cập trong Django?

**Xác thực người dùng:**

- Sử dụng mô hình `User` của Django để lưu trữ thông tin người dùng.
- Hỗ trợ nhiều phương thức xác thực, ví dụ:
    
    - Username và password
    - Token
    - Social authentication (Google, Facebook, v.v.)
    

**Kiểm tra quyền truy cập:**

- Sử dụng hệ thống permission của Django để xác định những gì người dùng được phép làm.
- Có thể dựa trên:
    
    - Nhóm người dùng (groups)
    - Quyền riêng lẻ (permissions)
    

**Ví dụ:**

- **Xác thực:** Sử dụng `django.contrib.auth` để authenticate người dùng bằng username và password.
- **Kiểm tra quyền truy cập:** Sử dụng decorator `@login_required` để đảm bảo chỉ người dùng đã đăng nhập mới có thể truy cập trang web.
### 8.3. Ví dụ mã code: Tạo một trang yêu cầu đăng nhập để xem danh sách bài viết.

**Vị trí file:**

- `myproject/urls.py`: Khai báo URL cho trang đăng nhập và danh sách bài viết.
- `myproject/views.py`: Xử lý logic cho trang đăng nhập và danh sách bài viết.
- `myproject/templates/login.html`: Template cho trang đăng nhập.
- `myproject/templates/blog/list.html`: Template cho danh sách bài viết.

**Code:**

**myproject/urls.py:**

```python
from django.contrib.auth.views import LoginView
from django.urls import path

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('blog/', include('blog.urls')),
]
```

**myproject/views.py:**

```python
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def blog_list(request):
    # Lấy danh sách bài viết
    # ...

    return render(request, 'blog/list.html', {'posts': posts})

@login_required
def blog_list_authenticated(request):
    # Chỉ người dùng đã đăng nhập mới có thể truy cập
    return blog_list(request)
```

**myproject/templates/login.html:**

```HTML
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Đăng nhập</title>
</head>
<body>
    <h1>Đăng nhập</h1>
    <form action="{% url 'login' %}" method="post">
        {% csrf_token %}
        <label for="username">Tên đăng nhập:</label>
        <input type="text" id="username" name="username">
        <br>
        <label for="password">Mật khẩu:</label>
        <input type="password" id="password" name="password">
        <br>
        <input type="submit" value="Đăng nhập">
    </form>
</body>
</html>
```

**myproject/templates/blog/list.html:**

```HTML
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Danh sách bài viết</title>
</head>
<body>
    <h1>Danh sách bài viết</h1>
    {% for post in posts %}
        <h2>{{ post.title }}</h2>
        <p>{{ post.content }}</p>
    {% endfor %}
</body>
</html>
```
    

## 9. Cấu trúc lưu trữ và cơ chế bộ nhớ trong MongoDB:
### 9.1. Cấu trúc lưu trữ của MongoDB dựa trên gì?

MongoDB sử dụng cấu trúc lưu trữ **BSON** (Binary JSON) để lưu trữ dữ liệu. BSON là định dạng nhị phân được tối ưu hóa cho việc lưu trữ và truy xuất dữ liệu trong MongoDB.

**Lợi ích:**

- Hiệu quả: BSON được thiết kế để lưu trữ dữ liệu một cách hiệu quả, sử dụng ít dung lượng hơn JSON truyền thống.
- Linh hoạt: BSON hỗ trợ nhiều kiểu dữ liệu khác nhau, bao gồm số nguyên, chuỗi, ngày giờ, mảng và tài liệu.
- Mở rộng: BSON có thể được sử dụng để lưu trữ lượng dữ liệu khổng lồ.

**Cấu trúc:**

- **Tài liệu:** Đơn vị dữ liệu cơ bản trong MongoDB.
- **Bộ sưu tập:** Nhóm các tài liệu có cùng cấu trúc.
- **Cơ sở dữ liệu:** Nhóm các bộ sưu tập.

**Mối quan hệ:**

- **_id:** Mỗi tài liệu trong MongoDB có một trường _id duy nhất.
- **Embedded Documents:** Tài liệu có thể được nhúng vào các tài liệu khác.
- **References:** Tài liệu có thể tham khảo các tài liệu khác thông qua trường _id.

**Ví dụ:**

- Tài liệu mô tả người dùng:

JSON

```json
{
    "_id": "1234567890",
    "name": "Hoang Minh Nhat",
    "age": 30,
    "address": {
        "street": "123 P7 Phu Nhuan",
        "city": "HCM City",
        "state": "HCM",
        "zip": "96000"
    }
}
```

**Cơ chế bộ nhớ:**

- MongoDB sử dụng **MMAP** (Memory-Mapped Files) để ánh xạ dữ liệu vào bộ nhớ.
- **WiredTiger** là bộ lưu trữ mặc định cho MongoDB, cung cấp hiệu suất cao và khả năng mở rộng.
- **Journaling:** MongoDB sử dụng journaling để đảm bảo tính toàn vẹn dữ liệu trong trường hợp xảy ra lỗi.

### 9.2 Làm thế nào MongoDB xử lý bộ nhớ?

MongoDB sử dụng một số kỹ thuật để quản lý bộ nhớ hiệu quả:

**1. MMAP (Memory-Mapped Files):**

- Ánh xạ dữ liệu trực tiếp vào bộ nhớ từ ổ đĩa.
- Giúp truy cập dữ liệu nhanh chóng.
- Giảm thiểu việc sao chép dữ liệu.

**2. WiredTiger:**

- Bộ lưu trữ mặc định cho MongoDB.
- Cung cấp hiệu suất cao và khả năng mở rộng.
- Sử dụng nhiều kỹ thuật tối ưu hóa bộ nhớ, bao gồm:
    
    - **B-tree:** Cấu trúc dữ liệu hiệu quả cho việc truy vấn dữ liệu.
    - **Lempel-Ziv-Storer-Szymanski (LZSS):** Thuật toán nén dữ liệu để giảm dung lượng lưu trữ.
    - **Buffer cache:** Lưu trữ dữ liệu truy cập thường xuyên trong bộ nhớ để truy cập nhanh hơn.
    

**3. Journaling:**

- Ghi lại các thay đổi dữ liệu vào nhật ký để đảm bảo tính toàn vẹn dữ liệu trong trường hợp xảy ra lỗi.
- Giúp phục hồi dữ liệu trong trường hợp mất điện hoặc lỗi phần cứng.
- Có thể ảnh hưởng đến hiệu suất nếu được cấu hình không hợp lý.

**4. Cấu hình bộ nhớ:**

- Có thể cấu hình MongoDB để sử dụng nhiều bộ nhớ hơn hoặc ít hơn.
- Cấu hình bộ nhớ ảnh hưởng đến hiệu suất và khả năng mở rộng của MongoDB.
- Cần cân nhắc các yếu tố như khối lượng dữ liệu, lượng truy cập và yêu cầu hiệu suất khi cấu hình bộ nhớ.

**5. Giám sát bộ nhớ:**

- Sử dụng các công cụ giám sát để theo dõi việc sử dụng bộ nhớ của MongoDB.
- Giúp xác định các vấn đề tiềm ẩn và điều chỉnh cấu hình bộ nhớ khi cần thiết.
### 9.3. Ví dụ mã code: Thêm một document mới vào collection.

**Vị trí file:**

- `myproject/models.py`: Định nghĩa model Django cho dữ liệu được lưu trữ trong MongoDB.
- `myproject/views.py`: Xử lý logic thêm document.

**Cài đặt PyMongo:**

```python
pip install pymongo
```

**Model Django:**

Python

```python
# Định nghĩa model Django trong models.py

from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
```

**Thêm document:**

```python
# Xử lý logic thêm document trong views.py

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db = client['my_database']
collection = db['my_collection']

# Tạo document mới
document = {'name': 'John Doe', 'age': 30}

# Thêm document vào collection
collection.insert_one(document)
```
## 10. Wire Protocol trong MongoDB:

### 10.1. Wire Protocol là gì?

Wire Protocol là gì?

Wire Protocol là giao thức mạng được sử dụng để truyền dữ liệu giữa các máy chủ MongoDB và các ứng dụng khách. Nó là một giao thức nhị phân được thiết kế để hiệu quả và có thể mở rộng.

**Chức năng:**

- Truyền tải các yêu cầu và phản hồi giữa client và server.
- Cho phép thực hiện các thao tác CRUD (Create, Read, Update, Delete) trên dữ liệu MongoDB.
- Hỗ trợ các tính năng nâng cao như sharding và replication.

**Lợi ích:**

- Hiệu quả: Wire Protocol được thiết kế để truyền dữ liệu nhanh chóng và hiệu quả.
- Mở rộng: Wire Protocol có thể hỗ trợ các ứng dụng lớn với lượng dữ liệu khổng lồ.
- Linh hoạt: Wire Protocol có thể được sử dụng bởi nhiều ngôn ngữ lập trình khác nhau.

**Thành phần:**

- **Header:** Chứa thông tin về loại tin nhắn, độ dài tin nhắn và các cờ khác.
- **Body:** Chứa dữ liệu cụ thể cho loại tin nhắn.

**Loại tin nhắn:**

- **OP_QUERY:** Truy vấn dữ liệu từ MongoDB.
- **OP_INSERT:** Thêm dữ liệu vào MongoDB.
- **OP_UPDATE:** Cập nhật dữ liệu trong MongoDB.
- **OP_DELETE:** Xóa dữ liệu khỏi MongoDB.
### 10.1. Cấu trúc gói tin Wire Protocol bao gồm những gì?

**Cấu trúc cơ bản:**

- **Header:**
    - **Message length (4 bytes):** Độ dài của gói tin (bao gồm cả header).
    - **Request ID (4 bytes):** Mã định danh cho yêu cầu.
    - **Response to (4 bytes):** Mã định danh cho yêu cầu mà gói tin này là phản hồi (nếu có).
    - **Op code (1 byte):** Mã lệnh cho thao tác được thực hiện.
    - **Flags (1 byte):** Cờ cho các tùy chọn bổ sung.
- **Body:**
    - Dữ liệu cụ thể cho loại thao tác được thực hiện.

**Ví dụ:**

- Gói tin OP_QUERY với message length là 100 bytes, request ID là 1234, response to là 0, op code là OP_QUERY và flags là 0:

```
00000000 00000064 00001234 00000000 02 00
... (body) ...
```

**Thành phần header:**

- **Message length:**
    
    - Cho biết độ dài của gói tin (bao gồm cả header).
    - Giúp server xác định vị trí bắt đầu của body.
- **Request ID:**
    
    - Mã định danh duy nhất cho yêu cầu.
    - Giúp server khớp các gói tin phản hồi với các yêu cầu tương ứng.
- **Response to:**
    
    - Mã định danh cho yêu cầu mà gói tin này là phản hồi (nếu có).
    - Giúp client xác định kết quả của yêu cầu.
- **Op code:**
    
    - Mã lệnh cho thao tác được thực hiện.
    - Xác định loại thao tác được thực hiện trên MongoDB.
- **Flags:**
    
    - Cờ cho các tùy chọn bổ sung.
    - Có thể được sử dụng để thay đổi hành vi của thao tác.

**Thành phần body:**

- Dữ liệu cụ thể cho loại thao tác được thực hiện.
- Cấu trúc của body phụ thuộc vào op code.

### 10.3. Ví dụ mã code: Sử dụng PyMongo để thực hiện truy vấn đến MongoDB.

**Vị trí file:**

- `myproject/models.py`: Định nghĩa model Django cho dữ liệu được lưu trữ trong MongoDB.
- `myproject/views.py`: Xử lý logic truy vấn.

**Cài đặt PyMongo:**

```python
pip install pymongo
```

**Model Django:**

```python
# Định nghĩa model Django trong models.py

from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
```

**Truy vấn MongoDB:**

```python
# Xử lý logic truy vấn trong views.py

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db = client['my_database']
collection = db['my_collection']

# Truy vấn tất cả tài liệu
results = collection.find()

# Truy vấn tài liệu theo tên
results = collection.find({'name': 'Nhat Hoang'})

# Lặp qua kết quả
for result in results:
    print(result)
```
    
## 11. Giao dịch và khóa trong MongoDB:
    
### 11.1 Câu hỏi lý thuyết: Làm thế nào để thực hiện giao dịch và khóa trong MongoDB?

**Giao dịch:**

MongoDB không hỗ trợ giao dịch ACID đầy đủ. Tuy nhiên, nó cung cấp một số tính năng để đảm bảo tính nhất quán dữ liệu trong các hoạt động cập nhật:

- **Write Concern:** Xác định mức độ đảm bảo ghi cho các hoạt động.
- **Journaling:** Ghi lại các thay đổi dữ liệu để phục hồi trong trường hợp lỗi.
- **Replication:** Sao chép dữ liệu sang nhiều máy chủ để tăng tính sẵn sàng và khả năng phục hồi.

**Khóa:**

MongoDB cung cấp các loại khóa sau:

- **Document-level locks:** Khóa cấp tài liệu, chỉ cho phép một hoạt động truy cập tài liệu đó tại một thời điểm.
- **Collection-level locks:** Khóa cấp bộ sưu tập, chỉ cho phép một hoạt động truy cập bộ sưu tập đó tại một thời điểm.
- **Database-level locks:** Khóa cấp cơ sở dữ liệu, chỉ cho phép một hoạt động truy cập cơ sở dữ liệu đó tại một thời điểm.

**Sử dụng:**

- **Write Concern:** Sử dụng `w` và `j` để đảm bảo dữ liệu được ghi và ghi nhật ký trước khi trả về.
- **Journaling:** Bật journaling để đảm bảo dữ liệu có thể được phục hồi trong trường hợp lỗi.
- **Replication:** Sao chép dữ liệu để tăng tính sẵn sàng và khả năng phục hồi.
- **Document-level locks:** Sử dụng `findAndModify` với `upsert` để khóa và cập nhật tài liệu.
- **Collection-level locks:** Sử dụng `lock` và `unlock` để khóa và mở khóa bộ sưu tập.
- **Database-level locks:** Sử dụng `fsync` để khóa cơ sở dữ liệu.
### 11.2 Ví dụ mã code: Viết một ví dụ về giao dịch sử dụng start_session và commit_transaction.

**Vị trí file:**

- `myproject/views.py`: Xử lý logic cho giao dịch.

```python
from django.contrib.sessions.models import Session
from django.db import transaction

def my_view(request):
    # Bắt đầu phiên mới
    session = Session()
    session.save()

    # Bắt đầu giao dịch
    with transaction.atomic():
        # Thực hiện các hoạt động cập nhật
        # ...

        # Ghi nhận giao dịch
        transaction.commit()

    # Xóa phiên
    session.delete()
```
    
## 12. Mở rộng dữ liệu trong MongoDB:
### 12.1 Câu hỏi lý thuyết: Khi nào và ở mức độ nào dữ liệu được mở rộng đến nhiều lát?

**Mở rộng dữ liệu** trong MongoDB là quá trình chia dữ liệu thành các phần nhỏ hơn được gọi là **lát**. Lát được phân phối trên nhiều máy chủ, giúp tăng khả năng mở rộng và hiệu suất cho các truy vấn lớn.

**Khi nào:**

- Khi lượng dữ liệu tăng lên và không thể lưu trữ trên một máy chủ duy nhất.
- Khi cần cải thiện hiệu suất cho các truy vấn lớn.

**Mức độ:**

- **Cấp shard:** Dữ liệu được chia thành các shard dựa trên một key shard.
- **Cấp chunk:** Mỗi shard được chia thành các chunk nhỏ hơn.

**Quyết định mức độ mở rộng:**

- Phụ thuộc vào nhu cầu cụ thể của ứng dụng.
- Cần cân nhắc các yếu tố như lượng dữ liệu, loại truy vấn và hiệu suất mong muốn.
### 12.2 Ví dụ mã code: Sử dụng sharding để mở rộng dữ liệu trong MongoDB.

**Vị trí file:**

- `myproject/settings.py`: Cấu hình sharding cho MongoDB.
- `myproject/models.py`: Định nghĩa model Django cho dữ liệu được shard.

**Cấu hình sharding:**

```python
# Cấu hình sharding trong settings.py

MONGODB_SETTINGS = {
    'db': 'my_database',
    'username': 'my_username',
    'password': 'my_password',
    'authSource': 'admin',
    'replicaSet': 'my_replica_set',
    'sharded': True,
    'shard_key': {'_id': 'hashed'},
}
```

**Model Django:**

```python
# Định nghĩa model Django trong models.py

from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
```

# II: Thực hành

Bài 1:

Xây dựng một ứng dụng Django đơn giản quản lý danh sách sinh viên với các yêu cầu sau:

Cơ sở dữ liệu sử dụng MongoDB.

Có chức năng CRUD (Create, Read, Update, Delete) sinh viên.

Mỗi sinh viên có các thông tin: Họ tên, ngày sinh, lớp, điểm trung bình.

Có trang hiển thị danh sách sinh viên và chi tiết sinh viên.

Sử dụng Django Template để render giao diện.

Bài 2:

Xây dựng một API đơn giản sử dụng Django REST Framework và MongoDB để quản lý danh sách sản phẩm với các yêu cầu sau:

Cơ sở dữ liệu sử dụng MongoDB.

Có các endpoint để thực hiện CRUD (Create, Read, Update, Delete) sản phẩm.

Mỗi sản phẩm có các thông tin: Tên sản phẩm, giá, mô tả, danh mục.

Sử dụng Django REST Framework Serializers để serialize/deserialize dữ liệu.

Triển khai xác thực và phân quyền đơn giản cho API.

Lưu ý: Ứng viên có thể sử dụng bất kỳ công cụ, thư viện hỗ trợ nào để hoàn thành bài tập.

Chúc ứng viên may mắn!

**