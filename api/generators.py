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
        poem = list()
        count = 0
        for rec in line_iter(source, filters):
            poem.append(rec)
            if len(poem) == 5:
                yield """
                    <div class="panel panel-default" style="display:inline-block;">
                        <div class="panel-heading">
                            <h3 class="panel-title">Free verse {0}</h3>
                        </div>
                        <div class="panel-body">
                            <div>{1}</div>
                            <div>{2}</div>
                            <div>{3}</div>
                            <div>{4}</div>
                            <div>{5}</div>
                        </div>
                    </div>""".format(count, poem[0], poem[1], poem[2], poem[3], poem[4])

                count += 1
                poem = list()
                time.sleep(0.3)

    return freeverse

def generate_couplets():
    source = app.config['COUPLETS_SOURCE']

    def couplets():
        with open(source) as f:
            line_one = None
            count = 0
            for line in f:
                if len(line.rstrip()):
                    if line_one:
                        yield """
                        <div class="panel panel-default" style="display:inline-block;">
                            <div class="panel-heading">
                                <h3 class="panel-title">Couplet #{0}</h3>
                            </div>
                            <div class="panel-body">
                                <div>{1}</div>
                                <div>{2}</div>
                            </div>
                        </div>""".format(count, line_one, line)

                        count += 1
                        line_one = None
                        time.sleep(1)

                    else:
                        line_one = line
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
                            <h3 class="panel-title">Haiku #{0}</h3>
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
