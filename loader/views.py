import logging
import uuid

from flask import Blueprint, render_template, request

from functions import add_new_post, read_json, check_extention

loader = Blueprint('loader', __name__)
POST_PATH = "posts.json"
ALLOWED_EXTENTION = {'jpeg'}


@loader.route('/post/', methods=['GET'])
def load_post_page():
    return render_template('post_form.html')


@loader.route('/post/', methods=['POST'])
def try_load():
    picture = request.files.get('picture')
    content = request.form.get('content')
    if picture:
        extention = picture.content_type.split("/")[-1]
        if check_extention(ALLOWED_EXTENTION, extention):
            img_path = f'uploads/images/{str(uuid.uuid4())}.{extention}'
            data = read_json(POST_PATH)
            if not data:
                return 'Ошибка загрузки JSON'
            add_new_post(POST_PATH, picture, content, img_path, data)
            return render_template('post_uploaded.html', img=img_path, content=content)
        else:
            logging.info('Загруженный файл - не картинка')
            return 'Неверный формат'
    else:
        return 'Не удалось загрузить пост'
