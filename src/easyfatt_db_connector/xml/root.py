import dataclasses
from typing import Optional

from easyfatt_db_connector.xml.company import Company
from easyfatt_db_connector.xml.document import Document
from easyfatt_db_connector.xml.common import Field, XMLMapper


@dataclasses.dataclass(init=False, repr=False)
class EasyfattXML(XMLMapper):
    """ Python object representation of the `.DefXml` file. 
    
	Each XML text gets encoded to its relative Python type (e.g. `false` becomes `False`).
    """
    
    __xml_name__ = "EasyfattDocuments"
    __xml_mapping__ = {
        "protocol_version": "@AppVersion",
        "creator_name": "@Creator",
        "creator_url": "@CreatorUrl",
        "company": Field(target=Company),
        "documents": Field(tag="Documents", is_parent=True, child=Field(Document)),
    }

    protocol_version: str = ""
    """ Versione del protocollo usato; va usato nell'integrazione e-commerce. 
    
    Example:
        ```xml
        <EasyfattDocuments AppVersion="[...]">...</EasyfattDocuments>
        ```
    """

    creator_name: str = ""
    """ Informazioni sul software o sul servizio che ha originato il file (nome della software house e/o del programma). 
    
    Example:
        ```xml
        <EasyfattDocuments Creator="[...]">...</EasyfattDocuments>
        ```
    """

    creator_url: str = ""
    """ Eventuale indirizzo web di approfondimento sul software o sul servizio che ha originato il file.
    
    Example:
        ```xml
        <EasyfattDocuments CreatorUrl="[...]">...</EasyfattDocuments>
        ```
    """

    company: Optional[Company] = None
    """ Informazioni sull'azienda che ha originato il file. 
    
    Example:
        ```xml
        <EasyfattDocuments>
            <Company>...</Company>
        </EasyfattDocuments>
        ```
    """

    documents: list[Document] = dataclasses.field(default_factory=list)
    """ Lista dei documenti contenuti nell'ordine. 
    
    Example:
        ```xml
        <EasyfattDocuments>
            <Documents>
                <Document>...</Document>
            </Documents>
        </EasyfattDocuments>
        ```
    """

    # def __init__(
    #     self,
    #     protocol_version: Optional[str] = None,
    #     creator_name: Optional[str] = None,
    #     creator_url: Optional[str] = None,
    # ):
    #     self.protocol_version = protocol_version
    #     self.creator_name = creator_name
    #     self.creator_url = creator_url

    #     self.company = None
    #     self.documents = []

    def add_document(self, document: Document):
        self.documents.append(document)

    def remove_document(self, document: Document):
        self.documents.remove(document)

    def set_company(self, company: Company):
        self.company = company

    def remove_company(self):
        self.company = None

