from django.shortcuts import render, redirect
from .models import UserProfile, LostReport, FoundReport
from .forms import LostReportForm, FoundReportForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test


def is_admin(user):
    return user.is_staff

def admin_dashboard(request):
    return render(request, 'admin/admin_dashboard.html')

def manage_users(request):
    return render(request, 'admin/manage_users.html')

def manage_lost_items(request):
    return render(request, 'admin/manage_lost_items.html')

# View for Managing Found Items
@login_required
@user_passes_test(is_admin)
def manage_found_items(request):
    return render(request, 'admin/manage_found_items.html')

# View for Notifications
@login_required
@user_passes_test(is_admin)
def notifications(request):
    return render(request, 'admin/notifications.html')

# View for Reports
@login_required
@user_passes_test(is_admin)
def reports(request):
    return render(request, 'admin/reports.html')

# View for System Settings
@login_required
@user_passes_test(is_admin)
def system_settings(request):
    return render(request, 'admin/system_settings.html')

def home(request):
    return render(request, 'templates/home.html')

def signup(request):
    return render(request, 'templates/signup.html')

def signin(request):
    return render(request, 'templates/signin.html')

def item_report(request):
        return render(request, 'templates/item_report.html')

def lost_report(request):
    return render(request, 'udus_lost_and_found/templates/lost_report.html')

def found_report(request):
    if request.method == 'POST':
        form = FoundReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home or another page after submission
    else:
        form = FoundReportForm()
    return render(request, 'templates/found_report.html', {'form': form})

def help_page(request):
    return render(request, 'templates/help.html')

def view_items(request):
    lost_items = LostReport.objects.all()
    found_items = FoundReport.objects.all()
    context = {
        'lost_items': lost_items,
        'found_items': found_items
    }
    return render(request, 'view_items.html')

def submit_details(request):
    if request.method == 'POST':
        # Process the form data
        name = request.POST['name']
        gsm = request.POST['gsm']
        address = request.POST['address']
        item = request.POST['item']
        description = request.POST['description']

        return HttpResponse("Details submitted successfully.")
