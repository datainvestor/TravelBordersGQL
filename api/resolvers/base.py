from ariadne import QueryType, MutationType
#establish binder that binds resolvers to schema // alternative query=ObjectType("Query")
query = QueryType()
# mutation = MutationType()

@query.field("hello")
def resolve_hello(*_):
    return "Hello!"