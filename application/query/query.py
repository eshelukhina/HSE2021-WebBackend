import graphene
from application.db.fake_db import people
from application.models.person import Person


class Query(graphene.ObjectType):
    info: Person = graphene.Field(Person, id=graphene.Int())

    def resolve_info(self, info, id):
        return people[id]

    add: Person = graphene.Field(Person, firstname=graphene.String(), lastname=graphene.String(), age=graphene.Int())

    def resolve_add(self, info, firstname, lastname, age):
        people.append(Person(firstname, lastname, age))
        return people[len(people) - 1]
