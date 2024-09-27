from flask import Flask, render_template, send_from_directory, request, jsonify

app = Flask(__name__)

# Initialize counters
visit_count = 0
button_click_count = 0
image_visit_count = 0  # Add counter for image endpoint visits

@app.route('/')
def index():
    global visit_count
    visit_count += 1  # Increment the visit count for the main page
    return render_template('index.html',visits=visit_count, clicks=button_click_count, image_visits=image_visit_count)

# Route to serve the image and count the number of visits to the image endpoint
@app.route('/image')
def serve_image():
    global image_visit_count
    image_visit_count += 1  # Increment image visit count
    return send_from_directory('src', 'picture.jpg')

# Route to handle button clicks and update the button click count
@app.route('/button-click', methods=['POST'])
def button_click():
    global button_click_count
    button_click_count += 1  # Increment the button click count
    # Return current click count as JSON (useful for front-end)
    return jsonify(click_count=button_click_count)

# Route to expose metrics, including image visit count
@app.route('/metrics')
def metrics():
    return f"Website Visits: {visit_count}, Button Clicks: {button_click_count}, Image Visits: {image_visit_count}"

if __name__ == "__main__":
    app.run(debug=True)