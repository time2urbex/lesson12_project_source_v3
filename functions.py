import json

# Загружаем посты из json

def load_posts() -> list[dict]:
    with open('posts.json', 'r', encoding='utf-8') as file:
        return json.load(file)


# Поиск - в этой функции мы делаем перебор по значению


def get_posts_by_word(word:str) -> list[dict]:
    result = []
    for post in load_posts():
        if word.lower() in post['content'].lower():
            result.append(post)
    return result

# Функция добавления поста


def add_post(post: dict) -> dict:
    posts: list[dict] = load_posts()
    posts.append(post)
    with open('posts.json', 'w', encoding='utf-8') as file:
        json.dump(posts, file)
    return post