from flask import Flask, render_template, request, redirect, url_for
from salesloft_importer import SalesLoftImporter
import schedule
import time
import threading
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        username = os.getenv("USERNAME")
        password = os.getenv("PASSWORD")
        csv_file_path = request.form["csv_file"]
        schedule_time = request.form["schedule_time"]

        def start_import():
            importer = SalesLoftImporter(username, password, csv_file_path)
            importer.run()

        schedule.every().day.at(schedule_time).do(start_import)

        def run_schedule():
            while True:
                schedule.run_pending()
                time.sleep(60)

        t = threading.Thread(target=run_schedule)
        t.start()

        return redirect(url_for("success"))

    return render_template("index.html")

@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True)
