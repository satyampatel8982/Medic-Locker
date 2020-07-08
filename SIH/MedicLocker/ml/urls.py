from django.urls import path
from . import views

urlpatterns = [
        path('' , views.IndexView , name = 'index' ),

        path('about/' , views.About , name = 'about'),

        path('addicition/' , views.Addicition , name = 'addicition'),

        path('contact/' , views.Contact , name = 'contact'),

        path('corona/' , views.Corona , name = 'corona'),

        path('disease/' , views.Disease , name = 'disease'),

        path('doc_login/' , views.Dlogin , name = 'doc_login'),

        path('doc_singup/' , views.DSingup , name = 'doc_singup'),

        path('emergency/' , views.Emergency , name = 'emergency'),

        path('life/' , views.Life , name = 'life'),

        path('pat_login/' , views.Plogin , name = 'pat_login'),

        path('pat_singup/' , views.PSingup , name = 'pat_singup'),

        path('support/' , views.Support , name = 'support'),

        path('write/' , views.Write , name = 'write'),
]
