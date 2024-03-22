
# Modules
from flask import Flask, render_template, request, jsonify
import json

# Initialize Flask App
app = Flask(__name__)

# HTML Routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/practice_tests')
def practice_tests():
    return render_template('practice_tests.html')

@app.route('/vocabulary_trainer')
def vocabulary_trainer():
    return render_template('vocabulary_trainer.html')

@app.route('/grammar_exercises')
def grammar_exercises():
    return render_template('grammar_exercises.html')

@app.route('/progress_tracker')
def progress_tracker():
    return render_template('progress_tracker.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')


# API Routes
@app.route('/api/practice_tests')
def get_tests():
    tests = [{"name": "Test 1", "questions": 10}, {"name": "Test 2", "questions": 20}]
    return jsonify(tests)

@app.route('/api/vocabulary')
def get_vocabulary():
    vocabulary = [{"word": "apple", "definition": "a red fruit"}, {"word": "banana", "definition": "a yellow fruit"}]
    return jsonify(vocabulary)

@app.route('/api/grammar')
def get_grammar():
    exercises = [{"question": "Which is correct?", "options": ["I am", "I'm"]}]
    return jsonify(exercises)

@app.route('/api/progress')
def get_progress():
    progress = {"practice_tests": 3, "vocabulary_learned": 100, "grammar_exercises": 50}
    return jsonify(progress)

# Main Function
if __name__ == "__main__":
    app.run(debug=True)
