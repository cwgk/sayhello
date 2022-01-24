from flask import flash, redirect, url_for, render_template, request
import random
from sayhello import app, db
from sayhello.forms import HelloForm, CommentForm
from sayhello.models import Message, Comment


@app.route('/', defaults={'page': 1}, methods=['GET', 'POST'])
@app.route('/pages/<int:page>', methods=['GET', 'POST'])
def index(page):
    form = HelloForm()
    c_form = CommentForm()
    ip = request.remote_addr
    iname = get_iname(Message.query.filter(Message.ip == ip).first())
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        message = Message(name=name, body=body, ip=ip, iname=iname)
        db.session.add(message)
        db.session.commit()
        flash('已成功发布留言！')
        return redirect(url_for('index', page=page))
    page = request.args.get('page', page, type=int)
    per_page = app.config['SAYHELLO_POST_PER_PAGE']
    messages = Message.query.order_by(Message.timestamp.desc()).paginate(page, per_page=per_page)
    comments = Comment.query.order_by(Comment.timestamp).all()
    return render_template('index.html', form=form, messages=messages, c_form=c_form, comments=comments)


@app.route('/input/<int:m_id>/<int:cur_p>', methods=['GET', 'POST'])
def input(m_id, cur_p):
    if request.method == 'POST':
        input1 = request.form.get('com', '')
        ip = request.remote_addr
        iname = get_iname(Message.query.filter(Message.ip == ip).first())
        comment = Comment(body=input1, ip=ip, iname=iname, message_id=m_id)
        db.session.add(comment)
        db.session.commit()
        flash('回复成功！')
        return redirect(url_for('index', page=cur_p))


def get_iname(is_exit):
    if is_exit is None:
        return get_name() + get_name()
    return is_exit.iname


def get_name():
    head = random.randint(0xb0, 0xd7)
    body = random.randint(0xa1, 0xfe)
    val = f'{head:x} {body:x}'
    str = bytes.fromhex(val).decode('gb2312')
    return str


# 注册全局函数
@app.template_global()
def t_bar(cur_l, total, pages, page):
    per_page = app.config['SAYHELLO_POST_PER_PAGE']
    if pages == page:
        return cur_l
    elif total % per_page == 0:
        return (pages - page) * per_page + cur_l
    else:
        return (pages - page) * per_page + cur_l + total % per_page - per_page
