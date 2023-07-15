from dataclasses import dataclass
from typing import Literal, Optional

try:
    from typing import TypeAlias
except ImportError:
    from typing_extensions import TypeAlias

from easyfatt_db_connector.xml.product import Product
from easyfatt_db_connector.xml.common import Field, XMLMapper

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
