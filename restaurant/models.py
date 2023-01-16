from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Orders(models.Model):
  
    date = models.DateField(verbose_name="Дата заказа")
    num_table = models.PositiveIntegerField(verbose_name="Номер стола", null=None)
    name = models.CharField(max_length=22, null=True, verbose_name="Введите ваше имя")
    def __str__(self):
        return f"Стол {self.num_table} заказан {self.date}"

class Table(models.Model):
    number = models.PositiveIntegerField(verbose_name="Номер стола")
    seats = models.PositiveIntegerField(verbose_name="Количество мест")
    SHAPE_CHOICES = [
        ('rectangular', 'Прямоугольный'),
        ('oval', 'Овальный'),
    ]

    shape = models.CharField(max_length=50, choices=SHAPE_CHOICES, verbose_name="Форма стола")
    x = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)], verbose_name="Расположение стола x")
    y = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)], verbose_name="Расположение стола y",)
    width = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)], verbose_name="Ширина стола", )
    length = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)], verbose_name="Длина стола",)

    def __str__(self):
        return f"Стол {self.number} ({self.seats} мест)"
    
 
