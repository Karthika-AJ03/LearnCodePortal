from flask import Flask, render_template, request

app = Flask(__name__)

# Quiz data
quizzes = {
    "Python Basics": [
        {"question": "Which of the following is a valid Python data type?", "options": ["int", "num", "digit"], "answer": "int"},
        {"question": "What symbol is used to start a comment in Python?", "options": ["//", "#", "/*"], "answer": "#"}
    ],
    "HTML Fundamentals": [
        {"question": "What does HTML stand for?", "options": ["HyperText Markup Language", "HighText Machine Language", "HyperTool Multi Language"], "answer": "HyperText Markup Language"},
        {"question": "Which tag is used for inserting an image?", "options": ["<img>", "<image>", "<pic>"], "answer": "<img>"}
    ],
    "CSS Essentials": [
        {"question": "Which property changes the text color?", "options": ["font-color", "color", "text-style"], "answer": "color"},
        {"question": "Which symbol is used to select an id in CSS?", "options": [".", "#", "*"], "answer": "#"}
    ]
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/topic', methods=['POST'])
def topic():
    topic_name = request.form['topic']
    return render_template('topic.html', topic_name=topic_name)

@app.route('/quiz', methods=['POST'])
def quiz():
    topic_name = request.form['topic']
    quiz_data = quizzes.get(topic_name, [])
    return render_template('quiz.html', topic_name=topic_name, quiz=quiz_data)

@app.route('/result', methods=['POST'])
def result():
    topic_name = request.form['topic']
    quiz_data = quizzes.get(topic_name, [])
    score = 0

    for i, q in enumerate(quiz_data):
        user_answer = request.form.get(f"q{i+1}")
        if user_answer == q['answer']:
            score += 1

    return f"<h1>Result for {topic_name}</h1><p>Your Score: {score}/{len(quiz_data)}</p><a href='/'>Back to Home</a>"

if __name__ == '__main__':
    app.run(debug=True)