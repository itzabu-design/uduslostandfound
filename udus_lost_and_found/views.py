from django.shortcuts import render, redirect
from .models import UserProfile, LostReport, FoundReport
from .forms import LostReportForm, FoundReportForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test



from django.shortcuts import render

def report_lost_item(request):
    return render(request, 'lost_report.html')

def report_found_item(request):
    return render(request, 'found_report.html')


def home(request):
    return render(request, 'home.html')


def sign_up(request):
    return render(request, 'sign_up.html')



def login(request):
    return render(request, 'login.html')



def found_report(request):
    if request.method == 'POST':
        form = FoundReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  
    else:
        form = FoundReportForm()
    return render(request, 'found_report.html', {'form': form})

def lost_report(request):
    return render(request, 'lost_report.html')


from django.shortcuts import render

def view_items(request):
    return render(request, 'view_items.html')


def help_view(request):
    return render(request, 'help_page.html')


def profile(request):
    context = {'user': request.user} 
    return render(request, 'profile.html', context)


def is_admin(user):
    return user.is_staff

def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

def manage_users(request):
    return render(request, 'manage_users.html')

# View for System Settings
@login_required
@user_passes_test(is_admin)
def system_settings(request):
    return render(request, 'admin/system_settings.html')


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

def submit_details(request):
    if request.method == 'POST':
        # Process the form data
        name = request.POST['name']
        gsm = request.POST['gsm']
        address = request.POST['address']
        item = request.POST['item']
        description = request.POST['description']

        return HttpResponse("Details submitted successfully.")

