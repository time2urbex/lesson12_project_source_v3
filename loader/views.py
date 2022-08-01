import logging
import json
from flask import Blueprint, render_template, request
from loader.utils import save_picture
from functions import load_posts, get_posts_by_word, add_post


loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')

# Загружаем страницу добавления поста

@loader_blueprint.route('/post')
def post_page():
    return render_template('post_form.html')


# Присваеваем загруженному посту данные и передаем их в  переменные


@loader_blueprint.route('/post', methods=['POST'])
def add_post_page():
    picture = request.files.get('picture')
    content = request.form.get('content')

# Делаем различные проверки

    if not picture or not content:
        return 'Нет картинки или текста'

    if picture.filename.split('.')[-1] not in ['jpeg', 'png']:
        logging.info('Загруженный файл не имеет формат jpg и png')
        return 'Неверное расширение файла'
    try:
        picture_path: str = '/' + save_picture(picture)
    except FileNotFoundError:
        logging.error('Файл не найден')
        return 'Файл не найден'

    except JSONDecoderError:
        return 'Невалидный файл'

# Возвращаем данные в виде html


    post: dict = add_post({'pic': picture_path, 'content': content})
    return render_template('post_uploaded.html', post=post)
