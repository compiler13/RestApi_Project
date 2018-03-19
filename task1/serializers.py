from rest_framework import serializers
from task1.models import Language
from task1.models import Application
from task1.models import Product
from task1.models import Website
from task1 .models import Contact
from task1.models import Profession
from task1 .models import Friend


class CompilerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ( 
         'title',
         'name', 
         )




class ApplicationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Application 
        fields = (
         'name',
         'description',
         'language', 
        )

class ApplicationGETSerializers(serializers.ModelSerializer):
    language = CompilerSerializer()
    class Meta:
        model = Application 
        fields = (
            'name',
            'description',
            'language', 
        )


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'name', 
            'product_type',
        )

class ProductDetailsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (

            'name', 
            'product_type',
        )



class ProfessionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = ('occupation',)


class ContactSerializers(serializers.ModelSerializer):
    profession = ProfessionSerializers()
    class Meta:
        model = Contact
        fields = (
            'id',
            'name', 
            'phone', 
            'email',
            'profession',
        )


class ContactBasicSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = (
            'name', 
            'phone', 
            'email',
            'profession',
        )
      

class FriendSerializers(serializers.ModelSerializer):
    friend1 = ContactSerializers()
    friend2 = ContactSerializers()
    
    class Meta:
        model = Friend
        fields = (
            'id',
            'friend1',
            'friend2',
        )


class FriendBasicSerializers(serializers.ModelSerializer):
   
    class Meta:
        model = Friend
        fields = ('friend1', 'friend2',)


    
        


class WebsiteSerializers(serializers.ModelSerializer):
    # app1 = ApplicationSerializers()
    # app2 = ProductSerializers() 

    class Meta:
        model = Website
        fields = (
            'app1', 
            #'app2',
            'app3',
            
 
            )


class WebsiteGETSerializers(serializers.ModelSerializer):
    app1 = ApplicationGETSerializers()
    #app2 = ProductSerializers() 
    app3 = ContactSerializers()
    app4 = ProfessionSerializers()


    class Meta:
        model = Website
        fields = (
            'app1', 
            # 'app2',
            'app3',
            'app4',


            
            )
