from flask import Flask, send_from_directory

from functions import get_posts_by_tag
from loader.views import *
from main.views import *

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(loader)


@app.route("/search")
def page_tag():
    value = request.args['s']
    data = read_json(POST_PATH)
    if not data:
        return f'Ошибка загрузки JSON'
    found_posts = get_posts_by_tag(value, data)
    return render_template('search.html', found_posts=found_posts, value=value)


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run()
