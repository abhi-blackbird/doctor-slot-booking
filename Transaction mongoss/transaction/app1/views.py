
# from django.http.response import HttpResponse
# from django.shortcuts import redirect, render
# from django.db import transaction
# from .models import user, user_detail
# from django.db import transaction,IntegrityError





# def index(request):   
#       if request.method == 'POST':   
#         name = request.POST.get('username')        
#         phone_no = request.POST.get('phone_no')
#         email = request.POST.get('email')
#         a = user(username=name)     
          
#         a.save()   

#         b = user_detail(phone_no=phone_no, email=email)  
#         a.u_id 

#         b.save() 
          
        
#         return redirect('/')

#       else:
             
#             return render(request, '/index.html')

# def home(request):   
     
             
#    return HttpResponse( '/home.html')            





from django.db.utils import DatabaseError, Error
from django.shortcuts import redirect, render
from django.utils import translation
from .models import user, user_detail
from django.db import transaction,IntegrityError





def index(request):   
      if request.method == 'POST':   
        name = request.POST.get('username', None)        
        phone_no = request.POST.get('phone_no',None )
        email = request.POST.get('email',None)
        
        try: 
          a = user(username=name)  

          with transaction.atomic():  
            print(len (phone_no))     
            a.save()
            if (len (phone_no)==0 or len(email)==0):
              raise IntegrityError("error")
            

            b = user_detail(phone_no=phone_no, email=email, user= a)          
            b.save() # Could throw exception
            return render(request, 'index.html')
        except:
          return render(request, 'index.html')             

      else:
        return render(request, 'index.html')
             
      
