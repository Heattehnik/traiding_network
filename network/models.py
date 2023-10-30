from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from products.models import Product


class NetworkNode(models.Model):
    LEVEL_CHOICES = (
        (0, 'Завод'),
        (1, 'Розничная сеть'),
        (2, 'Индивидуальный предприниматель'),
    )

    name = models.CharField(max_length=255, verbose_name="Название")
    level = models.IntegerField(choices=LEVEL_CHOICES, blank=True, null=True)
    email = models.EmailField(verbose_name="Почта")
    country = models.CharField(max_length=100, verbose_name="Страна")
    city = models.CharField(max_length=100, verbose_name="Город")
    street = models.CharField(max_length=100, verbose_name="Улица")
    house_number = models.CharField(max_length=10, verbose_name="номер дома")
    products = models.ManyToManyField(Product, related_name='network_nodes', verbose_name="Продукты")
    supplier = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Поставщик")
    debt = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Задолженость")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"{self.name}, {self.email}, {self.country}"

@receiver(pre_save, sender=NetworkNode)
def set_network_node_level(sender, instance, **kwargs):
    if instance.supplier:
        instance.level = instance.supplier.level + 1
    else:
        # Если у объекта нет поставщика, он считается заводом (уровень 0)
        instance.level = 0
