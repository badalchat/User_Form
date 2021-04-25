from django.shortcuts import render
from Project.settings import EMAIL_HOST_USER
from app import forms
from django.core.mail import send_mail
from app.models import RegForm

# Create your views here.


def ModelView(request):
    data_list = RegForm.objects.all()
    my_dict = {'my_dict': data_list}
    return render(request, 'listview.html', context=my_dict)


# Save Data into DataBase and Send Confirmation Email to User
def UserView(request):
    if request.method == 'POST':
        form = forms.UserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            subject = 'Message Send By Badal Kumar'
            message = 'Thanks for submiting Form'
            recepient = str(form['Email'].value())
            send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently=False)
            return ModelView(request)
    else:
        form = forms.UserForm()
    return render(request, 'userform.html', {'form': form})
