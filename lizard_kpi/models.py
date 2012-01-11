# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.
from django.db import models
from django.utils.translation import ugettext_lazy as _


class KPI(models.Model):
    """Key performance indicator."""
    name = models.CharField(
        _('name'),
        max_length=200,
        null=True,
        blank=True)
    value = models.IntegerField(
        help_text=_("Value of the indicator (1 bad - 10 good)."),
        default=1)
    url = models.CharField(
        _('url'),
        help_text=_("URL used when clicking on the indicator."),
        max_length=200,
        blank=True,
        null=True)
