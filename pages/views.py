from django.shortcuts import render


def about_us(request):
    return render(request, template_name='pages/about-us.html')


def single_speaker(request):
    return render(request, template_name='pages/single-speaker.html')


def gallery(request):
    return render(request, template_name='pages/gallery.html')


def testimonial(request):
    return render(request, template_name='pages/testimonial.html')


def pricing(request):
    return render(request, template_name='pages/pricing.html')
