import json
import logging
from json import JSONDecodeError


def get_posts_by_tag(value, data):
    found_posts = []
    for i in data:
        if value in i['content']:
            found_posts.append(i)
    return found_posts


def add_new_post(POST_PATH, picture, content, img_path, data):
    picture.save(img_path)
    data.append({
        'pic': img_path,
        'content': content
    })
    with open(POST_PATH, 'w') as write_file:
        json.dump(data, write_file, ensure_ascii=False, indent=4)


def read_json(POST_PATH):
    try:
        with open(POST_PATH, 'r') as read_file:
            data = json.load(read_file)
    except FileNotFoundError as e:
        logging.error(e)
        print("Файл не найден")
    except JSONDecodeError as e:
        print("Не удается получить JSON из файла")
        logging.error(e)
    else:
        logging.info("Данные получены")
        print("Данные получены")
        return data


def check_extention(ALLOWED_EXTENTION, extention):
    return extention in ALLOWED_EXTENTION
