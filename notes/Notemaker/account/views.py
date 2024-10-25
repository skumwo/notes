from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, 'main/index.html', {'section': 'dashboard'})


from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordResetForm
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

class PasswordResetRequestView(FormView):
    template_name = 'password_reset_form.html'
    success_url = reverse_lazy('password_reset_done')
    form_class = PasswordResetForm

    def form_valid(self, form):
        form.save(
            request=self.request,
            use_https=self.request.is_secure(),
            from_email='webmaster@localhost',
            email_template_name='password_reset_email.html'
        )
        return super().form_valid(form)




def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save()
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
        return render(request, 'account/register.html', {'user_form': user_form})


def register_done(request):
    return render(request, 'account/dashboard.html')

