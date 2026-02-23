import requests
from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello.html')

# Déposez votre code à partir d'ici :
@app.route("/contact")
def MaPremiereAPI():
    return render_template('contact.html')

@app.get("/paris")
def api_paris():
    
    url = "https://api.open-meteo.com/v1/forecast?latitude=48.8566&longitude=2.3522&hourly=temperature_2m"
    response = requests.get(url)
    data = response.json()

    times = data.get("hourly", {}).get("time", [])
    temps = data.get("hourly", {}).get("temperature_2m", [])

    n = min(len(times), len(temps))
    result = [
        {"datetime": times[i], "temperature_c": temps[i]}
        for i in range(n)
    ]

    return jsonify(result)

@app.route("/rapport")
def mongraphique():
    return render_template("graphique.html")

@app.route("/histogramme")
def histogramme():
    return render_template("graphique2.html")

@app.get("/lisbonne")
def api_lisbonne():
    
    url = "https://api.open-meteo.com/v1/forecast?latitude=38.7167&longitude=-9.1333&hourly=temperature_2m,rain,wind_speed_50m&models=meteofrance_seamless"
    response = requests.get(url)
    data = response.json()

    times = data.get("hourly", {}).get("time", [])
    temps = data.get("hourly", {}).get("temperature_2m", [])
    rain = data.get("hourly", {}).get("rain", [])
    wind_speed = data.get("hourly", {}).get("wind_speed_50m", [])

    n = min(len(times), len(temps), len(rain), len(wind_speed))
    result = [
        {"datetime": times[i], "temperature_c": temps[i], "pluie_mm": rain[i], "vitesse_du_vent_km_h": wind_speed[i]}
        for i in range(n)
    ]

    return jsonify(result)

@app.route("/atelier")
def atelier():
    return render_template("atelier.html")
# Ne rien mettre après ce commentaire
    
if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000, debug=True)
