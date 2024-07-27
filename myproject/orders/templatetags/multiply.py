from django import template

register=template.Library()

@register.simple_tag(name='multiply')
def multiply(a,b):
    return a * b


    
# Here we define the custom tag for multiplication operation because django templates doesnt support 
# direct multiplication operations