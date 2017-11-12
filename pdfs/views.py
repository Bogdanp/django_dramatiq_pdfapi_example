from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import PDF
from .serializers import PDFSerializer
from .tasks import generate_pdf


@csrf_exempt
@api_view(["POST"])
def create_pdf(request):
    serializer = PDFSerializer(data=request.data)
    if serializer.is_valid():
        pdf = serializer.save()
        generate_pdf.send(pdf.pk)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def view_pdf(request, pk):
    try:
        pdf = PDF.objects.get(pk=pk)
        serializer = PDFSerializer(pdf)
        return Response(serializer.data)
    except PDF.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
