from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def form():
    states = ["AL", "IN", "DC", "FL", "GA", "IL", "KS", "KY", "OH", "MD", "MI", "MO", "TX", "TN", "WI", "NY", "LA",
              "OK", "IA", "AR"]
    health_ministries = ["ALBIR", "CTBRI", "DCWAS", "FLJAC", "FLPEN", "ILARL", "INEVA", "ININD", "KSWIC", "MDBAL",
                         "MIDET", "MIGRA", "MIKAL", "MIROC", "MISAG", "MITAW", "MOSTL", "OKTUL", "TNNAS", "TXAUS",
                         "TXWAC", "WIAPP", "WIMIL"]

    if request.method == 'POST':
        # handle form submission here
        data = request.form
        return f"Form submitted! {data}"

    return render_template('form.html', states=states, health_ministries=health_ministries)


if __name__ == "__main__":
    app.run(debug=True)