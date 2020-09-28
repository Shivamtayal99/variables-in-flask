from flask import Flask, jsonify,render_template
from multiprocessing import Value

app = Flask(__name__)
@app.route('/string/<name>')
def string(name):
    return "Hello %s" %name
@app.route('/int/<int:number>')
def emp_id(number):
    return "Your emp_id is %d" %number
@app.route('/float/<float:salary>')
def salary(salary):
    return "your sal is %f" %salary


app.run(port=5001,debug=True)