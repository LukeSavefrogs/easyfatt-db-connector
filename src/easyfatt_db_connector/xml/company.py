from dataclasses import dataclass
from easyfatt_db_connector.xml.common import XMLMapper

@dataclass(init=False)
class Company(XMLMapper):
    """ Dati dell'azienda che ha originato il file. 
    
    Fonte: https://www.danea.it/software/easyfatt/xml/documenti/#section-126
    """
    __xml_mapping__ = {
        "name": "Name",
        "address": "Address",
        "postcode": "Postcode",
        "city": "City",
        "province": "Province",
        "country": "Country",
        "fiscal_code": "FiscalCode",
        "vat_code": "VatCode",
        "phone": "Tel",
        "fax": "Fax",
        "email": "Email",
        "homepage": "HomePage",
    }

    name: str = ""
    """ Nome del mittente (l'azienda che ha originato il file). 
    
    Example:
        ```xml
        <Company>
            <Name>Arredufficio Srl</Name>
        </Company>
    """

    address: str = ""
    """ Indirizzo dell'azienda.
    
    Example:
        ```xml
        <Company>
            <Address>Via Crissolo, 12</Address>
        </Company>
    """

    postcode: str = ""
    """ CAP dell'azienda.
    
    Example:
        ```xml
        <Company>
            <Postcode>10138</Postcode>
        </Company>
    """

    city: str = ""
    """ Città dell'azienda.
    
    Example:
        ```xml
        <Company>
            <City>Torino</City>
        </Company>
    """

    province: str = ""
    """ Provincia dell'azienda (2 caratteri).
    
    Example:
        ```xml
        <Company>
            <Province>TO</Province>
        </Company>
    """

    country: str = ""
    """ Nazione dell'azienda.
    
    Example:
        ```xml
        <Company>
            <Country>Italia</Country>
        </Company>
    """

    fiscal_code: str = ""
    """ Codice fiscale dell'azienda.
    
    Example:
        ```xml
        <Company>
            <FiscalCode>01303760282</FiscalCode>
        </Company>
    """

    vat_code: str = ""
    """ Partita IVA dell'azienda.
    
    Example:
        ```xml
        <Company>
            <VatCode>01303760282</VatCode>
        </Company>
    """

    phone: str = ""
    """ Numero di telefono dell'azienda.
    
    Example:
        ```xml
        <Company>
            <Tel>011-2568745</Tel>
        </Company>
    """

    fax: str = ""
    """ Numero di fax dell'azienda.
    
    Example:
        ```xml
        <Company>
            <Fax>011-2548793</Fax>
        </Company>
    """

    email: str = ""
    """ Indirizzo email dell'azienda.
    
    Example:
        ```xml
        <Company>
            <Email>arredufficiosrl@arredufficio.it</Email>
        </Company>
    """

    homepage: str = ""
    """ Sito web dell'azienda.
    
    Example:
        ```xml
        <Company>
            <HomePage>www.arredufficiosrl.it</HomePage>
        </Company>
    """


if __name__ == "__main__":
    xml = """
        <Company>
            <Name>Tuttobimbi Srl</Name>
            <Address>Via Armando Diaz, 162</Address>
            <Postcode>35010</Postcode>
            <City>Vigonza</City>
            <Province>PD</Province>
            <Country>Italia</Country>
            <FiscalCode>00165987261</FiscalCode>
            <VatCode>00165987261</VatCode>
            <Tel>049/1234567</Tel>
            <Fax>049/1234568</Fax>
            <Email>info@tutto-bimbi.com</Email>
            <HomePage>www.tutto-bimbi.com</HomePage>
        </Company>
    """
    
    company = Company.from_xml_string(xml)
    
    print(f"Example of <Company> as object: {company}\n")
    print(f"Company address is            : {company.address}\n")

    # TODO: fix this
    # print(f"Example of <Company> as XML   : {company.to_xml_string()}\n")