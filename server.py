from flask import Flask, render_template, request, redirect, url_for
import data_handler
import datetime

app = Flask(__name__)


@app.route("/", methods=('GET', 'POST'))
def route_list():
    questions = data_handler.get_last_5_questions('submission_time', 'DESC')
    if request.method == 'POST':
        attribute = request.form['attribute']
        reverse = request.form['order_direction']
        sorted_questions = data_handler.get_last_5_questions(attribute, reverse)
        return render_template('list.html', questions=sorted_questions, attribute=attribute, reverse=reverse, method='last')
    return render_template('list.html', questions=questions, method='last')


@app.route('/list', methods=('POST', 'GET'))
def list_all_question():
    questions = data_handler.get_all_questions('submission_time', 'DESC')
    if request.method == 'POST':
        attribute = request.form['attribute']
        reverse = request.form['order_direction']
        sorted_questions = data_handler.get_all_questions(attribute, reverse)
        return render_template('list.html', questions=sorted_questions, attribute=attribute, reverse=reverse, method='all')
    return render_template('list.html', questions=questions, method='all')


@app.route('/question/<int:question_id>')
def display_question(question_id):
    data_handler.increase_view_number(question_id)
    displayed_question = data_handler.get_question_by_id(question_id)
    displayed_answers = data_handler.get_answers_by_question_id(question_id)
    displayed_tags = data_handler.get_question_tags(question_id)
    return render_template('question.html', question=displayed_question[0], answers=displayed_answers, tags=displayed_tags)


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
        return redirect("/")
    return render_template("add_question.html", mode="add")


@app.route('/question/<int:question_id>/edit', methods=('GET','POST'))
def edit_question(question_id):
    question_params = data_handler.get_question_by_id(question_id)
    if request.method == "POST":
        data_handler.edit_questions(question_id, request.form['title'], request.form['message'], request.form['image'])
        return redirect('/question/' + str(question_params[0]['id']))
    return render_template('add_question.html', question_params=question_params[0], mode="edit")


@app.route("/question/<int:question_id>/delete")
def delete_question(question_id):
    data_handler.delete(question_id, 'question')
    return redirect("/")


@app.route('/question/<int:question_id>/new_answer', methods=['GET', 'POST'])
def add_new_answer(question_id):
    if request.method == 'POST':
        new_answer = {}
        for key in request.form.keys():
            new_answer[key] = request.form[key]
        new_answer['submission_time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_answer['vote_number'] = 0
        new_answer['question_id'] = question_id
        data_handler.insert_data_to_answer(new_answer)
        return redirect('/question/' + str(question_id))
    return render_template('answer.html', question_id=question_id)


@app.route('/answer/<int:answer_id>/edit', methods=['GET', 'POST'])
def edit_answer(answer_id):
    answer_params = data_handler.get_answer_by_id(answer_id)
    if request.method == "POST":
        data_handler.edit_answer(answer_id, request.form['message'], request.form['image'])
        return redirect('/question/' + str(answer_params[0]['question_id']))
    return render_template('answer.html', question_params=answer_params[0], mode='edit')


@app.route('/answer/<int:answer_id>/delete')
def delete_an_answer(answer_id):
    query_string = request.referrer
    data_handler.delete(answer_id, 'answer')
    return redirect(query_string)


@app.route('/question/<question_id>/new-tag', methods=['GET', 'POST'])
def add_new_tag(question_id):
    if request.method == 'POST':
        new_tag = request.form['create_tag']
        selected_tag = request.form['selected_tag']
        print(new_tag, selected_tag)
        if new_tag:
            data_handler.add_question_tag(new_tag)
            curr_link = request.referrer
            return redirect(curr_link)
        else:
            tag_id = data_handler.get_tag_id(selected_tag)['id']
            data_handler.add_tag_to_question(tag_id, question_id)
            return redirect(url_for('display_question', question_id=question_id))
    question_tag = data_handler.get_all_tag()
    return render_template('new_tag.html', tags=question_tag)



@app.route('/<story_type>/<int:id>/<vote_type>')
def vote(story_type, id, vote_type):  # story_type: 'question' or 'answer', vote_type: 'vote-up' or 'vote-down'
    query_string = request.referrer
    data_handler.count_vote(story_type, id, vote_type)
    return redirect(query_string)


@app.route('/question/<int:question_id>/tag/<int:tag_id>')
def delete_tag(question_id, tag_id):
    data_handler.delete_tag(question_id, tag_id)
    return_route = request.referrer
    return redirect(return_route)


if __name__ == "__main__":
    app.run(
        debug=True,
        port=9992
    )
