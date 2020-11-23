# from django import template 
# register = template.Library() 

# from property.models import Property 

# @register.simple_tag 
# def any_function(name="my_tag"): 
#     return Property.objects.count()



# @register.inclusion_tag('includes/indexNav.html')
# def any_function():
#     variable = Property.objects.order_by('-id')[:5]
#     return {'variable': variable}

from django import template
from property.models import Property
register = template.Library()

# @register.inclusion_tag('base.html')
# def show_poll():
#     poll = Property.objects.all()
#     print(poll)
#     return { 'poll' : poll }

def show_results(poll):
    property = Property.get.all()
    return {'property': property}

register.inclusion_tag('about.html')(show_results) 

