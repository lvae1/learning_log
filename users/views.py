from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def register(request):
    '''Регистрирует нового пользователя'''
    if request.method != 'POST':
        # Выводит пустую формурегистрации
        form = UserCreationForm()
    else:
        # Обработка заполненной формы
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # Выполнение входа и перенаправления на домашнюю страницу
            login(request, new_user)
            return redirect('learning_logs:index')
    # Вывести пустую или недействительную форму
    context = {'form': form}
    return render(request, 'registration/register.html', context)

     