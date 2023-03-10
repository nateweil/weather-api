from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

stations = pd.read_csv("data_small/stations.txt", skiprows=17)
stations = stations[["STAID","STANAME                                 "]]
@app.route("/")
def home():
    return render_template("home.html", data=stations.to_html())

@app.route("/api/v1/<station>/<date>")
def about(station, date):
    filepath = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    data = pd.read_csv(filepath, skiprows=20, parse_dates=["    DATE"])

    # temperature = data.station(date)
    temperature = data.loc[data["    DATE"] == date]["   TG"].squeeze() / 10
    # return render_template("about.html")
    return {"Station: ": station,
            "Date: ": date,
            "Temperature: ": temperature}

if __name__ == "__main__":
    app.run(debug=True, port=5001)