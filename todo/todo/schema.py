import graphene
from graphene import ObjectType, Mutation
from graphene_django import DjangoObjectType
from users.models import User, Project, ToDo


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class TODOType(DjangoObjectType):
    class Meta:
        model = ToDo
        fields = '__all__'


class CustomUserUpdateMutation(Mutation):
    class Arguments:
        username = graphene.String(required=True)
        id = graphene.ID()

    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, **kwargs):
        user = User.objects.get(id=kwargs.get('id'))
        user.username = kwargs.get('username')
        user.save()
        return cls(user=user)


class CustomUserCreateMutation(Mutation):
    class Arguments:
        username = graphene.String(required=True)
        firstname = graphene.String()
        lastname = graphene.String()
        email = graphene.String(required=True)

    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, **kwargs):
        user = User.objects.create(**kwargs)
        return cls(user=user)


class CustomUserDeleteMutation(Mutation):
    class Arguments:
        id = graphene.ID()

    users = graphene.List(UserType)

    @classmethod
    def mutate(cls, root, info, **kwargs):
        User.objects.get(id=kwargs.get('id')).delete()
        return cls(users=User.objects.all())


class Mutations(ObjectType):
    update_user = CustomUserUpdateMutation
    create_user = CustomUserCreateMutation
    delete_user = CustomUserDeleteMutation


class Query(ObjectType):
    all_users = graphene.List(UserType)
    all_projects = graphene.List(ProjectType)
    all_todos = graphene.List(TODOType)

    user_by_id = graphene.List(UserType, id=graphene.Int(required=False))

    def resolve_user_by_id(root, info, id=None):
        if id:
            return User.objects.get(id=id)
        return User.objects.all()

    project_by_user = graphene.List(ProjectType, username=graphene.String(required=False))

    def resolve_project_by_user(root, info, username=None):
        if username:
            return Project.objects.filter(users__username=username)
        return Project.objects.all()

    def resolve_all_users(root, info):
        return User.objects.all()

    def resolve_all_projects(root, info):
        return Project.objects.all()

    def resolve_all_todos(root, info):
        return ToDo.objects.all()


schema = graphene.Schema(query=Query, mutation=Mutations)
