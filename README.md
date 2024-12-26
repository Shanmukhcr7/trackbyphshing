# trackbyphshing
This project is a location-based video streaming application designed using Flask for the backend and a simple, responsive HTML/CSS/JavaScript frontend. The application serves a live video stream while ensuring that the user's geographic location is captured and logged securely. 
# How It Works
A user visits the application page served by the Flask backend.
The user clicks the "click here to watch" button, prompting the browser to request location access.
Upon granting permission, the browser sends the user's location (latitude and longitude) to the Flask server.
The backend logs the Google Maps link for the user's location in the terminal and returns a response confirming success.
The video player is dynamically displayed, and the user can watch the video you dispalyed.

