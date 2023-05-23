from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Articulo
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin

class ArticleListView(ListView):
    model = Articulo
    template_name = 'ver_articulos.html'
    context_object_name = 'articulos'

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Articulo
    template_name = 'crear_articulo.html'
    fields = ['titulo', 'subtitulo', 'cuerpo', 'autor', 'fecha', 'imagen']
    success_url = reverse_lazy('ver_articulos')
    
    def form_valid(self, form):
        form.instance.creador = self.request.user
        return super().form_valid(form)


class ArticleUpdateView(UpdateView):
    model = Articulo
    template_name = 'editar_articulo.html'
    fields = ['titulo', 'subtitulo', 'cuerpo', 'autor', 'fecha', 'imagen']
    success_url = reverse_lazy('ver_articulos')

class ArticleDeleteView(DeleteView):
    model = Articulo
    template_name = 'eliminar_articulo.html'
    success_url = reverse_lazy('ver_articulos')




def ver_articulo(request, pk):
    articulo = get_object_or_404(Articulo, pk=pk)
    return render(request, 'ver_articulo.html', {'articulo': articulo})
