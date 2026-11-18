from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import ItemOrRecord
from .forms import ItemForm

@login_required
def item_list_view(request):
    if request.user.role == 'ADMIN':
        items = ItemOrRecord.objects.all()
    else:
        items = ItemOrRecord.objects.filter(user=request.user)
    return render(request, 'core/item_list.html', {'items': items})

@login_required
def item_create_view(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            messages.success(request, "Record created successfully!")
            return redirect('item_list')
    else:
        form = ItemForm()
    return render(request, 'core/item_form.html', {'form': form})

@login_required
def item_update_view(request, pk):
    item = get_object_or_404(ItemOrRecord, pk=pk)
    if request.user.role != 'ADMIN' and item.user != request.user:
        messages.error(request, "You do not have permission to edit this record.")
        return redirect('item_list')
    
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, "Record updated successfully!")
            return redirect('item_list')
    else:
        form = ItemForm(instance=item)
    return render(request, 'core/item_form.html', {'form': form})

@login_required
def item_delete_view(request, pk):
    item = get_object_or_404(ItemOrRecord, pk=pk)
    if request.user.role != 'ADMIN' and item.user != request.user:
        messages.error(request, "You do not have permission to delete this record.")
        return redirect('item_list')
    
    if request.method == 'POST':
        item.delete()
        messages.success(request, "Record deleted successfully!")
        return redirect('item_list')
    return render(request, 'core/item_confirm_delete.html', {'item': item})