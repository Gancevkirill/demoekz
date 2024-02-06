from django.urls import path
from .views import productsView, login, registration, logout, cartInfo, cartChange

urlpatterns = [
    path('cart', cartInfo),
    path('cart/<int:pk>', cartChange),
    path('products', productsView),
    path('reg', registration),
    path('login', login),
    path('logout', logout),
    path('products/<int:pk>', productsView),

]