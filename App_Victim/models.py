from typing import Union, Optional

from django.db import models
from datetime import datetime


class Victim(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    ic_no = models.CharField(primary_key=True, max_length=15, verbose_name='IcNo')
    name = models.CharField(max_length=255, verbose_name='Name')
    hp_no = models.CharField(max_length=15, verbose_name='Phone')

    @property
    def calc_age(self):
        ic_year = self.ic_no[:2]
        current_year = datetime.now().year
        now = str(current_year)[:2]
        if int(now + ic_year) <= current_year:
            return current_year - (int(now + "00") + int(ic_year))
        else:
            return current_year - (int(now + "00") - 100 + int(ic_year))



