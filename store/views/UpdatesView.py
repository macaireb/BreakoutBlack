from django.shortcuts import render


def updates_view(request):
    return render(request, "updates.html", {})
