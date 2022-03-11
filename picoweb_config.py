import re
import picoweb


app = picoweb.WebApp(__name__)

@app.route('/')
def index(req, resp):
    yield from picoweb.start_response(resp)
    yield from resp.awrite("Hello world from picoweb running on the ESP32")


@app.route("/form_url")
def index(req, resp):
    if req.method == "POST":
        yield from req.read_form_data()
    else:  # GET, apparently
        # Note: parse_qs() is not a coroutine, but a normal function.
        # But you can call it using yield from too.
        req.parse_qs()

    # Whether form data comes from GET or POST request, once parsed,
    # it's available as req.form dictionary

    yield from picoweb.start_response(resp)
    yield from resp.awrite("Hello %s!" % req.form['device_id'])


import ulogging as logging
logging.basicConfig(level=logging.INFO)
