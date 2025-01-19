import random
import re
import string

from flask import flash, redirect, render_template, url_for

from . import app, db
from .constants import MAX_LENGTH_SHORT
from .forms import UrlForm
from .models import URLMap


def generate_random_link(length=6):
    characters = string.ascii_letters + string.digits
    random_link = ''.join(random.choice(characters) for _ in range(length))
    if check_duplicate(random_link):
        random_link = generate_random_link()
    return random_link


def check_duplicate(short):
    return URLMap.query.filter_by(short=short).first() is not None


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = UrlForm()
    if not form.validate_on_submit():
        return render_template('create_short.html', form=form)
    if form.custom_id.data != '' and form.custom_id.data is not None:
        short = form.custom_id.data
        if (
                len(short) > MAX_LENGTH_SHORT
                or not re.findall('^[a-zA-Z0-9]+$', short)
        ):
            flash('Указано недопустимое имя для короткой ссылки')
            return render_template('create_short.html', form=form)
        if check_duplicate(short):
            flash('Предложенный вариант короткой ссылки уже существует.')
            return render_template('create_short.html', form=form)
    else:
        short = generate_random_link()
    url_map = URLMap(
        original=form.original_link.data,
        short=short
    )
    db.session.add(url_map)
    db.session.commit()
    return render_template(
        'create_short.html',
        form=form,
        link=url_for(
            'redirect_view',
            short=url_map.short,
            _external=True
        )
    )


@app.route('/<short>')
def redirect_view(short):
    return redirect(
        URLMap.query.filter_by(short=short).first_or_404().original
    )