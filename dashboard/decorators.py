from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **Kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard:dashboard')
        else:
            return view_func(request, *args, **Kwargs)
    return wrapper_func


# def allowed_users(view_func):
#     def wrapper_func(request, *args, **Kwargs):
#         if request.user.profile.allow_access:
#             return view_func(request, *args, **Kwargs)
#         else:
#             return redirect('dashboard:dashboard')
#     return wrapper_func


def check_admin(view_func):
    def wrapper_func(request, *args, **Kwargs):
        if request.user.is_superuser:
            return view_func(request, *args, **Kwargs)
        else:
            messages.warning(
                request, "You don not have acces to that paticular page"
            )
            return redirect('core:index')
    return wrapper_func
    
# def check_staff(view_func):
#     def wrapper_func(request, *args, **Kwargs):
#         if request.user.is_staff:
#             return view_func(request, *args, **Kwargs)
#         else:
#             messages.warning(
#                 request, "You don not have acces to that paticular page"
#             )
#             return redirect('dashboard:dashboard')
#     return wrapper_func