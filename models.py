from typing import List, Optional
from pydantic import BaseModel

class CompanyInfo(BaseModel):
    name: str
    website: str
    email: str
    phone: str

class InvoiceInfo(BaseModel):
    invoiceNumber: str
    date: str
    transactionNumber: str

class ClientInfo(BaseModel):
    senderName: str
    document: str

class Transaction(BaseModel):
    originCountry: str
    destinationBank: str
    recipient: str
    reference: str
    amountSent: str
    usdEquivalent: Optional[str] = None

class Totals(BaseModel):
    totalPayments: int
    totalDeclaredAmount: str

class InvoiceRequest(BaseModel):
    companyInfo: CompanyInfo
    invoiceInfo: InvoiceInfo
    clientInfo: ClientInfo
    transactions: List[Transaction]
    totals: Totals
