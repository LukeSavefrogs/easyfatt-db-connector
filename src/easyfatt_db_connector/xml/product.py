from dataclasses import dataclass
import lxml.etree as ET

from easyfatt_db_connector.xml.common import Field, XMLMapper


@dataclass(init=False)
class VatCode(XMLMapper):
    """ Informazioni sull'IVA applicata al prodotto. """
    __xml_mapping__ = {}
    
    code: str
    """ Codice IVA (deve essere già presente nella tabella "Categorie Iva" dell'applicazione). 
    
    Example:
        ```xml
        <Row>
            <VatCode>20</VatCode>
        </Row>
        ```
    """

    description: str
    """ Descrizione libera del codice Iva.
    
    Example:
        ```xml
        <Row>
            <VatCode Description="Aliquota 20%">...</VatCode>
        </Row>
        ```
    """

    percentage: str
    """ Percentuale tassazione applicata.
    
    Example:
        ```xml
        <Row>
            <VatCode Perc="20">...</VatCode>
        </Row>
        ```
    """

    vat_class: str
    """ Classe: imponibile, non imponibile, intra-ue, extra-ue, esente, escluso, fuori campo, iva non esposta, rev. charge.
    
    Example:
        ```xml
        <Row>
            <VatCode Class="Imponibile">...</VatCode>
        </Row>
        ```
    """

    @classmethod
    def from_xml(cls, xml: ET._Element) -> "VatCode":
        """ Costruisce un'istanza di VatCode da un elemento XML. """
        self = cls()
        
        self.code = xml.text
        self.description = xml.get("Description", None)
        self.percentage = xml.get("Perc", None)
        self.vat_class = xml.get("Class", None)

        return self



@dataclass(init=False, repr=False)
class Product(XMLMapper):
    """ Campi nelle righe del documento (elementi <Row>). """
    __xml_name__ = "Row"

    __xml_mapping__ = {
        "code": "Code",
        "supplier_code": "SupplierCode",
        "description": "Description",
        "quantity": "Qty",
        "unit_measure": "Um",
        "size": "Size",
        "color": "Color",
        "lot": "Lot",
        "expiry_date": "ExpiryDate",
        "serial": "Serial",
        "price": "Price",
        "discounts": "Discounts",
        "eco_fee": "EcoFee",
        "vat_info": Field(VatCode),
        "total": "Total",
        "withholding_tax": "WithholdingTax",
        "stock": "Stock",
        "notes": "Notes",
        "commission_percentage": "CommissionPerc",
    }

    code: str
    """ Codice prodotto.
    
    Example:
        ```xml
        <Row>
            <Code>...</Code>
        </Row>
        ```
    """

    supplier_code: str
    """ Codice prodotto del fornitore.
    
    Example:
        ```xml
        <Row>
            <SupplierCode>...</SupplierCode>
        </Row>
        ```
    """

    description: str
    """ Descrizione prodotto o nota.
    
    Example:
        ```xml
        <Row>
            <Description>...</Description>
        </Row>
        ```
    """

    quantity: int
    """ Quantità prodotti.
    
    Example:
        ```xml
        <Row>
            <Qty>...</Qty>
        </Row>
        ```
    """

    unit_measure: str
    """ Unità di misura della quantità.
    
    Example:
        ```xml
        <Row>
            <Um>...</Um>
        </Row>
        ```
    """

    size: str
    """ Taglia (usato nel settore dell'abbigliamento).
    
    Example:
        ```xml
        <Row>
            <Size>...</Size>
        </Row>
        ```
    """

    color: str
    """ Colore (usato nel settore dell'abbigliamento).
    
    Example:
        ```xml
        <Row>
            <Color>...</Color>
        </Row>
        ```
    """

    lot: str
    """ Lotto.
    
    Example:
        ```xml
        <Row>
            <Lot>...</Lot>
        </Row>
        ```
    """

    expiry_date: str
    """ Data scadenza lotto [Data].
    
    Example:
        ```xml
        <Row>
            <ExpiryDate>...</ExpiryDate>
        </Row>
        ```
    """

    serial: str
    """ Codice seriale
    
    Example:
        ```xml
        <Row>
            <Serial>...</Serial>
        </Row>
        ```
    """

    price: float
    """ Prezzo unitario [Valuta].
    
    Example:
        ```xml
        <Row>
            <Price>...</Price>
        </Row>
        ```
    """

    discounts: str
    """ Sconti (es: "20+5.5%").
    
    Example:
        ```xml
        <Row>
            <Discounts>...</Discounts>
        </Row>
        ```
    """

    eco_fee: str
    """ Importo dell'eco-contributo unitario associato all'articolo.
    
    Example:
        ```xml
        <Row>
            <EcoFee>...</EcoFee>
        </Row>
        ```
    """

    vat_info: "VatCode"
    """ Informazioni sull'IVA applicata al prodotto.
    
    Example:
        ```xml
        <Row>
            <VatCode>...</VatCode>
        </Row>
        ```
    """

    total: str
    """ Importo complessivo della riga [Valuta]. Ignorato in importazione.
    
    Example:
        ```xml
        <Row>
            <Total>...</Total>
        </Row>
        ```
    """

    withholding_tax: bool
    """ Ritenuta d'acconto applicata.
    
    Example:
        ```xml
        <Row>
            <WithholdingTax>false</WithholdingTax>
        </Row>
        ```
    """

    stock: bool
    """ Movimentazione magazzino.
    
    Example:
        ```xml
        <Row>
            <Stock>true</Stock>
        </Row>
        ```
    """

    notes: str
    """ Note della riga.
    
    Example:
        ```xml
        <Row>
            <Notes>...</Notes>
        </Row>
        ```
    """

    commission_percentage: float
    """ Percentuale provvigione agente.
    
    Example:
        ```xml
        <Row>
            <CommissionPerc>...</CommissionPerc>
        </Row>
        ```
    """


if __name__ == "__main__":
    xml = """
        <Row>
            <Code>0012</Code>
            <Description>Clip con catenella</Description>
            <Qty>10</Qty>
            <Um>pz</Um>
            <Price>4.62</Price>
            <Discounts/>
            <VatCode Perc="20">My20VAT</VatCode>
            <Total>46.2</Total>
            <Stock>false</Stock>
        </Row>
    """
     
    product = Product.from_xml_string(xml)
    print(f"Example of <Product> as object: {product}\n")
    print(f"Product description is        : {product.description}\n")
    print(f"Product VatCode is            : {product.vat_info}")
    print(f"Product VatCode percentage is : {product.vat_info.percentage}")
    print(f"Product VatCode codeID is     : {product.vat_info.code}")
    print(f"Product VatCode class is      : {product.vat_info.vat_class}\n")

    # TODO: fix this
    # print(f"Example of <Product> as XML   : {product.to_xml_string()}\n")