# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.translation import ugettext as _

from lizard_kpi.models import KPI


def gauges(request):
    """Render page with the KPI gauges."""
    template_name = 'lizard_kpi/gauges.html'
    title = _("Key performance indicators")
    gauges = KPI.objects.all()
    return render_to_response(
        template_name,
        {'title': title,
         'gauges': gauges},
        context_instance=RequestContext(request))
