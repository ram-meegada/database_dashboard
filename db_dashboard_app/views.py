from django.shortcuts import render
from django.views.generic.base import TemplateView
import psycopg2

class DashBoardView(TemplateView):
    template_name = "dashboard/dashboard.html"
    def get(self, request):
        return render(request, self.template_name)

class CreateTableView(TemplateView):
    template_name = "createTable/create_table.html"
    def post(self, request):
        print(request.POST, '========requsjdb--------')
        conn = psycopg2.connect(
            database="database_dashboard_db", 
            user="postgres",
            password="Ramu@123",
            host="localhost",
            port=5432
            )
        cursor = conn.cursor()
        cursor.execute('''create table public."User1" (
                            id serial primary key,
                            name varchar(50)
                        )''')
        conn.commit()
        cursor.close()
        conn.close()
        return render(request, self.template_name)

