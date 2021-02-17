from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name="main"),
    path('account', views.account, name="account"),
    path('log', views.Log_in, name="log"),
    path('reg', views.reg, name="reg"),
    path('shop', views.shop, name="shop"),
    path('create', views.create, name="create"),
    path('change', views.change, name="change"),
    path('login/', auth_views.LoginView.as_view(template_name="regestration/login.html"), name='login'),  # Вход
    path('logout/', auth_views.LogoutView.as_view(template_name="regestration/logged_out.html"), name='logout'),
    # Выход
    path('main', views.dashboard, name='dashboard'),  # Главная страница

    # Смена пароля
    path('password_change/',
         auth_views.PasswordChangeView.as_view(template_name="regestration/password_change_form.html"),
         name='password_change'),  # Изменение пароля
    path('password_change/done',
         auth_views.PasswordChangeDoneView.as_view(template_name="regestration/password_change_done.html"),
         name='password_change_done'),  # Сообщение об успешном изменение пароля

    # Востановление пароля
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='regestration/password_reset_form.html'),
         name='password_reset'),  # Востановление пароля
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='regestration/password_reset_done.html'),
         name='password_reset_done'),  # Сообщение об успешной отправке письма на почту
    path('accounts/reset_password_confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='regestration/password_reset_confirm.html'),
         name='password_reset_confirm'),  # Ввод нового пароля
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='regestration/password_reset_complete.html'),
         name='password_reset_complete'),  # Сообщение об успешном востановление пароля

    # Регистрация
    path('register/', views.register, name='register'),

    # Редактирование профиля
    path('edit/', views.edit, name='edit')
]