"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return f"""
            <!doctype html>
              <html>
                Hi! This is the home page.
                <div>
                  <a href='/hello'>Go to hello page</a>
                </div>
              </html>
            """


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
          Do you want a compliment or an insult?
          <div>
            <a href='/compliment'>Compliment</a>
            <a href='/insult'>Insult</a>
          </div>
        </form>
        <div>
          <a href='/'>Home</a>
        </div>
      </body>
    </html>
    """


@app.route('/compliment')
def get_compliment():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Compliment Generator</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          <div>
            Which compliment would you like?
            <select name="compliment-choice">
              <option value="great">great
              <option value="cool">cool
              <option value="funny">funny
            </select>
          </div>
          <input type="submit" value="Submit">
        </form>
        <div>
          <a href='/'>Home</a>
        </div>
      </body>
    </html>
    """


@app.route('/greet')
def say_compliment():
    """Get user by name."""

    player = request.args.get("person")
    compliment = request.args.get("compliment-choice")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
        <div>
          <a href='/hello'>Return to hello page</a>
        </div>
        <div>
          <a href='/'>Home</a>
        </div>
      </body>
    </html>
    """.format(player, compliment)


@app.route('/insult')
def get_insult():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/diss">
          What's your name? <input type="text" name="person">
          <div>
            Which insult would you like?
            <select name="insult-choice">
              <option value="poopy">poopy
              <option value="annoying">annoying
              <option value="stupid">stupid
            </select>
          </div>
          <input type="submit" value="Submit">
        </form>
        <div>
          <a href='/'>Home</a>
        </div>
      </body>
    </html>
    """


@app.route('/diss')
def say_insult():
    """Get user by name."""

    player = request.args.get("person")
    insult = request.args.get("insult-choice")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
        <div>
          <a href='/hello'>Return to hello page</a>
        </div>
        <div>
          <a href='/'>Home</a>
        </div>
      </body>
    </html>
    """.format(player, insult)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
