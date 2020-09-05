#Import Flask modules

from flask import Flask,redirect,url_for,render_template

#Create an object named app 
app = Flask(__name__)

# Create a function named home which returns a string 'This is home page for no path, <h1> Welcome Home</h1>' 
# and assign route of no path ('/')

@app.route("/")
def home():
    return "This is home page for no path, <h1> Welcome Home</h1> \
        <a href = '/about'> About Page </a><br>\
        <a href = '/error'> Error Page </a><br>\
        <a href = '/hello'> Hello Page </a><br>\
        <a href = '/admin'> Admin Page(redirect error page) </a>    "
        
# Create a function named about which returns a formatted string '<h1>This is my about page </h1>' 
# and assign to the static route of ('about')

@app.route("/about")
def about():
    return "<h1> This is my about page <h1>\
        <a href = '/'> Back </a>"
# Create a function named error which returns a formatted string '<h1>Either you encountered an error or you are not authorized.</h1>' 
# and assign to the static route of ('error')

@app.route("/error")
def error():
    return "<h1> Either you  encountered an error or you are not authorized. </h1>\
        <a href = '/'> Back </a>"
# Create a function named hello which returns a string of '<h1>Hello, World! </h1>' 
# and assign to the static route of ('/hello')
@app.route("/hello")
def hello():
    return """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dynamic Page</title>
</head>
<body>
    <h1>welcome {{value}}</h1>
</body>
</html>
"""

# Create a function named admin which redirect the request to the error path 
# and assign to the route of ('/admin')        
@app.route("/admin")
def admin():
    return redirect(url_for("error"))

# Create a function named greet which return formatted inline html string 
# and assign to the dynamic route of ('/<name>')

@app.route("/<name>")
def greet(name):
    deneme = name
    return render_template("deneme.html",isim = deneme)

# Create a function named greet_admin which redirect the request to the hello path with param of 'Master Admin!!!!' 
# and assign to the route of ('/greet-admin')
@app.route("/greet-admin")
def greet_admin():
    value2 = "deneme"
    return redirect(url_for("hello",value = value2))


if __name__ == "__main__":

    app.run(debug = True)