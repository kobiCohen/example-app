from flask import Flask
app = Flask(__name__)
@app.route("/")
def first_route():
    return "Shalom!"

    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("8090"), debug=True)