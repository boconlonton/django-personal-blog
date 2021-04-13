from django.shortcuts import render, redirect, get_object_or_404

from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now

from .models import Item


@login_required
def wlist(request):
    list_items = Item.objects.filter()
    return render(request,
                  'wishlist/home.html',
                  {'list_items': list_items})


@login_required
def detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return render(request,
                  'wishlist/detail.html',
                  {'item': item})


@login_required
def create_update(request):
    if request.method['POST']:
        item = Item()
        item.name = request.POST['name']
        item.url = request.POST['url']
        item.note = request.POST['note']
        item.image = request.FILES['image']
        item.created_at = now()
        item.created_by = request.user
        item.save()
        return redirect('detail', item.id)
    return render(request, 'wishlist/create.html')


@login_required
def delete(request, item_id):
    return render(request, 'wish')