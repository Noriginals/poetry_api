from poetryutils2 import filters as poetry_filters, line_iter, Coupler
from app import app
import time

def generate_freeverse():
    source = open(app.config['SOURCE'])

    # Build Filters
    filters = []
    filters.append(poetry_filters.low_letter_filter(.9))
    filters.append(poetry_filters.url_filter)
    filters.append(poetry_filters.emoticons)

    def freeverse():
        for rec in line_iter(source, filters):
            print rec
            yield "<div>{0}</div>".format(rec)
            time.sleep(1)
    return freeverse

def generate_couplets():
    source = open(app.config['SOURCE'])

    def couplets():
        coupler = Coupler()
        for line in source:
            print line
            result = coupler.add_line(line)
            if result:
                yield "<div>{0}</div>".format(result)
    return couplets
