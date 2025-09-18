from django.shortcuts import render, redirect
from .models import Mahasiswa
from django.http import HttpResponse

# Create your views here.

def daftar_mahasiswa(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        
        if action == 'add':
            Mahasiswa.objects.create(
                nim=request.POST.get('nim'),
                firstname=request.POST.get('firstname'),
                lastname=request.POST.get('lastname'),
                jurusan=request.POST.get('jurusan')
            )
            
        elif action == 'update':
            mhs = Mahasiswa.objects.get(id=request.POST.get('id'))
            mhs.nim = request.POST.get('nim')
            mhs.firstname = request.POST.get('firstname')
            mhs.lastname = request.POST.get('lastname')
            mhs.jurusan = request.POST.get('jurusan')
            mhs.save()
            
        elif action == 'delete':
            mhs = Mahasiswa.objects.filter(id=request.POST.get('id')).delete()
        
        return redirect('daftar_mahasiswa')
    mymahasiswa = Mahasiswa.objects.all()
    context = {
        'mymahasiswa': mymahasiswa,
    }
    
    return render(request, 'view.html', context)