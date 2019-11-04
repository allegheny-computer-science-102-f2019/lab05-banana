###################################
#   Graph Networks
#   By Team Banana
#      Danny Ullrich
#      Adam Cook
#      Caden Koscinski
###################################

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import network as n


app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def home():
    n.build_network("mygraph2")
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
