from django.shortcuts import render
from .my_captcha import FormWithCaptcha

def home(request):
    context = {
        'captcha': FormWithCaptcha,
    }
    return render(request, 'account/login.html', context)


# from .my_captcha import FormWithCaptcha

# def home(request):
#     if request.method == 'POST':
#         form = FormWithCaptcha(request.POST)
#         if form.is_valid():
#             # process the form data here
#             pass
#     else:
#         form = FormWithCaptcha()

#     context = {
#         'form': form,
#     }
#     return render(request, 'index.html', context)
