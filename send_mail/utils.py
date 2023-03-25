# # from sendinblue import SibApiV3Sdk
# from sib_api_v3_sdk import SibApiV3Sdk
# # from sendinblue.exceptions import ApiException
# from sib_api_v3_sdk.rest import ApiException
# from django.conf import settings

# def send_email(to_email, subject, body):
#     try:
#         # create an instance of the Sendinblue client
#         configuration = SibApiV3Sdk.Configuration()
#         configuration.api_key['api-key'] = settings.SENDINBLUE_API_KEY
#         api_instance = SibApiV3Sdk.TransactionalEmailsApi(SibApiV3Sdk.ApiClient(configuration))

#         # create the email message
#         send_smtp_email = SibApiV3Sdk.SendSmtpEmail(to=[{'email': to_email}], subject=subject, html_content=body)

#         # send the email
#         response = api_instance.send_transac_email(send_smtp_email)
#         print(response)
#     except ApiException as e:
#         print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)
