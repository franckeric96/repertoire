from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import Contact
# Create your views here.


@login_required(login_url="/login/")

def contact_list(request):
    user = request.user
    contacts = Contact.objects.filter(auteur=user, archive=False)
    datas = {
        "contacts":contacts

    }
    
    return render(request, "contacts/contact_list.html", datas)


@login_required(login_url="/login/")


def contact_details(request, id):

    contact = get_object_or_404(Contact, id=id)

    datas = {
        "contact":contact
    }
    
    return render(request, "contacts/contact_details.html", datas)


@login_required(login_url="/login/")

def new_contact(request):

    if request.method == "POST":
        auteur = request.user
        nom = request.POST["nom"]
        prenom = request.POST["prenom"]
        telephone = request.POST["telephone"]
        email = request.POST["email"]
        contact = Contact.objects.create(
            auteur=auteur,
            nom=nom,
            prenom=prenom,
            telephone=telephone,
            email=email

        )

        contact.save()
        return redirect("/contacts/")

    datas = {

    }
    
    return render(request, "contacts/new_contact.html", datas)


def edit_contact(request, id):


    contact = get_object_or_404(Contact, id=id)
    if request.method == "POST":
        nom = request.POST["nom"]
        prenom = request.POST["prenom"]
        telephone = request.POST["telephone"]
        email = request.POST["email"]
        contact_to_update = Contact.objects.filter(pk=contact.id)
        contact_to_update.update(
            nom=nom,
            prenom=prenom,
            telephone=telephone,
            email=email

        )
        return redirect("/contacts/")

    datas ={
        "contact": contact
    }

    return render(request, "contacts/edit_contact.html", datas)


@login_required(login_url="/login/")

def delete_contact(request, id):
    contact = get_object_or_404(Contact, id=id)
    if request.method == "POST":
        contact_to_delete = Contact.objects.filter(pk=contact.id)
        contact_to_delete.update(
            archive = True
        )
        #contact.delete()
        return redirect("/contacts/")

    datas ={
        "contact": contact
    }
    return render(request,"contacts/delete_contact.html", datas)
