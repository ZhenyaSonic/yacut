import random
import re
import string

from flask import flash, redirect, render_template, url_for

from . import app, db
from .constants import MAX_LENGTH_SHORT, MAX_RANDOM_LINK_LENGTH
from .forms import UrlForm
from .models import URLMap


def generate_random_link(length=MAX_RANDOM_LINK_LENGTH):
    characters = string.ascii_letters + string.digits
    while True:
        random_link = ''.join(random.choice(characters) for _ in range(length))
        if not check_duplicate(random_link):
            return random_link


def is_valid_custom_id(custom_id):
    return (
        len(custom_id) <= MAX_LENGTH_SHORT and
        re.match('^[a-zA-Z0-9]+$', custom_id)
    )


def check_duplicate(short):
    return URLMap.query.filter_by(short=short).first() is not None


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = UrlForm()
    if form.validate_on_submit():
        if form.custom_id.data:
            short = form.custom_id.data
            if not is_valid_custom_id(short):
                flash('Указано недопустимое имя для короткой ссылки')
                return render_template('create_short.html', form=form)
            if check_duplicate(short):
                flash('Предложенный вариант короткой ссылки уже существует.')
                return render_template('create_short.html', form=form)
        else:
            short = generate_random_link()

        url_map = URLMap(original=form.original_link.data, short=short)
        db.session.add(url_map)
        db.session.commit()
        return render_template(
            'create_short.html',
            form=form,
            link=url_for('redirect_view', short=url_map.short, _external=True)
        )
    return render_template('create_short.html', form=form)


@app.route('/<short>')
def redirect_view(short):
    return redirect(
        URLMap.query.filter_by(short=short).first_or_404().original
    )