# Import Flask and render_template (used to return HTML pages)
from flask import Flask, render_template

# Create the Flask app
app = Flask(_name_)

# ------------------------------
# HOME PAGE ROUTE
# ------------------------------
@app.route("/")                # When user opens the main URL ("/"), this function runs
def home():
    # Return HTML code directly (simple method)
    return """
    <html>
    <head>
        <title>Simple Homepage</title>   <!-- Title shown on the browser tab -->
        <style>
            body {
                font-family: Arial;       /* Sets font style */
                background: #f2f2f2;      /* Light gray background */
                text-align: center;       /* Center-aligns all text */
                padding: 50px;            /* Adds space around the content */
            }
            .card {
                background: white;         /* White card background */
                padding: 20px;             /* Space inside the card */
                width: 400px;              /* Card width */
                margin: auto;              /* Center the card */
                border-radius: 10px;       /* Rounded corners */
                box-shadow: 0 0 10px rgba(0,0,0,0.1); /* Soft shadow */
            }
            a {
                display: inline-block;     /* Makes the link look like a button */
                margin-top: 20px;          /* Space above the button */
                padding: 10px 15px;        /* Button size */
                background: #007bff;       /* Blue background */
                color: white;              /* White text */
                text-decoration: none;     /* Removes underline */
                border-radius: 5px;        /* Rounded button corners */
            }
            a:hover {
                background: #0056b3;       /* Darker blue when hovered */
            }
        </style>
    </head>
    <body>
        <div class='card'>                 <!-- Card container -->
            <h1>Welcome to My Homepage</h1>  <!-- Main title -->
            <p>This is a simple homepage built using Python and Flask.</p>
            <a href="/about">Go to About Page</a> <!-- Button linking to About page -->
        </div>
    </body>
    </html>
    """

# ------------------------------
# ABOUT PAGE ROUTE
# ------------------------------
@app.route("/about")       # This function runs when user goes to /about
def about():
    return """
    <html>
    <head>
        <title>About Page</title>    <!-- Browser tab title -->
        <style>
            body {
                font-family: Arial;   /* Same font as homepage */
                background: #fcfcfc;  /* Very light background */
                text-align: center;   /* Centers the text */
                padding: 50px;        /* Space around everything */
            }
        </style>
    </head>
    <body>
        <h1>About This System</h1>   <!-- About page title -->
        <p>This is a simple multi-page website built with Flask.</p>
        <a href="/">Back to Home</a> <!-- Button to go back to homepage -->
    </body>
    </html>
    """

# ------------------------------
# RUN THE APP
# ------------------------------
if _name_ == "_main_":   # Runs only if this file is executed directly
    app.run(debug=True)      # Starts the Flask server with debug mode on