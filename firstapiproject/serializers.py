from rest_framework import serializers
from firstapiproject.models import Contact

#tag kora sob class serialize
#class ContactSerializer(serializers.Serializer):
   #name=serializers.CharField(max_length=100)
   #title=serializers.CharField(max_length=100)
  # email=serializers.EmailField(max_length=30)
   
#def create(self, validated_data):
       
    #return Contact.objects.create(validated_data)

#def update(self, instance, validated_data):
        
        #instance.name = validated_data.get('name', instance.name)
       # instance.title = validated_data.get('title', instance.title)
        #instance.email = validated_data.get('email', instance.email)
        #instance.save()
        #return instance
    
#model serializer create now
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['name', 'title', 'email']    
    