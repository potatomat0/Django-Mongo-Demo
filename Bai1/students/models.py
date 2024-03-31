from django.db import models


# Create your models here.

class student(models.Model):
    ho_ten = models.CharField(verbose_name="Họ tên", max_length=255)
    ngay_sinh = models.DateField(verbose_name="Ngày sinh")
    lop = models.CharField(verbose_name="Lớp", max_length=20)
    diem_trung_binh = models.DecimalField(verbose_name="Điểm trung bình", max_digits=5, decimal_places=2)

    def __str__(self):
        return self.ho_ten
