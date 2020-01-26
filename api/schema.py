import graphene

from gateway.managers import course_manager


class CourseType(graphene.ObjectType):
    title = graphene.String()
    start = graphene.String()
    end = graphene.String()
    pacing_type = graphene.String()
    _id = graphene.ID()
    image_url = graphene.String()


class Query(graphene.ObjectType):
    courses = graphene.List(CourseType)

    def resolve_courses(self, info):
        data_source = course_manager.our_suggested_courses()
        return data_source


schema = graphene.Schema(query=Query)
