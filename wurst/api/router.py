from rest_framework.routers import DefaultRouter

from wurst.api.views import CommentViewSet, IssueViewSet, ProjectViewSet


def get_router():
    """
    Get a Django REST Framework router instance with all viewsets.

    :rtype: rest_framework.routers.DefaultRouter
    """
    router = DefaultRouter()
    router.register(r'projects', ProjectViewSet)
    router.register(r'issues', IssueViewSet)
    router.register(r'comments', CommentViewSet)
    return router
