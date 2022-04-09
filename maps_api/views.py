from django.shortcuts import render

# Create your views here.
def default_map(request):
    # TODO: move this token to Django settings from an environment variable
    mapbox_access_token = 'pk.eyJ1IjoibGl2ZWJyaWdodGx5IiwiYSI6ImNsMXI1ODdlMTBoYjEzY285czU2azN0aXcifQ._1Ir-vvfeVEh-OJnUGWiVg'   
    return render(request, 'default.html', { 'mapbox_access_token': mapbox_access_token })




