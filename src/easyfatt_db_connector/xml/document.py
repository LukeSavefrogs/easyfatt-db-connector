from dataclasses import dataclass
from typing import Literal, Optional

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


@dataclass(init=False, repr=False)
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
    """ Se "true", segnala che il pagamento è riferito ad un acconto. 
    
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
    
@dataclass(init=False, repr=False)
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

	name: str
	""" Nome e cognome o denominazione.
	
	Example:
		```xml
        <Document>
		    <DeliveryName>...</DeliveryName>
        </Document>
		```
	"""

	address: str
	""" Indirizzo.
	
	Example:
		```xml
        <Document>
		    <DeliveryAddress>...</DeliveryAddress>
        </Document>
		```
	"""

	postcode: str
	""" CAP.
	
	Example:
		```xml
        <Document>
		    <DeliveryPostcode>...</DeliveryPostcode>
        </Document>
		```
	"""

	city: str
	""" Città.
	
	Example:
		```xml
        <Document>
		    <DeliveryCity>...</DeliveryCity>
        </Document>
		```
	"""

	province: str
	""" Provincia (2 caratteri).
	
	Example:
		```xml
        <Document>
		    <DeliveryProvince>...</DeliveryProvince>
        </Document>
		```
	"""

	country: str
	""" Nazione.
	
	Example:
		```xml
        <Document>
		    <DeliveryCountry>...</DeliveryCountry>
        </Document>
		```
	"""

@dataclass(init=False, repr=False)
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

    carrier: str
    """ Denominazione vettore.

    Example:
        ```xml
        <Document>
            <Carrier>...</Carrier>
        </Document>
        ```
    """

    reason: str
    """ Causale trasporto.

    Example:
        ```xml
        <Document>
            <TransportReason>...</TransportReason>
        </Document>
        ```
    """

    goods_appearance: str
    """ Aspetto delle merci.

    Example:
        ```xml
        <Document>
            <GoodsAppearance>...</GoodsAppearance>
        </Document>
        ```
    """

    pieces: int
    """ Numero colli.

    Example:
        ```xml
        <Document>
            <NumOfPieces>...</NumOfPieces>
        </Document>
        ```
    """

    date_time: str
    """ Data e ora del trasporto.

    Example:
        ```xml
        <Document>
            <TransportDateTime>...</TransportDateTime>
        </Document>
        ```
    """

    shipment_terms: str
    """ Porto (franco, assegnato...).

    Example:
        ```xml
        <Document>
            <ShipmentTerms>...</ShipmentTerms>
        </Document>
        ```
    """

    weight: str
    """ Peso trasportato.

    Example:
        ```xml
        <Document>
            <TransportedWeight>...</TransportedWeight>
        </Document>
        ```
    """

    tracking_number: str
    """ Numero di tracciatura spedizione.

    Example:
        ```xml
        <Document>
            <TrackingNumber>...</TrackingNumber>
        </Document>
        ```
    """

@dataclass(init=False, repr=False)
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

    code: str
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

    web_login: str
    """ Login web del cliente (usato nell'integrazione e-commerce).
     
    Nella fase di identificazione dell'anagrafica, questo campo viene preso in considerazione solo in mancanza di `CustomerCode`.

    Example:
        ```xml
        <Document>
            <CustomerWebLogin>...</CustomerWebLogin>
        </Document>
        ```
    """

    name: str
    """ Cognome e nome o denominazione sociale.

    Example:
        ```xml
        <Document>
            <CustomerName>...</CustomerName>
        </Document>
        ```
    """

    address: str
    """ Indirizzo.

    Example:
        ```xml
        <Document>
            <CustomerAddress>...</CustomerAddress>
        </Document>
        ```
    """

    postcode: str
    """ CAP.

    Example:
        ```xml
        <Document>
            <CustomerPostcode>...</CustomerPostcode>
        </Document>
        ```
    """

    city: str
    """ Città.

    Example:
        ```xml
        <Document>
            <CustomerCity>...</CustomerCity>
        </Document>
        ```
    """

    province: str
    """ Provincia (2 caratteri).

    Example:
        ```xml
        <Document>
            <CustomerProvince>...</CustomerProvince>
        </Document>
        ```
    """

    country: str
    """ Nazione.

    Example:
        ```xml
        <Document>
            <CustomerCountry>...</CustomerCountry>
        </Document>
        ```
    """

    fiscal_code: str
    """ Codice fiscale.

    Example:
        ```xml
        <Document>
            <CustomerFiscalCode>...</CustomerFiscalCode>
        </Document>
        ```
    """

    vat_code: str
    """ Partita Iva.

    Example:
        ```xml
        <Document>
            <CustomerVatCode>...</CustomerVatCode>
        </Document>
        ```
    """

    e_invoice_dest_code: str
    """ Codice destinatario o PEC per l'invio della fattura elettronica.

    Example:
        ```xml
        <Document>
            <CustomerEInvoiceDestCode>...</CustomerEInvoiceDestCode>
        </Document>
        ```
    """

    telephone: str
    """ Numero di telefono.

    Example:
        ```xml
        <Document>
            <CustomerTel>...</CustomerTel>
        </Document>
        ```
    """

    mobile_phone: str
    """ Numero di cellulare.

    Example:
        ```xml
        <Document>
            <CustomerCellPhone>...</CustomerCellPhone>
        </Document>
        ```
    """

    fax: str
    """ Numero di fax.

    Example:
        ```xml
        <Document>
            <CustomerFax>...</CustomerFax>
        </Document>
        ```
    """

    email: str
    """ Indirizzo e-mail.

    Example:
        ```xml
        <Document>
            <CustomerEmail>...</CustomerEmail>
        </Document>
        ```
    """

    pec: str    
    """ Indirizzo PEC.

    Example:
        ```xml
        <Document>
            <CustomerPec>...</CustomerPec>
        </Document>
        ```
    """
    
    reference: str
    """ Persona di riferimento.

    Example:
        ```xml
        <Document>
            <CustomerReference>...</CustomerReference>
        </Document>
        ```
    """

@dataclass(init=False, repr=False)
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



@dataclass(init=False, repr=False)
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
    }

    rows: list["Product"]
    """ Lista dei prodotti o delle note contenute nel documento. 
    
    Example:
        ```xml
        <Rows>
            <Row>...</Row>
        </Rows>
        ```
    """

    payments: list["Payment"]
    """ Lista di scadenze di pagamento del documento.
    
    Example:
        ```xml
        <Payments>
            <Payment>...</Payment>
        </Payments>
        ```
    """

    date: str
    """ Data del documento. 
    
    Example:
        ```xml
        <Document>
            <Date>2010-03-23</Date>
        </Document>
        ```
    """

    number: str
    """ Numero del documento. 
    
    Example:
        ```xml
        <Document>
            <Number>4</Number>
        </Document>
        ```
    """

    numbering: Optional[str] = None
    """ Numerazione documento ( /a, /b, etc.). Se omesso, l'importazione userà la numerazione scelta nelle relative impostazioni.
    
    Example:
        ```xml
        <Document>
            <Numbering/>
        </Document>
        ```
    """

    type: Optional[DocumentType] = None
    """ Codice corrispondente al tipo di documento. Se `None`, il documento sarà considerato un ordine cliente. 
    
    Example:
        ```xml
        <Document>
            <DocumentType>C</DocumentType>
        </Document>
        ```
    """

    delivery: Optional[DeliveryInfo] = None
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

    transport: Optional[TransportInfo] = None
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

    customer: Optional[CustomerInfo] = None
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

    notes: Optional[DocumentNotes] = None
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
