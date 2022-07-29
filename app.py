import logging

from flask import Flask, request, render_template, send_from_directory
from functions import load_posts, get_posts_by_word, add_post
from loader.views import loader_blueprint

# Указываем расположение словаря с данными и папки с изображениями
POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

# Запускаем блупринты (вместо апп роут)
app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)

logging.basicConfig(filename="basic.log", level=logging.INFO)

# Выводим список всех постов


@app.route("/list")
def page_tag():
    pass


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run()

