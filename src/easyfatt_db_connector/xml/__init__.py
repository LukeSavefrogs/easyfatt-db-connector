from pathlib import Path
from typing import Optional, Union

from easyfatt_db_connector.xml.root import EasyfattXML

# __all__ = ["read_xml", "EasyfattXML"]

def read_xml(filename: Optional[Union[str, Path]] = None, text: Optional[str] = None) -> EasyfattXML:
    """ Legge un file XML e lo converte in un oggetto `EasyfattXML`. 
    
    Args:
        filename (Union[str, Path], optional): Percorso del file XML da leggere. Defaults to None.
        text (str, optional): Testo del file XML da leggere. Defaults to None.
    
    Raises:
        ValueError: Se non viene fornito né un filename né un testo, oppure se vengono forniti entrambi.

    Returns:
        EasyfattXML: Oggetto `EasyfattXML` contenente i dati del file XML.
    """
    if (filename is not None and text is not None) or (filename is None and text is None):
        raise ValueError("You must provide a filename or a text")

    xml_string = ""
    if filename is not None:
        with open(filename, "r", encoding='utf-8-sig') as f:
            xml_string = f.read().strip()

    elif text is not None:
        xml_string = text.strip()
    
    return EasyfattXML.from_xml_string(bytes(xml_string, encoding='utf-8'))
    

if __name__ == "__main__":
    print("-" * 80)
    xml_objects = read_xml("fatture.Defxml")
    # print(xml_objects)
    # print("\n")
    # print("-" * 80)
    # print("\n")
    # print(f"Has been paid: {xml_objects.documents[0].payments[0].paid}")
    # for document in xml_objects.documents:
    #     print(f"Document number      : {document.number}")
    #     print(f"Document date        : {document.date}")

    #     print(f"Document rows        : {len(document.rows)}")
    #     print(f"Document total price : {sum([row.quantity * row.price for row in document.rows])}")

    #     print(f"Document total paid  : {sum([paym.amount for paym in document.payments if paym.paid])}")

    #     print("\n")

    # print("-" * 80)
