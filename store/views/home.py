from django.shortcuts import render


def home_view(request):
    context = {}
    return render(request, 'home.html', context)

def third_party(request):
    context = {}
    return render(request, 'account/third party.html', context)
