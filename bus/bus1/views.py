from django.shortcuts import render,redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import  adminsidedetail,usersideinfo
from .serializer import serializer1,serializer2
from django.shortcuts import get_object_or_404

@api_view(['GET'])
def travel_package_list(request):
    packages = adminsidedetail.objects.all()  # Retrieve all travel packages
    serializer = serializer1(packages, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def travel_package_detail(request, pk):
    try:
        package = adminsidedetail.objects.get(pk=pk)  # Retrieve the package by pk
    except adminsidedetail.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = serializer1(package)
    return Response(serializer.data)

@api_view(['POST'])
def booking_create(request):
    serializer = serializer2(data=request.data)
    if serializer.is_valid():
        serializer.save()  # Save the booking
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
def package_list(request):
    packages = adminsidedetail.objects.all()
    return render(request, 'home.html', {'packages': packages})

def package_detail(request, pk):
    package = adminsidedetail.objects.get(pk=pk)
    if request.method == 'POST':
        form_data = request.POST
        booking = usersideinfo(
            package=package,
            travel_date=form_data['travel_date'],
            number_of_people=form_data['number_of_people'],
            customer_name=form_data['customer_name'],
            customer_email=form_data['customer_email'],
            mobile_number=form_data['mobile_number']  # Save the mobile number
        )
        booking.save()
        return redirect('booking_confirmation', pk=booking.id)  # Redirect to the confirmation page with the booking ID
    
    return render(request, 'package_detail.html', {'package': package})

def booking_confirmation(request, pk):
    booking = usersideinfo.objects.get(pk=pk)
    return render(request, 'confirmation.html', {'booking': booking})

def home(request):
    bo = adminsidedetail.objects.all()
    return render(request, 'home.html', {'bo': bo})