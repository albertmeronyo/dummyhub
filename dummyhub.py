import flask
app = flask.Flask(__name__)

@app.route("/")
def dummyhub():
    return "DummyHub here! Try other routes, like /albertmeronyo/lodapi or /contents"

@app.route("/repos/albertmeronyo/lodapi")
def dummyapi():
    d = {}
    d['name'] = "DUMMY API"
    d['owner'] = {}
    d['owner']['login'] = "albertmeronyo (DUMMY)"
    d['owner']['html_url'] = "http://dummy/url"

    return flask.jsonify(**d)

if __name__ == "__main__":
    app.run(port=8089, debug=True)
