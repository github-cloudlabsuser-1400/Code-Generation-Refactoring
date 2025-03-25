import requests

class WeatherAPI:
    """
    Clase para interactuar con la API de OpenWeatherMap.
    """

    def __init__(self, api_key):
        """
        Inicializa la clase con la clave de API.

        Args:
            api_key (str): Tu clave de API de OpenWeatherMap.
        """
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"

    def get_weather_by_city(self, city_name):
        """
        Obtiene los datos meteorológicos de una ciudad.

        Args:
            city_name (str): El nombre de la ciudad.

        Returns:
            dict: Los datos meteorológicos en formato JSON.
        """
        params = {
            "q": city_name,
            "appid": self.api_key,
            "units": "metric",  # Para obtener los datos en grados Celsius
            "lang": "es"        # Para obtener los datos en español
        }
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()


# Ejemplo de uso
if __name__ == "__main__":
    # Reemplaza 'TU_API_KEY' con tu clave de API de OpenWeatherMap
    api_key = "e85d2a24c3ec9ea48196e24a43c34dec"
    weather_api = WeatherAPI(api_key)

    ciudad = input("Introduce el nombre de la ciudad: ")
    try:
        datos_clima = weather_api.get_weather_by_city(ciudad)
        print(f"Clima en {ciudad}:")
        print(f"Temperatura: {datos_clima['main']['temp']}°C")
        print(f"Descripción: {datos_clima['weather'][0]['description']}")
        print(f"Humedad: {datos_clima['main']['humidity']}%")
        print(f"Viento: {datos_clima['wind']['speed']} m/s")
    except requests.exceptions.HTTPError as e:
        print(f"Error al obtener los datos: {e}")