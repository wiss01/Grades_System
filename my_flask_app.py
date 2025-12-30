from flask import Flask, render_template, request
import my_flask_app_source_code

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index2.html')

@app.route('/run_software', methods=['POST'])
def run_software():
    # Call your Python software's function here and get the result
    result = my_flask_app_source_code.main()
    return {'result': result}

if __name__ == '__main__':
    app.run(debug=True)
