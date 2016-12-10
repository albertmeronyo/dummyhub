import flask
import json
import os

app = flask.Flask(__name__)

@app.route("/")
def dummyhub():
    return "DummyHub here! Try other routes, like /repos/<user>/<repo> or /repos/<user>/<repo>/contents"

@app.route("/repos/<user>/<repo>")
def dummyapi(user, repo):
    d = {}
    d['name'] = "DUMMY API for user {} and repo {}".format(user, repo)
    d['owner'] = {}
    d['owner']['login'] = "{} (DUMMY)".format(user)
    d['owner']['html_url'] = "http://dummy/url/{}/{}".format(user, repo)

    return flask.jsonify(**d)

@app.route("/repos/<user>/<repo>/contents")
def contents(user, repo):
    d = []
    for f in os.listdir('static/{}/{}/'.format(user, repo)):
        d.append({'name' : f})

    return json.dumps(d)

@app.route("/raw/<user>/<repo>/master/<filename>")
def raw(filename):
    return app.send_static_file('{}/{}/'.format(user, repo) + filename)

if __name__ == "__main__":
    app.run(port=8089, debug=True)
