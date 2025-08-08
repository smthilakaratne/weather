from django.shortcuts import render
import requests


API_KEY = '672a951ea0c749dd80f175906252407'

def get_weather(request):
    city = request.GET.get('city', 'Colombo')
    url = f'https://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={city}&days=3'

    response = requests.get(url)
    data = response.json()

    forecast_days = []
    temps = []
    humidities = []

    for day in data['forecast']['forecastday']:
        forecast_days.append(day['date'])
        temps.append(day['day']['avgtemp_c'])
        humidities.append(day['day']['avghumidity'])

    combined_data = zip(forecast_days, temps, humidities)

    context = {
        'city': city,
        'combined_data': combined_data,
        'data': data
    }

    return render(request, 'home/weather.html', context)

