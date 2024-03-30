from django.shortcuts import render, redirect
from .models import Client, Project
from django.contrib.auth.decorators import login_required

@login_required
def register_client(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        client = Client.objects.create(name=name)
        return redirect('client_info', client_id=client.id)
    return render(request, 'register_client.html')

@login_required
def client_info(request, client_id):
    client = Client.objects.get(id=client_id)
    return render(request, 'client_info.html', {'client': client})

@login_required
def edit_client(request, client_id):
    client = Client.objects.get(id=client_id)
    if request.method == 'POST':
        client.name = request.POST.get('name')
        client.save()
        return redirect('client_info', client_id=client.id)
    return render(request, 'edit_client.html', {'client': client})

@login_required
def delete_client(request, client_id):
    client = Client.objects.get(id=client_id)
    client.delete()
    return redirect('client_list')

@login_required
def add_project(request, client_id):
    client = Client.objects.get(id=client_id)
    if request.method == 'POST':
        name = request.POST.get('name')
        project = Project.objects.create(client=client, name=name)
        return redirect('client_info', client_id=client.id)
    return render(request, 'add_project.html', {'client': client})

@login_required
def assigned_projects(request):
    user = request.user
    projects = Project.objects.filter(assigned_users=user)
    return render(request, 'assigned_projects.html', {'projects': projects})
