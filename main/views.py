import logging
import json
from flask import Blueprint, render_template, request
from functions import load_posts, get_posts_by_word, add_post



main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')

# Создаем роут главной страницы

@main_blueprint.route('/')
def main_page():
    return render_template('index.html')

# Создаем роут страницы для поиска


@main_blueprint.route('/search/')
def search_page():
    search_query = request.args.get('s', '')
    logging.info('Выполняю поиск')

    # Делаем проверку на наличие и работоспособность файла

    try:
        posts = get_posts_by_word(search_query)

    except FileNotFoundError:
        return 'Файл не найден'

    except JSONDecoderError:
        return 'Невалидный файл'
    return render_template('post_list.html', query=search_query, posts=posts)
