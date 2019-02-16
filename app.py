from flask import Flask, render_template
from plot_it import *
from bokeh.embed import components
from calculations import sample_score_perc

script, div = components(plot)
app = Flask(__name__)


@app.route('/')
def main():
    return render_template('main.html',
                           script=script,
                           div=div,
                           us_score=sample_score_perc)


if __name__ == '__main__':
    app.run()
