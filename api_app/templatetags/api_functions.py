from django import template

register = template.Library()

@register.filter(name='var')
def variable_generator(value, arg):
    for k in value.keys():
        k = k

    for j in value[k]['quote'].keys():
        j = j

    return value[k]['quote'][j][arg]

@register.filter(name='cur')
def variable_generator(value):
    for k in value.keys():
        k = k

    cur = list(value[k]['quote'].keys())[0]

    if cur == 'EUR' :
        cur = '€'
    elif cur == 'USD' :
        cur = '$'
    return cur