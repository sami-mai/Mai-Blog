from . import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, index=True)
    uname = db.Column(db.String(255))
    password = password_hash = db.Column(db.String(255))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    comment = db.relationship('Comment', backref='user', lazy="dynamic")
    blogPost = db.relationship('BlogPost', backref='user_admin', lazy="dynamic")

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'User {self.username}'


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    users = db.relationship('User', backref='role', lazy="dynamic")

    def __repr__(self):
        return f'User {self.name}'


class Subscriber(db.Model):
    __tablename__ = 'subscribers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, index=True)

    def __repr__(self):
        return f'User {self.name}'


class BlogPost(db.Model):
    '''
    BlogPost class to define blog post Objects
    '''

    __tablename__ = 'blogPosts'

    id = db.Column(db.Integer, primary_key=True)
    blogPost_category = db.Column(db.String)
    blogPost_title = db.Column(db.String)
    blogPost_description = db.Column(db.String)
    blogPost_body = db.Column(db.String)
    posted_on = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def save_blogPost(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def clear_blogPosts(cls):
        BlogPost.all_blogPosts.clear()

    @classmethod
    def get_blogPosts(cls, id):
        blogPosts = BlogPost.query.filter_by(blogPost_id=id).all()
        return blogPosts
