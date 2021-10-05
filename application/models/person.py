import graphene


class Person(graphene.ObjectType):
    firstname: str = graphene.String()
    lastname: str = graphene.String()
    age: int = graphene.Int()