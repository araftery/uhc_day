import cStringIO

from django.http import HttpResponse
from django.shortcuts import render
from django.core.files.storage import default_storage as storage
from django.core.files.base import ContentFile

from PIL import Image

from poster import forms
from poster.utils import general


def overlay(request):
    if request.method == 'POST':
        form = forms.CropForm(request.POST, request.FILES)
        if form.is_valid():
            x = form.cleaned_data.get('x')
            y = form.cleaned_data.get('y')
            w = form.cleaned_data.get('w')
            h = form.cleaned_data.get('h')
            image = form.cleaned_data.get('image')
            overlay_choice = form.cleaned_data.get('overlay_choice')
            image_file = cStringIO.StringIO(image.read())
            background = Image.open(image_file)

            # sizes we have overlays for
            sizes = [200, 250, 300, 350, 400, 450, 500, 550, 600]

            size = general.round_down(w, sizes)
            background = background.convert('RGB').crop((x, y, x + w, y + h)).resize((size, size), Image.ANTIALIAS)

            # overlay
            foreground = Image.open(storage.open('/overlays/{}_600.png'.format(overlay_choice), 'r')).resize((size, size), Image.ANTIALIAS)
            background.paste(foreground, (0, 0), foreground)

            output = cStringIO.StringIO()
            background.save(output, "PNG")
            content = output.getvalue()
            offset = 1
            while storage.exists('/propics/%03d.png' % offset):
                offset += 1

            storage.save('/propics/%03d.png' % offset, ContentFile(content))
            output.close()
            response = HttpResponse(content, content_type='image/png')
            response['Content-Length'] = len(content)
            response['Content-Disposition'] = 'filename="uhc-day-propic.png";'
            return response
    else:
        form = forms.CropForm()

    return render(request, 'poster/overlay.html', {'form': form})
