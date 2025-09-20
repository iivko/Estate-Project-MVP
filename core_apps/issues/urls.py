from django.urls import path

from .views import (
    IssueCreateAPIView,
    IssueDetailAPIView,
    IssueUpdateAPIView,
    IssueDeleteAPIView,
    IssueListAPIView,
    MyIssuesListAPIView,
    AssignedIssueListAPIView,
)


urlpatterns = [
    path("", IssueListAPIView.as_view(), name="issue-list"),
    path("me/", MyIssuesListAPIView.as_view(), name="my-issue-list"),
    path("assigned/", AssignedIssueListAPIView.as_view(), name="assigned-issue-list"),

    # CRUD
    path("create/<uuid:apartment_id>/", IssueCreateAPIView.as_view(), name="create-issue"),
    path("<uuid:id>/", IssueDetailAPIView.as_view(), name="issue-detail"),
    path("update/<uuid:id>/", IssueUpdateAPIView.as_view(), name="update-issue"),
    path("delete/<uuid:id>/", IssueDeleteAPIView.as_view(), name="delete-issue")
]