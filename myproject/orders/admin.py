from django.contrib import admin
from orders.models import Order, OrderItem

# Register your models here.


# Customizing OrderItem inline display
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0  # To prevent empty extra rows
    fields = ('product', 'quantity', 'product_price', 'total_price')
    readonly_fields = ('product_price', 'total_price')

    def product_price(self, obj):
        return obj.product.price
    product_price.short_description = 'Product Price'

    def total_price(self, obj):
        return obj.product.price * obj.quantity
    total_price.short_description = 'Total Price'

# Customizing Order admin display
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner_username', 'order_status', 'total_price', 'created_at', 'updated_at')
    list_filter = ('order_status', 'created_at', 'updated_at')
    search_fields = ('id', 'owner__user__username')
    inlines = [OrderItemInline]

    def owner_username(self, obj):
        return obj.owner.user.username
    owner_username.short_description = 'Customer'

    def total_order_price(self, obj):
        total = sum(item.product.price * item.quantity for item in obj.added_items.all())
        return total
    total_order_price.short_description = 'Total Order Price'





"""class OrderAdmin(admin.ModelAdmin):
    list_filter=[
        "owner",
        "order_status",
    ]
    search_fields=(
        "owner",
        "id",
    ) """

admin.site.register(Order,OrderAdmin)

admin.site.register(OrderItem)