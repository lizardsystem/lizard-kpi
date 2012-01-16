# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.
from django.db import models
from django.utils.translation import ugettext_lazy as _


class KPIPage(models.Model):
    """Page with key performance indicators."""
    name = models.CharField(
        _('name'),
        max_length=200,
        null=True,
        blank=True)
    slug = models.CharField(
        _('name'),
        max_length=40,
        null=True,
        blank=True,
        help_text=_("Identificator used in the url."))
    description = models.TextField(
        _('description'),
        blank=True,
        null=True,
        help_text=_("Extra text shown in sidebar."))

    class Meta:
        ordering = ("name",)
        verbose_name = _('Page with KPI gauges')
        verbose_name_plural = _('Pages with KPI gauges')

    def __unicode__(self):
        return self.name


class KPI(models.Model):
    """Key performance indicator."""
    name = models.CharField(
        _('name'),
        max_length=200,
        null=True,
        blank=True,
        help_text=_("Title shown above gauge."))
    value = models.IntegerField(
        _('value'),
        help_text=_("Value of the indicator (1 bad - 10 good)."),
        default=1)
    url = models.CharField(
        _('url'),
        help_text=_("URL used when clicking on the indicator."),
        max_length=200,
        blank=True,
        null=True)
    kpi_page = models.ForeignKey(
        KPIPage,
        verbose_name='KPI page',
        help_text=_("KPI page on which we're shown."),
        blank=True,
        null=True,
        )
    order = models.IntegerField(
        _('order'),
        help_text=_("Relative order on KPI page."),
        default=1)

    class Meta:
        ordering = ("kpi_page", "order",)
        verbose_name = _('Key performance indicator')
        verbose_name_plural = _('Key performance indicators')

    def __unicode__(self):
        return self.name
