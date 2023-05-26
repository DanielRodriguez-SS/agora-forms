from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter,A4
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Image
from reportlab.lib.units import inch
from io import BytesIO
from dataclasses import asdict, dataclass
"""
https://docs.reportlab.com/reportlab/userguide/ch1_intro/
https://docs.reportlab.com/reportlab/userguide/ch5_platypus/
"""
@dataclass
class ProductInfo:
    shop:str = '_NA'
    segments:str = '[CONSUMER, SMB]'
    device_type:str = '_NA'
    plans:str = '[Small, Medium]'
    products:str = '_NA'

@dataclass
class PromoDetails:
    type:str = 'ATL'
    code:str = '_NA'
    apply:str = '_NA'
    elegibility:str = '_NA'
    name:str = '_NA'
    credit:str = '_NA'
    recurring:str = '_NA'
    start_date:str = '_NA'
    start_time:str = '_NA'
    end_date:str = '_NA'
    end_time:str = '_NA'
    email_coms:str = '_NA'

def readiable_item(raw_item:str) -> str:
    return raw_item.replace('_',' ').capitalize()

def generate_pdf(product_info:object, promo_details:object):
    pdf_buffer = BytesIO()
    
    product_dict = asdict(product_info)
    promo_dict = asdict(promo_details)
    styles = getSampleStyleSheet()
    story = []
    story.append(Image('telstraLogo.png',width=0.4*inch, height=0.4*inch, hAlign='LEFT'))
    story.append(Paragraph('Agora Forms',styles['Title']))
    story.append(Spacer(0,20))

    story.append(Paragraph('Product Information',styles['Heading1']))
    for key in product_dict:
        story.append(Paragraph(f'<b>{key}:</b>',styles['Normal']))
        story.append(Paragraph(f'{product_dict[key]}',styles['Normal']))
        story.append(Spacer(0,5))

    story.append(Spacer(0,5))
    
    story.append(Paragraph('Promo Details',styles['Heading1']))
    for key in promo_dict:
        story.append(Paragraph(f'<b>{key}:</b>',styles['Normal']))
        story.append(Paragraph(f'{promo_dict[key]}',styles['Normal']))
        story.append(Spacer(0,5))

    
    pdf_doc = SimpleDocTemplate(pdf_buffer, pagesize=letter)
    pdf_doc.build(story)
    return pdf_buffer

def get_stories(story:list,styles:object,content_class:object)->list:
    content_dict = asdict(content_class)
    for key in content_dict:
        if not is_str_na(content_dict[key]):
            story.append(Paragraph(f'<b>{readiable_item(key)}:</b>',styles['Normal']))
            story.append(Spacer(0,5))
            if type(content_dict[key]) is list:
                for item in content_dict[key]:
                    story.append(Paragraph(f'- {item}', styles['Normal']))
            else:
                story.append(Paragraph(f'{content_dict[key]}',styles['Normal']))                
            story.append(Spacer(0,10))
    return story

def is_str_na(string:str):
    return string.__contains__('_NA')
        
def generate_pdf_file(product_info:object, promo_details:object):    
    pdf_buffer = BytesIO()
    styles = getSampleStyleSheet()
    story = []
    story.append(Image('telstraLogo.png',width=0.4*inch, height=0.4*inch, hAlign='LEFT'))
    story.append(Paragraph('Agora Promo Form',styles['Title']))
    story.append(Spacer(0,20))
    story.append(Paragraph('Product Information',styles['Heading1']))
    story = get_stories(story,styles,product_info)
    story.append(Spacer(0,5))
    story.append(Paragraph('Promo Details',styles['Heading1']))
    story = get_stories(story,styles,promo_details)
    #pdf_doc = SimpleDocTemplate("test_form_out.pdf", pagesize=A4)
    pdf_doc = SimpleDocTemplate(pdf_buffer, pagesize=A4)
    pdf_doc.build(story)
    return pdf_buffer

if "__main__" == __name__:
    prod_inf = ProductInfo()
    promo_det = PromoDetails()
    generate_pdf_file(prod_inf, promo_det)