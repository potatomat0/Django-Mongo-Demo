#-*- coding:utf-8 -*-

from django.urls import path, re_path
from . import views

# namespace
app_name = 'students'

urlpatterns = [
    # tạo một học sinh
    path('create/', views.studentCreateView.as_view(), name='student_create'),
    # tìm nhiều học sinh
    path('', views.studentListView.as_view(), name='student_list'),
    # tìm một học sinh
    re_path(r'^(?P<pk>\d+)/$', views.studentDetailView.as_view(), name='student_detail'),
    # Cập nhật học sinh
    re_path(r'^(?P<pk>\d+)/update/$', views.studentUpdateView.as_view(), name='student_update'),
    # xóa học sinh
    re_path(r'^(?P<pk>\d+)/delete/$', views.studentDeleteView.as_view(), name='student_delete')
]