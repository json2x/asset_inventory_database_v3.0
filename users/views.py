from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active = False
            user.save()
            #username = form.cleaned_data.get('username')
            #messages.success(request, f'Account created for {username}')
            return redirect('home')
    else:
        form = UserRegisterForm()
        
    return render(request, 'users/register.html', {'form': form})


def user_router(request):
    print(request.user.groups)
    groups_list = []
    for g in request.user.groups.all():
        groups_list.append(g.name)

    if not request.GET.get('next'):
        if 'AID_USER_GROUP' in groups_list:
            return redirect('edrar_home')
        else:
            return redirect('datatable_device')
    else:
        return redirect(request.GET.get('next'))

    


