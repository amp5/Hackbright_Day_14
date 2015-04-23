from random import choice

from flask import Flask, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

# route to handle the landing page of a website.
@app.route('/')
def start_here():
    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title> Start Page </title>
        </head>
        <body>
            <a href="http://localhost:5000/hello">Hi! This is the home page.</a>
        </body>
    </html>
        """

# route to display a simple web page
@app.route('/hello')
def say_hello():
    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Hi There!</title>
        </head>
        <body>
            <h1>Hi There!</h1>
            <form action="/greet">
                <label>What's your name? <input type="text" name="person"></label>
                <br>
                <br>
                <label>Select a compliment</label>
                    <select name="compliment"> 
                        <option value="awesome">Awesome!</option>
                        <option value="sweet">Sweet!</option>
                        <option value="rad">Rad!</option>
                        <option value="gnarly">Gnarly!</option>
                        <option value="tubular">Tubular!</option>
                    </select>
                <br>
                <br>
                <label>Pick a House!</label>
                    <input type="radio" name="house" value="Gryffendor">Gryffendor
                    <input type="radio" name="house" value="Slytherin">Slytherin
                    <input type="radio" name="house" value="Hufflepuff">Hufflepuff
                    <input type="radio" name="house" value="Ravenclaw">Ravenclaw
                <br>
                <br>
                <input type="submit">
            </form>
        </body>
    </html>

    """

@app.route('/greet')
def greet_person():
    player = request.args.get("person")
    compliment = request.args.get("compliment")
    house = request.args.get("house")

    # AWESOMENESS = [
    #     'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    #     'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

    # compliment = choice(AWESOMENESS)

    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>A Compliment</title>
        </head>
        <body>
            Hi %s I think you're %s!  You are now in %s.
        </body>
    </html>""" % (player, compliment, house)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
