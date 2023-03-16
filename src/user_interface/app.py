from flask import Flask, render_template, request, jsonify
from chatbot import Chatbot
from scraper import Scraper

app = Flask(__name__)
chatbot = Chatbot()
scraper = Scraper()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    user_input = request.form["user_input"]
    response = chatbot.generate_response(user_input)
    return jsonify({"response": response})


@app.route("/scrape", methods=["POST"])
def scrape():
    search_query = request.form["search_query"]
    source = request.form["source"]

    if source == "imdb":
        data = scraper.fetch_imdb_data(search_query)
    elif source == "rotten_tomatoes":
        data = scraper.fetch_rotten_tomatoes_data(search_query)
    elif source == "goodreads":
        data = scraper.fetch_goodreads_data(search_query)
    elif source == "wrapped_ordinals":
        data = scraper.fetch_wrapped_ordinals_data(search_query)
    elif source == "taproot_wizards":
        data = scraper.fetch_taproot_wizards_data(search_query)
    elif source == "magic_jpegs":
        data = scraper.fetch_magic_jpegs_data(search_query)
    else:
        return jsonify({"error": "Invalid source"})

    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
