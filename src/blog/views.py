from django.shortcuts import render, redirect

from django.contrib import auth


def home(request):
    return render(request, "blog/home.html")


def signin(request):
    if request.method == "POST":
        # Query from db and validate
        user = auth.authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user is not None:
            # Bring the user object to the global session
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request,
                          'blog/signin.html',
                          {'error': 'username or password is incorect'})
    else:
        return render(request, "blog/signin.html")


def signout(request):
    if request.method == "POST":
        auth.logout(request)
    return redirect("home")
