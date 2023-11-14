from flask import Flask, request, render_template

from stories import story

app = Flask(__name__)


@app.route("/")
def home_page():
    """Generate and show form to ask words."""
    prompts = story.prompts
    return render_template("homepage.html", prompts=prompts)


@app.route("/story")
def show_story():
    """Show story result."""
    text = story.generate(request.args)
    return render_template("story.html", text=text)
