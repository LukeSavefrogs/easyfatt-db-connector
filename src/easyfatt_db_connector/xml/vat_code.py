from dataclasses import dataclass

import lxml.etree as ET
from easyfatt_db_connector.xml.common import XMLMapper


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