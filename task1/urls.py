from django.conf.urls import url
from task1 import views

urlpatterns = [
    # url(r'^compiler/$', views.compiler_list),
    # url(r'^compiler/(?P<pk>[0-9]+)/$', views.compiler_detail),
    #url(r'language-create/$', views.LanguageCreate.as_view() ),
    url(r'language-list/$', views.LanguageList.as_view() ),
    url(r'languageView/$', views.LanguageView.as_view() ),

    #url(r'application-create/$', views.ApplicationCreate.as_view() ),
    url(r'application-list/$', views.ApplicationList.as_view() ),
    url(r'application-list/(?P<pk>[\d-]+)/$', views.ApplicationDetails.as_view() ),

    #url(r'product-create/$', views.ProductCreate.as_view() ),
    url(r'Product-list/$', views.ProductList.as_view() ),
    url(r'Product-list/(?P<pk>[\d-]+)/$', views.ProductDetails.as_view() ),
    url(r'product-view/$', views.ProductView.as_view() ),

    url(r'contact-list/$', views.ContactList.as_view() ),
    url(r'contact-list/(?P<pk>[\d-]+)/$', views.ContactDetails.as_view() ),
    

    # url(r'profession-create/$', views.ProfessionCreate.as_view() ),
    url(r'profession-list/$', views.ProfessionList.as_view() ),
    url(r'profession-list/(?P<pk>[\d-]+)/$', views.ProfessionDetails.as_view() ),


     
     url(r'friends/$', views.FriendView.as_view() ),
     url(r'friends/(?P<pk>[\d-]+)/$', views.FriendDetails.as_view() ),


    #url(r'website-create/$', views.WebsiteCreate.as_view() ),
    url(r'website-list/$', views.WebsiteList.as_view() ),
    url(r'website-list/(?P<pk>[\d-]+)$', views.WebsiteDetails.as_view() ),
    url(r'website-view/$', views.WebsiteView.as_view() ),
        

]