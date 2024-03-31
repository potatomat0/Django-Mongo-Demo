from django.db import models


class product(models.Model):
    # tên, ghi chú, giá thành, danh mục
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200, blank=False, default='')
    category = models.CharField(max_length=50, default='')
    price = models.FloatField(default=100)
