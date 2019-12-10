from django.shortcuts import render
from .models import Floreria,Ticket
from .clases import elemento
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login as login_autent
from django.contrib.auth.decorators import login_required
import datetime;

# Create your views here.
@login_required(login_url='/login/')
def grabar_carro(request):
    x=request.session["carritox"]    
    usuario=request.user.username
    suma=0
    try:
        for item in x:        
            nombre=item["nombre"]
            precio=int(item["precio"])
            cantidad=int(item["cantidad"])
            total=int(item["total"])        
            ticket=Ticket(
                usuario=usuario,
                nombre=nombre,
                precio=precio,
                cantidad=cantidad,
                total=total,
                fecha=datetime.date.today()
            )
            ticket.save()
            suma=suma+int(total)  
            print("reg grabado")                 
        mensaje="Grabado"
        request.session["carritox"] = []
    except:
        mensaje="error al grabar"            
    return render(request,'core/carrito.html',{'x':x,'total':suma,'mensaje':mensaje})

@login_required(login_url='/login/')
def carro_compras(request,id):
    p=Floreria.objects.get(name=id)
    x=request.session["carritox"]
    el=elemento(1,p.name,p.valor,1)
    sw=0
    suma=0
    clon=[]
    for item in x:        
        cantidad=item["cantidad"]
        if item["nombre"]==p.name:
            sw=1
            cantidad=int(cantidad)+1
        ne=elemento(1,item["nombre"],item["precio"],cantidad)
        suma=suma+int(ne.total())
        clon.append(ne.toString())
    if sw==0:
        clon.append(el.toString())
    x=clon    
    request.session["carritox"]=x
    florcita=Floreria.objects.all()    
    return render(request,'core/galeria.html',{'listaFlores':florcita,'flores':florcita,'total':suma})

@login_required(login_url='/login/')
def carro_compras_mas(request,id):
    f=Floreria.objects.get(name=id)
    x=request.session["carritox"]
    suma=0
    clon=[]
    for item in x:        
        cantidad=item["cantidad"]
        if item["nombre"]==f.name:
            cantidad=int(cantidad)+1
        ne=elemento(1,item["nombre"],item["precio"],cantidad)
        suma=suma+int(ne.total())
        clon.append(ne.toString())
    x=clon    
    request.session["carritox"]=x
    x=request.session["carritox"]        
    return render(request,'core/carrito.html',{'x':x,'total':suma})

@login_required(login_url='/login/')
def carro_compras_menos(request,id):
    f=Floreria.objects.get(name=id)
    x=request.session["carritox"]
    clon=[]
    suma=0
    for item in x:        
        cantidad=item["cantidad"]
        if item["nombre"]==f.name:
            cantidad=int(cantidad)-1
        ne=elemento(1,item["nombre"],item["precio"],cantidad)
        suma=suma+int(ne.total())
        clon.append(ne.toString())
    x=clon    
    request.session["carritox"]=x
    x=request.session["carritox"]    
    return render(request,'core/carrito.html',{'x':x,'total':suma})

    

@login_required(login_url='/login/')
def galeria(request):
    florcita=Floreria.objects.all()
    return render(request,'core/galeria.html',{'listaFlores':florcita})

@login_required(login_url='/login/')
def home(request):
    return render(request,'core/home.html')

@login_required(login_url='/login/')
def carrito(request):
    x=request.session["carritox"]
    suma=0
    for item in x:
        suma=suma+int(item["total"])
    return render(request,'core/carrito.html',{'x':x,'total':suma})    

@login_required(login_url='/login/')
def formulario(request):
    flores=Floreria.objects.all()
    if request.POST:
        nombre=request.POST.get("InputName")
        imagen=request.FILES.get("InputFile")
        valor=request.POST.get("InputPrecio")
        descripcion=request.POST.get("InputDescripcion")
        estado=request.POST.get("InputEstado")
        stock=request.POST.get("Inputstock")
        flor=Floreria(
            name=nombre,
            fotografia=imagen,
            valor=valor,
            descripcion=descripcion,
            estado=estado,
            stock=stock
        )
        flor.save()
        return render(request,'core/formulario.html',{'listaflores':flores,'msg':'Flor Resgistrada'})
    return render(request,'core/formulario.html',{'listaflores':flores})



def login(request):
    if request.POST:
        usuario=request.POST.get("txtUsuario")
        password=request.POST.get("txtPass")
        us=authenticate(request,username=usuario,password=password)
        msg=''
        request.session["carrito"] = []
        request.session["carritox"] = []
        print('ingresado')
        if us is not None and us.is_active:
            login_autent(request,us)
            florcita=Floreria.objects.all()
            return render(request,'core/home.html',{'listaFlores':florcita})
        else:
            return render(request,'core/login.html')
    return render(request,'core/login.html')


def cerrar_session(request):
    logout(request)
    return render(request,'core/logout.html') 