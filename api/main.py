from flask import Flask, Response, render_template
from flask_wtf.csrf import CsrfProtect
import time

from poetryutils2 import filters as poetry_filters, line_iter

from forms import PoetrySearchForm

# CSRF Protection
csrf = CsrfProtect()
app = Flask(__name__)
app.config.from_object('config')
csrf.init_app(app)


@app.route('/', methods=('GET', 'POST'))
def index():
    form = PoetrySearchForm()
    if form.validate_on_submit():

        # Build Filters
        data = form.data
        filters = []

        if data['letter_ratio']:
            filters.append(poetry_filters.low_letter_filter(data['letter_ratio']))
        if data['url']:
            filters.append(poetry_filters.url_filter)
        if data['emoji']:
            filters.append(poetry_filters.emoticons)

        source = open(app.config['SOURCE'])

        # Stream
        return Response(line_iter(source, filters), mimetype='text/event-stream')

    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run()
