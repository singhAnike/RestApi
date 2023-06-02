from rest_framework import serializers
from .models import Students, Board, Standard, Medium, Address
from .utils import create_student

# Here Address Serializer
class AddressSerializer(serializers.Serializer):
    postal_address = serializers.CharField( max_length=100)
    city = serializers.CharField( max_length=50)

# Here Students Serializer
class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    student_name = serializers.CharField(max_length=30)
    board_id = serializers.IntegerField()
    medium_id = serializers.IntegerField()
    standard_id = serializers.IntegerField()
    address = AddressSerializer()



    def create(self, validated_data):
        address_data = validated_data.pop('address')
        return create_student(
            Student_Name=validated_data.pop('student_name'),
            Board_id=validated_data.pop('board_id'),
            Medium_id = validated_data.pop('medium_id'),
            Standard_id = validated_data.pop('standard_id'),
            Postal_Address=address_data['postal_address'],
            City=address_data['city']
            
        )
        

    

    def update(self, instance, validated_data):
        instance.Student_Name = validated_data.get('student_name', instance.student_name)
        instance.board_id = validated_data.get('student_board_id', instance.board_id)
        instance.standard_id = validated_data.get('student_standard_id', instance.standard_id)
        instance.medium_id = validated_data.get('student_medium_id', instance.medium_id)
        instance.save()
        return instance
