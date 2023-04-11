from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home_page():
    return render_template('/index.html')


@app.route('/postman', methods=['POST'])
def math_operation():
    if request.method == 'POST':
        opp = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        if opp == 'add':
            rest = num1 + num2
            result = 'The is sum of' + str(num1), 'and', +str(num2), 'is', + str(rest)

        if opp == 'subtract':
            rest = num1 - num2
            result = 'The is sum of' + str(num1), 'and', +str(num2), 'is', + str(rest)

        if opp == "multiply":
            rest = num1 * num2
            result = 'The is sum of' + str(num1), 'and', +str(num2), 'is', + str(rest)

        if opp == 'divide':
            rest = num1 / num2
            result = 'The is sum of' + str(num1), 'and', +str(num2), 'is', + str(rest)

        return render_template('result.html', result=result)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
