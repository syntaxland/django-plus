# from django.shortcuts import render
# # from future import print_function
# # import time
# import sib_api_v3_sdk
# from sib_api_v3_sdk.rest import ApiException
# from pprint import pprint
# from django.conf import settings

# def send_email(request):
#     configuration = sib_api_v3_sdk.Configuration()
#     configuration.api_key['api-key'] = settings.SENDINBLUE_API_KEY
#     api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
    
#     subject = "Activation Email"
#     html_content = "<html><body><h1>OTP: 494838</h1></body></html>"
#     sender = {"name":"Softglobal","email":"grammarpoint2@gmail.com"}
#     to = [{"email":"chibuzo.okenwa@gmail.com","name":"GrammarPoint"}]

#     # cc = [{"email":"example2@example2.com","name":"Janice Doe"}]
#     # bcc = [{"name":"John Doe","email":"example@example.com"}]
#     # reply_to = {"email":"replyto@domain.com","name":"John Doe"}


#     # params = {"parameter":"My param value","subject":"New Subject"}
#     send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(to=to,
#                                                    html_content=html_content,
#                                                     sender=sender, 
#                                                     subject=subject)

#     try:
#         api_response = api_instance.send_transac_email(send_smtp_email)
#         pprint(api_response)
#         return render(request, 'email_sent.html')
#     except ApiException as e:
#         print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)









# from django.shortcuts import render
# # from future import print_function
# # import time
# import sib_api_v3_sdk
# from sib_api_v3_sdk.rest import ApiException
# from pprint import pprint
# from django.conf import settings

# def send_email(request):
#     configuration = sib_api_v3_sdk.Configuration()
#     configuration.api_key['api-key'] = settings.SENDINBLUE_API_KEY
#     api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
    
#     subject = "Activation Email"
#     html_content = "<html><body><h1>OTP: 553483</h1></body></html>"
#     sender = {"name":"Softglobal","email":"grammarpoint2@gmail.com"}
#     to = [{"email":"chibuzo.okenwa@gmail.com","name":"GrammarPoint"}]

#     send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(to=to,
#                                                    html_content=html_content,
#                                                     sender=sender, 
#                                                     subject=subject)

#     try:
#         api_response = api_instance.send_transac_email(send_smtp_email)
#         pprint(api_response)

#         pprint(subject)
#         pprint(html_content)
#         pprint(sender)
#         pprint(to)
        
#         return render(request, 'email_sent.html')
#     except ApiException as e:
#         print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)





# from django.shortcuts import render
# import sib_api_v3_sdk
# from sib_api_v3_sdk.rest import ApiException
# from pprint import pprint
# from django.conf import settings

# def send_email(request):
#     if request.method == 'POST':
#         sender_email = request.POST.get('sender_email')
#         receiver_email = request.POST.get('receiver_email')
#         subject = request.POST.get('subject')
#         message = request.POST.get('message')

#         configuration = sib_api_v3_sdk.Configuration()
#         configuration.api_key['api-key'] = settings.SENDINBLUE_API_KEY
#         api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))

#         send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(to=[{"email":receiver_email,"name":"GrammarPoint"}],
#                                                        html_content=message,
#                                                        sender={"name":"Softglobal","email":sender_email},
#                                                        subject=subject)

#         try:
#             api_response = api_instance.send_transac_email(send_smtp_email)
#             pprint(api_response)

#             print('Field sent successfully!')
#             print(subject)
#             print(message)
#             print(sender_email)
#             print(receiver_email)

#             # return render(request, 'email_sent.html')
#         except ApiException as e:
#             print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)
#     return render(request, 'email.html')






# from django.shortcuts import render
# import sib_api_v3_sdk
# from sib_api_v3_sdk.rest import ApiException
# from pprint import pprint
# from django.conf import settings

# def send_email(request):
#     if request.method == 'POST':
#         sender_email = request.POST.get('sender_email')
#         receiver_email = request.POST.get('receiver_email')
#         subject = request.POST.get('subject')
#         message = request.POST.get('message')

#         # sender_email = request.POST['sender_email']
#         # receiver_email = request.POST['receiver_email']
#         # subject = request.POST['subject']
#         # message = request.POST['message']
        
#         configuration = sib_api_v3_sdk.Configuration()
#         configuration.api_key['api-key'] = settings.SENDINBLUE_API_KEY
#         api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))

#         send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(to=[{"email":receiver_email,"name":"GrammarPoint"}],
#                                                        html_content=message,
#                                                        sender={"name":"Softglobal","email":sender_email},
#                                                        subject=subject)
#         try:
#             api_response = api_instance.send_transac_email(send_smtp_email)
#             pprint(api_response)

#             print('Field sent successfully!')
#             print(subject)
#             print(message)
#             print(sender_email)
#             print(receiver_email)
#             # return render(request, 'email_sent.html')
#         except ApiException as e:
#             print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)
#     render(request, 'email.html')




import logging
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
# from future import print_function
# import time
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint
from django.conf import settings

logger = logging.getLogger(__name__)

def send_email(request):
    """Sending mail using SendinBlue"""

    # Handling of request
    if request.method == 'POST':
        sender_name = request.POST.get('sender_name')
        sender_email = request.POST.get('sender_email')
        to_email = request.POST.get('to_email')
        to_name = request.POST.get('to_name')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # API Config
        configuration = sib_api_v3_sdk.Configuration()
        configuration.api_key['api-key'] = settings.SENDINBLUE_API_KEY
        api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
        
        # Sending email
        subject = subject
        html_content = message
        sender = {"name":sender_name,"email":sender_email}
        to = [{"email":to_email,"name":to_name}]
        headers = {"SoftGlobal":"unique-id-1234"}
        send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(to=to, 
                                                       headers=headers,
                                                       html_content=message,
                                                       sender=sender, 
                                                       subject=subject)
        try:
            api_response = api_instance.send_transac_email(send_smtp_email)
            pprint(api_response)
            # return HttpResponseRedirect(reverse('success'))
            print('Email sent successfully!')

            print(subject)
            print(message)
            print(sender_name)
            print(sender_email)
            print(to_name)
            print(to_email)

            # messages.success(request, 'Email sent successfully!')
            # return render(request, 'email_sent.html')
        except ApiException as e:
            print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)
            # return HttpResponseRedirect(reverse('error'))
    return render(request, 'send_email.html') 
