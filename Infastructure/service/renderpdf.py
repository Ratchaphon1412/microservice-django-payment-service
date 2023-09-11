from io import BytesIO
from django.http import HttpResponse
from django.conf import settings
from django.template.loader import get_template

from xhtml2pdf import pisa

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    if pdf.err:
        return HttpResponse("Invalid PDF", status_code=400, content_type='text/plain')
    
    
    with open(f'media/quotation/{context_dict["invoice_number"]}.pdf', 'wb') as f:
        f.write(result.getvalue())
        

    # return HttpResponse(result.getvalue(), content_type='application/pdf')
    return settings.BASE_URL+ settings.MEDIA_URL + f'quotation/{context_dict["invoice_number"]}.pdf'
