from dataclasses import dataclass, field
from typing import Literal, Optional

from easyfatt_db_connector.xml.vat_code import VatCode

try:
    from typing import TypeAlias
except ImportError:
    from typing_extensions import TypeAlias

from easyfatt_db_connector.xml.product import Product
from easyfatt_db_connector.xml.common import Field, FieldGroup, XMLMapper

DocumentType: TypeAlias = Literal[
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
]


@dataclass(eq=False, init=False, repr=False)
class Payment(XMLMapper):
    """Campi nelle righe di pagamento (elementi `<Payment>`)."""
    __xml_name__ = "Payment"

    __xml_mapping__ = {
        "advance": "Advance",
        "amount": "Amount",
        "date": "Date",
        "paid": "Paid",
    }

    advance: bool
    """ Se `true`, segnala che il pagamento è riferito ad un acconto.
    
    Example:
        ```xml
        <Payment>
            <Advance>false</Advance>
        </Payment>
        ```
    """

    amount: float
    """ Importo [Valuta].
    
    Example:
        ```xml
        <Payment>
            <Amount>100</Amount>
        </Payment>
        ```
    """

    date: str
    """ Data [Data].
    
    Example:
        ```xml
        <Payment>
            <Date>2010-01-31</Date>
        </Payment>
        ```
    """

    paid: bool
    """ Se "true", significa che il pagamento è stato eseguito.
    
    Example:
        ```xml
        <Payment>
            <Paid>false</Paid>
        </Payment>
        ```
    """
    
@dataclass(eq=False, init=False, repr=False)
class DeliveryInfo(XMLMapper):
	""" Campi nelle righe di consegna (elementi `<Delivery*>`).
    
    I campi "Delivery" si riferiscono all'indirizzo di consegna o spedizione e
	vanno specificati se tale indirizzo differisce da quello nei precedenti campi "Customer".
	"""
    
	__xml_name__ = ""
        
	__xml_mapping__ = {
		"name": "DeliveryName",
		"address": "DeliveryAddress",
		"postcode": "DeliveryPostcode",
		"city": "DeliveryCity",
		"province": "DeliveryProvince",
		"country": "DeliveryCountry",
	}

	name: str = ""
	""" Nome e cognome o denominazione.
	
	Example:
		```xml
        <Document>
		    <DeliveryName>...</DeliveryName>
        </Document>
		```
	"""

	address: str = ""
	""" Indirizzo.
	
	Example:
		```xml
        <Document>
		    <DeliveryAddress>...</DeliveryAddress>
        </Document>
		```
	"""

	postcode: str = ""
	""" CAP.
	
	Example:
		```xml
        <Document>
		    <DeliveryPostcode>...</DeliveryPostcode>
        </Document>
		```
	"""

	city: str = ""
	""" Città.
	
	Example:
		```xml
        <Document>
		    <DeliveryCity>...</DeliveryCity>
        </Document>
		```
	"""

	province: str = ""
	""" Provincia (2 caratteri).
	
	Example:
		```xml
        <Document>
		    <DeliveryProvince>...</DeliveryProvince>
        </Document>
		```
	"""

	country: str = ""
	""" Nazione.
	
	Example:
		```xml
        <Document>
		    <DeliveryCountry>...</DeliveryCountry>
        </Document>
		```
	"""

@dataclass(eq=False, init=False, repr=False)
class TransportInfo(XMLMapper):
    """ Campi nelle righe di trasporto (elementi `<Transport*>`, `<Shipment>`, ecc). """

    __xml_mapping__ = {
        "carrier": "Carrier",
        "reason": "TransportReason",
        "goods_appearance": "GoodsAppearance",
        "pieces": "NumOfPieces",
        "date_time": "TransportDateTime",
        "shipment_terms": "ShipmentTerms",
        "weight": "TransportedWeight",
        "tracking_number": "TrackingNumber",
    }

    carrier: str = ""
    """ Denominazione vettore.

    Example:
        ```xml
        <Document>
            <Carrier>...</Carrier>
        </Document>
        ```
    """

    reason: str = ""
    """ Causale trasporto.

    Example:
        ```xml
        <Document>
            <TransportReason>...</TransportReason>
        </Document>
        ```
    """

    goods_appearance: str = ""
    """ Aspetto delle merci.

    Example:
        ```xml
        <Document>
            <GoodsAppearance>...</GoodsAppearance>
        </Document>
        ```
    """

    pieces: str = "0"
    """ Numero colli.

    Example:
        ```xml
        <Document>
            <NumOfPieces>...</NumOfPieces>
        </Document>
        ```
    """

    date_time: str = ""
    """ Data e ora del trasporto.

    Example:
        ```xml
        <Document>
            <TransportDateTime>...</TransportDateTime>
        </Document>
        ```
    """

    shipment_terms: str = ""
    """ Porto (franco, assegnato...).

    Example:
        ```xml
        <Document>
            <ShipmentTerms>...</ShipmentTerms>
        </Document>
        ```
    """

    weight: str = "0"
    """ Peso trasportato.

    Example:
        ```xml
        <Document>
            <TransportedWeight>...</TransportedWeight>
        </Document>
        ```
    """

    tracking_number: str = ""
    """ Numero di tracciatura spedizione.

    Example:
        ```xml
        <Document>
            <TrackingNumber>...</TrackingNumber>
        </Document>
        ```
    """

@dataclass(eq=False, init=False, repr=False)
class CustomerInfo(XMLMapper):
    """ Campi del'intestatario del documento. 
    
    Va notato che i campi "Customer" (ovvero ... "Cliente") conterranno invece i dati del fornitore per i documenti di fornitura (ordine cliente, arrivo merce, etc.).
    """

    __xml_mapping__ = {
        "code": "CustomerCode",
        "web_login": "CustomerWebLogin",
        "name": "CustomerName",
        "address": "CustomerAddress",
        "postcode": "CustomerPostcode",
        "city": "CustomerCity",
        "province": "CustomerProvince",
        "country": "CustomerCountry",
        "fiscal_code": "CustomerFiscalCode",
        "vat_code": "CustomerVatCode",
        "e_invoice_dest_code": "CustomerEInvoiceDestCode",
        "telephone": "CustomerTel",
        "mobile_phone": "CustomerCellPhone",
        "fax": "CustomerFax",
        "email": "CustomerEmail",
        "pec": "CustomerPec",
        "reference": "CustomerReference",
    }

    code: str = ""
    """ Codice anagrafica; serve per associare l'ordine all'eventuale cliente già inserito in anagrafica. 
    
    Durante l'importazione, in presenza di `<CustomerCode>` e in assenza altri codici `<Customer...>`, 
    i relativi campi anagrafica del documento saranno riempiti con i dati dell'anagrafica corrispondente 
    a `<CustomerCode>` e già codificata nell'archivio.

    Example:
        ```xml
        <Document>
            <CustomerCode>...</CustomerCode>
        </Document>
        ```
    """

    web_login: str = ""
    """ Login web del cliente (usato nell'integrazione e-commerce).
     
    Nella fase di identificazione dell'anagrafica, questo campo viene preso in considerazione solo in mancanza di `CustomerCode`.

    Example:
        ```xml
        <Document>
            <CustomerWebLogin>...</CustomerWebLogin>
        </Document>
        ```
    """

    name: str = ""
    """ Cognome e nome o denominazione sociale.

    Example:
        ```xml
        <Document>
            <CustomerName>...</CustomerName>
        </Document>
        ```
    """

    address: str = ""
    """ Indirizzo.

    Example:
        ```xml
        <Document>
            <CustomerAddress>...</CustomerAddress>
        </Document>
        ```
    """

    postcode: str = ""
    """ CAP.

    Example:
        ```xml
        <Document>
            <CustomerPostcode>...</CustomerPostcode>
        </Document>
        ```
    """

    city: str = ""
    """ Città.

    Example:
        ```xml
        <Document>
            <CustomerCity>...</CustomerCity>
        </Document>
        ```
    """

    province: str = ""
    """ Provincia (2 caratteri).

    Example:
        ```xml
        <Document>
            <CustomerProvince>...</CustomerProvince>
        </Document>
        ```
    """

    country: str = ""
    """ Nazione.

    Example:
        ```xml
        <Document>
            <CustomerCountry>...</CustomerCountry>
        </Document>
        ```
    """

    fiscal_code: str = ""
    """ Codice fiscale.

    Example:
        ```xml
        <Document>
            <CustomerFiscalCode>...</CustomerFiscalCode>
        </Document>
        ```
    """

    vat_code: str = ""
    """ Partita Iva.

    Example:
        ```xml
        <Document>
            <CustomerVatCode>...</CustomerVatCode>
        </Document>
        ```
    """

    e_invoice_dest_code: str = ""
    """ Codice destinatario o PEC per l'invio della fattura elettronica.

    Example:
        ```xml
        <Document>
            <CustomerEInvoiceDestCode>...</CustomerEInvoiceDestCode>
        </Document>
        ```
    """

    telephone: str = ""
    """ Numero di telefono.

    Example:
        ```xml
        <Document>
            <CustomerTel>...</CustomerTel>
        </Document>
        ```
    """

    mobile_phone: str = ""
    """ Numero di cellulare.

    Example:
        ```xml
        <Document>
            <CustomerCellPhone>...</CustomerCellPhone>
        </Document>
        ```
    """

    fax: str = ""
    """ Numero di fax.

    Example:
        ```xml
        <Document>
            <CustomerFax>...</CustomerFax>
        </Document>
        ```
    """

    email: str = ""
    """ Indirizzo e-mail.

    Example:
        ```xml
        <Document>
            <CustomerEmail>...</CustomerEmail>
        </Document>
        ```
    """

    pec: str = ""
    """ Indirizzo PEC.

    Example:
        ```xml
        <Document>
            <CustomerPec>...</CustomerPec>
        </Document>
        ```
    """
    
    reference: str = ""
    """ Persona di riferimento.

    Example:
        ```xml
        <Document>
            <CustomerReference>...</CustomerReference>
        </Document>
        ```
    """

@dataclass(eq=False, init=False, repr=False)
class DocumentNotes(XMLMapper):
    """ Campi note/commenti del documento. """

    __xml_mapping__ = {
        "internal_comment": "InternalComment",
        "custom1": "CustomField1",
        "custom2": "CustomField2",
        "custom3": "CustomField3",
        "custom4": "CustomField4",
        "foot_note": "FootNotes",
    }

    internal_comment: str = ""
    """ Commento (nell'e-commerce, usare questo campo per indicare note libere dell'acquirente durante la fase dell'ordine).

    Example:
        ```xml
        <Document>
            <InternalComment>...</InternalComment>
        </Document>
        ```
    """

    custom1: str = ""
    """ Campo note 1.

    Example:
        ```xml
        <Document>
            <CustomField1>...</CustomField1>
        </Document>
        ```
    """

    custom2: str = ""
    """ Campo note 2.

    Example:
        ```xml
        <Document>
            <CustomField2>...</CustomField2>
        </Document>
        ```
    """

    custom3: str = ""
    """ Campo note 3.

    Example:
        ```xml
        <Document>
            <CustomField3>...</CustomField3>
        </Document>
        ```
    """

    custom4: str = ""
    """ Campo note 4.

    Example:
        ```xml
        <Document>
            <CustomField4>...</CustomField4>
        </Document>
        ```
    """

    foot_note: str = ""
    """ Note a fine pagina.

    Example:
        ```xml
        <Document>
            <FootNotes>...</CustomerCode>
        </Document>
        ```
    """

@dataclass(eq=False, init=False, repr=False)
class WithholdingTax(XMLMapper):
    """ Campi ritenute d'acconto. """

    __xml_mapping__ = {
        "rate1": "WithholdingTaxPerc",
        "rate2": "WithholdingTaxPerc2",
        "amount": "WithholdingTaxAmount",
        "amount_extras": "WithholdingTaxAmountB",
        "name_extras": "WithholdingTaxNameB",
    }

    rate1: float = 0
    """ Percentuale ritenuta d'acconto applicata [Numerico].
    
    Example:
        ```xml
        <Document>
            <WithholdingTaxPerc>...</WithholdingTaxPerc>
        </Document>
        ```
    """

    rate2: float = 0
    """ Seconda percentuale della ritenuta d'acconto (es.: 20% del 50%) [Numerico].
    
    Example:
        ```xml
        <Document>
            <WithholdingTaxPerc2>...</WithholdingTaxPerc2>
        </Document>
        ```
    """

    amount: float = 0
    """ Totale ritenuta d'acconto calcolata nel documento [Valuta]. Ignorato in importazione.
    
    Example:
        ```xml
        <Document>
            <WithholdingTaxAmount>...</WithholdingTaxAmount>
        </Document>
        ```
    """

    amount_extras: float = 0
    """ Totale altre ritenute (es.: Enasarco) [Valuta]. Ignorato in importazione.
    
    Example:
        ```xml
        <Document>
            <WithholdingTaxAmountB>...</WithholdingTaxAmountB>
        </Document>
        ```
    """

    name_extras: str = ""
    """ Descrizione altre ritenute (es.: "Ritenuta ENASARCO").
    
    Example:
        ```xml
        <Document>
            <WithholdingTaxNameB>...</WithholdingTaxNameB>
        </Document>
        ```
    """


@dataclass(eq=False, init=False, repr=False)
class Contributions(XMLMapper):
    """ Campi contributi previdenziali. """

    __xml_mapping__ = {
        "description": "ContribDescription",
        "percentage": "ContribPerc",
        "is_subject_to_withholding_tax": "ContribSubjectToWithholdingTax",
        "total": "ContribAmount",
        "vat_code": "ContribVatCode",
    }

    description: str = ""
    """ Descrizione contributi previdenziali.
    
    Example:
        ```xml
        <Document>
            <ContribDescription>...</ContribDescription>
        </Document>
        ```
    """
    
    percentage: float = 0
    """ Percentuale contributi previdenziali.
    
    Example:
        ```xml
        <Document>
            <ContribPerc>...</ContribPerc>
        </Document>
        ```
    """
    
    is_subject_to_withholding_tax: bool = False
    """ Contributi previdenziali soggetti a ritenuta d'acconto [true|false].
    
    Example:
        ```xml
        <Document>
            <ContribSubjectToWithholdingTax>false</ContribSubjectToWithholdingTax>
        </Document>
        ```
    """
    
    total: float = 0
    """ Ammontare contributi previdenziali. Ignorato in importazione.
    
    Example:
        ```xml
        <Document>
            <ContribAmount>...</ContribAmount>
        </Document>
        ```
    """
    
    vat_code: int = 0
    """ Aliquota Iva contributi previdenziali. Ignorato in importazione.
    
    Example:
        ```xml
        <Document>
            <ContribVatCode>...</ContribVatCode>
        </Document>
        ```
    """


@dataclass(eq=False, init=False, repr=False)
class DocumentPDFFile(XMLMapper):
    """ Campo `<Pdf>`. """

    __xml_name__ = "Pdf"
    __xml_mapping__ = {
        "filename": "@FileName",
        "content": "#TEXT",
    }

    filename: str = ""
    """ Nome file PDF. 
    
    Example:
        ```xml
        <Document>
            <Pdf FileName="..."></Pdf>
        </Document>
        ```
    """

    content: str = ""
    """ Contenuto file codificato in base64.
    
    Example:
        ```xml
        <Document>
            <Pdf>...</Pdf>
        </Document>
        ```
    """
    

@dataclass(eq=False, init=False, repr=False)
class Document(XMLMapper):
    """ Dati del documento corrente (elementi `<Document>`).

    Fonte: https://www.danea.it/software/easyfatt/xml/documenti/#section-124
    """

    __xml_mapping__ = {
        "date": "Date",
        "number": "Number",
        "rows": Field(tag="Rows", is_parent=True, child=Field(Product)),
        "payments": Field(tag="Payments", is_parent=True, child=Field(Payment)),
        "numbering": "Numbering",
        "type": "DocumentType",

        "delivery": FieldGroup(DeliveryInfo),
        "transport": FieldGroup(TransportInfo),
        "customer": FieldGroup(CustomerInfo),
        "notes": FieldGroup(DocumentNotes),

        "cost_description": "CostDescription",
        "cost_vat_code": Field(VatCode, tag="CostVatCode"),
        "cost_amount": "CostAmount",

        "total_without_tax": "TotalWithoutTax",
        "total_vat": "VatAmount",
        "total": "Total",
        "total_paid": "PaymentAdvanceAmount",
        
        "prices_include_vat": "PricesIncludeVat",
        "total_subject_to_withholding_tax": "TotalSubjectToWithholdingTax",

        "withholding_tax": FieldGroup(WithholdingTax),
        "contributions": FieldGroup(Contributions),

        # ----------------------------------

        "delayed_vat": "DelayedVat",
        "delayed_vat_description": "DelayedVatDesc",
        "delayed_vat_dueWithinOneYear": "DelayedVatDueWithinOneYear",


        "warehouse": "Warehouse",
        "price_list": "PriceList",
        "payment_name": "PaymentName",
        "payment_bank": "PaymentBank",
        "sales_agent": "SalesAgent",
        "expected_conclusion": "ExpectedConclusionDate",
        "reference": "DocReference",
        "pdf": Field(DocumentPDFFile, tag="Pdf"),
    }

    rows: list["Product"] = field(default_factory=list)
    """ Lista dei prodotti o delle note contenute nel documento. 
    
    Example:
        ```xml
        <Rows>
            <Row>...</Row>
        </Rows>
        ```
    """

    payments: list["Payment"] = field(default_factory=list)
    """ Lista di scadenze di pagamento del documento.
    
    Example:
        ```xml
        <Payments>
            <Payment>...</Payment>
        </Payments>
        ```
    """

    date: str = ""
    """ Data del documento. 
    
    Example:
        ```xml
        <Document>
            <Date>2010-03-23</Date>
        </Document>
        ```
    """

    number: str = ""
    """ Numero del documento. 
    
    Example:
        ```xml
        <Document>
            <Number>4</Number>
        </Document>
        ```
    """

    numbering: Optional[str] = ""
    """ Numerazione documento ( /a, /b, etc.). Se omesso, l'importazione userà la numerazione scelta nelle relative impostazioni.
    
    Example:
        ```xml
        <Document>
            <Numbering/>
        </Document>
        ```
    """

    type: Optional[DocumentType] = "C"
    """ Codice corrispondente al tipo di documento. Se `None`, il documento sarà considerato un ordine cliente. 
    
    Example:
        ```xml
        <Document>
            <DocumentType>C</DocumentType>
        </Document>
        ```
    """

    delivery: DeliveryInfo = field(default_factory=DeliveryInfo)
    """ Informazioni aggiuntive sulla consegna o spedizione.

    Example:
        ```xml
        <Document>
            <DeliveryName>...</DeliveryName>
            <DeliveryAddress>...</DeliveryAddress>
            <DeliveryPostcode>...</DeliveryPostcode>
            <DeliveryCity>...</DeliveryCity>
            <DeliveryProvince>...</DeliveryProvince>
            <DeliveryCountry>...</DeliveryCountry>
        </Document>
        ```
    """

    transport: TransportInfo = field(default_factory=TransportInfo)
    """ Informazioni aggiuntive sul trasporto.

    Example:
        ```xml
        <Document>
            <Carrier>...</Carrier>
            <TransportReason>...</TransportReason>
            <GoodsAppearance>...</GoodsAppearance>
            <NumOfPieces>...</NumOfPieces>
            <TransportDateTime>...</TransportDateTime>
            <ShipmentTerms>...</ShipmentTerms>
            <TransportedWeight>...</TransportedWeight>
            <TrackingNumber>...</TrackingNumber>
        </Document>
        ```
    """

    customer: CustomerInfo = field(default_factory=CustomerInfo)
    """ Informazioni aggiuntive sull'intestatario del documento.
    
    Questo può essere cliente o fornitore a seconda del tipo di documento.

    Example:
        ```xml
        <Document>
            <CustomerCode>...</CustomerCode>
            <CustomerWebLogin>...</CustomerWebLogin>
            <CustomerName>...</CustomerName>
            <CustomerAddress>...</CustomerAddress>
            <CustomerVatCode>...</CustomerVatCode>
            <CustomerEmail>...</CustomerEmail>
        </Document>
        ```
    """

    notes: DocumentNotes = field(default_factory=DocumentNotes)
    """ Note aggiuntive sul documento.

    Example:
        ```xml
        <Document>
            <InternalComment>...</InternalComment>
            <CustomField1>...</CustomField1>
            <CustomField2>...</CustomField2>
            <CustomField3>...</CustomField3>
            <CustomField4>...</CustomField4>
            <FootNotes>...</FootNotes>
        </Document>
        ```
    """

    cost_description: Optional[str] = None
    """ Descrizione spese aggiuntive (ad esempio per spese di trasporto).

    Example:
        ```xml
        <Document>
            <CostDescription>...</CostDescription>
        </Document>
        ```
    """

    cost_vat_code: VatCode = field(default_factory=VatCode)
    """ Codice IVA spese aggiuntive (deve essere già presente nella tabella "Categorie Iva" dell'applicazione).
    
    Il codice è accompagnato dalle seguenti proprietà, il cui uso è facoltativo:
    - `Perc` (percentuale di tassazione applicata)
    - `Class` (classe: imponibile, non imponibile, intra-ue, extra-ue, esente, escluso, fuori campo, iva non esposta, rev. charge)
    - `Description`: descrizione libera del codice Iva

    Example:
        ```xml
        <Document>
            <CostVatCode>...</CostVatCode>
        </Document>
        ```
    """

    cost_amount: Optional[float] = 0
    """ Importo spese aggiuntive.

    Example:
        ```xml
        <Document>
            <CostAmount>...</CostAmount>
        </Document>
        ```
    """

    total_without_tax: Optional[float] = 0
    """ Totale documento al netto dell'imposta IVA [Valuta]. Ignorato in fase di importazione.

    Example:
        ```xml
        <Document>
            <TotalWithoutTax>...</TotalWithoutTax>
        </Document>
        ```
    """

    total_vat: Optional[float] = 0
    """ Totale Iva calcolata [Valuta]. Ignorato in importazione.

    Example:
        ```xml
        <Document>
            <VatAmount>...</VatAmount>
        </Document>
        ```
    """

    total: float = 0
    """ Totale documento [Valuta]. Ignorato in importazione.

    Example:
        ```xml
        <Document>
            <Total>...</Total>
        </Document>
        ```
    """

    total_paid: float = 0
    """ Importo acconto già versato (va usato solo nei documenti che non prevedono l'indicazione dei singoli Payment).

    Example:
        ```xml
        <Document>
            <TotalPaid>...</TotalPaid>
        </Document>
        ```
    """

    prices_include_vat: Optional[bool] = None
    """ Se "true" i campi CostAmount e Row.Price vengono considerati importi ivati, altrimenti netti [true|false].

    Example:
        ```xml
        <Document>
            <PricesIncludeVat>true</PricesIncludeVat>
        </Document>
        ```
    """

    total_subject_to_withholding_tax: float = 0
    """ Totale imponibile per ritenuta d'acconto [Numerico].

    Example:
        ```xml
        <Document>
            <TotalSubjectToWithholdingTax>...</TotalSubjectToWithholdingTax>
        </Document>
        ```
    """

    withholding_tax: WithholdingTax = field(default_factory=WithholdingTax)
    """ Informazioni sulla ritenuta d'acconto. """

    contributions: Contributions = field(default_factory=Contributions)
    """ Informazioni sui contributi previdenziali. """

    # ----------------------------------

    delayed_vat: Optional[bool] = None
    """ Iva ad esigibilità differita [true|false].

    Example:
        ```xml
        <Document>
            <DelayedVat>...</DelayedVat>
        </Document>
        ```
    """

    delayed_vat_description: str = ""
    """ Causale Iva ad esigibilità differita.

    Example:
        ```xml
        <Document>
            <DelayedVatDesc>...</DelayedVatDesc>
        </Document>
        ```
    """

    delayed_vat_dueWithinOneYear: Optional[bool] = None
    """ Iva ad esigibilità differita comunque dovuta dopo un anno [true|false].

    Example:
        ```xml
        <Document>
            <DelayedVatDueWithinOneYear>...</DelayedVatDueWithinOneYear>
        </Document>
        ```
    """


    warehouse: str = ""
    """ Denominazione del magazzino movimentato.

    Example:
        ```xml
        <Document>
            <Warehouse>...</Warehouse>
        </Document>
        ```
    """

    price_list: str = ""
    """ Denominazione del listino prezzi usato.

    Example:
        ```xml
        <Document>
            <PriceList>...</PriceList>
        </Document>
        ```
    """


    payment_name: str = ""
    """ Nome pagamento (deve essere già presente nella tabella "Tipi pagamento" di Easyfatt).

    Example:
        ```xml
        <Document>
            <PaymentName>...</PaymentName>
        </Document>
        ```
    """

    payment_bank: str = ""
    """ Banca pagamento.

    Example:
        ```xml
        <Document>
            <PaymentBank>...</PaymentBank>
        </Document>
        ```
    """

    sales_agent: str = ""
    """ Nome dell'agente venditore (deve corrispondere ad un nominativo già presente nella tabella degli agenti).

    Example:
        ```xml
        <Document>
            <SalesAgent>...</SalesAgent>
        </Document>
        ```
    """

    expected_conclusion: str = "2999-12-31"
    """ Data di conclusione prevista (usato esclusivamente negli ordini clienti e fornitori) [Data].

    Example:
        ```xml
        <Document>
            <ExpectedConclusionDate>...</ExpectedConclusionDate>
        </Document>
        ```
    """

    reference: str = ""
    """ Causale del documento.
    
    Example:
        ```xml
        <Document>
            <DocReference>...</DocReference>
        </Document>
        ```
    """

    pdf: DocumentPDFFile = field(default_factory=DocumentPDFFile)
    """ Documento in formato Pdf condificato Base64.

    Example:
        ```xml
        <Document>
            <Pdf>...</Pdf>
        </Document>
        ```
    """

    # def __init__(
    #     self,
    #     date: str,
    #     number: str,
    #     rows: list[Product] = [],
    #     payments: list["Payment"] = [],
    #     numbering: Optional[str] = None,
    #     type: Optional[DocumentType] = None,
    # ):
    #     self.date = date
    #     self.number = number
    #     self.rows = rows
    #     self.payments = payments
    #     self.numbering = numbering
    #     self.type = type


if __name__ == "__main__":
    xml = """
        <Document>
            <CustomerCode>0058</CustomerCode>
            <CustomerWebLogin/>
            <CustomerName>Amici del Gioco</CustomerName>
            <CustomerAddress>Via Ctr. Di Suio, 56</CustomerAddress>
            <CustomerPostcode>04021</CustomerPostcode>
            <CustomerCity>Castelforte</CustomerCity>
            <CustomerProvince>LT</CustomerProvince>
            <CustomerCountry/>
            <CustomerVatCode>66982157196</CustomerVatCode>
            <CustomerTel>0771 656890</CustomerTel>
            <DocumentType>I</DocumentType>
            <Warehouse>Principale</Warehouse>
            <Date>2009-02-28</Date>
            <Number>72</Number>
            <Numbering/>
            <CostDescription/>
            <CostVatCode/>
            <CostAmount/>
            <TotalWithoutTax>511.6</TotalWithoutTax>
            <VatAmount>102.32</VatAmount>
            <WithholdingTaxAmount>0</WithholdingTaxAmount>
            <Total>613.92</Total>
            <PriceList>Privati</PriceList>
            <PricesIncludeVat>false</PricesIncludeVat>
            <WithholdingTaxPerc>0</WithholdingTaxPerc>
            <PaymentName>Bonifico 30-60 gg F.M.</PaymentName>
            <PaymentBank>Cassa di Risparmio - IBAN IT83 H062 2562 9610 7404 2366 76W</PaymentBank>
            <Payments>
                <Payment>
                    <Advance>false</Advance>
                    <Date>2009-03-31</Date>
                    <Amount>306.96</Amount>
                    <Paid>true</Paid>
                </Payment>
                <Payment>
                    <Advance>false</Advance>
                    <Date>2009-04-30</Date>
                    <Amount>306.96</Amount>
                    <Paid>true</Paid>
                </Payment>
            </Payments>
            <InternalComment/>
            <CustomField1/>
            <CustomField2/>
            <CustomField3/>
            <CustomField4/>
            <FootNotes/>
            <SalesAgent/>
            <Rows>
                <Row>
                    <Code>0011</Code>
                    <Description>Anello refrigerante</Description>
                    <Qty>5</Qty>
                    <Um>pz</Um>
                    <Price>5.24</Price>
                    <Discounts/>
                    <VatCode>20</VatCode>
                    <Total>26.2</Total>
                    <Stock>false</Stock>
                </Row>
                <Row>
                    <Code>0010</Code>
                    <Description>Bicchiere antigoccia</Description>
                    <Qty>5</Qty>
                    <Um>pz</Um>
                    <Price>4.26</Price>
                    <Discounts/>
                    <VatCode>20</VatCode>
                    <Total>21.3</Total>
                    <Stock>false</Stock>
                </Row>
                <Row>
                    <Code>0009</Code>
                    <Description>Cucchiaio silicone</Description>
                    <Qty>5</Qty>
                    <Um>pz</Um>
                    <Price>3.06</Price>
                    <Discounts/>
                    <VatCode>20</VatCode>
                    <Total>15.3</Total>
                    <Stock>false</Stock>
                </Row>
                <Row>
                    <Code>0008</Code>
                    <Description>Seggiolone</Description>
                    <Qty>2</Qty>
                    <Um>pz</Um>
                    <Price>130.56</Price>
                    <Discounts/>
                    <VatCode>20</VatCode>
                    <Total>261.12</Total>
                    <Stock>false</Stock>
                </Row>
                <Row>
                    <Code>0007</Code>
                    <Description>Seggiolino da tavolo</Description>
                    <Qty>2</Qty>
                    <Um>pz</Um>
                    <Price>66.64</Price>
                    <Discounts/>
                    <VatCode>20</VatCode>
                    <Total>133.28</Total>
                    <Stock>false</Stock>
                </Row>
                <Row>
                    <Code>0006</Code>
                    <Description>Posatine</Description>
                    <Qty>5</Qty>
                    <Um>pz</Um>
                    <Price>10.88</Price>
                    <Discounts/>
                    <VatCode>20</VatCode>
                    <Total>54.4</Total>
                    <Stock>false</Stock>
                </Row>
            </Rows>
        </Document>
    """
    
    document = Document.from_xml_string(xml)
    print(f"Example of <Document> as object: {document}\n")
    print(f"Document number is             : {document.number}\n")
    print(f"Document VatCode is            : {document.date}")
    print(f"Document VatCode percentage is : {document.type}")
    print(f"Document first product is      : {document.rows[0].description}")
    print(f"Document first payment is      : {document.payments[0].amount}\n")

    print(f"Same object              : {document == document}")
    unique_documents = set([document, document])
    print(f"Count of unique documents: {len(unique_documents)}")

    document2 = Document.from_xml_string(xml)
    document.number = "TEST2"

    print(f"Same object              : {document == document2}")
    unique_documents = set([document, document, document2])
    print(f"Count of unique documents: {len(unique_documents)}")