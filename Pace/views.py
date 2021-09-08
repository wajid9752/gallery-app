from django.shortcuts import render,redirect
from .models import *
from .forms import * 


def home(request):
    categories=Category.objects.all()
    categoryid=request.GET.get('category')
    photos=None
    if categoryid:
        photos=Photo.objects.filter(category=categoryid)
    else:
        photos=Photo.objects.all()    

    context={
        'categories':categories,
        'photos':photos,
    }
    return render(request, 'gallery/home.html',context)
def upload_file(request):
    form=UploadForm()

    if request.POST:
        form=UploadForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print("something went wrong")    


    return render(request, 'Upload_Photo/upload.html',{'form':form})