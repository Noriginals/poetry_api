from flask import Flask, Response

app = Flask(__name__)

def limerick():
    limericks = list()
    with open('api/limerick.txt') as f:
        for line in f:
            if len(line.strip()):
                limericks.append(line)

    return limericks

@app.route('/stream')
def stream_feed():
    def generate():
        for line in limerick():
            yield line
    return Response(generate(), mimetype='text/plain')

if __name__ == '__main__':
    print 'Good afternoon'
    app.run()
