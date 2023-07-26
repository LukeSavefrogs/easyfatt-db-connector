from dataclasses import dataclass

import lxml.etree as ET
from easyfatt_db_connector.xml.common import XMLMapper


@dataclass(eq=False, init=False, repr=False)
class VatCode(XMLMapper):
    """ Informazioni sull'IVA applicata al prodotto. """
    __xml_mapping__ = {
        "code": "#TEXT",
        "description": "@Description",
        "percentage": "@Perc",
        "vat_class": "@Class",
    }
    
    code: str = ""
    """ Codice IVA (deve essere già presente nella tabella "Categorie Iva" dell'applicazione). 
    
    Attenzione, non si tratta del valore percenutale di tassazione.

    Example:
        ```xml
        <Row>
            <VatCode>20</VatCode>
        </Row>
        ```
    """

    description: str = ""
    """ Descrizione libera del codice Iva.
    
    Example:
        ```xml
        <Row>
            <VatCode Description="Aliquota 20%">...</VatCode>
        </Row>
        ```
    """

    percentage: str = ""
    """ Percentuale tassazione applicata.
    
    Example:
        ```xml
        <Row>
            <VatCode Perc="20">...</VatCode>
        </Row>
        ```
    """

    vat_class: str = ""
    """ Classe: imponibile, non imponibile, intra-ue, extra-ue, esente, escluso, fuori campo, iva non esposta, rev. charge.
    
    Example:
        ```xml
        <Row>
            <VatCode Class="Imponibile">...</VatCode>
        </Row>
        ```
    """