# -*- coding: utf-8 -*-

from rest_framework import generics
from task1.models import ( Language, Application, Website, Product, Contact, Profession, Friend )

from task1.serializers import ( CompilerSerializer, ApplicationSerializers , ApplicationGETSerializers, WebsiteSerializers, WebsiteGETSerializers, ProductSerializers, ProductDetailsSerializers, ContactSerializers, ContactBasicSerializers, ProfessionSerializers, FriendSerializers, FriendBasicSerializers, ProfessionDetailsSerializers  )



class LanguageCreate(generics.CreateAPIView):
    """#LANGUAGE APPLICATION"""
    serializer_class = CompilerSerializer


class LanguageList(generics.ListAPIView):
    serializer_class = CompilerSerializer
    def get_queryset(self):
        return Language.objects.all()

class LanguageView(generics.ListCreateAPIView):
    serializer_class = CompilerSerializer
    def get_queryset(self):
        return Language.objects.all()


class ApplicationCreate(generics.CreateAPIView):
    """ #APPLICATION APP"""
    serializer_class = ApplicationSerializers


class ApplicationList(generics.ListCreateAPIView):
    
    serializer_class = ApplicationSerializers
    
    def get_queryset(self):
        return Application.objects.all()

class ApplicationDetails(generics.RetrieveDestroyAPIView):
    serializer_class = ApplicationSerializers
    queryset = Application.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ApplicationSerializers
        else:
            return ApplicationDetailsSerializers 


class ApplicationView(generics.ListCreateAPIView):
    
    def get_serializer_class(self):
        
        if self.request.method == 'GET':
            return ApplicationGETSerializers
        else:
            return ApplicationSerializers    

    def get_queryset(self):
        return Application.objects.all()

# class ProductCreate(generics.CreateAPIView):
#     """#PRODUCT APP"""
#     serializer_class = ProductSerializers

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductSerializers 
        else:
            return ProductDetailsSerializers

class ProductView(generics.ListCreateAPIView):
    serializer_class = ProductSerializers
    def get_queryset(self):
        return Product.objects.all()

class ProductDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializers
    queryset = Product.objects.all()

class ContactList(generics.ListCreateAPIView):
    """#CONTACT APP"""
    queryset = Contact.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ContactSerializers
        else:
            return ContactBasicSerializers

class ContactView(generics.ListCreateAPIView):
    serializer_class = ContactSerializers
    queryset = Contact.objects.all()

class ContactDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ContactSerializers
    queryset = Contact.objects.filter()

class ProfessionCreate(generics.CreateAPIView):
    serializer_class = ProfessionSerializers

class ProfessionList(generics.ListCreateAPIView):
    serializer_class = ProfessionSerializers
    queryset = Profession.objects.all()

class ProfessionDetails(generics.RetrieveDestroyAPIView):
    queryset = Profession.objects.all()
    def get_serializer_class (self):
        if self.request.method == 'GET':
            return ProfessionSerializers
            
        else:
            return ProfessionDetailsSerializers 
     
                     
    
class ProfessionView(generics.ListCreateAPIView):
    serializer_class = ProfessionSerializers
    def get_queryset(self):
        return Profession.objects.all()


class FriendView(generics.ListCreateAPIView):
     queryset = Friend.objects.all()
     def get_serializer_class(self):
        if self.request.method == 'GET':
            return FriendSerializers
        else:
            return FriendBasicSerializers

class FriendDetails(generics.RetrieveUpdateDestroyAPIView):
     queryset = Friend.objects.filter()
     def get_serializer_class(self):
        if self.request.method == 'GET':
            return FriendSerializers
        else:
            return FriendBasicSerializers

class WebsiteCreate(generics.CreateAPIView):
    serializer_class = WebsiteSerializers

class WebsiteList(generics.ListCreateAPIView):
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return WebsiteGETSerializers
        else:
            return WebsiteSerializers
    def get_queryset(self):
        return Website.objects.all()

class WebsiteDetails(generics.RetrieveDestroyAPIView):
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return WebsiteGETSerializers
        else:
            return WebsiteDetailsSerializers
    def get_queryset(self):
        return Website.objects.all()

class WebsiteView(generics.ListCreateAPIView):
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return WebsiteGETSerializers
        else:
            return WebsiteSerializers
    def get_queryset(self):
        return Website.objects.all()

        
        