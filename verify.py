import sys
import os

# Add current directory to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from services import generate_pdf
from models import InvoiceRequest, CompanyInfo, InvoiceInfo, ClientInfo, Transaction, Totals

data = {
    "companyInfo": {
        "name": "WALLET CAMBIOS",
        "website": "www.walletcambios.com",
        "email": "envios@walletcambios.com",
        "phone": "+58 414610 8166"
    },
    "invoiceInfo": {
        "invoiceNumber": "FAC-48",
        "date": "2026-01-20",
        "transactionNumber": "TRANSACCIÓN-143"
    },
    "clientInfo": {
        "senderName": "JOSE ARAPE Canal Mariadelsi",
        "document": "246810659"
    },
    "transactions": [
        {
            "originCountry": "VENEZUELA 🇻🇪",
            "destinationBank": "PAGOMOVIL BANESCO",
            "recipient": "DELIANNYS SCANDELA ",
            "reference": "060205290910",
            "amountSent": "21714,00 VES",
            "usdEquivalent": "55.00"
        }
    ],
    "totals": {
        "totalPayments": 1,
        "totalDeclaredAmount": "55 USD"
    }
}

try:
    req = InvoiceRequest(**data)
    pdf_bytes = generate_pdf(req)
    with open("invoice_test.pdf", "wb") as f:
        f.write(pdf_bytes)
    print("SUCCESS: PDF generated at invoice_test.pdf")
except Exception as e:
    print(f"ERROR: {e}")
    import traceback
    traceback.print_exc()
