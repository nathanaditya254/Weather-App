from flask import Flask, redirect, render_template, request, jsonify, url_for
from flask_cors import CORS
from weather import get_coordinates, get_weather, geo_reverse
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OpenWeather_apiKey")

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('welcome.html')

@app.route("/city", methods=["GET"])
def get_coords():
    city = request.args.get("cty")
    if city is None:
        return render_template("cty.html")
    
    lat, lon = get_coordinates(city)
    return redirect(url_for('weather', lat=lat, lon=lon, city=city))

@app.route("/coords", methods = ['GET'])
def coords():
    lat = request.args.get('lat', 40.7127281, type = float)
    lon = request.args.get("lon", default=None, type=float)
    if lat is None or lon is None:
            return render_template("coords.html")
    city = geo_reverse(lat, lon)
    return redirect(url_for('weather', lat=lat, lon=lon, city=city))

@app.route("/weather", methods=['GET'])
def weather():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    city = request.args.get('city')
    weather_desc, temp, feels_like, temp_min, temp_max = get_weather(lat, lon)
    return render_template(
        "weather.html",
        city=city,
        weather=weather_desc,
        temp=temp,
        feels_like=feels_like,
        temp_min=temp_min,
        temp_max=temp_max
    )

if __name__ == '__main__':
    app.run(debug=True)