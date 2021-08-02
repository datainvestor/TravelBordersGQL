from .models import Post
from ariadne import QueryType, MutationType
from datetime import date
from . import db
#File containing graphql resolvers(queries)

#establish binder that binds resolvers to schema // alternative query=ObjectType("Query")
query = QueryType()
mutation = MutationType()



#bind resolver to schema item with query.field
@query.field("listPosts")
def listPosts_resolver(obj, info):
    """Get all posts from database and modify output- resolver"""
    try:
        posts = [post.to_dict() for post in Post.query.all()]
        print(posts)
        payload = {
            "success": True,
            "posts": posts
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload

@query.field("getPost")
def getPost_resolver(obj, info, id):
    """Get single post by ID- resolver"""
    try:
        post = Post.query.get(id)
        payload = {
            "success": True,
            "post": post.to_dict()
        }
    except AttributeError:  # post not found
        payload = {
            "success": False,
            "errors": ["Post item matching {id} not found"]
        }
    return payload

@query.field("posts")
def resolve_posts(*_):
    """Simple way to create graphql resolver that lists all items from the model"""
    return Post.query.all()

@mutation.field("createPost")
def resolve_create_post(obj, info, input):
    """mutation type resolver to create post(item)"""
    try:
        today=date.today()
        post = Post(
            title=input['title'], description=input['description'], created_at=today.strftime("%b-%d-%Y")
        )
        db.session.add(post)
        db.session.commit()
        payload = {
            "success": True,
            "post": post.to_dict()
        }
    except ValueError:  # date format errors
        payload = {
            "success": False,
            "errors": [f"Incorrect date format provided. Date should be in "
                       f"the format dd-mm-yyyy"]
        }
    return payload

@mutation.field("updatePost")
def update_post_resolver(obj, info, id, input):
    """Update post by its ID"""
    try:
        post = Post.query.get(id)
        if post:
            post.title = input['title']
            post.description = input['description']
        db.session.add(post)
        db.session.commit()
        payload = {
            "success": True,
            "post": post.to_dict()
        }
    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": ["item matching id {id} not found"]
        }
    return payload

@mutation.field("deletePost")
def delete_post_resolver(obj, info, id):
    try:
        post = Post.query.get(id)
        db.session.delete(post)
        db.session.commit()
        payload = {"success": True, "post": post.to_dict()}
    except:
        payload = {
            "success": False,
            "errors": ["Not found"]
        }
    return payload

@query.field("hello")
def resolve_hello(*_):
    return "Hello!"