import base64

import img2pdf
from django.shortcuts import HttpResponse, render

from .tools import determine_colors, image_from_base64, rgb2hex


def home_page(request):
    return render(
        request,
        'home.html',
        {
            'page1_active': '',
            'page2_active': '',
        })


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
        colors = [rgb2hex(x[1][0], x[1][1], x[1][2]) for x in colors]
    return render(
        request,
        'colors.html',
        {
            'page1_active': 'active',
            'page2_active': '',
            'encoded_image': encoded_image,
            'colors': colors,
        }
    )


def pdf_page(request):
    if request.method == 'POST' and request.FILES.getlist('images'):
        images = request.FILES.getlist('images')
        pdf_data = img2pdf.convert(images)
        print(type(pdf_data))
    return render(
        request,
        'pdf.html',
        {
            'page1_active': '',
            'page2_active': 'active',
        })


def convert_to_pdf(request):
    if request.method == 'POST' and request.FILES.getlist('images'):
        images = request.FILES.getlist('images')
        pdf_data = img2pdf.convert(images)
        response = HttpResponse(pdf_data, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="document.pdf"'
        return response
