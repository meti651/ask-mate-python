from flask import Flask, render_template, request, redirect, url_for
import os
import data_handler
import datetime

app = Flask(__name__)


@app.route("/", methods=('GET', 'POST'))
@app.route('/list', methods=('POST', 'GET'))
def route_list():
    questions = data_handler.get_last_5_questions('submission_time', 'DESC')
    if request.method == 'POST':
        attribute = request.form['attribute']
        reverse = request.form['order_direction']
        sorted_questions = data_handler.get_last_5_questions(attribute, reverse)
        return render_template('list.html', questions=sorted_questions, attribute=attribute, reverse=reverse)
    return render_template('list.html', questions=questions)

@app.route('/question/<question_id>')
def display_question(question_id):
    x = 2
    displayed_question = data_handler.get_question_by_id(question_id)
    displayed_answers = data_handler.get_answers_by_question_id(question_id)
    displayed_tags = data_handler.get_question_tags(question_id)
    return render_template('question.html', question=displayed_question[0], answers=displayed_answers, tags=displayed_tags[0])


@app.route('/add_question', methods=('GET', 'POST'))
def ask_question():
    if request.method == "POST":
        new_question = {}
        for key in request.form.keys():
            new_question[key] = request.form[key]
        new_question["view_number"] = 0
        new_question["vote_number"] = 0
        new_question["submission_time"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data_handler.insert_data_to_question(new_question)
        return redirect("/list")
    return render_template("add_question.html", mode="add")


@app.route('/question/<question_id>/edit', methods=('GET','POST'))
def edit_question(question_id):
    if request.method == "POST":
        data_handler.edit_questions(question_id, request.form['title'], request.form['message'], request.form['image'])
        return redirect(url_for("route_list"))

    question_params = data_handler.get_question_by_id(question_id)
    return render_template('add_question.html', question_params=question_params[0], mode="edit")


@app.route("/question/<question_id>/delete")
def delete_question(question_id):
    data_handler.delete(question_id, 'question')
    return redirect("/list")



@app.route('/question/<question_id>/new_answer', methods=['GET', 'POST'])
def add_new_answer(question_id):
    if request.method == 'POST':
        new_answer = {}
        for key in request.form.keys():
            new_answer[key] = request.form[key]
        new_answer['submission_time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_answer['vote_number'] = 0
        new_answer['question_id'] = question_id
        data_handler.insert_data_to_answer(new_answer)
        return redirect('/question/' + question_id)
    return render_template('answer.html', question_id=question_id)


@app.route('/answer/<answer_id>/delete')
def delete_an_answer(answer_id):
    query_string = request.referrer
    data_handler.delete(answer_id, 'answer')
    return redirect(query_string)


@app.route('/question/<question_id>/new-tag', methods=['GET', 'POST'])
def add_new_tag(question_id):
    if request.method == 'POST':
        print(request.form)
        new_tag = request.form['create_tag']
        selected_tag = request.form['selected_tag']
        if new_tag:
            data_handler.add_question_tag(new_tag)
            curr_link = request.referrer
            return redirect(curr_link)
        else:
            tag_id = data_handler.get_tag_id(selected_tag)['id']
            print(tag_id, question_id)
            data_handler.add_tag_to_question(question_id, tag_id)
            return redirect('/question/<question_id>')
    question_tag = data_handler.get_all_tag()
    return render_template('new_tag.html', tags=question_tag)



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
        port=9992
    )
