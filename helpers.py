class Exercises:
    id: int
    exercise: str
    weight: str
    sets: str
    reps: str
    date: str
    color: str

    def __init__(self, id: int, exercise: str, weight: str, sets: str, reps: str, date: str, color: str):
        self.id = id
        self.exercise = exercise
        self.weight = weight
        self.sets = sets
        self.reps = reps
        self.date = date
        self.color = color