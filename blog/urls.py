from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeListView.as_view(), name='home-page'),
    path('blog/', views.BlogListView.as_view(), name='blog-page'),
    path('blog/<int:pk>', views.BlogDetailView.as_view(), name='single-page'), # 'blog/<int:pk>' для уникальной записи в url будет подставляться blog/1 Итд
    #path('contacts/', views.contacts, name='blog-contacts'),
   # path('about_us/', views.about_us, name='blog-about_us'),
   # path('photos/', views.photos, name='blog-photos')
]
