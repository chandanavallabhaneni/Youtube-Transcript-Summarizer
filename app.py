from flask import Flask, render_template, request
from ytb import *

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('miniht.html')

@app.route('/frm',methods=['POST','GET'])
def frm():
    if request.method == 'POST':
        link = request.form.get('link')
        return render_template('miniht.html',link=sumriz(link))
        # print(sumriz(link))


if __name__ == '__main__':
    app.run(debug=True)