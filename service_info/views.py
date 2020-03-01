from django.shortcuts import render, get_object_or_404
from django.views import View
from service_info.models import *


class ServiceInfoView(View):
    def get(self, request):
        info = Info.objects.first()
        documents = Document.objects.all()
        executions = Execution.objects.all()
        structures = Structure.objects.all()

        context = {
            'info': info,
            'executions': executions,
            'documents': documents,
            'structures': structures,
        }
        template = 'lo/{0}' if request.session.get('is_lo') else '{0}'
        return render(request, template.format('service_info/info.html'), context)


class StructureView(View):
    def get(self, request, structure_slug):
        structure = get_object_or_404(Structure, slug=structure_slug)

        context = {
            'structure': structure,
        }
        template = 'lo/{0}' if request.session.get('is_lo') else '{0}'
        return render(request, template.format('service_info/structure.html'), context)