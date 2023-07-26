# Lettura file `.DefXml`

Questo modulo permette di leggere il tracciato XML dei **documenti esportati da Easyfatt** e trasformarlo in una serie di **oggetti Python**.

Ad esempio, il seguente codice leggerà il file `fatture.DefXml` e restituirà i dati desiderati riguardo i documenti definiti all'interno:

```python
from easyfatt_db_connector import read_xml

xml_file = read_xml("fatture.DefXml")

for document in xml_file.documents:
    print(f"Document number      : {document.number}")
    print(f"Document date        : {document.date}")
    print(f"Document rows        : {len(document.rows)}")
    print(f"Document total price : {sum([row.quantity * row.price for row in document.rows])}")
    print(f"Document total paid  : {sum([paym.amount for paym in document.payments if paym.paid])}")
```

I dati vengono automaticamente convertiti nel relativo tipo Python (_nell'esempio precedente infatti `paym.paid` è un valore `bool` mentre `paym.amount` è un valore `float`_).

## Note

Questa API è stata sviluppata seguendo le linee guida [documentazione ufficiale](https://www.danea.it/software/easyfatt/xml/).

Per questo motivo sono state mantenute le stesse convenzioni specificate nella sezione ["Note preliminari per il formato XML"](https://www.danea.it/software/easyfatt/xml/formato/) della documentazione ufficiale:

> - **Tutti i campi**, se non specificato diversamente, **sono opzionali**.
> - I campi di tipo `[Valuta]` e `[Numerico]` utilizzano il `.` come separatore decimale. Non va utilizzato il separatore delle migliaia.
> - I campi di tipo `[Data]` sono in formato ISO `aaaa-mm-gg` (es: `2007-02-28`).
> - In **esportazione da Easyfatt**, se un campo ha un valore nullo (stringa vuota, oppure numero uguale a zero), il relativo tag viene omesso dal tracciato.
> - In **importazione**, se Easyfatt riscontra un tag con contenuto nullo (stringa vuota, oppure numero uguale a zero), imposterà tale valore nel relativo campo; se, invece, il tag viene omesso del tutto, Easyfatt imposterà il valore di default per quel contesto (ad esempio, se in un tracciato è assente il tag <Date>, il documento importato avrà la data del giorno e non la data nulla, se invece è assente il tag <Number> Easyfatt imposterà l'incremento automatico del numero del documento).
> - Il file XML deve essere codificato in **UNICODE UTF-8** che prevede importanti regole nella codifica delle stringhe racchiuse tra tag

## Limitazioni

- Al momento della scrittura di questo documento, è possibile solamente **leggere** i file XML esportati da Easyfatt, non è possibile crearli o modificarli.
