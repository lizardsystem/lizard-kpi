# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.translation import ugettext as _

from lizard_kpi.models import KPI
from lizard_kpi.models import KPIPage


def kpi_pages(request):
    """Render page that lists all KPI pages."""
    template_name = 'lizard_kpi/kpi_pages.html'
    title = _("Key performance indicators")
    pages = KPIPage.objects.all()
    return render_to_response(
        template_name,
        {'pages': pages,
         'title': title},
        context_instance=RequestContext(request))


def gauges(request, page=None):
    """Render page with the KPI gauges."""
    template_name = 'lizard_kpi/gauges.html'
    page = get_object_or_404(KPIPage, slug=page)
    gauges = KPI.objects.filter(kpi_page=page)
    return render_to_response(
        template_name,
        {'page': page,
         'gauges': gauges},
        context_instance=RequestContext(request))
