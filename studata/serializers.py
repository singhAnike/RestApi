from rest_framework import serializers
from .models import STUDENT, BOARD, STANDARD, MEDIUM

class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    Student_Name = serializers.CharField(max_length=30)
    Board_id = serializers.IntegerField(source='Student_Board_id')
    Medium_id = serializers.IntegerField(source='Student_Medium_id')
    Standard_id = serializers.IntegerField(source='Student_Standard_id')



    def create(self, validated_data):
        board_id = validated_data.pop('Student_Board_id')
        medium_id = validated_data.pop('Student_Medium_id')
        standard_id = validated_data.pop('Student_Standard_id')

        board = BOARD.objects.get(id=board_id)
        medium = MEDIUM.objects.get(id=medium_id)
        standard = STANDARD.objects.get(id=standard_id)

        student = STUDENT.objects.create(
            Student_Name=validated_data['Student_Name'],
            Student_Board=board,
            Student_Medium=medium,
            Student_Standard=standard,
        )
        return student

    

    

    def update(self, instance, validated_data):
        instance.Student_Name = validated_data.get('Student_Name', instance.Student_Name)
        instance.Student_Board_id = validated_data.get('Student_id', instance.Student_Board_id)
        instance.Student_Standard_id = validated_data.get('Standard_id', instance.Student_Standard_id)
        instance.Student_Medium_id = validated_data.get('Medium_id', instance.Student_Medium_id)
        instance.save()
        return instance
