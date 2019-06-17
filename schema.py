import graphene
import json
import uuid
from datetime import datetime
from models import listData , listpost


class Post(graphene.ObjectType):
    title = graphene.String()
    content = graphene.String()


class User(graphene.ObjectType):
    id = graphene.ID(default_value=str(uuid.uuid4()))
    username = graphene.String()
    created_at = graphene.DateTime(default_value=datetime.now())
    avatar_url = graphene.String()
    list_post = graphene.List(Post)

    def resolve_avatar_url(self, info):
        print(self['username'])
        return 'https://cloudinary.com/{}/{}'.format(self['username'], self['id'])
    def resolve_list_post(self, info):
        
        return listpost()


class Query(graphene.ObjectType):
    users = graphene.List(User)
    hello = graphene.String()
    is_admin = graphene.Boolean()

    def resolve_hello(self, info):
        return "world"

    def resolve_is_admin(self, info):
        return True

    def resolve_users(self, info):
        n=listData()
        return n




schema = graphene.Schema(query=Query, )

result = schema.execute(
    '''
    {
      users {
        id
        createdAt
        username
        avatarUrl
      }
    }
    ''',
    # context={'is_anonymous': True}
    # variable_values={'limit': 1}
)

dictResult = dict(result.data.items())
print(json.dumps(dictResult, indent=2))
