from rest_framework import serializers
from spacium.interior.models import (
    SpaciumDesignTeam
)


# class PricingPackageSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = PricingPackage
#         fields = '__all__'
#         read_only_fields = (
#             'id',
#         )
#
#     def create(self, validated_data):
#         if self.context['request'].user.is_authenticated and self.context['request'].user.is_staff:
#             return PricingPackage.objects.create(**validated_data)
#         raise serializers.ValidationError("You are not able to crate.")


# class InteriorFileSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = InteriorFile
#         fields = "__all__"
#         read_only_fields = (
#             'id',
#         )


class InteriorDesignServiceSerializer(serializers.ModelSerializer):
    # files = serializers.SerializerMethodField()

    class Meta:
        model = SpaciumDesignTeam
        fields = (
            'id',
            'user',
            'project_type',
            'project_space',
            'project_sqm',
            'design_theme',
            'pricing_package',
            'project_details',
            'attach_file',
            'status',
            'actual_price',
            'discount_percent'
        )
        read_only_fields = (
            'id',
            'user',
            'status',
        )

    # def get_files(self, instance):
    #     return InteriorFileSerializer(
    #         instance.interiorfile_set.all(),
    #         many=True
    #     ).data
    #
    # def create(self, validated_data):
    #     images_data = self.context.get('view').request.FILES
    #     interior_data = SpaciumDesignTeam.objects.create(**validated_data)
    #     for attach_file in images_data.values():
    #         InteriorFile.objects.create(interior_design=interior_data, attach_file=attach_file)
    #     return interior_data
    #
    # def update(self, instance, validated_data):
    #     if self.context['request'].user.is_authenticated and self.context['request'].user.is_admin:
    #         instance.model_method()
    #         return super().update(instance, validated_data)
    #     else:
    #         raise serializers.ValidationError("You are not able to update.")
