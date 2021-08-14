from django.shortcuts import redirect, render
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username} !')
            return redirect('login')
    else:
        form = UserRegistration()
    context = {
        "user_form": form,
    }
    return render(request, 'register.html', context)

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)

        if u_form.is_valid() :
            u_form.save()
            messages.success(request, f'Account Updated')
            return redirect('music_list')
    else:
        u_form = UserUpdateForm(instance=request.user)
    context = {
        'u_form':u_form,
    }
    return render(request, 'profile.html',context)