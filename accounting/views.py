from django.http import HttpResponse
from django.template import RequestContext, loader
from accounting.models import ChartType

# Create your views here.
def index(request): 
    chart_types = ChartType.objects.all()
    template = loader.get_template('dashboard.html')
    context = RequestContext(request, {
        'chart_types': chart_types,
    })
    return HttpResponse(template.render(context))