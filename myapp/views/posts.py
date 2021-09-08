from flask.json import jsonify
from datetime import datetime
from myapp.model.post_model import Posts
from myapp.model.db_extension import db
from myapp.model.post_model import Posts, PostsSchema
from flask import Blueprint, render_template, request, url_for, flash, redirect
from flask_login import login_required, current_user

posts = Blueprint('posts', __name__, url_prefix='/api')

@posts.route('/getposts', methods=['GET', 'POST'])
@login_required
def get_posts():
    all_posts = Posts.query.filter_by(user_id=current_user.id)
    if all_posts:
        user_posts = all_posts.all()
        post_schema = PostsSchema(many=True)
        output = post_schema.dump(user_posts)
        return render_template('posts.html', all_posts=output)

        # return jsonify(output)
    else:
        return render_template('posts.html', all_posts=[])

@posts.route('/createpost')
@login_required
def create_post_get():
    return render_template('create_post.html')

@posts.route('/createpost', methods=['POST'])
@login_required
def create_post():
    post_title = request.form.get('title')
    post_description = request.form.get('description')
    created_at = datetime.now()
    user_id = current_user.id
    
    # Incodicates Post already exists in database
    prev_post = Posts.query.filter_by(title=post_title).first()
    
    # Redirect to Create_Post Page if Post already exists
    if prev_post:
        flash('A Post with Same Title Already Exists in Database')
        return redirect(url_for('posts.create_post'))

    new_post = Posts(title=post_title, description=post_description, created_at=created_at, user_id=user_id)

    db.session.add(new_post)
    db.session.commit()
    
    return redirect(url_for('posts.get_posts'))

@login_required
@posts.route('/updatepost',methods=['PUT'])
def update_post():
    pass

@login_required
@posts.route('/deletepost',methods=['DELETE'])
def delete_post():
    pass
