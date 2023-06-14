from django.db import models
from django.contrib.auth.models import User

# Create your models here.

MOVEMENT = (
    ('e', 'entrada'),
    ('s', 'saida'),
)
PRODUCT_TYPE = (
    ('cx', 'caixa'),
    ('pcts','pacote'),
    ('grf','garrafa'),
    ('gl','galão'),
    ('cp','copo'),
    ('fltr','filtro'),
    ('bb','bomba'),
    ('sp','suporte'),
)
PRODUCT_VOL = (
    ('ml','mililitro'),
    ('l','litro' ),
    ('pc', 'unidade')
)


class TimeLineModel(models.Model):
    created = models.DateTimeField(verbose_name=('Criando em'), auto_now_add=True, auto_now=False)
    modified = models.DateTimeField(verbose_name=('Alterado em'), auto_now_add=False, auto_now=True)

    class Meta:
        abstract = True

class ProductModel(models.Model):
    product = models.CharField(verbose_name=('Nome'), max_length=100, unique=True)
    price = models.DecimalField(verbose_name=('Preço Unitário'), max_digits=7, decimal_places=2)
    stock_current = models.IntegerField(verbose_name=('Quantidade'))
    product_type = models.CharField(max_length=4, choices=PRODUCT_TYPE, blank=True, null=True)
    produtc_vol = models.CharField(max_length=4, choices=PRODUCT_VOL, blank=True, null=True)
    stock_mini = models.PositiveIntegerField(verbose_name=('Estoque mínimo'), blank=True, null=True)

    def __str__(self):
        return self.product

class StockModel(TimeLineModel):
    employee = models.ForeignKey(User, verbose_name=('Funcionario'), on_delete=models.CASCADE)
    invoice = models.PositiveIntegerField(verbose_name=('Nota Fiscal'), null=True, blank=True)
    movement = models.CharField(verbose_name=('Movimento'), max_length=1, choices=MOVEMENT)
    
    def __str__(self):
        return str(self.pk)

class StockLineModel(models.Model):
    stock = models.ForeignKey(StockModel, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    amount = models.FloatField(verbose_name=('Valor'))
    balance = models.PositiveIntegerField(verbose_name=('Quantidade'))
    
    def __str__(self):
        return f'{self.pk}-{self.stock}-{self.product}'