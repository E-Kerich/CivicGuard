
from django.shortcuts import render, redirect
from .forms import IncidentForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Incident

def home(request):
    return render(request, 'incidents/home.html')

def about(request):
    return render(request, 'incidents/about.html')

def support(request):
    return render(request, 'incidents/support.html')

def report_incident(request):
    if request.method == 'POST':
        form = IncidentForm(request.POST, request.FILES)
        if form.is_valid():
            incident = form.save()  # automatically saves to DB
            return redirect('thank_you')
    else:
        form = IncidentForm()

    return render(request, 'incidents/report_incident.html', {'form': form})

def thank_you(request):
    return render(request, 'incidents/thank_you.html')

# Admin Authentication Views


def admin_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("admin_dashboard")  # replace soon when dashboard exists
        else:
            return render(request, "incidents/admin_login.html", {
                "error": "Invalid username or password."
            })

    return render(request, "incidents/admin_login.html")

def admin_logout(request):
    logout(request)
    return redirect("admin_login")




# Admin Dashboard

@login_required(login_url='admin_login')
def admin_dashboard(request):
    total_incidents = Incident.objects.count()
    pending_incidents = Incident.objects.filter(status='Pending').count()
    solved_incidents = Incident.objects.filter(status='Solved').count()

    context = {
        "total_incidents": total_incidents,
        "pending_incidents": pending_incidents,
        "solved_incidents": solved_incidents
    }

    return render(request, 'incidents/admin_dashboard.html', context)

@login_required(login_url='admin_login')
def admin_incident_list(request):
    incidents = Incident.objects.order_by('-date_lodged')
    return render(request, 'incidents/admin_incident_list.html', {
        'incidents': incidents
    })

# Incident Detail and Update

@login_required(login_url='admin_login')
def admin_incident_detail(request, incident_id):
    incident = Incident.objects.get(id=incident_id)

    if request.method == "POST":
        incident.status = request.POST.get("status")
        incident.admin_notes = request.POST.get("admin_notes")
        incident.admin_report = request.POST.get("admin_report")
        incident.save()

        return redirect('admin_incident_detail', incident_id=incident.id)

    return render(request, 'incidents/admin_incident_detail.html', {
        'incident': incident
    })

# Edit Incident

@login_required(login_url='admin_login')
def admin_incident_edit(request, incident_id):
    incident = Incident.objects.get(id=incident_id)

    if request.method == "POST":
        incident.user_name = request.POST.get("user_name")
        incident.user_email = request.POST.get("user_email")
        incident.user_phone = request.POST.get("user_phone")
        incident.incident_type = request.POST.get("incident_type")
        incident.description = request.POST.get("description")
        incident.location = request.POST.get("location")

        if request.FILES.get('evidence_file'):
            incident.evidence_file = request.FILES['evidence_file']

        incident.save()
        return redirect('admin_incident_detail', incident_id=incident.id)

    return render(request, 'incidents/admin_incident_edit.html', {
        'incident': incident
    })

# Delete Incident

@login_required(login_url='admin_login')
def admin_incident_delete(request, incident_id):
    incident = Incident.objects.get(id=incident_id)

    if request.method == "POST":
        incident.delete()
        return redirect('admin_incident_list')

    return render(request, 'incidents/admin_incident_delete.html', {
        'incident': incident
    })


# Add Incident reported by Admin

@login_required(login_url='admin_login')
def admin_incident_add(request):
    if request.method == "POST":
        user_name = request.POST.get("user_name")
        user_email = request.POST.get("user_email")
        user_phone = request.POST.get("user_phone")
        incident_type = request.POST.get("incident_type")
        description = request.POST.get("description")
        location = request.POST.get("location")
        evidence_file = request.FILES.get("evidence_file")

        new_incident = Incident(
            user_name=user_name,
            user_email=user_email,
            user_phone=user_phone,
            incident_type=incident_type,
            description=description,
            location=location,
            reported_by_admin=True
        )

        if evidence_file:
            new_incident.evidence_file = evidence_file

        new_incident.save()

        return redirect('admin_incident_list')

    return render(request, 'incidents/admin_incident_add.html')



# Analytics Dashboard

@login_required(login_url='admin_login')
def admin_dashboard(request):
    total_incidents = Incident.objects.count()
    pending_incidents = Incident.objects.filter(status='Pending').count()
    reviewed_incidents = Incident.objects.filter(status='Reviewed').count()
    solved_incidents = Incident.objects.filter(status='Solved').count()

    # Category breakdown
    categories = {}
    for incident in Incident.objects.all():
        categories[incident.incident_type] = categories.get(incident.incident_type, 0) + 1

    context = {
        "total_incidents": total_incidents,
        "pending_incidents": pending_incidents,
        "reviewed_incidents": reviewed_incidents,
        "solved_incidents": solved_incidents,
        "categories": categories
    }

    return render(request, 'incidents/admin_dashboard.html', context)


# Public Incident Views

def public_incident_list(request):
    pending = Incident.objects.filter(status='Pending').order_by('-date_lodged')
    reviewed = Incident.objects.filter(status='Reviewed').order_by('-date_lodged')
    solved = Incident.objects.filter(status='Solved').order_by('-date_lodged')

    return render(request, 'incidents/public_incident_list.html', {
        'pending': pending,
        'reviewed': reviewed,
        'solved': solved,
    })

# Public Incident Detail View

def public_incident_detail(request, incident_id):
    incident = Incident.objects.get(id=incident_id)
    return render(request, 'incidents/public_incident_detail.html', {
        'incident': incident
    })

