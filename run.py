from flask import Flask, render_template, request, redirect

app = Flask(__name__,static_url_path="/static", static_folder="./static")

list_kapal = {
    "1": {
        "name": "KM Dorolonda",
        "tipe": "Passenger Ship",
        "mmsi": 525005046,
        "LOA": 146.5,
        "Draft": 5.90,
        "Breadth": 23.4,
        "Displacement": 10534.7,
        "vt_design": 23.67,
        "gross_tonnage":14.685,
        "netto_tonnage": 4.629,
        "death_weight": 3.175,
        "main_engine": "2 Krupp MAK 8M 601C",
        "aux_engine": "Daihatsu 6DL-24"
        },
    "2": {
        "name": "KM Labobar",
        "tipe": "Passenger Ship",
        "mmsi": 525005052,
        "LOA": 146.5,
        "Draft": 5.90,
        "Breadth": 23.4,
        "Displacement": 10534.7,
        "vt_design": 23.67,
        "gross_tonnage":14.685,
        "netto_tonnage": 4.629,
        "death_weight": 3.175,
        "main_engine": "2 Krupp MAK 8M 601C",
        "aux_engine": "Daihatsu 6DL-24"
        },
    "3": {
        "name": "KM Sangiang",
        "tipe": "Passenger Ship",
        "mmsi": 525005037,
        "LOA": 146.5,
        "Draft": 5.90,
        "Breadth": 23.4,
        "Displacement": 10534.7,
        "vt_design": 23.67,
        "gross_tonnage":14.685,
        "netto_tonnage": 4.629,
        "death_weight": 3.175,
        "main_engine": "2 Krupp MAK 8M 601C",
        "aux_engine": "Daihatsu 6DL-24"
        },
    "4": {
        "name": "KM Sinabung",
        "tipe": "Passenger Ship",
        "mmsi": 525005031,
        "LOA": 146.5,
        "Draft": 5.90,
        "Breadth": 23.4,
        "Displacement": 10534.7,
        "vt_design": 23.67,
        "gross_tonnage":14.685,
        "netto_tonnage": 4.629,
        "death_weight": 3.175,
        "main_engine": "2 Krupp MAK 8M 601C",
        "aux_engine": "Daihatsu 6DL-24"
        },
    "5": {
        "name": "KM Tatamailau",
        "tipe": "Passenger Ship",
        "mmsi": 525005012,
        "LOA": 146.5,
        "Draft": 5.90,
        "Breadth": 23.4,
        "Displacement": 10534.7,
        "vt_design": 23.67,
        "gross_tonnage":14.685,
        "netto_tonnage": 4.629,
        "death_weight": 3.175,
        "main_engine": "2 Krupp MAK 8M 601C",
        "aux_engine": "Daihatsu 6DL-24"
        },
    "6": {
        "name": "KM Tilongkabila",
        "tipe": "Passenger Ship",
        "mmsi": 525005016,
        "LOA": 146.5,
        "Draft": 5.90,
        "Breadth": 23.4,
        "Displacement": 10534.7,
        "vt_design": 23.67,
        "gross_tonnage":14.685,
        "netto_tonnage": 4.629,
        "death_weight": 3.175,
        "main_engine": "2 Krupp MAK 8M 601C",
        "aux_engine": "Daihatsu 6DL-24"
        },
}

@app.route('/')
def home():
    return render_template("dashboard.html")

@app.route('/vessel/')
def ves_redir():
    return redirect(request.host_url+"vessel/1")

@app.route('/vessel/<id>')
@app.route('/vessel/<id>/')
def vessel(id=None):
    return render_template('kapal.html', name=list_kapal[id]["name"], id=id, mmsi=list_kapal[id]["mmsi"], hostname=request.host, spec=list_kapal[id])

@app.route('/vessel/<id>/speed')
def speed(id=None):
    return render_template('chart.html', name=list_kapal[id]["name"], id=id, data="Kecepatan")
@app.route('/vessel/<id>/distance')
def distance(id=None):
    return render_template('chart.html', name=list_kapal[id]["name"], id=id, data="Jarak")
@app.route('/vessel/<id>/time')
def sail(id=None):
    return render_template('chart.html', name=list_kapal[id]["name"], id=id, data="Waktu Berlayar")
@app.route('/vessel/<id>/anchor')
def anchor(id=None):
    return render_template('chart.html', name=list_kapal[id]["name"], id=id, data="Waktu Jangkar")
@app.route('/vessel/<id>/analyze')
def analyze(id=None):
    return render_template('chart.html', name=list_kapal[id]["name"], id=id, data="Analisa")