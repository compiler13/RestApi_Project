    # -*- coding: utf-8 -*-


from django.db import models


class compiler(models.Model):
        created = models.DateField(auto_now_add=True)
        title = models.CharField(max_length=100, blank=True, default='')
        code = models.TextField()
        language = models.CharField( max_length=100 )
        style = models.CharField( max_length=100 )

        class Meta:
                
             ordering = ('created',)

class Language(models.Model):
    title  = models.CharField( max_length = 50)
    name  =  models.CharField( max_length = 40) 

    def __str__(self):
        return '{} '.format( self.name)


class Application(models.Model):
    name = models.CharField(max_length = 20)
    description = models.TextField()
    language = models.ForeignKey(Language)


    def __str__(self):
        return '{} : {} :{}'.format(self.name, self.description, self.language)

class Product(models.Model):
    name = models.CharField(max_length = 20)
    product_type = models.CharField(max_length = 20 )

    def __str__(self):
        return '{}  : {}'.format( 

            self.name, 
            self.product_type
            
            )

class Profession(models.Model):
    """Profession
    """
    occupation = models.CharField(max_length = 20, null = True)

    def __str__(self):
        return '{} '.format(self.occupation)

class Contact(models.Model):
    name = models.CharField(max_length = 30, default = None, null=True)
    phone  = models.CharField(max_length = 12, null = True, default = None)
    email = models.EmailField(max_length = 100, null=True, default = None )
    profession = models.ForeignKey(Profession, null = True, default = None)

def __str__(self):
        return '{} : {} : {} : {}'.format(
            self.name, 
            self.phone, 
            self.email,
            self.profession,    
        )
        class Meta:
            unique_together = ('email', 'phone')

class Friend(models.Model):
    friend1 = models.ForeignKey(Contact, related_name="first_friend")
    friend2 = models.ForeignKey(Contact, related_name="second_friend")

    def __str__(self):
        return '{} : {} '.format('friend1', 'friend2', )

class Website(models.Model):
    app1 = models.ForeignKey(Application)
    app2 = models.ForeignKey(Product)
    app3 = models.ForeignKey(Contact)
    app4 = models.ForeignKey(Profession, null = True, default = None)

    