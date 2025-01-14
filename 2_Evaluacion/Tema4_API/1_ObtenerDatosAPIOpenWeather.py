import requests
from config import API_KEY

# Definir parámetros

lat = "44.34"
lon = "10.99"
ciudad = "Valladolid"
# URL de la API de OpenWeather
url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={API_KEY}"

# Realizamos una solicitud GET para obtener información de la API
response = requests.get(url)

# Verificamos si la solicitud es correcta
if response.status_code == 200:
    # Extraemos la información del JSON
    data = response.json()

    # Obtener datos específicos del JSON
    ciudad = data['name']
    temperatura = data['main']['temp']- 273.15
    descripcion_clima = data['weather'][0]['description']
    humedad = data['main']['humidity']
    presion = data['main']['pressure']
    temperaturaNumero=int(temperatura)
    temperaturaCelsius=(temperaturaNumero * 9 / 5) + 32
    # Mostrar los datos de forma clara y organizada
    print(f"Ciudad: {ciudad}")
    print(f"Temperatura: {temperatura:.2f}°C")
    print(f"Descripción del clima: {descripcion_clima}")
    print(f"Humedad: {humedad}%")
    print(f"Presión atmosférica: {presion} hPa")
else:
    print(f"Error en la solicitud. Código de estado: {response.status_code}")
