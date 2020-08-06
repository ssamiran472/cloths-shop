from django import template
from core.models import Order, OrdeItem, OrderItem

register = template.Library()


@register.filter
def cart_item_count(user):
    if user.is_authenticated:
        qs = Order.objects.filter(user=user, ordered=False)
        print('<<<<<<<< cart item count >>>>>>>>>', qs[0].items)
        if qs.exists():
            return qs[0].items.count()
    return 0


@register.filter
def wish_item_count(user):
    if user.is_authenticated:
        qs = OrdeItem.objects.filter(user=user, ordeed=False)
        if qs.exists():
            return qs.count()

    return 0
