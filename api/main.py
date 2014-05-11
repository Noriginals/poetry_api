
from __future__ import division
import time

from flask import Flask, Response, render_template

from app import app, csrf
from forms import PoetrySearchForm
from generators import generate_freeverse, generate_couplets

def stream_template(template_name, **context):
    app.update_template_context(context)
    t = app.jinja_env.get_template(template_name)
    rv = t.stream(context)
    rv.enable_buffering(5)
    return rv


@app.route('/', methods=('GET', 'POST'))
def index():
    form = PoetrySearchForm()
    if form.validate_on_submit():

        # Build Filters
        data = form.data
        styles = data.get('styles', None)
        generator = None

        if styles == 'couplets':
            generator = generate_couplets()
        elif styles == 'free-verse':
            generator = generate_freeverse()

        # Stream
        return Response(generator(), mimetype='text/event-stream')

    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run()
