from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('products/', views.products,name="products"),
    path('create_sale/', views.create_sale, name='create_sale'),
    path('sales_list/', views.sales_list, name='sales_list'),
    path('export_sales_to_excel/', views.export_sales_to_excel, name='export_sales_to_excel'),
    path('no_stock_show/', views.no_stock_show, name='no_stock_show'),
    path('create_product/', views.create_product,name='create_product'),
    path('add_existing_product/', views.add_existing_product,name='add_existing_product'),
    path('delete/<int:pk>/', views.delete_product,name='delete'),
]