import base64

from django.shortcuts import render

from .tools import determine_colors, image_from_base64


def colors_page(request):
    encoded_image = None
    colors = None
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']
        image_data = image.read()
        encoded_image = base64.b64encode(image_data).decode('utf-8')
        colors = determine_colors(
            image_from_base64(encoded_image)
        )
        colors = [f'rgb({x[1][0]}, {x[1][1]}, {x[1][2]})' for x in colors]
    return render(
        request,
        'colors.html',
        {
            'encoded_image': encoded_image,
            'colors': colors,
        }
    )


def pdf_page(request):
    if request.method == 'POST' and request.FILES.getlist('images'):
        images = request.FILES.getlist('images')
    return render(request, 'pdf.html')
