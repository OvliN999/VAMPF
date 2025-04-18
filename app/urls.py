from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


from app.controller import authview, book, admins

urlpatterns =[
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('', views.home, name="home"),
    path('category/', views.category, name="category"),
    path('category/<str:id>', views.categoryview, name="categoryview"),
    path('category/<str:categ_id>/<str:car_id>', views.carview, name="carview"),

    # path('category/<str:categ_id>/<str:car_id>/book', book.addtobook, name="addtobook"),
    path('book/', book.addtobook, name="addtobook"),
    # path('carsCheckBox/', book.carsCheckBox, name="carsCheckBox"),

    path('register/',authview.register, name="register"),
    path('login/',authview.loginpage, name="loginpage"),
    path('logout/',authview.logoutpage, name="logout"),

    path('admin-panel/', admins.dashboard, name="dashboard"),
    path('addcar/', admins.addcar, name="addcar"),
    path('delete/<int:id>', admins.deletecar, name="deletecar"),

    path('adduser/', admins.adduser, name="adduser"),
    path('viewuser/', admins.viewuser, name="viewuser"),
    path('delete/<int:id>', admins.deleteuser, name="deleteuser"),

    path('bookview/', admins.bookview, name="bookview"),
    # path('viewuser/<str:user_id>', admins.deleteuser,name="deleteuser"),

    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
