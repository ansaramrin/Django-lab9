from django.shortcuts import render

from django.http.response import JsonResponse

from category.models import Category

def category_list(request):
    # SELECT * FROM store_category;
    categories = Category.objects.all()
    categories_json = [category.to_json() for category in categories]
    return JsonResponse(categories_json, safe=False)

def category_detail(request, category_id):
    # SELECT * FROM store_category WHERE id = <category_id>;
    try:
        category = Category.objects.get(id = category_id)
    except Category.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)

    return JsonResponse(category.to_json())
