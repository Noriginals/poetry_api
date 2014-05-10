from flask import Flask, Response, render_template
from flask_wtf.csrf import CsrfProtect

from forms import PoetrySearchForm

csrf = CsrfProtect()
app = Flask(__name__)
app.config.from_object('config')
csrf.init_app(app)


def limerick():
    limericks = list()
    with open('api/limerick.txt') as f:
        for line in f:
            if len(line.strip()):
                limericks.append(line)

    return limericks

@app.route('/', methods=('GET', 'POST'))
def index():
    form = PoetrySearchForm()
    if form.validate_on_submit():
        #return render_template('index.html')
        print 'Awesome'
    return render_template('index.html', form=form)

@app.route('/stream')
def stream_feed():
    def generate():
        for line in limerick():
            yield line
    return Response(generate(), mimetype='text/plain')

if __name__ == '__main__':
    app.run()
