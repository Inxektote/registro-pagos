from flask import Flask, render_template, request, redirect
import csv
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nombre = request.form['nombre']
        monto = request.form['monto']
        fecha = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        with open('pagos.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([nombre, monto, fecha])

        return redirect('/')
    return render_template('formulario.html')

if __name__ == '__main__':
    app.run(debug=True)