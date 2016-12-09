import flask
app = flask.Flask(__name__)

@app.route("/")
def dummyhub():
    return "DummyHub here! Try other routes, like /repos/albertmeronyo/lodapi or /repos/albertmeronyo/lodapi/contents"

@app.route("/repos/albertmeronyo/lodapi")
def dummyapi():
    d = {}
    d['name'] = "DUMMY API"
    d['owner'] = {}
    d['owner']['login'] = "albertmeronyo (DUMMY)"
    d['owner']['html_url'] = "http://dummy/url"

    return flask.jsonify(**d)

@app.route("/repos/albertmeronyo/lodapi/contents")
def contents():
    d = []
    d.append({'name' : "q1.rq"})

    return flask.jsonify(d) 

if __name__ == "__main__":
    app.run(port=8089, debug=True)
