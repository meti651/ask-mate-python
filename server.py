from flask import Flask, render_template, request, redirect
import os
import connection
import data_handler
import utility
import datetime

app = Flask(__name__)
PATH_QUESTIONS = 'sample_data/question.csv'
PATH_ANSWERS = 'sample_data/answer.csv'

UPLOAD_FOLDER = os.path.basename("Pictures")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
@app.route('/list', methods=('POST', 'GET'))
def route_list():
    questions = connection.read_data('sample_data/question.csv')
    questions =data_handler.sort_questions(questions, "id", "desc")
    if request.method == 'POST':
        attribute = request.form['attribute']
        reverse = request.form['order_direction']
        sorted_questions = data_handler.sort_questions(questions, attribute, reverse)
        return render_template('list.html', questions=sorted_questions, attribute=attribute, reverse=reverse)
    return render_template('list.html', questions=questions, q_keys=data_handler.QUESTION_KEYS)

@app.route('/question/<question_id>')
def display_question(question_id):
    displayed_question = data_handler.get_story_by_id(PATH_QUESTIONS, question_id)
    displayed_answers = data_handler.get_answers_by_question_id(PATH_ANSWERS, question_id)
    return render_template('question.html', question=displayed_question, answers=displayed_answers)

@app.route('/add_question', methods=('GET', 'POST'))
def ask_question():
    if request.method == "POST":
        new_question = {}
        for key in request.form.keys():
            new_question[key] = request.form[key]
        new_question["view_number"] = 0
        new_question["vote_number"] = 0
        new_question["submission_time"] = datetime.datetime.now()
        data_handler.insert_data_to_question(new_question['submission_time'], new_question['view_number'],
                new_question['vote_number'], new_question['title'], new_question['message'], new_question['image'])
        return redirect("/list")
    question_details = ['apa', 'cuka', 'fundaluka']
    return render_template("add_question.html", question_details=question_details, mode="add")

@app.route('/question/<question_id>/edit', methods=('GET','POST'))
def edit_question(question_id):
    if request.method == "POST":
        questions = list(connection.read_data(PATH_QUESTIONS))
        for index in range(len(questions)):
            if questions[index]['id'] == question_id:
                for key in request.form.keys():
                    questions[index][key] = request.form[key]
        connection.write_data(PATH_QUESTIONS, data_handler.QUESTION_KEYS, questions)
        return redirect("/list")
    question_details = data_handler.get_story_by_id(PATH_QUESTIONS, question_id)
    return render_template('add_question.html', question_details=question_details, mode="edit")


@app.route("/question/<question_id>/delete")
def delete_question(question_id):
    questions_fieldnames = data_handler.QUESTION_KEYS
    data_handler.delete_by_id(PATH_QUESTIONS, "id", question_id, questions_fieldnames)
    answers_fieldnames = data_handler.ANSWER_KEYS
    data_handler.delete_by_id(PATH_ANSWERS, "question_id", question_id, answers_fieldnames)
    return redirect("/list")



@app.route('/question/<question_id>/new_answer', methods=['GET', 'POST'])
def add_new_answer(question_id):
    if request.method == 'POST':
        new_answer = {}
        for key in request.form.keys():
            new_answer[key] = request.form[key]
        new_answer['submission_time'] = datetime.datetime.now()
        new_answer['vote_number'] = 0
        new_answer['question_id'] = question_id
        data_handler.insert_data_to_answer(new_answer['submission_time'], new_answer['vote_number'],
                   new_answer['question_id'], new_answer['message'], new_answer['image'])
        return redirect('/question/' + question_id)
    return render_template('answer.html', question_id=question_id)


@app.route('/answer/<answer_id>/delete')
def delete_an_answer(answer_id):
    filename = "sample_data/answer.csv"
    question_id = data_handler.get_question_id_by_answer_id(answer_id)
    data_handler.delete_by_id(filename, "id", answer_id, data_handler.ANSWER_KEYS)
    return redirect('/question/' + question_id)


@app.route('/<story_type>/<id>/<vote_type>')
def vote(story_type, id, vote_type):  # story_type: 'question' or 'answer', vote_type: 'vote-up' or 'vote-down'
    if story_type == "question":
        data_handler.count_vote(PATH_QUESTIONS, id, vote_type, data_handler.QUESTION_KEYS)
        return redirect('/question/' + id)
    if story_type == "answer":
        question_id = data_handler.get_question_id_by_answer_id(id)
        data_handler.count_vote(PATH_ANSWERS, id, vote_type, data_handler.ANSWER_KEYS)
        return redirect('/question/' + question_id)


if __name__ == "__main__":
    app.run(
        debug=True,
        port=8888
    )
