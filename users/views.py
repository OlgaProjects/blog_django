from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import OurRegistration, UserUpdateForm, ProfileAvatar

def register(request):
    if request.method == 'POST':
        form = OurRegistration(request.POST)
        if form.is_valid(): #проверка на валидность,если все верно, юзер сохраняется
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Пользователь {username} был успешно зарегестрирован. Войдите!')
            return redirect('login')
        else:
            form = OurRegistration()
    form = OurRegistration()
    return render(request, 'users/registration.html', {'form': form})

@login_required #Если пользователь не авторизован, то перенаправляет его на URL, указанный в параметре конфигурации settings.LOGIN_URL, передавая текущий абсолютный путь в запросе.
def profile(request):
    if request.method == 'POST':
        avatar_form = ProfileAvatar(request.POST, request.FILES, instance=request.user.profile) #подставляет в полях имя пользователя через instance,получаем данные через request
        update_form = UserUpdateForm(request.POST, instance=request.user)
        
        if update_form.is_valid() and avatar_form.is_valid():
            avatar_form.save()
            update_form.save()
            
            messages.success(request, 'Данные пользователя обновлены!')
            return redirect('profile')
    else:
        avatar_form = ProfileAvatar(instance=request.user.profile) #подставляет в полях имя пользователя через instance
        update_form = UserUpdateForm(instance=request.user)
    return render(request, 'users/profile.html', {'avatar_form': avatar_form, 'update_form': update_form})