from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from micro_learning_app.utils import get_recommendation
from micro_learning_app.models import Module

bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    return render_template('index.html')

@bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', user=current_user)


@bp.route('/quiz', methods=['GET', 'POST'])
@login_required
def quiz():
    if request.method == 'POST':
        topic = request.form['topic']
        prompt = f"Create 5 quiz questions for {topic} for beginners with answers and  provide hints and explanations for answers."
        quiz_questions = get_recommendation(prompt)
        return render_template('quiz.html', questions=quiz_questions)
    return render_template('quiz_form.html')

@bp.route('/learning_nuggets')
@login_required
def learning_nuggets():
    prompt = "Offer users small, bite-sized learning content (e.g., a 3-minute video, infographic, or code snippet) that they can consume in under 5 minutes each day. create micro-content dynamically, such as summarizing the latest tech articles or generating beginner-level code examples in various programming languages"
    learning_nugget = get_recommendation(prompt)
    return render_template('learning_nugget.html', nugget=learning_nugget)

@bp.route('/personalized_learning', methods=['GET', 'POST'])
@login_required
def personalized_learning():
    if request.method == 'POST':
        interests = request.form.getlist('interests')
        if interests:
            interests_str = ', '.join(interests)
            prompt = f"Recommend a learning path for someone interested in {interests_str}."
            learning_path = get_recommendation(prompt)
        else:
            learning_path = "Please select at least one interest."
        return render_template('learning_path.html', path=learning_path)
    return render_template('learning_path_form.html')
