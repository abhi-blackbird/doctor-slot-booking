
from django.db.utils import DatabaseError, Error
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import user_profile, user_detail
from django.db import transaction,IntegrityError





def index(request):   
      if request.method == 'POST':   
        name = request.POST.get('username')        
        phone_no = request.POST.get('phone_no',None )
        email = request.POST.get('email',None)

        if (len (phone_no)==0 or len(email)==0):   
         return HttpResponse('please enter your phone number or email')
        #  return render(request, 'index.html', )



        
        sid=transaction.savepoint()
                 
        
        try:
          a = user_profile(username=name)
          a.save()               

          b = user_detail(phone_no=phone_no, email=email, u_id=a.id) 
                   
          b.save() 
          # Could throw exception
           
          transaction.savepoint_commit(sid)

          return render(request, 'index.html')
        except IntegrityError:
          print(name)
          transaction.savepoint_rollback(sid)
          transaction.clean_savepoints(sid)
      else:
        return render(request, 'index.html',{})
             
      
