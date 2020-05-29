from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    html = """
    <html lang="en">
    <head>
      <meta charset="utf-8">

      <title>Junyi Student Retention Predictor</title>
      <meta name="description" content="Student Retention Predictor">
      <meta name="author" content="Brandon Lindsey">

    </head>

    <body>

    <h1>Junyi Student Retetion Predictor</h1>
    <p>This app will give the probability that a student will use the site in the next month!</p>
    <p>Please enter some information about the student below!</p>

    </body>
    </html>
    """
    return html


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
