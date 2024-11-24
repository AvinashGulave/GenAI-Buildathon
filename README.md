# Micro-Learning Upskilling App

## Introduction
The Micro-Learning Upskilling App is designed to help users upskill with short, digestible learning modules on the latest tech topics. It features daily tech quizzes, daily learning nuggets, and personalized learning paths.

## Features
- **Tech Quiz & Challenges**: Daily short quizzes on programming languages, tools, or frameworks.
- **Daily Learning Nuggets**: Small, bite-sized learning content that users can consume in under 5 minutes each day.
- **Personalized Learning Path**: Suggestions of learning modules based on the user's interests or career goals

## Setup Instructions

### Prerequisites
- Python 3.10
- Flask
- Flask-SQLAlchemy
- Flask-Login
- OpenAI API Key
- dotenv

### Installation
1. **Create Folder**:
    ``
    cd micro_learning_app
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Create a `.env` file in the root directory and add your OpenAI API key**:
    ```plaintext
    OPENAI_API_KEY=your_openai_api_key
    ```

## Running the Application
1. **Start the Flask application**:
    ```bash
    python run.py
    ```

2. **Access the application in your browser**:
    ```plaintext
    http://127.0.0.1:5000/
    ```

## Usage
### Registering a New User
1. Navigate to the registration page.
2. Fill in the username and password fields.
3. Click the "Register" button.
4. You will be redirected to the login page with a success message.

### Logging In
1. Navigate to the login page.
2. Enter your registered username and password.
3. Click the "Login" button.
4. You will be redirected to the dashboard if the credentials are correct, or you will see an error message if they are incorrect.

### Personalized Learning Path
1. From the dashboard, navigate to the "Personalized Learning Path" section.
2. Select your interests from the checkboxes.
3. Click the "Get Learning Path" button.
4. View your personalized learning path recommendations.

### Daily Tech Quiz
1. From the dashboard, navigate to the "Tech Quiz & Challenges" section.
2. Enter a topic for your quiz.
3. Click the "Generate Quiz" button.
4. View and answer the quiz questions.

### Daily Learning Nuggets
1. From the dashboard, navigate to the "Daily Learning Nuggets" section.
2. View the generated learning nugget content.


## Acknowledgments
- Flask: [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)
- OpenAI: [https://www.openai.com/](https://www.openai.com/)
