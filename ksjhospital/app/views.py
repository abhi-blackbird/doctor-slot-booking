from collections import namedtuple
from django.shortcuts import redirect, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from .form import Patientappointment


# Create your views here.

def thanku(request):
    return render(request, 'dr/thanku.html')

@api_view(['GET'])
def app(request):
    appointment_objs = appointment.objects.all().values()
    serializers = appointmentSerializer(appointment_objs, many=True)
    return Response({'status': 200, 'payload' : serializers.data})



@api_view(['GET'])
def timeslot(request):
    appointment_objs = appointment.objects.all().values()
    serializers = timeslotSerializer(appointment_objs, many=True)
    return Response({'status': 200, 'payload' : serializers.data})




@api_view(['POST'])
def post_app(request):
    data = request.data 
    serializers = appointmentSerializer(data = request.data)

    if not serializers.is_valid():
      print(serializers.errors)

      return Response({'status': 403, 'errors' : serializers.errors,  'message' : 'somthing went wrong'})
    serializers.save()

    return Response({'status': 200, 'payload': serializers.data, 'message' : 'your data is save'})   






# def appointment_handlers (request):
#     if request.method == 'POST':
#         # fm = Patientappointment(request.POST)
#         # if fm.is_valid():
#         #     patient_name = fm.cleaned_data['patient_name']
#         #     Age = fm.cleaned_data['Age']
#         #     oppintment_Date = fm.cleaned_data['oppintment_Date']
#         #     Doctor = fm.cleaned_data['Doctor']
#                 # reg = appointment(id=id, patient_name=patient_name, Age=Age, oppintment_Date=oppintment_Date, Doctor=Doctor)

#                 #  reg.save()

#         name = request.POST.get('patient_name', '')
#         Age = request.POST.get('Age', '')
        
#         X = appointment( name=name, Age=Age)

#         X.save()
#         return render(request,'dr/thanku.html')
#     else:
#         return render(request, 'dr/appointment.html')

# # def appointment_handler(request):
    
# #     return render(request, 'dr/appointment.html')        


