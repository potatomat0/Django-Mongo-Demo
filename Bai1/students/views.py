from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from .models import student
from .forms import studentForm

from django.views.generic import ListView, DetailView, \
    CreateView, UpdateView, DeleteView

class studentListView(ListView):
    model = student
    context_object_name = 'students'

class studentDetailView(DetailView):
    model = student

class studentCreateView(CreateView):
    model = student
    form_class = studentForm
    success_url = reverse_lazy('students:student_list')

class studentUpdateView(UpdateView):
    model = student
    form_class = studentForm
    success_url = reverse_lazy('students:student_list')

class studentDeleteView(DeleteView):
    model = student
    success_url = reverse_lazy('students:student_list')
