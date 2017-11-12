from rest_framework import serializers

from .models import PDF


class PDFSerializer(serializers.ModelSerializer):
    source_url = serializers.URLField(max_length=512)
    pdf_url = serializers.URLField(read_only=True)

    class Meta:
        model = PDF
        fields = ("id", "source_url", "pdf_url", "status")
        read_only_fields = ("status",)
