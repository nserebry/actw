from flask import Flask, jsonify, render_template
import os

app = Flask(__name__)

VERSION = os.environ['BUILD_NUMBER']

@app.route("/")
def hello():
    return jsonify(message='Hello Portland!', version=VERSION)

@app.route('/showme/<location>')
def hello_thing(location):
    place = f'This is :  { location.capitalize() }'
    STATIC_MAP_TEMPLATE = f'https://maps.googleapis.com/maps/api/staticmap?zoom=8&size=700x300&markers=${location}'
    return render_template('index.html', name=place, url=STATIC_MAP_TEMPLATE)
#
if __name__ == '__main__':
    # app.run(debug=True, use_reloader=True) # DEBUG MODE
    app.run(host='0.0.0.0')
