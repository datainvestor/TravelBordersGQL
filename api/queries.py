from .models import Post
from ariadne import QueryType

#File containing graphql resolvers(queries)

#establish binder that binds resolvers to schema // alternative query=ObjectType("Query")
query = QueryType()

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

@query.field("hello")
def resolve_hello(*_):
    return "Hello!"