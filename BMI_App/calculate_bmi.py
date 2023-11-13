from flask import Flask, render_template, request

app = Flask(__name__)

def convert_cm_to_m(h): 
    # Convert centimeter to meter
    return h/100

def bmi_classification(bmi):
    if bmi < 18.5:
        return 'Thinness'
    elif bmi >= 18.5 and bmi <= 25:
        return 'Normal'
    else:
        return 'Overweight'


@app.route('/', methods=['POST', 'GET'])
def bmi_calculation():
    if request.method == "POST":
        height = request.form['height']
        weight = request.form['weight']

        h_m = convert_cm_to_m(float(height))
        bmi = float(weight)/(h_m)**2

        bmi_type = bmi_classification(bmi)
        
        return render_template('index.html', output1 = round(bmi, 2), output_2 = bmi_type)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True) 