from flask import Blueprint, render_template, redirect, url_for, request
from models.post import Post

post_bp = Blueprint('post', __name__)


@post_bp.route('/post/new', methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        post = Post(title=title, content=content)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('post.read_post', post_id=post.id))
    else:
        return render_template('new_post.html')


@post_bp.route('/post/<int:post_id>')
def read_post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('read_post.html', post=post)


@post_bp.route('/post/<int:post_id>/edit', methods=['GET', 'POST'])
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)
    if request.method == 'POST':
        post.title = request.form['title']
        post.content = request.form['content']
        db.session.commit()
        return redirect(url_for('post.read_post', post_id=post.id))
    else:
        return render_template('edit_post.html', post=post)


@post_bp.route('/post/<int:post_id>/delete', methods=['POST'])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('post.index'))
