from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import AudioForm, SearchAudio
from .models import Audios


app_name = "api"


def home(request):
    all_audios = Audios.objects.all().values()
    print(all_audios)
    return render(request, "home.html", {
        "audios": all_audios,
        "total": len(all_audios),
    })


@login_required
def upload_audio(request):
    if request.method == 'POST':
        # I used django forms. see forms.py file 
        form = AudioForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, 'simple_upload.html', {
                'form': form,
                'error': "Something went wrong please try to upload again!"
            })
    else:
        form = AudioForm()
    return render(request, 'simple_upload.html', {
        'form': form
    })
    

@login_required
def get_audio(request):
    if request.method == 'POST':
        # search data from the search form 
        title = request.POST['title']
        
        # find the audio from the db
        audio = Audios.objects.filter(title=title).values()
        
        if audio:
            # if audio found then render the search_audio.html file and pass the audio
            return render(request, 'search_audio.html', {
                'audio': "http://127.0.0.1:8000/media/audio/" + audio[0]['audio'].split('/')[1],
                'title': title,
            })  
        else:
            # if there is no audio for search then render the upload form with a 
            # error message 
            form = AudioForm()
            return redirect('/upload/')
    else:
        form = SearchAudio()
        
    return render(request, 'search_audio.html', {
        'form': form,
    })
    
