from flask import Flask, jsonify
import csv

app = Flask(__name__)

def read_csv(file_name):
    data = []
    try:
        with open(file_name, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(row)
    except Exception as e:
        print(f"Error reading {file_name}: {e}")
    return data

@app.route("/jobs")
def jobs():
    return jsonify(read_csv("jobs.csv"))

if __name__ == "__main__":
    app.run(debug=True)
