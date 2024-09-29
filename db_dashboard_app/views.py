from django.shortcuts import render
from django.views.generic.base import TemplateView


class DashBoardView(TemplateView):
    template_name = "dashboard/dashboard.html"
    def get(self, request):
        return render(request, self.template_name)

class CreateTableView(TemplateView):
    template_name = "createTable/create_table.html"
    def get(self, request):
        
        return render(request, self.template_name)

