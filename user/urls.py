from django.urls import path,include

from user import views


urlpatterns = [
    path('/register',views.register_user),
    path('/login',views.login_user),
    path('/<str:user_id>/advisor',views.get_advisor),
    path('/<str:user_id>/advisor/booking',views.fetch_bookings),
    path('/<str:user_id>/advisor/<str:advisor_id>',views.book_advisor),
    path('/<str:user_id>',views.test),
]
