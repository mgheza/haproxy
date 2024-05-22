data = []

# read data from CSV file
with open('backend_frontend.csv', 'r') as f:
    # create CSV dictionary reader instance
    csv_reader = csv.DictReader(f)

    # estrarre righe da csv
    for row in csv_reader:
        data.append(row)

# render HTML page dinamically
return render_template_string('''
        <html>
            <head>
                <!-- Bootstrap CDN -->
                <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css">
            </head>
            <body>
                <h1 class="text-danger">Read data from CSV</h1>
                <div class="container">
                    <!-- CSV data -->
                    <table class="table">
                        <thead>
                            <tr>
                                {% for header in data[0].keys() %}
                                    <th scope="col">{{ header }}</th>
                                {% endfor %}
                            </tr>
                        </thead>
                        <tbody>
                            {% for row in data %}
                                <tr>
                                    {% for value in row.values() %}
                                        <td>{{ value }}</td>
                                    {% endfor %}
                                </tr>
                            {% endfor %}

                        </tbody>
                    </table>
                </div>
            </body>
        </html>
    ''', data=data)

# run HTTP server
if __name__ == '__main__':
    app.run(debug=True, threaded=True)