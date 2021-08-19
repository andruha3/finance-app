from src import app

if __name__ == "__main__":
    with open("src/parse.py", "r") as f:
        exec(f.read())
    app.run(debug=True, host="0.0.0.0")
