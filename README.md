---

# Quora Clone - Django Web Application

A simple Quora-inspired web application built with Django. This project allows users to register, log in, post questions, view questions, answer questions, like answers, and log out. It demonstrates core Django features like user authentication, models, forms, views, and templates.

---

## Features

### Core Functionality
1. **User Authentication**
   - **Register**: Create a new account with a username, email, and password.
   - **Login**: Log in with existing credentials.
   - **Logout**: End the user session and return to the homepage.
2. **Post Questions**
   - Authenticated users can post questions with a title and description.
3. **View Questions**
   - All posted questions are displayed on the homepage, ordered by most recent.
4. **Answer Questions**
   - Authenticated users can submit answers to specific questions.
5. **Like Answers**
   - Authenticated users can like or unlike answers, with the like count displayed.
6. **Logout**
   - Users can log out, ending their session.

### Technical Details
- **Framework**: Django 4.x (ensure compatibility with your installed version).
- **Database**: SQLite (default Django database; can be swapped for PostgreSQL, MySQL, etc.).
- **Models**: 
  - `Question`: Stores question title, description, creator, and timestamp.
  - `Answer`: Stores answer text, linked question, creator, timestamp, and likes.
- **Forms**: Custom forms for registration, question posting, and answering.
- **Templates**: Basic HTML templates with minimal styling.
- **Authentication**: Leverages Django’s built-in `User` model and authentication system.

---

## Project Structure

```
quora_clone/
├── core/
│   ├── migrations/
│   ├── templates/
│   │   ├── registration/
│   │   │   └── login.html
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── post_question.html
│   │   ├── question_detail.html
│   │   └── register.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── quora_clone/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── README.md
```

---

## Prerequisites

- **Python**: 3.8 or higher
- **Django**: Install via `pip install django`
- **Virtual Environment** (recommended): Use `venv` or `virtualenv`

---

## Setup Instructions

1. **Clone or Download the Project**
   - If using Git: `git clone <repository-url>`
   - Otherwise, download and extract the project folder.

2. **Set Up a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   - Ensure you're in the `quora_clone/` directory, then run:
     ```bash
     pip install django
     ```

4. **Apply Migrations**
   - Create the database tables:
     ```bash
     python manage.py makemigrations
     python manage.py migrate
     ```

5. **Run the Development Server**
   - Start the server:
     ```bash
     python manage.py runserver
     ```
   - Open your browser and navigate to `http://127.0.0.1:8000/`.

---

## How to Use

### 1. Register an Account
- Go to `/register/`.
- Fill in the username, email, and password fields.
- Submit to create an account and be automatically logged in.

### 2. Log In
- Go to `/accounts/login/`.
- Enter your username and password.
- Submit to log in and be redirected to the homepage.

### 3. Post a Question
- While logged in, click "Post a Question" on the homepage (`/post_question/`).
- Enter a title and description, then submit.
- You’ll be redirected to the question’s detail page.

### 4. View Questions
- Visit the homepage (`/`) to see all questions, listed by most recent.
- Click a question title to view its details and answers.

### 5. Answer a Question
- On a question’s detail page (`/question/<id>/`), scroll to the "Post an Answer" section.
- Enter your answer and submit (requires login).

### 6. Like an Answer
- On a question’s detail page, find an answer and click "Like" (or "Unlike" if already liked).
- The like count updates immediately (requires login).

### 7. Log Out
- Click "Logout" in the header (`/accounts/logout/`) to end your session and return to the homepage.

---

## Key Functions and Files

### Models (`core/models.py`)
- **`Question`**: Represents a question with `title`, `description`, `created_by` (User), and `timestamp`.
- **`Answer`**: Represents an answer with `question` (ForeignKey), `text`, `created_by` (User), `timestamp`, and `likes` (ManyToMany with User).

### Forms (`core/forms.py`)
- **`RegisterForm`**: Extends `UserCreationForm` for user registration.
- **`QuestionForm`**: For creating new questions.
- **`AnswerForm`**: For submitting answers.

### Views (`core/views.py`)
- **`register`**: Handles user registration and auto-login.
- **`home`**: Displays all questions.
- **`post_question`**: Creates new questions (login required).
- **`question_detail`**: Shows a question and its answers; handles answer submissions.
- **`like_answer`**: Toggles likes on answers (login required).

### URLs (`core/urls.py` and `quora_clone/urls.py`)
- Maps routes like `/`, `/register/`, `/question/<id>/`, and `/like_answer/<id>/`.
- Includes Django’s auth URLs (`/accounts/login/`, `/accounts/logout/`).

### Templates (`core/templates/`)
- **`base.html`**: Base template with header and navigation.
- **`register.html`**: Registration form.
- **`login.html`**: Login form.
- **`home.html`**: List of questions.
- **`post_question.html`**: Question posting form.
- **`question_detail.html`**: Question details, answers, and answer form.

---

## Limitations and Improvements
- **Styling**: The app uses minimal HTML without CSS. Add Bootstrap or custom CSS for a better UI.
- **Error Handling**: Basic views lack robust error handling (e.g., 404 for invalid question IDs).
- **Sorting**: Questions are sorted by timestamp; popularity-based sorting (e.g., by answer likes) could be added.
- **AJAX**: Likes require a page reload; AJAX could make this seamless.
- **Security**: Add CSRF protection (already included by Django) and validate inputs further.

---

## Troubleshooting

- **Server Won’t Start**: Ensure you’re in the `quora_clone/` directory and the virtual environment is active.
- **Database Issues**: Run `python manage.py migrate` if tables aren’t created.
- **404 Errors**: Check URLs in `core/urls.py` and `quora_clone/urls.py`.

---

## Contributing

Feel free to fork this project, submit pull requests, or suggest improvements via issues. Focus areas for enhancement include UI/UX, additional features (e.g., comments, tags), or performance optimization.

---

## License

This project is open-source and available under the MIT License.

---
