from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Job,Resident,Category,Client
from vendors.models import Vendor
# Create your views here.

def dashboard(req):
    if req.GET.get('secret') != 'akash123':  # Change this password
        return HttpResponse('Unauthorized - Secretaries only', status=401)
    client = Client.objects.first()
    jobs = Job.objects.all()
    vendors = Vendor.objects.filter(is_active=True)
    open = Job.objects.filter(status='OPEN').count()
    assigned = Job.objects.filter(status='ASSIGNED').count()
    resolved = Job.objects.filter(status='RESOLVED').count()
    vendor_name = Vendor.objects.filter(name='')
    context = {
        'client':client,
        'jobs':jobs,
        'vendors':vendors,
        'open':open,
        'assigned':assigned,
        'resolved':resolved,
        
    }
    return render(req,"complaints/dashboard.html",context)

def complaints(request):
    client = Client.objects.first()
    show_success = False 
    
    if request.method == 'POST':
        # 1. EXTRACT THE DATA
        flat_no = request.POST['flat_no']
        contact_no = request.POST.get('contact_no', '')
        category_id = request.POST['category']
        description = request.POST['description']
        photo = request.FILES.get('photo')
        
        # 2. GET THE CLIENT (hardcode for now)
        
        # 3. FIND OR CREATE RESIDENT
        resident, created = Resident.objects.get_or_create(
            client=client,
            flat_no=flat_no,
            defaults={'contact_no': contact_no}
        )
        
        # 4. CREATE THE JOB
        category = Category.objects.get(id=category_id)
        job = Job.objects.create(
            client=client,
            resident=resident,
            category=category,
            description=description,
            photo=photo,
            status='OPEN'
        )
        
        show_success = True        
    # GET request - show the empty form
    client = Client.objects.first()
    categories = Category.objects.filter(client=client)
    return render(request, 'complaints/job_form.html', {
        'client': client,
        'categories': categories,
        'show_success': show_success
    })
    
def assign_vendor(req,job_id):
    if req.method == 'POST':
        job = Job.objects.get(id=job_id)
        vendor_id = req.POST['vendor_id']
        job.assigned_vendor_id = vendor_id
        job.status = 'ASSIGNED'
        job.save()
        print(f"Assigned {job.id} to vendor {job.assigned_vendor}")
        return redirect('dashboard')
    
def mark_resolved(request, job_id):
    if request.method == 'POST':
        job = Job.objects.get(id=job_id)
        job.status = 'RESOLVED'
        job.save()
        return redirect('dashboard')