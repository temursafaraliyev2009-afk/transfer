from django.shortcuts import render

from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import TransferWindow
from .forms import TransferWindowForm



def home(request):
    search = request.GET.get('search', '')

    players = TransferWindow.objects.all().order_by('-id')

    if search:
        players = players.filter(
            Q(name__icontains=search) |
            Q(club__icontains=search)
        )

    context = {
        'players': players,
        'search': search,
    }

    return render(request, 'home.html', context)



def player_detail(request, pk):
    player = get_object_or_404(TransferWindow, pk=pk)

    return render(request, 'detail.html', {
        'player': player
    })



def player_create(request):
    if request.method == 'POST':
        form = TransferWindowForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = TransferWindowForm()

    return render(request, 'create.html', {
        'form': form
    })


def player_update(request, pk):
    player = get_object_or_404(TransferWindow, pk=pk)

    if request.method == 'POST':
        form = TransferWindowForm(
            request.POST,
            request.FILES,
            instance=player
        )

        if form.is_valid():
            form.save()
            return redirect('detail', pk=player.pk)

    else:
        form = TransferWindowForm(instance=player)

    return render(request, 'update.html', {
        'form': form,
        'player': player
    })


def player_delete(request, pk):
    player = get_object_or_404(TransferWindow, pk=pk)

    if request.method == 'POST':
        player.delete()
        return redirect('home')

    return render(request, 'delete.html', {
        'player': player
    })