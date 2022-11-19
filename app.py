from flask import Flask, render_template, request

from helpers import Exercises

app: Flask = Flask(__name__)
exercise_list: list[Exercises] = []
exercise_count: int = 0

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/create-exercise', methods=["GET", "POST"])
def create_exercise():
    if request.method == "POST":
        global exercise_list
        global exercise_count

        exercise: str = request.form['exercise']
        weight: str = request.form['weight']
        sets: str = request.form['sets']
        reps: str = request.form['reps']
        date: str = request.form['date']
        color: str = request.form['color']

        if exercise == '':
            return render_template("create-exercise.html")

        new_exercise: Exercises = Exercises(exercise_count, exercise, weight, sets, reps, date, color)
        exercise_list.append(new_exercise)

        exercise_count += 1

        return render_template("success.html", exercise = exercise, weight = weight, sets = sets, reps = reps, date = date)
    return render_template("create-exercise.html")

@app.route('/view-list')
def view_exercise_list():
    return render_template('view-list.html', exercise_list = exercise_list)


if __name__ == '__main__':
    app.run(debug=True)