from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/quiz")
def quiz():
    return render_template("quiz.html")

@app.route("/result", methods=["POST"])
def result():
    income = request.form.get("income")
    pressure = request.form.get("pressure")
    status = request.form.get("status")

    # Decision logic
    if income == "urgent" or pressure == "high":
        stage = "SURVIVAL MODE"
        message = "Your priority is income and stability."
    elif status == "exam":
        stage = "PREPARATION MODE"
        message = "You should focus on structured preparation."
    else:
        stage = "EXPLORATION MODE"
        message = "This is the right time to explore career paths."

    return render_template(
        "result.html",
        stage=stage,
        message=message
    )

@app.route("/plan")
def plan():
    return render_template("plan.html")


if __name__ == "__main__":
    app.run(debug=True)
