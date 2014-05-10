from flask import Flask, Response, render_template
from flask_wtf.csrf import CsrfProtect

from forms import PoetrySearchForm

from poetryutils2 import filters as poetry_filters, line_iter

# CSRF Protection
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

        # Build Filters
        data = form.data
        filters = []

        if data['letter_ratio']:
            filters.append(poetry_filters.low_letter_filter(data['letter_ratio']))
        if data['url']:
            filters.append(poetry_filters.url_filter)
        if data['emoji']:
            filters.append(poetry_filters.emoticons)

        # Source
        source = open(app.config['SOURCE'])

        # Return Generator
        def generate():
            for rec in line_iter(source, filters):
                yield rec

        # Stream
        return Response(generate(), mimetype='text/plain')

    return render_template('index.html', form=form)

@app.route('/stream')
def stream_feed():
    def generate():
        for line in limerick():
            yield line
    return Response(generate(), mimetype='text/plain')

if __name__ == '__main__':
    app.run()
