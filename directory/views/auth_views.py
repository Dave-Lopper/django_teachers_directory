from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from ..forms import LoginForm


def logout_view(request):
    logout(request)
    return redirect('directory:index')


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            return_value = authenticate(
                request=request,
                username=form.cleaned_data.get("username"),
                password=form.cleaned_data.get("password"))
            if return_value is not None:
                login(request, return_value)
                return redirect('directory:index')
            else:
                form.add_error("password",
                               "Please check your credentials and try again"
                               )
        return render(request, "login.html", {"form": form})

    else:
        form = LoginForm()
        return render(request, "login.html", {"form": form})
