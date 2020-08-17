from django.db import models

# Create your models here.
"""


class Category(models.Model):
    id = models.IntegerField(
        db_column="id",
        verbose_name="Id",
        primary_key=True,
        help_text="Auto incremental unique interger values.",
    )
    parent_id = models.ForeignKey(
        'self', 
        blank =True,
        help_text="Auto incremental unique interger values.",
        on_delete = models.CASCADE
    )
    name = models.CharField(
        db_column="name",
        max_length = 255,
        verbose_name="Product",
        help_text="Name of Products"
    )
    class Meta:
        db_table = "category"
        verbose_name = "Category"
        verbose_name_plural = "Category Masters"

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):

    name = models.ForeignKey(
        Category,
        db_column="product",
        max_length = 255,
        verbose_name="Product",
        help_text="Name of Products",
        on_delete = models.CASCADE
    )

    class Meta:
        db_table = "product"
        verbose_name = "Product Master"
        verbose_name_plural = "Product Masters"

    def __str__(self):
        return f"{self.name}"

"""

class Category(models.Model):
    name = models.CharField(max_length=80, null=True)
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('parent',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    def __str__(self):
        return f"{self.name}"

class Product(models.Model):
    
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
   
    name = models.CharField(max_length=200, null=True)
    def __str__(self):
        return f"{self.name}"
    