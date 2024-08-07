from flask import Flask, render_template, request
from . import extras

def create_app():
    app = Flask(__name__)
    
    @app.route("/")
    def index():
        return render_template('index.html')

    @app.route("/find_restaurants")
    def find():
        lat, lon = request.args.get('lat'), request.args.get('lon')
        
        if not lat or not lon: 
            return "Location error", 400
        
        name, message = extras.find_restaurants(lat, lon)
        return render_template('result.html', name=name, message=message)
    
    return app