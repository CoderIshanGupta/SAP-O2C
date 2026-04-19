from flask import Flask, render_template, request
from services.o2c_service import run_o2c_process

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    customer = request.form['customer']
    material = request.form['material']
    qty = int(request.form['qty'])

    result = run_o2c_process(customer, material, qty)

    return render_template('result.html', steps=result)

if __name__ == '__main__':
    app.run(debug=True)