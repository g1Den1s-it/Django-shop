from django.urls import path

from store.views import Menu, CategoryRetrieveAPIView, SubcategoryRetrieveAPIView, GoodsRetrieveAPIView

urlpatterns = [
    path('', Menu.as_view()),
    path('<slug:slug>/', CategoryRetrieveAPIView.as_view()),
    path('<slug:slug>/<slug:subslug>/', SubcategoryRetrieveAPIView.as_view()),
    path('<slug:slug>/<slug:subslug>/<int:pk>/', GoodsRetrieveAPIView.as_view()),
]