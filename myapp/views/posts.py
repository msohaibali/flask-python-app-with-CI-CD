from flask.json import jsonify
from myapp.model.post_model import Posts, PostsSchema
from flask import Blueprint, render_template, url_for
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

@posts.route('/createpost', methods=['POST'])
@login_required
def create_post():
    pass

@login_required
@posts.route('/updatepost',methods=['PUT'])
def update_post():
    pass

@login_required
@posts.route('/deletepost',methods=['DELETE'])
def delete_post():
    pass
