
from xml.dom.pulldom import parseString
from django.shortcuts import redirect, render
from django.http import HttpRequest
from django.contrib.auth import authenticate , login ,logout
from .models import *
from django.core.paginator import Paginator 
from .forms import  *
from django.contrib import messages


def Register (request):
    form = CreateUserForm()
    form2 = CreateAssociation()
    if request.method =='POST':
        form = CreateUserForm(request.POST)
        
        if form.is_valid():
            name = request.POST['name']
            file = request.POST['file']
            willaya = request.POST['willaya']
            
            user = form.save()
            user.is_association =True
            user.save()
            Association.objects.create(
                    user=user ,
                    name=name ,
                    file=file,
                    willaya=willaya
            )

            messages.success(request,'account created seccefully ')
            return redirect('login')

    context= {'form':form ,'form2':form2} 
    return render(request,'signup.html',context)





def RegisterUser (request):
    form = CreateUserForm()
    form2 = CreatePersonne()
    if request.method =='POST':
        form = CreateUserForm(request.POST)
        
        if form.is_valid():
            name = request.POST['first_name']
            last_name = request.POST['last_name']
            willaya = request.POST['willaya']
             
            user = form.save()
            user.is_person =True
            user.save()
            PhysicalUser.objects.create(
                    user=user ,
                    first_name=name ,
                    last_name=last_name,
                    willaya=willaya , 
            )

            messages.success(request,'account created seccefully ')
            return redirect('login')

    context= {'form':form ,'form2':form2} 
    return render(request,'physical.html',context)



def Loginin (request):
    form = LoginForm()
    if request.method =='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email=request.POST['email']
            password=request.POST['password']
            user = authenticate(request , email=email,password=password )  
            if user is not None :
                if  user.is_association   :
                    ass = Association.objects.get(user = user)
                    if ass.is_valid == True :
                        login (request , user ) 
                        return redirect('profile')
                    else :
                        messages.error(request , "cette association n'est pas valide")
                else :
                    login (request , user ) 
                    return redirect('profile')           
    context= {'form':form}
    return render(request,'login.html',context)


def Profile (request):
    context= {}
    return render(request,'profile.html',context)



def Select (request):
    
    context= {}
    return render(request,'select.html',context)


def Logoutt (request):
    logout(request)
    return redirect('login')

def annonce (request):
    annonces= Annonce.objects.all()
    formAnnonce = AnnonceForm()
    if request.method =='POST':
        auteur= request.user
        if formAnnonce.is_valid :
            image = request.FILES['image']
            contenu = request.POST['contenu']
            type = request.POST['type']
            Annonce.objects.create(
                auteur = auteur,
                image = image ,
                contenu =contenu ,
                type = type 
            )
            return redirect('annonce')

    context= {'formAnnonce':formAnnonce , 'annonces':annonces}
    return render(request,'annonce.html',context)

def delete_annonce (request,myid) :
    item = Annonce.objects.get(id =myid)
    item.delete()
    messages.info(request,'Annonce supprimé')
    return redirect(annonce)

def ListCagniote (request):
    cagnites= Cagniote.objects.all()
    form = CreateCagniote ()
    if request.method =='POST':
        username = request.user
        association = Association.objects.get(user=username)
        if form.is_valid :
            titre = request.POST['titre']
            contenu = request.POST['contenu']
            somme = request.POST['sommeDemander']
            Cagniote.objects.create(
                user = association,
                titre = titre ,
                contenu =contenu ,
                sommeDemander = somme 
            )

    context= {'form':form , 'cagniotes':cagnites}
    return render(request,'cagniote.html',context)


def Admin (request):
    cagniote = Cagniote.objects.all()
    association = Association.objects.all()
    person = PhysicalUser.objects.all()
    annonce = Annonce.objects.all()
    
    
    context= {'cagniote':cagniote.__len__,'association':association.__len__ , 'person':person.__len__ ,'annonce':annonce.__len__}
    return render(request,'admin.html',context)

def Arreter (request,myid) :
    item = Cagniote.objects.get(id =myid)
    item.arret = True
    item.save()
    
    return redirect(ListCagniote)

def Control (request):
    associations = Association.objects.all()
    users = User.objects.all()
    annonces = Annonce.objects.all()

    paginator= Paginator(users,5)
    page_number=request.GET.get('page')
    users=paginator.get_page(page_number)

    paginator= Paginator(associations,5)
    page_number=request.GET.get('page')
    associations=paginator.get_page(page_number)

    paginator= Paginator(annonces,5)
    page_number=request.GET.get('page')
    annonces=paginator.get_page(page_number)

    

    context= {'associations': associations,'users':users, 'annonces':annonces}
    return render(request,'control.html',context)    

def Valider (request,myid) :
    item = Association.objects.get(user_id =myid)
    item.is_valid = True
    item.save()
    
    return redirect(Control)

def deleteAssociation (request,myid) :
    item = User.objects.get(id =myid)
    item.delete()
    
    return redirect(Control)

def deleteUser (request,myid) :
    item = User.objects.get(id =myid)
    item.delete()
    
    return redirect(Control)

def deleteAnnonce (request,myid) :
    item = Annonce.objects.get(id =myid)
    item.delete()
    
    return redirect(Control)


def List_Association (request):
    associations = Association.objects.all()
    paginator= Paginator(associations,10)
    page_number=request.GET.get('page')
    associations=paginator.get_page(page_number)

    context= {'associations':associations}
    return render(request,'listAssociations.html',context)