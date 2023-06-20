from django.urls import path
from .views import *

urlpatterns = [
    path('savat/',ShoppingCard.as_view()),
    path('orders/',ProfilOrders.as_view()),
    path('wishlist/',ProfilWishlist.as_view()),
    path('wishlist_ochir/<int:son>/',WishOchir.as_view()),
    path('item_delete/<int:son>/',SavatItemOchir.as_view()),
    path('tanlangan_qosh/<int:son>/',TanlanganQosh.as_view()),
    path('savat_q/<int:pk>/',Miqdor_qosh.as_view()),
    path('savat_k/<int:pk>/',Miqdor_kamaytir.as_view()),
    path('item_qosh/<int:pk>/',Savat_qosh.as_view()),
]