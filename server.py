from flask import Flask, render_template, request, redirect, url_for
import connection
import data_handler
import utility

app = Flask(__name__)
PATH_QUESTIONS = 'sample_data/question.csv'
PATH_ANSWERS = 'sample_data/answer.csv'


@app.route("/")
@app.route('/list')
def route_list():
    questions = connection.read_data(PATH_QUESTIONS)
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
        new_id = data_handler.get_max_id(is_answer=False)
        new_question["id"] = new_id
        new_question["view_number"] = 0
        new_question["vote_number"] = 0
        new_submission_time = utility.get_submission_time()
        new_question["submission_time"] = new_submission_time
        connection.append_data(PATH_QUESTIONS, new_question, data_handler.QUESTION_KEYS)
        return redirect("/list")
    fieldnames = data_handler.QUESTION_KEYS
    question_details = utility.fill_dict_with_keys(fieldnames)
    return render_template("add_question.html", question_details=question_details)

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
    return render_template('add_question.html', question_details=question_details)


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
        new_id = data_handler.get_max_id(is_answer=True)
        new_answer['id'] = new_id
        new_answer['submission_time'] = utility.get_submission_time()
        new_answer['vote_number'] = 0
        new_answer['question_id'] = question_id
        connection.append_data('sample_data/answer.csv', new_answer, data_handler.ANSWER_KEYS)
        return redirect('/question/' + question_id)
    return render_template('answer.html')


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
        data_handler.count_vote(PATH_ANSWERS, id, vote_type, data_handler.ANSWER_KEYS)
        return redirect('/question/' + id)


if __name__ == "__main__":
    app.run(
        debug=True,
        port=5000
    )
