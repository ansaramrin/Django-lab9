from django.urls import path

from category.views import category_list, category_detail

urlpatterns = [
    path('categories/', category_list),
    path('categories/<int:category_id>/', category_detail)

]