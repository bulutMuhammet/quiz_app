from flask import Flask, render_template, request, redirect, url_for, make_response
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quizzes.db'
db = SQLAlchemy(app)

class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    questions = db.relationship('Question', backref='quiz', lazy=True)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.String(200), nullable=False)
    option1 = db.Column(db.String(100), nullable=False)
    option2 = db.Column(db.String(100), nullable=False)
    option3 = db.Column(db.String(100), nullable=False)
    option4 = db.Column(db.String(100), nullable=False)
    correct_option = db.Column(db.String(100), nullable=False)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    quizzes = Quiz.query.all()
    return render_template('index.html', quizzes=quizzes)

@app.route('/quiz/<int:quiz_id>', methods=['GET', 'POST'])
def quiz(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)
    best_score = int(request.cookies.get(f"quiz_{quiz_id}", 0))

    if request.method == 'POST':
        score = 0
        for question in quiz.questions:
            user_answer = request.form.get(str(question.id))
            if user_answer == question.correct_option:
                score += 1

        response = make_response(f"Your score is: {score} / {len(quiz.questions)}")

        if score > best_score:
            response.set_cookie(f"quiz_{quiz_id}", str(score))

        return response

    return render_template('quiz.html', quiz=quiz, best_score=best_score)

if __name__ == '__main__':
    app.run(debug=True)
