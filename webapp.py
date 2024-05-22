from flask import Flask, render_template_string, request, render_template
import csv

# create Flask web app's instance
app = Flask(__name__)

# read data from CSV
@app.route('/')
def read():

    data = []

    with open('backend_frontend.csv', 'r') as f:
        # create CSV dictionary reader instance
        csv_reader = csv.DictReader(f)

        # estrarre righe da csv
        for row in csv_reader:
            data.append(row)

        return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)