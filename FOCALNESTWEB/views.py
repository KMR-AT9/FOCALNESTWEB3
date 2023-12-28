from django.contrib.auth.views import LoginView

class login_page(LoginView):
    template_name = 'admin/login.html' 

class FocalNestAdminView(LoginView):
    template_name = 'admin/index.html'

class MainAdminView(LoginView):
    template_name = 'admin/home.html'
    
