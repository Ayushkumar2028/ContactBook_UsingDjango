from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
import requests
from django.contrib.auth.models import User


def apiContacts(request):
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/users")
        if response.status_code == 200:
            api_data = response.json()
            print("API Data:", api_data)  # Debugging line to check the fetched data
            for item in api_data:
                Contact.objects.create(
                    name=item['name'],
                    email=item['email'],
                    phone=item['phone'],
                    note='From API',  # Optional 
                    user=None  # Mark as shared API contact
                )
        else:
            print(f"Error fetching data: {response.status_code}")
    except Exception as e:
        print("API fetch failed:", e)

    api_contacts = Contact.objects.filter(user=None)
    return render(request, 'index.html', {'api_contacts': api_contacts})


# Create your views here.
@login_required(login_url='login')
def index(request):
    if request.method == "POST":
        name = request.POST['name'].strip()
        phone = request.POST['phone']
        email = request.POST['email']
        note = request.POST['note']
        Contact.objects.create(user=request.user, name=name, email=email, phone=phone, note=note)
        return redirect('index')
    contacts = Contact.objects.filter(user=request.user)
    api_contacts = Contact.objects.filter(user=None)[:5]
    return render(request, 'index.html', {'contacts': contacts, 'api_contacts': api_contacts})


def delete_contact(request, contact_id):
    cont = get_object_or_404(Contact, id=contact_id, user=request.user)
    Contact.objects.filter(user=request.user).delete()
    return redirect('index')


def edit_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id, user=request.user)
    if request.method == "POST":
        # Get form data
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        note = request.POST['note']

        # Update the contact instance
        contact.name = name
        contact.email = email
        contact.phone = phone
        contact.note = note
        contact.save()
        return redirect('index')
    return render(request, 'edit.html', {'contact': contact})


def signup_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            return render(request, 'login.html', {'error': "user already exits"})

        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('login')
    return render(request, 'signup.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error': 'Invalid credential'})
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')
