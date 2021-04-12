from django.shortcuts import render

from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required
def wish(request):
    return render(request, 'wishlist/me.html')
