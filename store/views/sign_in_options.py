from django.shortcuts import render
from django.views.generic import View


class SignInOptionsView(View):
    def get(self, *args, **kwargs):
        return render(self.request, "sign_in_options.html", {})
