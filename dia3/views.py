from django.shortcuts import render, redirect

# Create your views here.
def counter (req):
#preguntamos si ya existe la variables
    veces= req.session.get('veces', None)
# si es la primera vez que accede, iniciamos en 0
    if veces is None:
        veces = 0
        # le sumamos 1 a la cantidad de visitas de ESE usuario 
    veces +=1
        # lo guardamos en sesion
    req.session['veces']=veces
        
    
    return render(req,'counter.html')

def reset_counter(req):
    req.session['veces']= 0
    
    return redirect ('/counter')