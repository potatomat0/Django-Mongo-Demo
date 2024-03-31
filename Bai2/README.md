## Sư dung code
> python -m venv venv
> pip install -r requirements.txt

nếu máy dùng:

     windows: 

> .\venv\scripts\activate

    linux: 

> source venv/bin/activate

## test local database: 

### Bước 1: Kết nối với MongoDB

Mở Mongosh và kết nối với database và collection tương ứng với model product.

>mongd 

mở một terminal khác, vào mongosh:

>monngosh

> mongosh "mongodb://localhost:27017/product_db"
> use product_db
Bước 2: Thêm dữ liệu

Sử dụng lệnh db.collection.insertOne() để thêm từng document (dòng dữ liệu) vào collection. Ví dụ:
```
db.products.insertOne({
  title: "Áo thun cotton",
  description: "Áo thun cotton basic, thoải mái và thoáng mát.",
  category: "Quần áo",
  price: 200000
})

db.products.insertOne({
  title: "Điện thoại Samsung Galaxy S23",
  description: "Điện thoại thông minh cao cấp với nhiều tính năng hiện đại.",
  category: "Điện tử",
  price: 25000000
})

db.products.insertOne({
  title: "Sách Lập trình Python cơ bản",
  description: "Sách hướng dẫn lập trình Python cho người mới bắt đầu.",
  category: "Sách",
  price: 150000
})
```
Bước 3: Kiểm tra dữ liệu

Sử dụng lệnh db.collection.find() để xem dữ liệu đã được thêm vào hay chưa. Ví dụ:

> db.products.find()

Lệnh này sẽ hiển thị tất cả các document trong collection products.