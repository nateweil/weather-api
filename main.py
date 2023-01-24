from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")

def home():
    return render_template("home.html")

@app.route("/api/v1/<station>/<date>")
def about(station, date):

    # data = pandas.read_csv("")
    # temperature = data.station(date)
    temperature = 23
    # return render_template("about.html")
    return {"Station: ": station,
            "Date: ": date,
            "Temperature: ": temperature}

if __name__ == "__main__":
    app.run(debug=True)