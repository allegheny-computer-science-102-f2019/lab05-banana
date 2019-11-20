###################################
#   Graph Networks
#   By Team Banana
#      Danny Ullrich
#      Adam Cook
#      Caden Koscinski
###################################

from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import network as n


app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/', methods=['POST'])
def my_form_post():
    if request.method == 'POST':
        text = request.form['text']
        processed_text = text.upper() + ".html"
        print(processed_text)
        n.build_network(processed_text)
        return render_template('graph.html', value=processed_text)

if __name__ == '__main__':
    app.run(debug=True)
