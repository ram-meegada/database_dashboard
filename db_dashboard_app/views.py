from django.shortcuts import render
from django.views.generic.base import TemplateView
import psycopg2
from django.http import HttpResponse


class DashBoardView(TemplateView):
    template_name = "dashboard/dashboard.html"

    def get(self, request):
        return render(request, self.template_name)


class CreateTableView(TemplateView):
    template_name = "createTable/create_table.html"

    def post(self, request):
        try:
            conn = psycopg2.connect(
                database="database_dashboard_db",
                user="postgres",
                password="Ramu@123",
                host="localhost",
                port=5432
            )
            query = f'''create table public."{request.POST['table_name']}" (
                                id serial primary key,'''
            for i in range(len(request.POST.getlist('column_name'))):
                query += request.POST.getlist('column_name')[i] + " " + request.POST.getlist('select-datatype')[i] + \
                    " " + request.POST.getlist("select-constraints")[i] + ","
            query = query[:-1] + ")"        
            crsr = conn.cursor()
            crsr.execute(query)
            conn.commit()
            crsr.close()
            conn.close()
            return render(request, self.template_name)
        except Exception as err:
            return HttpResponse(str(err))
