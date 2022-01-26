from django.urls import path
from . import views
urlpatterns=[

    path('akhil/',views.samplefunction),
    path('2nd/',views.helloworldfunction),

]
