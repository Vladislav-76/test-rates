from django.db import models


class Currency(models.Model):
    """Модель валюты."""
    class Meta:
        verbose_name = 'Валюта'
        verbose_name_plural = 'Валюты'
        ordering = ['charcode']

    name = models.CharField(
        verbose_name='Наименование',
        max_length=250,
        blank=False,
        unique=True,
        help_text='Наименование Валюты',
    )
    charcode = models.CharField(
        verbose_name='Код',
        max_length=5,
        blank=False,
        unique=True,
        help_text='Код валюты',
    )

    def __str__(self):
        return self.charcode


class Rate(models.Model):
    """Модель курса валюты к рублю."""
    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ['-date', 'currency']

    currency = models.ForeignKey(
        Currency,
        verbose_name='Валюта',
        related_name='rates',
        on_delete=models.CASCADE,
    )
    nominal = models.IntegerField(
        verbose_name='Номинал',
        blank=False,
        help_text='Номинал обмена валюты',
    )
    value = models.DecimalField(
        verbose_name='Значение',
        max_digits=10,
        decimal_places=4,
        blank=False,
        help_text='Значение курса валюты',
    )
    date = models.DateField(
        verbose_name='Дата',
        blank=False,
        help_text='Дата курса валюты',
    )

    def __str__(self):
        return f'{self.date} - {self.currency} - {self.nominal} - {self.value}'
