from django.http import HttpResponse
from django.shortcuts import render
from .models import Job,Resident,Category,Client
# Create your views here.

def dashboard(req):
    client = Client.objects.first()
    return render(req,"complaints/dashboard.html",{'client':client})

def complaints(request):
    if request.method == 'POST':
        # 1. EXTRACT THE DATA
        flat_no = request.POST['flat_no']
        contact_no = request.POST.get('contact_no', '')
        category_id = request.POST['category']
        description = request.POST['description']
        photo = request.FILES.get('photo')
        
        # 2. GET THE CLIENT (hardcode for now)
        client = Client.objects.first()
        
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
        
        return HttpResponse("Complaint submitted successfully!")  # Temporary
        
    # GET request - show the empty form
    client = Client.objects.first()
    categories = Category.objects.filter(client=client)
    return render(request, 'complaints/job_form.html', {
        'client': client,
        'categories': categories
    })