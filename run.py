from bottle import route, run

@route('/')
def hello():
    return "weee"

run(host='0.0.0.0', port=5000, debug=True)
