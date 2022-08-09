from django.conf import settings
from django.db import models
from django.shortcuts import reverse
from store.models.image import ImageAlbum


CATEGORY_CHOICES = (
    ('P', "Pants"),
    ('S', "Shoes"),
    ("Sh", "Shirt"),
    ("So", "Socks"),
    ("Sho", "Shorts"),
    ("C", "Child"),
    ("A", "Athletic Wear"),
)


def add_category(add):
    cats = Category.objects.all()
    existed = False
    if cats:
        for cat in cats:
            if cat.name == add:
                existed = True
        if not existed:
            catty = Category.objects.create(name=add)
            catty.save()


def default_category():
    for i in range(len(CATEGORY_CHOICES)):
        if CATEGORY_CHOICES[i][1]:
            add_category(CATEGORY_CHOICES[i][1])


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("store:home")


class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.CharField(max_length=20, blank=True, null=True)
    slug = models.SlugField()
    description = models.TextField()
    image_url = models.URLField(blank=True, null=True)
    album = models.OneToOneField(ImageAlbum, related_name='model', on_delete=models.CASCADE, blank=True, null=True)
    #
    # class Color(models.TextChoices):
    #     red = 'Red', 'Red'
    #     blue = 'Blue', 'Blue'
    #     green = 'Green', 'Green'
    #     orange = 'Orange', 'Orange'
    #     white = 'White', 'White'
    #     black = 'Black', 'Black'
    #     yellow = 'Yellow', 'Yellow'
    #
    # color = models.CharField(choices=Color.choices, max_length=6, unique=True, blank=True, null=True)
    #
    # class ShoeSizes(models.TextChoices):
    #     six = '6', '6'
    #     seven = '7', '7'
    #     eight = '8', '8'
    #     nine = '9', '9'
    #     ten = '10', '10'
    #     eleven = '11', '11'
    #     twelve = '12', '12'
    #     thirteen = '13', '13'
    #
    # shoe_sizes = models.CharField(choices=ShoeSizes.choices, max_length=3, blank=True, null=True)
    #
    # class ShirtSizes(models.TextChoices):
    #     xs = 'Extra-Small', 'Extra-Small'
    #     s = 'Small', 'Small'
    #     m = 'Medium', 'Medium'
    #     L = 'Large', 'Large'
    #     xl = 'Extra-Large', 'Extra-Large'
    #
    # shirt_sizes = models.CharField(choices=ShirtSizes.choices, max_length=12, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_update_url(self):
        return reverse("store:home", kwargs={
            'slug': self.slug
        })

    def get_absolute_url(self):
        return reverse("store:home", kwargs={
            'slug': self.slug
        })

    def get_add_to_cart_url(self):
        return reverse("store:home", kwargs={
            'slug': self.slug
        })

    def get_remove_from_cart_url(self):
        return reverse("store:home", kwargs={
            'slug': self.slug
        })


class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"

    def get_total_item_price(self):
        return self.quantity * self.item.price

    def get_total_discount_item_price(self):
        pass
        # return self.quantity * self.item.discount_price

    def get_amount_save(self):
        pass


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ref_code = models.CharField(max_length=20)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    shipping_address = models.ForeignKey(
        'Address', related_name='shipping_address', on_delete=models.SET_NULL, blank=True, null=True)
    billing_address = models.ForeignKey(
        'Address', related_name='billing_address', on_delete=models.SET_NULL, blank=True, null=True)
    payment = models.ForeignKey('Payment', on_delete=models.SET_NULL, blank=True, null=True)
    coupon = models.ForeignKey('Coupon', on_delete=models.SET_NULL, blank=True, null=True)
    shipped = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)
    refund_requested = models.BooleanField(default=False)
    refund_granted = models.BooleanField(default=False)

    def __str__(self):
        item_title = ' '
        for orderitem in self.items.all():
            item_title = orderitem.item.title
        return self.start_date.strftime('%Y-%m-%d') + ' ' + self.user.username + ' ' + item_title

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_total_item_price()
        if self.coupon:
            total -= self.coupon.amount
        return total

