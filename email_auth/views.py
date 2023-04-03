# # from django.shortcuts import render

# # Create your views here.
# from django.core.mail import send_mail
# from django.conf import settings
# from django.urls import reverse

# from django.shortcuts import redirect, render
# # from django.urls import reverse
# from django.contrib.auth import get_user_model
# from django.http import Http404

# def send_email_verification_mail(user):
#     subject = 'Verify Your Email Address'
#     message = f'Hi {user.email}, Please click the link below to verify your email address'
#     link = reverse('verify-email', args=[str(user.email_verification_token)])
#     verification_link = settings.FRONTEND_URL + link
#     send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False, html_message=verification_link)


# User = get_user_model()

# def verify_email(request, token):
#     try:
#         user = User.objects.get(email_verification_token=token)
#         user.is_email_verified = True
#         user.save()
#         return redirect(reverse('login'))
#     except User.DoesNotExist:
#         raise Http404('Invalid verification token')






# from django.core.mail import send_mail
# from django.shortcuts import render, redirect
# from django.template.loader import render_to_string

# from .forms import ContactForm

# def sendmail(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)

#         if form.is_valid():
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             content = form.cleaned_data['content']

#             html = render_to_string('contact/emails/contactform.html', {
#                 'name': name,
#                 'email': email,
#                 'content': content
#             })

#             send_mail('The contact form subject', 'This is the message', 'noreply@codewithstein.com', ['codewithtestein@gmail.com'], html_message=html)

#             return redirect('index')
#     else:
#         form = ContactForm()

#     return render(request, 'contact/index.html', {
#         'form': form
#     })




from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint
from django.conf import settings

from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from .forms import ContactForm

def sendmail(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            sender_email = form.cleaned_data['email']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']

            # html = render_to_string('contact/emails/contactform.html', {
            #     'name': name,
            #     'email': email,
            #     'content': content
            # })

            # API Config
            configuration = sib_api_v3_sdk.Configuration()
            configuration.api_key['api-key'] = settings.SENDINBLUE_API_KEY
            api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))

            # Sending email
            sender = {"name":"Softglobal","email":sender_email}
            to = [{"email":email,"name":"GrammarPoint"}]
 
            send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(to=to, 
                                                            html_content=content,
                                                            # html_message=html,
                                                            sender=sender,
                                                            subject=name) 
            try:
                api_response = api_instance.send_transac_email(send_smtp_email)
                pprint(api_response)
            except ApiException as e:
                print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)
            
            # send_mail('The contact form subject', 'This is the message', 'noreply@codewithstein.com', ['codewithtestein@gmail.com'], html_message=html)

            return redirect('sendmail') 
    else:
        form = ContactForm()

    return render(request, 'contact/index.html', {
        'form': form
    })



    
    
    
