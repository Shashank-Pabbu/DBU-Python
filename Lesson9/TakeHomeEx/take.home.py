# Objective: Take the code from ex5 and modify it to include the following:

# Tasks:
from generate_weather_graphs import generate_weather_graphs
import requests
import datetime
from flask import Flask, request, render_template
import matplotlib.pyplot as plt
# Obtain and process 3 additional attributes in the weather data.
# Graphically represent the additional attributes.
# Update the HTML template to display the additional attributes.

# Submission Timeline:
# Submit the code in 2 weeks.
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def weather():
    weather_data = None
    graph_filenames = None
    
    if request.method == 'POST':
        city = request.form['city']
        
        # Fetch location data
        try:
            geocoding_response = requests.get(f'https://geocoding-api.open-meteo.com/v1/search?name={city}')
            if geocoding_response.status_code == 200 and geocoding_response.json().get('results'):
                location = geocoding_response.json()['results'][0]
                latitude, longitude = location['latitude'], location['longitude']

                # Fetch weather data with additional attributes
                weather_response = requests.get(
                 f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,windspeed_10m,precipitation,cloudcover&timezone=auto'
                   )

                print("Weather response:", weather_response.status_code, weather_response.text)

                
                if weather_response.status_code == 200:
                    weather_data = weather_response.json()
                    graph_filenames = generate_weather_graphs(weather_data)
                else:
                    weather_data = {'error': 'Unable to retrieve weather data.'}
            else:
                weather_data = {'error': 'City not found'}
        except Exception as e:
            weather_data = {'error': f'Error fetching data: {e}'}

    return render_template('dashboard.html', weather_data=weather_data, graph_filenames=graph_filenames)

if __name__ == '__main__':
    app.run(debug=True)
