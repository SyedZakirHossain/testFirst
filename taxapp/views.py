from django.shortcuts import render,get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import Group, User
from django.shortcuts import  redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib.auth.models import User, auth
from taxapp.forms import  Taxpayer
from django.http import HttpResponse
from .models import Taxpayer,Bank,Citizen
#========================================================= 
def notfound(request):
    nt=Taxpayer.objects.all()
    dict={"nontin": nt}
      
    return render(request,"notfound.html",context= dict)
#========================================================= 



def search_view2(request):
    
        t = Taxpayer.objects.all()
        dict = {'taxpayer': t,
                }
    
        if request.method == 'POST':
                
                input_nid = request.POST.get('nid')
                if  input_nid.isnumeric():
                    input_nid = int(input_nid)
                else:
                    error_msg = 'Invalid NID. Please enter a valid number.'
                    return render(request, 'search.html', {'error': error_msg})
                taxpayer = Taxpayer.objects.filter(nid=input_nid)
                dic={'taxpayer':taxpayer}
                if  taxpayer : 
                    message = " Found NID in Taxpayer list"
                    return render(request, 'all.html',{'taxpayer':taxpayer,'msg3': message})       
                else:    
                    msg = "NID not found in Taxpayer list"
                return render(request, 'search.html',{'tinlist':taxpayer,'msg1':msg})        
    
    
#===================================================
def home(request):
    t = Taxpayer.objects.all()
    
    return render(request, 'home.html',{'form':Taxpayer,'tinlist':t})     
#===================================================
def search(request):
    t = Taxpayer.objects.all()
    return render(request, 'search.html',{'form':Taxpayer,'tinlist':t})  
#=========================================================   
#===================================================
def dashboard(request):
    t = Taxpayer.objects.all()
    return render(request, 'dashboard.html',{'tinlist':t})  
#=========================================================    
def tinlist(request):
    t = Taxpayer.objects.all()    
    return render(request, 'tinlist.html',{'tinlist':t})       
#===================================================
def cb(request):#citizen wise bank report all citizen
    d = Bank.objects.all()
    c= Citizen.objects.all()    
    return render(request, 'cblist.html',{'cblist':d,'citizen':c})       
#===================================================    


def bwise(request):
    c= Bank.objects.all()
    #bname = Bank.objects.all().filter(bname='Asia').get(bname='Asia')
   
    data = {
        'bank': c,
       
    }
    return render(request, 'bwise.html', context=data)

# =========================================================   
def bwise2(request,bname):
    b= Bank.objects.all()
    c = Citizen.objects.all()
    #bname = Bank.objects.all().filter(bname='Asia').get(bname='Asia')
    bname= Bank.objects.all().filter(bname=bname)
    #bname = Bank.objects.all().filter(bname='Asia')
    data = {
        'citizen': c,
       'bname': bname,
       'b':b,
    }
    return render(request, 'bwise2.html', context=data)

# =========================================================      
def admin(request):
        return render(request, 'admin.site.urls')

#=========================================================          
def cb2(request, r):
        c = Citizen.objects.all()
       
        r= Bank.objects.all().filter(nid=r)
        #c= Citizen.objects.all()
       
        return render(request, 'cblist2.html', {'cb':r,'Bank':c})
                 
#citizen wise bank report all citizen
   
        
        #return render(request, 'cblist2.html',{'cblist':b,'citizen':c})     
            
 
     
       

    
      
  
       
            
            
        
          
     
  
  
        
     
       

