# XML Mapper

This module provides a simple way to map XML documents to python dataclasses.

## How to use

1. Create a dataclass which inherits from `XMLMapper`

    ```python
    from dataclasses import dataclass
    from easyfatt_db_connector.xml.common import XMLMapper

    @dataclass(init=False)
    class MyMapper(XMLMapper):
        pass
    ```

2. Define the `__xml_mapping__` and `__xml_name__` attributes accordingly:

    ```python
    from dataclasses import dataclass
    from easyfatt_db_connector.xml.common import XMLMapper

    @dataclass(init=False)
    class MyUser(XMLMapper):
        __xml_name__ = "Product"
        __xml_mapping__ = {
            'name': 'Name',
            'description': 'Description',
            'counter': 'Counter',
        }

        name: str = ""
        description: str = ""
        counter: int = 0
    ```

    > **NOTE:**
    >
    > Remember to **always** define the dataclass attributes with the same name as the keys in the `__xml_mapping__` dictionary.

3. Call the `from_xml_string` method to create an instance of the dataclass from an XML string:

    ```python
    from dataclasses import dataclass
    from easyfatt_db_connector.xml.common import XMLMapper

    @dataclass(init=False)
    class MyMapper(XMLMapper):
        __xml_name__ = "Product"
        __xml_mapping__ = {
            'name': 'Name',
            'description': 'Description',
            'counter': 'Counter',
        }

        name: str = ""
        description: str = ""
        counter: int = 0

    xml_string = """
    <Product>
        <Name>My name</Name>
        <Description>My description</Description>
        <Counter>42</Counter>
    </Product>
    """

    my_mapper = MyMapper.from_xml_string(xml_string)
    print(my_mapper.name) # ==> My name
    ```

## See also

- [xsdata](https://xsdata.readthedocs.io/en/latest/) - Complete **data binding** library for python allowing to access and use XML and JSON documents as simple objects; it also includes a **model generator** supporting XML schemas, DTD, WSDL definitions, XML & JSON documents.
- [xml-dataclasses](https://pypi.org/project/xml-dataclasses/) - (De)serialize XML documents into specially-annotated dataclasses
