from dataclasses import dataclass
from typing import Optional
import lxml.etree as ET

from easyfatt_db_connector.xml.common import Field, XMLMapper
from easyfatt_db_connector.xml.vat_code import VatCode


@dataclass(eq=False, init=False, repr=False)
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
        "vat_info": Field(VatCode, tag="VatCode"),
        "total": "Total",
        "withholding_tax": "WithholdingTax",
        "stock": "Stock",
        "notes": "Notes",
        "commission_percentage": "CommissionPerc",
    }

    code: str = ""
    """ Codice prodotto.
    
    Example:
        ```xml
        <Row>
            <Code>...</Code>
        </Row>
        ```
    """

    supplier_code: str = ""
    """ Codice prodotto del fornitore.
    
    Example:
        ```xml
        <Row>
            <SupplierCode>...</SupplierCode>
        </Row>
        ```
    """

    description: str = ""
    """ Descrizione prodotto o nota.
    
    Example:
        ```xml
        <Row>
            <Description>...</Description>
        </Row>
        ```
    """

    # I know it's strange, but in the XML schema the default is 0: 
    # `<xs:element name="Qty" type="xs:decimal" minOccurs="0" default="0"/>`
    quantity: int = 0
    """ Quantità prodotti.
    
    Example:
        ```xml
        <Row>
            <Qty>...</Qty>
        </Row>
        ```
    """

    unit_measure: str = ""
    """ Unità di misura della quantità.
    
    Example:
        ```xml
        <Row>
            <Um>...</Um>
        </Row>
        ```
    """

    size: str = ""
    """ Taglia (usato nel settore dell'abbigliamento).
    
    Example:
        ```xml
        <Row>
            <Size>...</Size>
        </Row>
        ```
    """

    color: str = ""
    """ Colore (usato nel settore dell'abbigliamento).
    
    Example:
        ```xml
        <Row>
            <Color>...</Color>
        </Row>
        ```
    """

    lot: str = ""
    """ Lotto.
    
    Example:
        ```xml
        <Row>
            <Lot>...</Lot>
        </Row>
        ```
    """

    expiry_date: str = "2999-12-31"
    """ Data scadenza lotto [Data].
    
    Example:
        ```xml
        <Row>
            <ExpiryDate>...</ExpiryDate>
        </Row>
        ```
    """

    serial: str = ""
    """ Codice seriale
    
    Example:
        ```xml
        <Row>
            <Serial>...</Serial>
        </Row>
        ```
    """

    price: float = 0
    """ Prezzo unitario [Valuta].
    
    Example:
        ```xml
        <Row>
            <Price>...</Price>
        </Row>
        ```
    """

    discounts: str = ""
    """ Sconti (es: "20+5.5%").
    
    Example:
        ```xml
        <Row>
            <Discounts>...</Discounts>
        </Row>
        ```
    """

    eco_fee: float = 0
    """ Importo dell'eco-contributo unitario associato all'articolo.
    
    Example:
        ```xml
        <Row>
            <EcoFee>...</EcoFee>
        </Row>
        ```
    """

    vat_info: Optional["VatCode"] = None
    """ Informazioni sull'IVA applicata al prodotto.
    
    Example:
        ```xml
        <Row>
            <VatCode>...</VatCode>
        </Row>
        ```
    """

    total: str = ""
    """ Importo complessivo della riga [Valuta]. Ignorato in importazione.
    
    Example:
        ```xml
        <Row>
            <Total>...</Total>
        </Row>
        ```
    """

    withholding_tax: Optional[bool] = None
    """ Ritenuta d'acconto applicata.
    
    Example:
        ```xml
        <Row>
            <WithholdingTax>false</WithholdingTax>
        </Row>
        ```
    """

    stock: Optional[bool] = None
    """ Movimentazione magazzino.
    
    Example:
        ```xml
        <Row>
            <Stock>true</Stock>
        </Row>
        ```
    """

    notes: str = ""
    """ Note della riga.
    
    Example:
        ```xml
        <Row>
            <Notes>...</Notes>
        </Row>
        ```
    """

    commission_percentage: float = 0
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