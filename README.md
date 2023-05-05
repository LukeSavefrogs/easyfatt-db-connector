# easyfatt-db-connector

## Development

### Database

1. Installare [**Firebird SQL** 2.5.9](https://firebirdsql.org/en/firebird-2-5/) (selezionare la versione "_64-bit Classic, Superclassic & Superserver_")
2. Assicurarsi di selezionare "**Run as service**"

Per controllare l'avvenuta installazione:

1. Aprire un terminale Powershell nella cartella di installzione (nel mio caso `C:\Program Files\Firebird\Firebird_2_5`)
2. Lanciare il comando `cd bin`
3. Lanciare il comando `./isql.exe "{PERCORSO_DATABASE}\{NOME_DATABASE}.eft" -u sysdba -p masterkey`
4. Ora è possibile eseguire query SQL (assicurandosi che finiscano SEMPRE con `;`)
   ![picture 10](images/b84c1a8129e2b6860dd8fb3ca97956e01f1df8ab2447a4b3a79aa503a7389066.png)  

### Database tool

1. Installare ed aprire [**DBeaver**](https://dbeaver.io/):

   ![picture 1](images/6ad115036db6d0cacd65cd56fd433824e02255f08aad3bfe807015622b98d251.png)  

2. Cliccare su "File > Nuovo":

   ![picture 3](images/5bf1d7e5c76f4d7428abc4f7dcaed9aefbb74c04a4adaa944446dfa714d13f9d.png)  

3. Cliccare su "DBeaver > Connessione a Database" e cliccare "Avanti":

   ![picture 2](images/b871bea2ba76855114647dff6732888f05cc37831d177b7172c90f9b581e54df.png)  

4. Nel campo di ricerca scrivere "Firebird", selezionare il primo risultato e cliccare "Avanti":

   ![picture 4](images/a1c9c3910a6054f08b630aa07e697704c3f834011b9666c6ba76d77f80a1c7bf.png)

5. Compilare i dati richiesti:
   - **Generale**:
     - Host: `localhost` (default)
     - Porta: `3050` (default)
     - Percorso: adeguare alla posizione del database nel proprio sistema
   - **Autenticazione**:
     - Nome utente: `SYSDBA` (default)
     - Password: `masterkey`

   ![picture 8](images/25f4675dde1c3ead454938029857e73e3c2ab931f5a3308e5a72bbf3c0c448d9.png)  

6. Terminare la configurazione del driver cliccando su "Fine"

## Alcune note

- Assicurarsi che sia visibile almeno la finestra "Navigatore Database":

  ![picture 9](images/4296d83f4dc4bcd259c117af17cc52b8084a220ecb46b1ca086c22fd7a760d85.png)  
