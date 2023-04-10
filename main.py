# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai
import os
from dotenv import load_dotenv

import json

load_dotenv()

openai.api_key = os.environ["OPENAI_API_KEY"]
DB_NAME = os.environ.get("DB_NAME", "db.db")


def get_breakdown(concept):
    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "system", "content": "you are an education assistant who breaks down large concepts into smaller ones. the smaller concepts that you generate need to be the ones i need to learn to understand the large concept. Your responses should only be in the format specified in the example."},
                {"role": "user", "content": "Front-end development"},
                {"role": "assistant", "content": "HTML***HTML (HyperText Markup Language) is the code that is used to structure a web page and its content. For example, content could be structured within a set of paragraphs, a list of bulleted points, or using images and data tables|CSS***CSS is the language for describing the presentation of Web pages, including colors, layout, and fonts. It allows one to adapt the presentation to different types of devices, such as large screens, small screens, or printers|Javascript***JavaScript is a scripting language used to develop web pages. Developed in Netscape, JS allows developers to create a dynamic and interactive web page to interact with visitors and execute complex actions|DOM Structure***The Document Object Model (DOM) is a programming interface for web documents. It represents the page so that programs can change the document structure, style, and content|Web servers***Web servers are primarily used to process and manage HTTP/HTTPS requests and responses from the client system"},
                {"role": "user", "content": concept},
            ]
    )
    generation = res["choices"][0]["message"]["content"]
    subtopics = generation.split("|")
    out = []
    for subtopic in subtopics:
        split_ = subtopic.split("***")
        out.append({
            "name": split_[0],
            "description": split_[1]
        })
    return out










from flask import Flask, request, jsonify, render_template, make_response, g, redirect
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS
import sqlite3
import uuid


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DB_NAME)
    return db

def init_db():
    with app.app_context():
        db = get_db()
        with open('schema.sql', 'r') as f:
            db.cursor().executescript(f.read())
        db.commit()
    print("Initialized the database.")


app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/api/breakdown", methods=["POST"])
def breakdown():
    concept = request.json["consept"]
    token = request.cookies.get("session")
    return redirect("/login") if token is None else jsonify({"subtopics": get_breakdown(concept), "topic": concept})


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        # get request body
        body = request.get_json()
        username = body['email']
        password = body['password']
        db = get_db()
        cursor = db.cursor()

        cursor.execute("SELECT * FROM users WHERE email = ?", (username,))
        user_data = cursor.fetchone()
        if user_data and check_password_hash(user_data[4], password):
            return jsonify({"token": user_data[1], "message": "User logged in successfully"}), 200
        else:
            return jsonify({"message": "Invalid username or password"}), 401
    response = make_response(render_template("login.html"))
    return response

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # get request body
        body = request.get_json()
        username = body['username']
        email = body['email']
        password = body['password']

        hashed_password = generate_password_hash(password, method='sha256')
        db = get_db()
        cursor = db.cursor()
        public_id = str(uuid.uuid4())
        cursor.execute("INSERT INTO users (public_id, username, email, password) VALUES (?, ?, ?, ?)", (public_id, username, email, hashed_password))
        db.commit()
        return jsonify({"token": public_id, "message": "User created successfully"}), 201

    return make_response(render_template("register.html"))

@app.route('/me', methods=['GET'])
def me():
    public_id = token_selector()
    db = get_db()
    cursor = db.cursor()
    # public_id is the token
    cursor.execute("SELECT * FROM users WHERE public_id = ?", (public_id,))
    user_data = cursor.fetchone()
    if user_data:
        return jsonify({"username": user_data[2], "email": user_data[3]}), 200
    else:
        return jsonify({"message": "User not found"}), 404

@app.route('/logout', methods=['GET'])
def logout():
    response = make_response(render_template("logout.html"))
    response.set_cookie("session", "", expires=0)
    return response

"""

SQL Schema
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    public_id TEXT NOT NULL UNIQUE,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
);

CREATE TABLE prompts if not exists (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    author TEXT NOT NULL,
    topic TEXT NOT NULL,
    subtopic TEXT NOT NULL,
    snowflake DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL    
);

"""


@app.route('/api/create', methods=['POST'])
def create():
    public_id = token_selector()
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE public_id = ?", (public_id,))
    user_data = cursor.fetchone()
    if not user_data:
        return jsonify({"message": "User not found"}), 404
    author = user_data[2]
    body = request.get_json()
    print(body)
    topic = body["topic"]
    subtopics = body["subtopics"]
    cursor.execute("INSERT INTO prompts (author, topic, subtopic) VALUES (?, ?, ?)", (author, topic, json.dumps(subtopics)))
    db.commit()
    return jsonify({"message": "Prompt created successfully"}), 201


@app.route('/api/getPrompts', methods=['GET', 'POST'])
def get_prompts():
    db = get_db()
    public_id = token_selector()
    cursor = db.cursor()
    print(public_id)
    cursor.execute("SELECT * FROM users WHERE public_id = ?", (public_id,))
    user_data = cursor.fetchone()
    cursor.execute("SELECT * FROM prompts WHERE author = ?", (user_data[2], ))
    prompts = cursor.fetchall()
    prompts_ = []
    for prompt in prompts:
        prompts_.append({
            "topic": prompt[2],
            "subtopics": json.loads(prompt[3]),
        })
    if prompts_:
        return jsonify(prompts_), 200
    else:
        return jsonify({"message": "No prompts found"}), 404
    """
    Example prompt that will be returned from the api
    {
        "id": 1, # Internal ID
        "author": "username",
        "topic": "topic", 
        "subtopic": "subtopic",
        "snowflake": "2020-10-10 10:10:10"
    }
    """    


# /me
# token_selector() -> public_id -> user_data -> return user_data

def token_selector():
    return request.cookies.get("session")


# User CR Auth POST
# Expects, Returns

# User
# email*, password*, username
# /me { #invalidAuth, #notFound }
# /login -> { token: string }
# /register -> { token: string }

# Proompt
# userId, Topic, Content

# /getall get-prompts { Topic[] }
# /create { data.json }
# ~~/getContent (userId~, Topic)  { data.json } { #notFound }~~


if __name__ == "__main__":
    init_db()
    app.run(debug=True)