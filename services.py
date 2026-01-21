import os
from weasyprint import HTML
from jinja2 import Environment, FileSystemLoader
from models import InvoiceRequest

def generate_pdf(data: InvoiceRequest) -> bytes:
    # Setup Jinja2 environment
    template_dir = os.path.join(os.path.dirname(__file__), 'templates')
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template('invoice.html')
    
    # Path to CSS
    static_dir = os.path.join(os.path.dirname(__file__), 'static')
    css_path = os.path.join(static_dir, 'style.css')
    
    # Path to Logo
    logo_path = os.path.join(template_dir, 'images', 'logo.png')

    # Render HTML
    # We pass 'css_path' and 'logo_path' as file:// URLs
    rendered_html = template.render(data=data, css_path=f"file://{css_path}", logo_path=f"file://{logo_path}")
    
    # Generate PDF
    # base_url is important for resolving relative paths if any
    pdf_bytes = HTML(string=rendered_html, base_url=template_dir).write_pdf()
    
    return pdf_bytes
