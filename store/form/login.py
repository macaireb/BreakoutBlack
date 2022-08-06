from allauth.account.forms import LoginForm


class StoreLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(StoreLoginForm, self).__init__(*args, **kwargs)
