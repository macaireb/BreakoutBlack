from django.shortcuts import render


def new_product_view(request):
    if request.method == "GET":
        context = {}
        return render(request, 'new_product.html', context)
