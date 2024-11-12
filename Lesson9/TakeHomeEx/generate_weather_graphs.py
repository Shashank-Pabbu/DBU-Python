import matplotlib.pyplot as plt
import datetime

def generate_weather_graphs(weather_data):
    times = weather_data['hourly']['time'][:24]
    time_labels = [datetime.datetime.fromisoformat(time).strftime('%H:%M') for time in times]

    # Plot Temperature
    if 'temperature_2m' in weather_data['hourly']:
        temperatures = weather_data['hourly']['temperature_2m'][:24]
        plt.figure(figsize=(10, 5))
        plt.plot(time_labels, temperatures, marker='o', linestyle='-', color='b')
        plt.xticks(rotation=45)
        plt.xlabel('Time (24 hours)')
        plt.ylabel('Temperature (°C)')
        plt.title('Temperature Forecast')
        plt.tight_layout()
        plt.savefig('static/temperature_plot.png')
        plt.close()
    else:
        print("Temperature data not available")

    # Plot Cloud Cover
    if 'cloudcover' in weather_data['hourly']:
        cloud_cover = weather_data['hourly']['cloudcover'][:24]
        plt.figure(figsize=(10, 5))
        plt.plot(time_labels, cloud_cover, marker='o', linestyle='-', color='purple')
        plt.xticks(rotation=45)
        plt.xlabel('Time (24 hours)')
        plt.ylabel('Cloud Cover (%)')
        plt.title('Cloud Cover Forecast')
        plt.tight_layout()
        plt.savefig('static/cloud_cover_plot.png')
        plt.close()
    else:
        print("Cloud cover data not available")

    # Plot Wind Speed
    if 'windspeed_10m' in weather_data['hourly']:
        wind_speed = weather_data['hourly']['windspeed_10m'][:24]
        plt.figure(figsize=(10, 5))
        plt.plot(time_labels, wind_speed, marker='o', linestyle='-', color='r')
        plt.xticks(rotation=45)
        plt.xlabel('Time (24 hours)')
        plt.ylabel('Wind Speed (m/s)')
        plt.title('Wind Speed Forecast')
        plt.tight_layout()
        plt.savefig('static/wind_speed_plot.png')
        plt.close()
    else:
        print("Wind speed data not available")

    # Plot Precipitation
    if 'precipitation' in weather_data['hourly']:
        precipitation = weather_data['hourly']['precipitation'][:24]
        plt.figure(figsize=(10, 5))
        plt.plot(time_labels, precipitation, marker='o', linestyle='-', color='c')
        plt.xticks(rotation=45)
        plt.xlabel('Time (24 hours)')
        plt.ylabel('Precipitation (mm)')
        plt.title('Precipitation Forecast')
        plt.tight_layout()
        plt.savefig('static/precipitation_plot.png')
        plt.close()
    else:
        print("Precipitation data not available")

    return {
        'temperature': 'static/temperature_plot.png' if 'temperature_2m' in weather_data['hourly'] else None,
        'cloud_cover': 'static/cloud_cover_plot.png' if 'cloudcover' in weather_data['hourly'] else None,
        'wind_speed': 'static/wind_speed_plot.png' if 'windspeed_10m' in weather_data['hourly'] else None,
        'precipitation': 'static/precipitation_plot.png' if 'precipitation' in weather_data['hourly'] else None
    }
