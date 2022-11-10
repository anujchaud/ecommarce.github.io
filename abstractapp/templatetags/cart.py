from django import template
register=template.Library()
@register.filter(name='is_in_cart')
def is_in_cart(product,cart):
    try:
        key=cart.keys()
        for i in key:
            if product == int(i):
                return True
        return False
    except:
        pass
@register.filter(name='quantity')
def quantity(product,cart):
    return cart.get(str(product))
    # return type(cart)
# @register.filter(name='sub_quantity')
# def quantity(product,cart):
#     return cart[str(product)]-1