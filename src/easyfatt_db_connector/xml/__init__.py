from pathlib import Path
from typing import Optional, Union

from easyfatt_db_connector.xml.root import EasyfattXML

__all__ = ["read_xml", "EasyfattXML"]

def read_xml(filename: Optional[Union[str, Path]] = None, text: Optional[str] = None, convert_types=True) -> EasyfattXML:
    """ Legge un file XML e lo converte in un oggetto `EasyfattXML`. 
    
    Args:
        filename (Union[str, Path], optional): Percorso del file XML da leggere. Defaults to None.
        text (str, optional): Testo del file XML da leggere. Defaults to None.
        convert_types (bool, optional): Se `True`, converte i valori dei tag in tipi Python. Defaults to True.
    
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
    
    return EasyfattXML.from_xml_string(bytes(xml_string, encoding='utf-8'), convert_types=convert_types)
