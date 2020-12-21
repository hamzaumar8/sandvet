from django.conf import settings
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from django.template.loader import get_template





# def generate_log(request,description):
#     name = f"{request.user.first_name} {request.user.last_name}"
#     entity = request.user.profile.entity.name
#     logs = Logs.objects.create(
#         name=name,
#         ip_address=generate_ip_address(request),
#         description = description,
#         entity=entity,
#     )
#     logs.save()




# def quarter_email(request,email, subject, message, attachment):
#     # url = request.build_absolute_uri(reverse("account_login"))
#     # html = get_template("dashboard/emails/quatermail.html")
#     # content = html.render({"url": url, "content": message})
#     try :
#         mail = EmailMessage(
#             "Quarterly Report for OAG Asset Management Portal",
#             message,
#             email_from,
#             [email],
#         )
#         mail.attach(attachment.name, attachment.read(), attachment.content_type)
#         mail.content_subtype = "html"
#         mail.send()
#     except:
#         messages.warning(request, f"Either the attachment's size is big or corrupt")
#         return HttpResponseRedirect(request.path_info)


# def signup_invite_email(request, email):
#     url = request.build_absolute_uri(reverse("dashboard:signup", kwargs={"token": generate_signup_token(email)}))
#     html = get_template("dashboard/emails/staffregister.html")
#     content = html.render({"url": url})
#     msg = "Kindly visit %s to create an account" % url
#     send_mail(
#         "Registration for OAG Asset Management Portal ",
#         msg,
#         email_from,
#         [email],
#         fail_silently=False,
#         html_message=content,
#     )