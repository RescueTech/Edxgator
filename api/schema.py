import graphene

from gateway.managers import course_manager


class CourseType(graphene.ObjectType):
    title = graphene.String()
    start = graphene.String()
    end = graphene.String()
    _id = graphene.ID()
    marketing_url = graphene.String()
    card_image_url = graphene.String()
    org = graphene.String()
    availability = graphene.String()
    pacing_type = graphene.String()
    weeks_to_complete = graphene.String()
    image_url = graphene.String()


class Query(graphene.ObjectType):
    courses = graphene.List(CourseType)

    def resolve_courses(self, info):
        data_source = course_manager.our_suggested_courses()
        return data_source


schema = graphene.Schema(query=Query)
