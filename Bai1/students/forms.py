#-*- coding:utf-8 -*-
from .models import student
from django import forms

class studentForm(forms.ModelForm):

    class Meta:
        model = student
        fields = "__all__"
