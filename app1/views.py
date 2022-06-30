from django.shortcuts import render

# Create your views here.


def dashboard(request):
    return render(request, 'dashboard_head.html')


def team_leader_clints(request):
    return render(request, 'clints.html')


def previous_leads(request):
    return render(request, 'previous_leads.html')


def sales_executive(request):
    return render(request, 'counsilers_tbl.html')


def executive_dashboards(request):
    return render(request, 'exe_dash.html')


def exe_previous_leads(request):
    return render(request, 'exe_previuos_leads.html')


def current_leads(request):
    return render(request, 'exe_current_leads.html')


def newly_assigned_leads(request):
    return render(request, 'exe_newly_assigned_leads.html')


def status_progress(request):
    return render(request, 'status.html')
