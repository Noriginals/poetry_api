from poetryutils2 import filters as poetry_filters, line_iter
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
            time.sleep(0.3)
    return freeverse

def generate_couplets():
    source = open(app.config['SOURCE'])

    def couplets():
        #coupler = Coupler()
        couler = None
        for line in source:
            print line
            result = coupler.add_line(line)
            if result:
                yield "<div>{0}</div>".format(result)
    return couplets

def generate_haiku():
    source = app.config['HAIKU_SOURCE']

    def haiku():
        with open(source) as f:
            haiku = list()
            count = 0
            for line in f:
                if len(line.rstrip()):
                    haiku.append(line)
                if len(haiku) == 3:
                    yield """
                    <div class="panel panel-default" style="display:inline-block;">
                        <div class="panel-heading">
                            <h3 class="panel-title">Haiku {0}</h3>
                        </div>
                        <div class="panel-body">
                            <div>{1}</div>
                            <div>{2}</div>
                            <div>{3}</div>
                        </div>
                    </div>
                    """.format(count, haiku[0], haiku[1], haiku[2])
                    count += 1
                    haiku = list()
                    time.sleep(1)
    return haiku

def generate_limerick():
    source = app.config['LIMERICK_SOURCE']

    def limerick():
        with open(source) as f:
            limerick = list()
            count = 0
            for line in f:
                if len(line.rstrip()):
                    limerick.append(line)
                if len(limerick) == 5:
                    yield """
                    <div class="panel panel-default" style="display:inline-block;">
                        <div class="panel-heading">
                            <h3 class="panel-title">Limerick {0}</h3>
                        </div>
                        <div class="panel-body">
                            <div>{1}</div>
                            <div>{2}</div>
                            <div>{3}</div>
                            <div>{4}</div>
                            <div>{5}</div>
                        </div>
                    </div>
                    """.format(count, limerick[0], limerick[1], limerick[2], limerick[3], limerick[4])
                    count += 1
                    limerick = list()
                    time.sleep(1)
    return limerick
