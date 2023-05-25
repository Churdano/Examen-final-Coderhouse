from django.urls import path
from . import views

urlpatterns = [
    path('articulo/', views.ArticleListView.as_view(), name='ver_articulos'),
    path('articulo/<int:pk>/', views.ver_articulo, name='ver_articulo'),
    path('crear/', views.ArticleCreateView.as_view(), name='crear_articulo'),
    path('editar/<int:pk>/', views.ArticleUpdateView.as_view(), name='editar_articulo'),
    path('eliminar/<int:pk>/', views.ArticleDeleteView.as_view(), name='eliminar_articulo'),
]
