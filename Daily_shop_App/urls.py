from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('shop',views.shop, name='shop'),
    path('signup',views.signup, name='signup'),
    path('login',views.login, name='login'),
    path('logout',views.logout, name='logout'),
    path('change_password',views.change_password, name='change_password'),
    path('forgot_pswd',views.forgot_pswd, name='forgot_pswd'),
    path('otp',views.otp, name='otp'),
    path('new_pswd',views.new_pswd, name='new_pswd'),
    path('seller_index',views.seller_index, name='seller_index'),
    path('seller_change_password',views.seller_change_password, name='seller_change_password'),
    path('seller_add_product',views.seller_add_product,name='seller_add_product'),
    path('seller_view_product',views.seller_view_product,name='seller_view_product'),
    path('seller_product_details/<int:pk>/',views.seller_product_details,name='seller_product_details'),
    path('seller_edit_product/<int:pk>/',views.seller_edit_product,name='seller_edit_product'),
    path('seller_delete_product/<int:pk>/',views.seller_delete_product,name='seller_delete_product'),
    path('view_product',views.view_product,name='view_product'),
    path('product_details/<int:pk>/',views.product_details,name='product_details'),
    path('add_to_wishlist/<int:pk>/',views.add_to_wishlist,name='add_to_wishlist'),
    path('wishlist',views.wishlist,name='wishlist'),
    path('remove_from_wishlist/<int:pk>/',views.remove_from_wishlist,name='remove_from_wishlist'),
    path('add_to_cart/<int:pk>/',views.add_to_cart,name='add_to_cart'),
    path('cart',views.cart,name='cart'),
    path('remove_from_cart/<int:pk>/',views.remove_from_cart,name='remove_from_cart'),
    path('change_qty/<int:pk>/',views.change_qty,name='change_qty'),
    path('category/<int:pk>/',views.category,name='category'),
    path('search',views.search,name='search'),
    path('success/',views.success,name='success')
]
