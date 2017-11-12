import dramatiq
import h2p

from .models import PDF


@dramatiq.actor
def generate_pdf(pk):
    pdf = PDF.objects.get(pk=pk)

    try:
        h2p.generate_pdf(
            pdf.filename,
            source_uri=pdf.source_url,
        ).result()

        pdf.status = PDF.STATUS_DONE
    except h2p.ConversionError:
        pdf.status = PDF.STATUS_FAILED

    pdf.save()
