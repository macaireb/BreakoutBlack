
from store.form.product import RequestProductForm
from django.shortcuts import render, redirect


def RequestProductView(request):
    if request.method == 'POST':
        try:
            return redirect("store:home")
        except Exception as e:
            print(e)
            return redirect('store:home')
    if request.method == 'GET':
        form = RequestProductForm()
        return render(request, "custom product.html", {'form': form})
