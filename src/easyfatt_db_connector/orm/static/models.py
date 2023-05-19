""" SQLAlchemy models 

All the models were generated using [sqlacodegen](https://github.com/agronholm/sqlacodegen).

To use a model `import` it and use it as follows:
```
from easyfatt_db_connector.orm.static import TDocRighe
with engine.connect() as conn:
    query = TDocRighe.__table__.select()
    for row in conn.execute(query):
        print(row)
```
"""

# coding: utf-8
# sqlacodegen.exe --outfile models.py "firebird:///C:\Users\lucas\Documents\Danea Easyfatt\TestArchivio.eft.tmp?fb_library_name=C:\Users\lucas\.cache\firebird-embedded\fbembed.dll&user=SYSDBA"
from sqlalchemy import Column, Date, DateTime, Float, ForeignKey, ForeignKeyConstraint, Index, Integer, LargeBinary, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TAgenti(Base):
    __tablename__ = 'TAgenti'

    Agente = Column(String(255), primary_key=True)
    Nascosto = Column(SmallInteger, nullable=False, server_default=text("0"))
    ProvvComeAgente = Column(ForeignKey('TAgenti.Agente'))
    PercProvv_Old = Column(Float)
    Note = Column(Text)

    parent = relationship('TAgenti', remote_side=[Agente])


class TAgyo(Base):
    __tablename__ = 'TAgyo'

    IDAgyo = Column(String(50), primary_key=True)
    Acq = Column(SmallInteger, nullable=False, server_default=text("0"))
    Inviata = Column(SmallInteger, nullable=False, server_default=text("0"))
    TipoDocFE = Column(String(4))
    NumDoc = Column(String(20))
    NumDocSort = Column(String(255))
    DataDoc = Column(Date, nullable=False)
    Az_CodiceFiscale = Column(String(16))
    CodiceFiscale = Column(String(50))
    Nome = Column(String(255))
    TotDovuto = Column(Numeric(18, 4))
    Flusso = Column(String(50))
    Stato = Column(String(50))
    DescStato = Column(String(255))
    DataOraStato = Column(DateTime)
    NumNotifiche = Column(Integer)
    UltimaNotifica = Column(String(2))
    DataRicezione = Column(Date)
    NomeFile = Column(String(255))
    IDSdi = Column(String(50))
    DataArchiviazione = Column(Date)


class TCalendari(Base):
    __tablename__ = 'TCalendari'

    Calendario = Column(String(50), primary_key=True)
    Colore = Column(Integer, nullable=False, server_default=text("49407"))


class TCap(Base):
    __tablename__ = 'TCap'

    IDCap = Column(Integer, primary_key=True)
    Cap = Column(String(5), nullable=False, index=True)
    Citta = Column(String(255), nullable=False, index=True)
    Prov = Column(String(2), nullable=False)


class TCategorie(Base):
    __tablename__ = 'TCategorie'

    NomeCategoria = Column(String(255), primary_key=True)


class TClassiProvv(Base):
    __tablename__ = 'TClassiProvv'

    ClasseProvv = Column(String(255), primary_key=True)


class TConfig2(Base):
    __tablename__ = 'TConfig2'

    Key = Column(String(255), primary_key=True)
    Value = Column(Text)


class TConti(Base):
    __tablename__ = 'TConti'

    Conto = Column(String(255), primary_key=True)
    Predef = Column(String(50))
    Rev_Conto = Column(String(9))


class TContiVend(Base):
    __tablename__ = 'TContiVend'

    ContoVend = Column(String(255), primary_key=True)
    Predef = Column(String(50))
    TS_ContoVend = Column(String(50))
    TS_CodIva11 = Column(Integer)
    Rev_Conto = Column(String(9))


class TEcommUpload(Base):
    __tablename__ = 'TEcommUpload'

    UploadSet = Column(String(255), primary_key=True, nullable=False)
    Cod = Column(String(255), primary_key=True, nullable=False)
    Hash = Column(String(255))
    NomeImg = Column(String(255))
    DataImg = Column(DateTime)
    DimImg = Column(Integer)
    Tmp_Deleted = Column(SmallInteger, server_default=text("0"))
    Tmp_NewHash = Column(String(255))
    Tmp_ImgToUpload = Column(String(255))


class TEcrConfig(Base):
    __tablename__ = 'TEcrConfig'

    Ecr_Key = Column(String(255), primary_key=True)
    Ecr_Modello = Column(String(255))
    Ecr_Porta = Column(String(50), nullable=False)
    Ecr_IndirizzoIp = Column(String(255))
    Ecr_ExportPathName = Column(String(255))
    Ecr_ExePathName = Column(String(255))
    Ecr_StampaCodArticolo = Column(SmallInteger, server_default=text("0"))
    Ecr_StampaSeriale = Column(SmallInteger, server_default=text("1"))
    Ecr_MsgFidelity = Column(Text)
    Ecr_ScontrinoParlante = Column(SmallInteger, server_default=text("0"))
    Ecr_ElencoPagam = Column(String(255))
    Ecr_MsgCortesia = Column(Text)
    Ecr_ScontrinoCortesia = Column(Text)


class TEmailTemplate(Base):
    __tablename__ = 'TEmailTemplate'

    KeyTemplate = Column(String(50), primary_key=True, nullable=False)
    TipoTemplate = Column(String(50), primary_key=True, nullable=False)
    NomeTemplate = Column(String(255), primary_key=True, nullable=False)
    Oggetto = Column(String(255))
    Messaggio = Column(Text)
    UsaPec = Column(SmallInteger, server_default=text("0"))
    IDEmailTemplate = Column(Integer, nullable=False, unique=True)
    SendAllegatiDoc = Column(SmallInteger, server_default=text("0"))


class TFrasiPredef(Base):
    __tablename__ = 'TFrasiPredef'

    NomeCampo = Column(String(50), primary_key=True, nullable=False)
    TestoFrase = Column(String(255), primary_key=True, nullable=False)
    DefaultKeys = Column(String(255))


class TGruppi(Base):
    __tablename__ = 'TGruppi'

    IDGruppo = Column(Integer, primary_key=True)
    NomeGruppo = Column(String(255))
    MostraPrezzoComplessivo = Column(SmallInteger, server_default=text("0"))


class TListini(Base):
    __tablename__ = 'TListini'

    IDListino = Column(String(50), primary_key=True)
    Visibile = Column(SmallInteger, server_default=text("0"))
    NomeListino = Column(String(255), nullable=False, unique=True)
    FormulaMru1 = Column(String(255))
    FormulaMru2 = Column(String(255))
    FormulaMru3 = Column(String(255))
    FormulaMru4 = Column(String(255))
    FormulaMru5 = Column(String(255))
    FormulaMru6 = Column(String(255))


class TLock(Base):
    __tablename__ = 'TLocks'

    NomeLock = Column(String(255), primary_key=True)
    IDUtente = Column(Integer, nullable=False)
    Cont = Column(Integer, nullable=False, server_default=text("0"))


class TLogUtenti(Base):
    __tablename__ = 'TLogUtenti'

    IDLog = Column(Integer, primary_key=True, unique=True)
    DataOra = Column(DateTime, nullable=False)
    Login = Column(String(50))
    NomeComputer = Column(String(255), nullable=False)
    UtenteComputer = Column(String(255), nullable=False)
    Desc = Column(Text)
    Hash = Column(String(255), nullable=False)


class TMagazz(Base):
    __tablename__ = 'TMagazz'

    Magazz = Column(String(255), primary_key=True)
    Note = Column(Text)


class TNazioni(Base):
    __tablename__ = 'TNazioni'

    NomeNazione = Column(String(255), primary_key=True)
    NomeNazionePrint = Column(String(255), nullable=False)
    IsoNazione = Column(String(2), nullable=False)
    UicNazione = Column(String(3))
    Predefinito = Column(SmallInteger, nullable=False, server_default=text("0"))
    Alias = Column(SmallInteger, nullable=False, server_default=text("0"))


class TReport(Base):
    __tablename__ = 'TReport'

    TipoReport = Column(String(50), primary_key=True, nullable=False)
    NomeReport = Column(String(255), primary_key=True, nullable=False)
    CategReport = Column(String(50))
    DatiReport = Column(LargeBinary, nullable=False)
    ReportPredefinito = Column(SmallInteger, server_default=text("0"))
    DefProOnly = Column(SmallInteger, server_default=text("0"))
    DefaultFor = Column(String(255))


class TRisorse(Base):
    __tablename__ = 'TRisorse'

    Risorsa = Column(String(255), primary_key=True)
    TipoRisorsa = Column(String(50), nullable=False)
    Url = Column(String(255))
    SaldoIniziale = Column(Numeric(18, 4), nullable=False, server_default=text("0"))
    RisorsaDefault = Column(SmallInteger, server_default=text("0"))
    CoordBancarie = Column(String(255))
    Sia = Column(String(5))
    Cuc = Column(String(8))
    CreditorId = Column(String(50))
    Note = Column(Text)
    TS_Conto = Column(String(50))


class TTipiDoc(Base):
    __tablename__ = 'TTipiDoc'

    TipoDoc = Column(String(50), primary_key=True)
    Nome = Column(String(50), nullable=False)
    NomeShortcut = Column(String(255), nullable=False)
    NomePlurale = Column(String(50), nullable=False)
    NomeBreve = Column(String(50), nullable=False)
    Ordinam = Column(Integer, nullable=False)
    IncludibileIn = Column(String(50))
    CodGruppo = Column(String(50), nullable=False)
    NomeGruppo = Column(String(50), nullable=False)
    Acq = Column(SmallInteger, server_default=text("0"))
    DefProOnly = Column(SmallInteger, server_default=text("0"))
    Registraz = Column(SmallInteger, server_default=text("0"))
    RegistroIva = Column(String(50))
    AnalisiDefault = Column(SmallInteger, server_default=text("0"))
    FuoriCampoIva = Column(SmallInteger, server_default=text("0"))
    InviaEmailAdAmmin = Column(SmallInteger, server_default=text("0"))
    UsaIDAnagr = Column(SmallInteger, server_default=text("0"))
    ObbligaIDAnagr = Column(SmallInteger, server_default=text("1"))
    SiaClientiCheForn = Column(SmallInteger, server_default=text("0"))
    UsaPagamento = Column(SmallInteger, server_default=text("0"))
    UsaScadenzePagamento = Column(SmallInteger, server_default=text("0"))
    UsaTrasporto = Column(SmallInteger, server_default=text("0"))
    UsaRitenute = Column(SmallInteger, server_default=text("1"))
    FattAcconto = Column(SmallInteger, server_default=text("0"))
    NotaVariaz = Column(SmallInteger, nullable=False, server_default=text("0"))
    SignQta = Column(Numeric(18, 4), nullable=False, server_default=text("0"))
    TipoMovMagazz = Column(String(255))
    UsaStatoOrdine = Column(SmallInteger, server_default=text("0"))
    UsaCausaleDoc = Column(SmallInteger, server_default=text("0"))
    UsaProtocollo = Column(SmallInteger, server_default=text("0"))
    UsaScontrino = Column(SmallInteger, server_default=text("0"))
    UsaAgente = Column(SmallInteger, server_default=text("0"))
    LiquidaProvvigioni = Column(SmallInteger, server_default=text("0"))
    PrefixImmagini = Column(String(50), nullable=False)
    UsaFattElettr = Column(SmallInteger, nullable=False, server_default=text("0"))
    TipoDocComFatt = Column(String(4))
    ReportTipoDoc = Column(String(50))
    Visibile = Column(SmallInteger, server_default=text("1"))
    TipoIndirizzo = Column(String(50))
    ObbligaNumerazione = Column(SmallInteger, server_default=text("1"))
    CodNumeraz = Column(String(50), nullable=False)
    ElencoNumeraz = Column(Text)
    NascondiTracciabilitaInStampa = Column(SmallInteger, server_default=text("0"))
    UsaPrezzoIvatoDefault = Column(SmallInteger, server_default=text("0"))
    BloccaModifiche = Column(SmallInteger, server_default=text("1"))
    TitoloReport = Column(String(255))
    NoteReport = Column(Text)


class TTmpDibaProduz(Base):
    __tablename__ = 'TTmpDiba_Produz'

    IDUtente = Column(Integer, primary_key=True, nullable=False)
    IDTmpDiba_Produz = Column(Integer, primary_key=True, nullable=False)
    IDComponente = Column(Integer, nullable=False)
    QtaRichiesta = Column(Numeric(18, 4), nullable=False)
    Livello = Column(Integer)
    Ordinam = Column(String(255))
    UsaDiba = Column(SmallInteger, server_default=text("0"))


class TTmpDistintePagam(Base):
    __tablename__ = 'TTmpDistintePagam'

    IDUtente = Column(Integer, primary_key=True, nullable=False)
    IDTmpDistintaPagam = Column(Integer, primary_key=True, nullable=False)
    Raggruppato = Column(SmallInteger, server_default=text("0"))
    IDAnagr = Column(Integer, nullable=False)
    Anagr_Nome = Column(String(255))
    Anagr_Indirizzo = Column(String(255))
    Anagr_Cap = Column(String(255))
    Anagr_Citta = Column(String(255))
    Anagr_Prov = Column(String(255))
    Anagr_Nazione = Column(String(255))
    Anagr_CodiceFiscale = Column(String(255))
    Anagr_PartitaIva = Column(String(255))
    CoordBancarie = Column(String(255))
    CausaleLong = Column(Text)
    CausaleShort = Column(Text)
    DataScad = Column(Date, nullable=False)
    ImportoPagam = Column(Numeric(18, 4), nullable=False)
    Sdd_TipoIncasso = Column(String(50))


class TTmpElencoID(Base):
    __tablename__ = 'TTmpElencoID'

    IDUtente = Column(Integer, primary_key=True, nullable=False)
    id = Column(Integer, primary_key=True, nullable=False)


class TTmpInvRiepilogo(Base):
    __tablename__ = 'TTmpInv_Riepilogo'

    IDUtente = Column(Integer, primary_key=True, nullable=False)
    IDArticolo = Column(Integer, primary_key=True, nullable=False)
    Magazz = Column(String(255), primary_key=True, nullable=False)
    QtaCaricata = Column(Numeric(18, 4))
    QtaScaricata = Column(Numeric(18, 4))
    DataUltimoCaricoConPrezzo = Column(Date)
    QtaCaricataConPrezzo = Column(Numeric(18, 4))
    QtaScaricataConPrezzo = Column(Numeric(18, 4))
    PrezzoMedioCarico = Column(Numeric(18, 4))
    PrezzoMedioScarico = Column(Numeric(18, 4))
    PrezzoUltimoCarico = Column(Numeric(18, 4))


class TTmpInvUltimoCarico(Base):
    __tablename__ = 'TTmpInv_UltimoCarico'

    IDUtente = Column(Integer, primary_key=True, nullable=False)
    IDArticolo = Column(Integer, primary_key=True, nullable=False)
    IDUltimoCarico = Column(Integer)


class TTmpMMAggiorna(Base):
    __tablename__ = 'TTmpMM_Aggiorna'

    IDUtente = Column(Integer, primary_key=True, nullable=False)
    IDArticolo = Column(Integer, primary_key=True, nullable=False)


t_TTmpMM_CheckLotti = Table(
    'TTmpMM_CheckLotti', metadata,
    Column('IDUtente', Integer, nullable=False),
    Column('IDArticolo', Integer, nullable=False),
    Column('Lotto', String(50)),
    Column('DataScadenza', Date),
    Column('DataScadenza_Max', Date),
    Column('Qta', Numeric(18, 4)),
    Column('Raggruppato', SmallInteger, server_default=text("0"))
)


t_TTmpMM_CheckLotti2 = Table(
    'TTmpMM_CheckLotti2', metadata,
    Column('IDUtente', Integer, nullable=False),
    Column('MM_IDArticolo', Integer, nullable=False),
    Column('MM_Lotto', String(50)),
    Column('MM_DataScadenza', Date),
    Column('MM_QtaCaricata', Numeric(18, 4)),
    Column('MM_QtaScaricata', Numeric(18, 4)),
    Column('MM_QtaImpegnata', Numeric(18, 4)),
    Index('TTmpMM_CheckLotti2_I1', 'IDUtente', 'MM_IDArticolo', 'MM_Lotto')
)


class TTmpMMRiepilogo(Base):
    __tablename__ = 'TTmpMM_Riepilogo'

    IDUtente = Column(Integer, primary_key=True, nullable=False)
    IDArticolo = Column(Integer, primary_key=True, nullable=False)
    Magazz = Column(String(255), primary_key=True, nullable=False)
    QtaCaricata = Column(Numeric(18, 4))
    QtaScaricata = Column(Numeric(18, 4))
    QtaImpegnata = Column(Numeric(18, 4))
    QtaInArrivo = Column(Numeric(18, 4))
    DataPrimoCarico = Column(Date)
    DataUltimoCarico = Column(Date)
    DataUltimoScarico = Column(Date)
    DataUltimoCaricoConPrezzo = Column(Date)
    QtaCaricataConPrezzo = Column(Numeric(18, 4))
    QtaScaricataConPrezzo = Column(Numeric(18, 4))
    PrezzoMedioCarico = Column(Numeric(18, 4))
    PrezzoMedioScarico = Column(Numeric(18, 4))
    PrezzoUltimoCarico = Column(Numeric(18, 4))


class TTmpMMUltimoCarico(Base):
    __tablename__ = 'TTmpMM_UltimoCarico'

    IDUtente = Column(Integer, primary_key=True, nullable=False)
    IDArticolo = Column(Integer, primary_key=True, nullable=False)
    IDUltimoCarico = Column(Integer)


class TTmpOrdAggiorna(Base):
    __tablename__ = 'TTmpOrd_Aggiorna'

    IDUtente = Column(Integer, primary_key=True, nullable=False)
    IDDoc = Column(Integer, primary_key=True, nullable=False)


class TTmpOrdQtaArrivata(Base):
    __tablename__ = 'TTmpOrd_QtaArrivata'

    IDDocRiga = Column(Integer, primary_key=True)
    QtaArrivata = Column(Numeric(18, 4))


class TTmpRicercaTaglieColori(Base):
    __tablename__ = 'TTmpRicercaTaglieColori'

    IDUtente = Column(Integer, primary_key=True, nullable=False)
    IDTmp = Column(Integer, primary_key=True, nullable=False)
    TagliaColore = Column(String(255))
    Qta = Column(Numeric(18, 4))


class TAgentiProvv(Base):
    __tablename__ = 'TAgentiProvv'

    Agente = Column(ForeignKey('TAgenti.Agente'), primary_key=True, nullable=False)
    ClasseProvv = Column(ForeignKey('TClassiProvv.ClasseProvv'), primary_key=True, nullable=False)
    ProvvListino1 = Column(Numeric(18, 4), nullable=False, server_default=text("0"))
    ProvvListino2 = Column(Numeric(18, 4), nullable=False, server_default=text("0"))
    ProvvListino3 = Column(Numeric(18, 4), nullable=False, server_default=text("0"))
    ProvvListino4 = Column(Numeric(18, 4), nullable=False, server_default=text("0"))
    ProvvListino5 = Column(Numeric(18, 4), nullable=False, server_default=text("0"))
    ProvvListino6 = Column(Numeric(18, 4), nullable=False, server_default=text("0"))
    ProvvListino7 = Column(Numeric(18, 4), nullable=False, server_default=text("0"))
    ProvvListino8 = Column(Numeric(18, 4), nullable=False, server_default=text("0"))
    ProvvListino9 = Column(Numeric(18, 4), nullable=False, server_default=text("0"))

    TAgenti = relationship('TAgenti')
    TClassiProvv = relationship('TClassiProvv')


class TIva(Base):
    __tablename__ = 'TIva'

    CodIva = Column(String(50), primary_key=True)
    PercIva = Column(Float, nullable=False, server_default=text("0"))
    PercIvaIndetr = Column(Float, nullable=False, server_default=text("0"))
    ClasseIva = Column(String(50))
    DescIva = Column(String(255), nullable=False)
    Note = Column(String(255))
    Ecr_Reparto = Column(Integer)
    TS_CodIva = Column(String(10))
    Rev_CodIvaAcq = Column(String(5))
    Rev_CodIvaVend = Column(String(5))
    ContoVendDefault = Column(ForeignKey('TContiVend.ContoVend'))

    TContiVend = relationship('TContiVend')


class TSottocategorie(Base):
    __tablename__ = 'TSottocategorie'

    NomeCategoria = Column(ForeignKey('TCategorie.NomeCategoria'), primary_key=True, nullable=False)
    NomeSottocategoria = Column(String(255), primary_key=True, nullable=False, index=True)

    TCategorie = relationship('TCategorie')


class TUtenti(Base):
    __tablename__ = 'TUtenti'

    Login = Column(String(50), primary_key=True)
    Password = Column(String(255))
    DataCambioPassword = Column(Date)
    Email = Column(String(255))
    Connesso = Column(SmallInteger, server_default=text("0"))
    DataOraUltimoAccesso = Column(DateTime)
    Sospeso = Column(SmallInteger, nullable=False, server_default=text("0"))
    Amministratore = Column(SmallInteger, server_default=text("0"))
    RestrizAgente = Column(ForeignKey('TAgenti.Agente'))
    AccessoDocAltriAgenti = Column(SmallInteger, server_default=text("1"))
    AccessoAnagrAltriAgenti = Column(SmallInteger, nullable=False, server_default=text("1"))
    RestrizMagazz = Column(ForeignKey('TMagazz.Magazz'))
    CalendarioDefault = Column(ForeignKey('TCalendari.Calendario'), nullable=False)
    AccessoPrezziAcq = Column(SmallInteger, server_default=text("1"))
    AccessoPrezziVend = Column(SmallInteger, server_default=text("1"))
    AccessoExport = Column(SmallInteger, nullable=False, server_default=text("1"))
    AccessoClienti = Column(SmallInteger, server_default=text("1"))
    AccessoClientiWrite = Column(SmallInteger, server_default=text("1"))
    AccessoForn = Column(SmallInteger, server_default=text("1"))
    AccessoFornWrite = Column(SmallInteger, server_default=text("1"))
    AccessoArticoli = Column(SmallInteger, server_default=text("1"))
    AccessoArticoliWrite = Column(SmallInteger, server_default=text("1"))
    AccessoElencoPagam = Column(SmallInteger, server_default=text("1"))
    AccessoMagazzino = Column(SmallInteger, server_default=text("1"))
    AccessoImpegni = Column(SmallInteger, server_default=text("1"))
    AccessoAnalisi = Column(SmallInteger, server_default=text("1"))
    AccessoStrRegistriIva = Column(SmallInteger, server_default=text("1"))
    AccessoStrRiepilogoRegistraz = Column(SmallInteger, server_default=text("1"))
    AccessoStrAgenti = Column(SmallInteger, server_default=text("1"))
    AccessoStrEcomm = Column(SmallInteger, server_default=text("1"))
    AccessoStrStampe = Column(SmallInteger, server_default=text("1"))
    AccessoStrConfig = Column(SmallInteger, server_default=text("1"))
    AccessoTblIva = Column(SmallInteger, server_default=text("1"))
    AccessoTblTipiPagam = Column(SmallInteger, server_default=text("1"))
    AccessoTblConti = Column(SmallInteger, server_default=text("1"))
    AccessoDocA = Column(SmallInteger, server_default=text("1"))
    AccessoDocB = Column(SmallInteger, server_default=text("1"))
    AccessoDocC = Column(SmallInteger, server_default=text("1"))
    AccessoDocD = Column(SmallInteger, server_default=text("1"))
    AccessoDocE = Column(SmallInteger, server_default=text("1"))
    AccessoDocF = Column(SmallInteger, server_default=text("1"))
    AccessoDocG = Column(SmallInteger, server_default=text("1"))
    AccessoDocH = Column(SmallInteger, server_default=text("1"))
    AccessoDocI = Column(SmallInteger, server_default=text("1"))
    AccessoDocJ = Column(SmallInteger, server_default=text("1"))
    AccessoDocL = Column(SmallInteger, server_default=text("1"))
    AccessoDocM = Column(SmallInteger, server_default=text("1"))
    AccessoDocN = Column(SmallInteger, server_default=text("1"))
    AccessoDocO = Column(SmallInteger, server_default=text("1"))
    AccessoDocP = Column(SmallInteger, server_default=text("1"))
    AccessoDocQ = Column(SmallInteger, server_default=text("1"))
    AccessoDocR = Column(SmallInteger, server_default=text("1"))
    AccessoDocS = Column(SmallInteger, server_default=text("1"))
    AccessoDocT = Column(SmallInteger, server_default=text("1"))
    AccessoDocU = Column(SmallInteger, server_default=text("1"))
    AccessoDocV = Column(SmallInteger, server_default=text("1"))
    AccessoDocW = Column(SmallInteger, server_default=text("1"))
    AccessoDocWriteA = Column(SmallInteger, server_default=text("1"))
    AccessoDocWriteB = Column(SmallInteger, server_default=text("1"))
    AccessoDocWriteC = Column(SmallInteger, server_default=text("1"))
    AccessoDocWriteD = Column(SmallInteger, server_default=text("1"))
    AccessoDocWriteE = Column(SmallInteger, server_default=text("1"))
    AccessoDocWriteF = Column(SmallInteger, server_default=text("1"))
    AccessoDocWriteG = Column(SmallInteger, server_default=text("1"))
    AccessoDocWriteH = Column(SmallInteger, server_default=text("1"))
    AccessoDocWriteI = Column(SmallInteger, server_default=text("1"))
    AccessoDocWriteJ = Column(SmallInteger, server_default=text("1"))
    AccessoDocWriteL = Column(SmallInteger, server_default=text("1"))
    AccessoDocWriteM = Column(SmallInteger, server_default=text("1"))
    AccessoDocWriteN = Column(SmallInteger, server_default=text("1"))
    AccessoDocWriteO = Column(SmallInteger, server_default=text("1"))
    AccessoDocWriteP = Column(SmallInteger, server_default=text("1"))
    AccessoDocWriteQ = Column(SmallInteger, server_default=text("1"))
    AccessoDocWriteR = Column(SmallInteger, server_default=text("1"))
    AccessoDocWriteS = Column(SmallInteger, server_default=text("1"))
    AccessoDocWriteT = Column(SmallInteger, server_default=text("1"))
    AccessoDocWriteU = Column(SmallInteger, server_default=text("1"))
    AccessoDocWriteV = Column(SmallInteger, server_default=text("1"))
    AccessoDocWriteW = Column(SmallInteger, server_default=text("1"))

    TCalendari = relationship('TCalendari')
    TAgenti = relationship('TAgenti')
    TMagazz = relationship('TMagazz')


class TSpese(Base):
    __tablename__ = 'TSpese'

    NomeSpesa = Column(String(255), primary_key=True)
    CodIva = Column(ForeignKey('TIva.CodIva'), nullable=False)
    ImportoNetto = Column(Numeric(18, 4), nullable=False, server_default=text("0"))
    ImportoIvato = Column(Numeric(18, 4), nullable=False, server_default=text("0"))

    TIva = relationship('TIva')


class TTrattenute(Base):
    __tablename__ = 'TTrattenute'

    IDTrattenuta = Column(Integer, primary_key=True)
    NomeTrattenuta = Column(String(255))
    PercTrattenuta = Column(Float, nullable=False, server_default=text("0"))
    RitAcconto = Column(SmallInteger, server_default=text("1"))
    CodIva = Column(ForeignKey('TIva.CodIva'), nullable=False)
    CalcolaSu = Column(String(50), nullable=False)

    TIva = relationship('TIva')


class TUtentiIstanze(Base):
    __tablename__ = 'TUtentiIstanze'

    IDUtente = Column(Integer, primary_key=True)
    Login = Column(ForeignKey('TUtenti.Login'))
    NomeComputer = Column(String(50))
    NumIstanza = Column(Integer, nullable=False)
    Connesso = Column(SmallInteger, server_default=text("0"))
    DataOraConnessione = Column(DateTime, nullable=False)

    TUtenti = relationship('TUtenti')


class TPagamenti(Base):
    __tablename__ = 'TPagamenti'

    NomePagamento = Column(String(255), primary_key=True, unique=True)
    CategPagamento = Column(String(50), nullable=False, server_default=text("'Contanti'"))
    Rate = Column(Text)
    SaldaSubito = Column(SmallInteger, server_default=text("0"))
    NumGiorniDopoFineMese = Column(Integer)
    SpostaFineAgostoDicembre = Column(SmallInteger, server_default=text("0"))
    UsaTSPay = Column(SmallInteger, nullable=False, server_default=text("0"))
    UsaPaypal = Column(SmallInteger, server_default=text("0"))
    NomeSpesaDefault = Column(ForeignKey('TSpese.NomeSpesa'))
    TS_CodPagam = Column(Integer)

    TSpese = relationship('TSpese')


class TAnagrafica(Base):
    __tablename__ = 'TAnagrafica'

    IDAnagr = Column(Integer, primary_key=True)
    CodAnagr = Column(String(50), unique=True)
    Nome = Column(String(255), nullable=False, index=True)
    Indirizzo = Column(String(255))
    Cap = Column(String(50))
    Citta = Column(String(255))
    Prov = Column(String(50))
    Regione = Column(String(255))
    Nazione = Column(ForeignKey('TNazioni.NomeNazione'))
    Referente = Column(String(50))
    Tel = Column(String(50))
    Cell = Column(String(50))
    Fax = Column(String(50))
    Email = Column(String(255))
    Pec = Column(String(255))
    CodiceFiscale = Column(String(50), index=True)
    PartitaIva = Column(String(50), index=True)
    Cliente = Column(SmallInteger, server_default=text("1"))
    Fornitore = Column(SmallInteger, server_default=text("0"))
    ScontiDefault = Column(String(50))
    IDListinoDefault = Column(String(50))
    PagamentoDefault = Column(ForeignKey('TPagamenti.NomePagamento'))
    CoordBancarieDefault = Column(String(255))
    NsBancaDefault = Column(ForeignKey('TRisorse.Risorsa'))
    Sdd_TipoIncasso = Column(String(50), nullable=False)
    Sdd_DataMandato = Column(Date)
    Fido = Column(Numeric(18, 4))
    AgenteDefault = Column(ForeignKey('TAgenti.Agente'))
    UsaRitAccontoDefault = Column(SmallInteger, server_default=text("0"))
    DocViaEmail = Column(SmallInteger, server_default=text("0"))
    CodIvaDefault = Column(ForeignKey('TIva.CodIva'))
    DichIntentoDefault = Column(String(50))
    DataDichIntentoDefault = Column(Date)
    ContoDefault = Column(ForeignKey('TConti.Conto'))
    PortoDefault = Column(String(255))
    VettoreDefault = Column(String(255))
    NoteDefault = Column(String(255))
    WarningNuovoDoc = Column(String(255))
    HomePage = Column(String(255))
    LoginWeb = Column(String(255), unique=True)
    Extra1 = Column(String(255))
    Extra2 = Column(String(255))
    Extra3 = Column(String(255))
    Extra4 = Column(String(255))
    Extra5 = Column(String(255))
    Extra6 = Column(String(255))
    Note = Column(String(20000))
    Fidelity_CodTessera = Column(String(50), unique=True)
    Fidelity_PuntiPartenza = Column(Integer, nullable=False, server_default=text("0"))
    Fidelity_PuntiGuadagnati = Column(Integer, nullable=False, server_default=text("0"))
    Fidelity_PuntiScalati = Column(Integer, nullable=False, server_default=text("0"))
    Tmp_DelMe = Column(SmallInteger, server_default=text("0"))
    FE_CodUfficio = Column(String(255))
    FE_RifAmmin = Column(String(20))

    TAgenti = relationship('TAgenti')
    TIva = relationship('TIva')
    TConti = relationship('TConti')
    TNazioni = relationship('TNazioni')
    TRisorse = relationship('TRisorse')
    TPagamenti = relationship('TPagamenti')


class TConfig(Base):
    __tablename__ = 'TConfig'

    IDUtente = Column(Integer, primary_key=True)
    ManArc_ApplName = Column(String(50), nullable=False)
    ManArc_ApplVersion = Column(Float, nullable=False, server_default=text("0"))
    ManArc_ApplRevision = Column(Numeric(18, 4), nullable=False, server_default=text("0"))
    ManArc_Password = Column(String(255))
    ManArc_Email = Column(String(255))
    ManArc_DataCreazioneDb = Column(Date)
    ManArc_DataUltimaCompress = Column(Date)
    ManArc_DataUltimoBackup = Column(Date)
    ManArc_NumAvviiDaCreazioneDb = Column(Integer, nullable=False, server_default=text("0"))
    ManArc_NumAvviiDaUltimaCompress = Column(Integer, nullable=False, server_default=text("0"))
    ManArc_NumAvviiDaUltimoBackup = Column(Integer, nullable=False, server_default=text("0"))
    ManArc_DbGuidPadre = Column(String(50))
    ManArc_DbGuid = Column(String(50))
    ManArc_Command = Column(String(50))
    ProfiloAttivita = Column(String(50))
    CurrencyString = Column(String(50), server_default=text("'L.'"))
    CurrencyFormat = Column(Integer, nullable=False, server_default=text("2"))
    CurrencyDecimals = Column(Integer, nullable=False, server_default=text("0"))
    CurrencyDecimalsPrezziAcq = Column(Integer, nullable=False, server_default=text("0"))
    NascondiValutaInDetailReport = Column(SmallInteger, server_default=text("0"))
    UsaEcoContrib = Column(SmallInteger, server_default=text("0"))
    NomeEcoContrib = Column(String(255))
    UsaSuoni = Column(SmallInteger, server_default=text("1"))
    GestAcc_Enabled = Column(SmallInteger, server_default=text("0"))
    GestAcc_MesiCambioPassword = Column(Integer, nullable=False, server_default=text("6"))
    GestAcc_MesiSospensUtente = Column(Integer, nullable=False, server_default=text("6"))
    GestAcc_PasswordSicure = Column(SmallInteger, nullable=False, server_default=text("0"))
    GestAcc_LogSeed = Column(String(255))
    Az_Nome = Column(String(255))
    Az_Nome2 = Column(String(255))
    Az_Indirizzo = Column(String(255))
    Az_Cap = Column(String(50))
    Az_Citta = Column(String(255))
    Az_Prov = Column(String(50))
    Az_Nazione = Column(ForeignKey('TNazioni.NomeNazione'))
    Az_CodiceFiscale = Column(String(50))
    Az_PartitaIva = Column(String(50))
    Az_Tel = Column(String(50))
    Az_Tel2 = Column(String(50))
    Az_Tel3 = Column(String(50))
    Az_Fax = Column(String(50))
    Az_Email = Column(String(255))
    Az_Pec = Column(String(255))
    Az_HomePage = Column(String(255))
    Az_RegistroImprese = Column(String(50))
    Az_Logo = Column(LargeBinary)
    Az_Extra1 = Column(String(255))
    Start_ShowDemoUpgradePro = Column(SmallInteger, server_default=text("0"))
    Start_ShowDemoUpgradeEnt1 = Column(SmallInteger, server_default=text("0"))
    Start_ShowDemoUpgradeNet = Column(SmallInteger, server_default=text("0"))
    Start_ShowBenvenuto = Column(SmallInteger, server_default=text("1"))
    Start_ShowAttivita = Column(SmallInteger, server_default=text("1"))
    Start_ShowFattElettr = Column(SmallInteger, nullable=False, server_default=text("1"))
    Start_ShowRinnovi = Column(SmallInteger, server_default=text("1"))
    Start_ShowPromemoria = Column(SmallInteger, server_default=text("1"))
    Start_ShowLavagna = Column(SmallInteger, server_default=text("1"))
    Start_NumFattElettrRicevute = Column(Integer, nullable=False, server_default=text("10"))
    Start_PagamInScadenzaFine = Column(String(50), nullable=False)
    Start_GgRinnoviInScadenza = Column(Integer, nullable=False, server_default=text("0"))
    Start_NumPromemoriaScaduti = Column(Integer, nullable=False, server_default=text("20"))
    Start_GgMemoInScadenza = Column(Integer, nullable=False, server_default=text("0"))
    Start_Lavagna = Column(Text)
    Art_TipologiaDefault = Column(String(50), nullable=False, server_default=text("'Art'"))
    Art_CodIvaDefault = Column(ForeignKey('TIva.CodIva'))
    Art_ClasseProvvDefault = Column(ForeignKey('TClassiProvv.ClasseProvv'))
    Art_MostraInTouchDefault = Column(SmallInteger, server_default=text("1"))
    Art_UsaDimensioniPeso = Column(SmallInteger, server_default=text("1"))
    Art_UsaGestMagazzino = Column(SmallInteger, server_default=text("1"))
    Art_MultiMagazz = Column(SmallInteger, server_default=text("0"))
    Art_UsaTracciabilita = Column(SmallInteger, server_default=text("0"))
    Art_UsaLottoPiuVecchio = Column(SmallInteger, server_default=text("0"))
    Art_UsaTaglieColori = Column(SmallInteger, server_default=text("0"))
    Art_CodAuto = Column(SmallInteger, server_default=text("0"))
    Art_NextCod = Column(String(50), nullable=False)
    Art_NomeExtra1 = Column(String(50))
    Art_NomeExtra2 = Column(String(50))
    Art_NomeExtra3 = Column(String(50))
    Art_NomeExtra4 = Column(String(50))
    Art_IDListinoDefault = Column(String(50), nullable=False)
    Art_IDListinoDefaultVbRf = Column(String(50), nullable=False)
    Art_PubblicaSuWebDefault = Column(SmallInteger, server_default=text("1"))
    Art_PubblicaSuWeb2Default = Column(SmallInteger, server_default=text("1"))
    Art_PubblicaSuWeb3Default = Column(SmallInteger, server_default=text("1"))
    Art_PubblicaSuAppAgentiDefault = Column(SmallInteger, nullable=False, server_default=text("1"))
    Art_UpdatePrezzoForn = Column(SmallInteger, server_default=text("0"))
    Art_ArrotondListini = Column(Numeric(18, 4), nullable=False, server_default=text("50"))
    Art_FmtCodBarreConPrezzoQta = Column(String(255))
    Art_FmtFileTerminaleBarcode = Column(String(255))
    Anagr_NomeExtra1 = Column(String(50))
    Anagr_NomeExtra2 = Column(String(50))
    Anagr_NomeExtra3 = Column(String(50))
    Anagr_NomeExtra4 = Column(String(50))
    Anagr_NomeExtra5 = Column(String(50))
    Anagr_NomeExtra6 = Column(String(50))
    Anagr_CodAuto = Column(SmallInteger, server_default=text("0"))
    Anagr_NextCod = Column(String(50), nullable=False)
    ContrPrev_Enabled = Column(SmallInteger, server_default=text("0"))
    ContrPrev_Nome = Column(String(50), nullable=False)
    ContrPrev_Perc = Column(Float, nullable=False, server_default=text("4"))
    ContrPrev_SoggettoRA = Column(SmallInteger, server_default=text("0"))
    DocT_UsaRitAcconto = Column(SmallInteger, server_default=text("1"))
    DocT_PercRitAccontoDefault = Column(Float, nullable=False, server_default=text("20"))
    DocT_PercRitAcconto2Default = Column(Float, nullable=False, server_default=text("100"))
    DocT_UsaRitVarie = Column(SmallInteger, server_default=text("1"))
    DocT_DescRitVarieDefault = Column(String(50))
    DocT_PercRitVarieDefault = Column(Float, nullable=False, server_default=text("20"))
    DocT_PercRitVarie2Default = Column(Float, nullable=False, server_default=text("100"))
    DocT_MassimaleRitVarie = Column(Numeric(18, 4))
    DocT_NomeExtra1 = Column(String(50))
    DocT_NomeExtra2 = Column(String(50))
    DocT_NomeExtra3 = Column(String(50))
    DocT_NomeExtra4 = Column(String(50))
    DocT_PagamentoDefault = Column(ForeignKey('TPagamenti.NomePagamento'))
    DocT_Pagam_PagatoInDocInclusi = Column(ForeignKey('TPagamenti.NomePagamento'))
    DocT_Pagam_PagamInDocIncludente = Column(ForeignKey('TPagamenti.NomePagamento'))
    DocT_Pagam_RegCorrisp = Column(ForeignKey('TPagamenti.NomePagamento'))
    DocT_Numeraz_AcqRevCharge = Column(String(255), nullable=False)
    DocT_AskBollo_Enabled = Column(SmallInteger, nullable=False, server_default=text("0"))
    DocT_AskBolloOrdPrev_Enabled = Column(SmallInteger, server_default=text("0"))
    DocT_AskBollo_Spesa = Column(ForeignKey('TSpese.NomeSpesa'), nullable=False)
    DocT_IvaPerCassa = Column(SmallInteger, server_default=text("0"))
    DocT_IvaPerCassa_DataFine = Column(Date)
    DocR_IncRigheEsistenti = Column(SmallInteger, server_default=text("1"))
    DocR_CodIvaFuoriCampo = Column(ForeignKey('TIva.CodIva'))
    DocR_NumDecQta = Column(Integer, nullable=False, server_default=text("0"))
    Mag_MagazzDefault = Column(ForeignKey('TMagazz.Magazz'), nullable=False)
    Ecr_Enabled = Column(SmallInteger, server_default=text("0"))
    Ecomm_NumSiti = Column(Integer, nullable=False, server_default=text("0"))
    Tmp_RicalcolaMagazz = Column(SmallInteger, server_default=text("0"))
    Tmp_RicalcolaListiniNettiIvati = Column(SmallInteger, server_default=text("0"))
    Tmp_ConvertiIva22 = Column(SmallInteger, server_default=text("0"))
    Tmp_RicalcolaTAnagrafica = Column(SmallInteger, server_default=text("0"))
    Tmp_RicalcolaDescDoc = Column(SmallInteger, server_default=text("0"))
    Touch_Enabled = Column(SmallInteger, server_default=text("0"))
    Touch_CodIva1 = Column(ForeignKey('TIva.CodIva'))
    Touch_CodIva2 = Column(ForeignKey('TIva.CodIva'))
    Touch_CodIva3 = Column(ForeignKey('TIva.CodIva'))
    Touch_CodIva4 = Column(ForeignKey('TIva.CodIva'))
    Touch_CodIva5 = Column(ForeignKey('TIva.CodIva'))
    Touch_DescIva1 = Column(String(255))
    Touch_DescIva2 = Column(String(255))
    Touch_DescIva3 = Column(String(255))
    Touch_DescIva4 = Column(String(255))
    Touch_DescIva5 = Column(String(255))
    Touch_NumCateg = Column(Integer, nullable=False, server_default=text("12"))
    Touch_NumBtnX = Column(Integer, nullable=False, server_default=text("5"))
    Touch_NumBtnY = Column(Integer, nullable=False, server_default=text("7"))
    Touch_Zoom = Column(Integer, nullable=False, server_default=text("100"))
    Touch_BtnFontSize = Column(Integer, nullable=False, server_default=text("8"))
    Touch_Buzzer = Column(SmallInteger, server_default=text("1"))
    Fidelity_Enabled = Column(SmallInteger, server_default=text("0"))
    Fidelity_EuroPerPunto = Column(Numeric(18, 4))
    Fidelity_ImportoIvato = Column(SmallInteger, server_default=text("0"))
    Fidelity_Soglie = Column(String(255))
    ExportComm_Email = Column(String(255))
    ExportComm_EmailIsPec = Column(SmallInteger, server_default=text("0"))
    ExportCommPdf_Enabled = Column(SmallInteger, server_default=text("0"))
    TS_Enabled = Column(SmallInteger, server_default=text("0"))
    TS_CodDitta = Column(String(5))
    TS_ContabSemplific = Column(SmallInteger, server_default=text("0"))
    TS_ExportPagamImmediati = Column(SmallInteger, server_default=text("0"))
    TS_ExportScadenzePagam = Column(SmallInteger, server_default=text("0"))
    Paypal_Email = Column(String(255))
    PayPal_LogoBig = Column(SmallInteger, server_default=text("0"))
    CervedPrem_Enabled = Column(SmallInteger, server_default=text("0"))
    CervedPrem_AutoCheckDoc = Column(SmallInteger, server_default=text("1"))
    ApertoDaDemo = Column(SmallInteger, server_default=text("0"))
    ApertoDaEdiz = Column(String(50))
    Cerved2_Enabled = Column(SmallInteger, nullable=False, server_default=text("1"))

    TClassiProvv = relationship('TClassiProvv')
    TIva = relationship('TIva', primaryjoin='TConfig.Art_CodIvaDefault == TIva.CodIva')
    TNazioni = relationship('TNazioni')
    TIva1 = relationship('TIva', primaryjoin='TConfig.DocR_CodIvaFuoriCampo == TIva.CodIva')
    TSpese = relationship('TSpese')
    TPagamenti = relationship('TPagamenti', primaryjoin='TConfig.DocT_Pagam_PagamInDocIncludente == TPagamenti.NomePagamento')
    TPagamenti1 = relationship('TPagamenti', primaryjoin='TConfig.DocT_Pagam_PagatoInDocInclusi == TPagamenti.NomePagamento')
    TPagamenti2 = relationship('TPagamenti', primaryjoin='TConfig.DocT_Pagam_RegCorrisp == TPagamenti.NomePagamento')
    TPagamenti3 = relationship('TPagamenti', primaryjoin='TConfig.DocT_PagamentoDefault == TPagamenti.NomePagamento')
    TMagazz = relationship('TMagazz')
    TIva2 = relationship('TIva', primaryjoin='TConfig.Touch_CodIva1 == TIva.CodIva')
    TIva3 = relationship('TIva', primaryjoin='TConfig.Touch_CodIva2 == TIva.CodIva')
    TIva4 = relationship('TIva', primaryjoin='TConfig.Touch_CodIva3 == TIva.CodIva')
    TIva5 = relationship('TIva', primaryjoin='TConfig.Touch_CodIva4 == TIva.CodIva')
    TIva6 = relationship('TIva', primaryjoin='TConfig.Touch_CodIva5 == TIva.CodIva')


class TAnagraficaContatti(Base):
    __tablename__ = 'TAnagraficaContatti'

    IDAnagr = Column(ForeignKey('TAnagrafica.IDAnagr'), primary_key=True, nullable=False)
    Contatto = Column(String(255), primary_key=True, nullable=False)
    RefAmmin = Column(SmallInteger, server_default=text("0"))
    Tel = Column(String(50))
    Cell = Column(String(50))
    Fax = Column(String(50))
    Email = Column(String(255))
    Pec = Column(String(255))
    Note = Column(Text)

    TAnagrafica = relationship('TAnagrafica')


class TAnagraficaDest(Base):
    __tablename__ = 'TAnagraficaDest'

    IDAnagr = Column(ForeignKey('TAnagrafica.IDAnagr'), primary_key=True, nullable=False)
    CodDest = Column(String(255), primary_key=True, nullable=False)
    SedeLegale = Column(SmallInteger, server_default=text("0"))
    SedeAmmin = Column(SmallInteger, server_default=text("0"))
    DestMerce = Column(SmallInteger, server_default=text("0"))
    Nome = Column(String(255), nullable=False)
    Indirizzo = Column(String(255))
    Cap = Column(String(50))
    Citta = Column(String(255))
    Prov = Column(String(50))
    Nazione = Column(ForeignKey('TNazioni.NomeNazione'))
    Tel = Column(String(50))
    Cell = Column(String(50))
    Fax = Column(String(50))
    Email = Column(String(255))
    Pec = Column(String(255))
    Note = Column(Text)
    Referente = Column(String(50))
    FE_CodUfficio = Column(String(255))
    FE_RifAmmin = Column(String(20))

    TAnagrafica = relationship('TAnagrafica')
    TNazioni = relationship('TNazioni')


class TArticoli(Base):
    __tablename__ = 'TArticoli'
    __table_args__ = (
        ForeignKeyConstraint(['NomeCategoria_Sott', 'NomeSottocategoria'], ['TSottocategorie.NomeCategoria', 'TSottocategorie.NomeSottocategoria']),
    )

    IDArticolo = Column(Integer, primary_key=True)
    CodArticolo = Column(String(50), unique=True)
    Desc = Column(String(2000))
    Tipologia = Column(String(50), nullable=False, server_default=text("'Art'"))
    NomeCategoria = Column(ForeignKey('TCategorie.NomeCategoria'))
    NomeCategoria_Sott = Column(String(255))
    NomeSottocategoria = Column(String(255))
    CodIva = Column(ForeignKey('TIva.CodIva'), nullable=False)
    ClasseProvv = Column(ForeignKey('TClassiProvv.ClasseProvv'))
    Udm = Column(String(50))
    PrezzoNetto1 = Column(Numeric(18, 4))
    PrezzoNetto2 = Column(Numeric(18, 4))
    PrezzoNetto3 = Column(Numeric(18, 4))
    PrezzoNetto4 = Column(Numeric(18, 4))
    PrezzoNetto5 = Column(Numeric(18, 4))
    PrezzoNetto6 = Column(Numeric(18, 4))
    PrezzoNetto7 = Column(Numeric(18, 4))
    PrezzoNetto8 = Column(Numeric(18, 4))
    PrezzoNetto9 = Column(Numeric(18, 4))
    PrezzoIvato1 = Column(Numeric(18, 4))
    PrezzoIvato2 = Column(Numeric(18, 4))
    PrezzoIvato3 = Column(Numeric(18, 4))
    PrezzoIvato4 = Column(Numeric(18, 4))
    PrezzoIvato5 = Column(Numeric(18, 4))
    PrezzoIvato6 = Column(Numeric(18, 4))
    PrezzoIvato7 = Column(Numeric(18, 4))
    PrezzoIvato8 = Column(Numeric(18, 4))
    PrezzoIvato9 = Column(Numeric(18, 4))
    FormulaPrezzo1 = Column(String(255))
    FormulaPrezzo2 = Column(String(255))
    FormulaPrezzo3 = Column(String(255))
    FormulaPrezzo4 = Column(String(255))
    FormulaPrezzo5 = Column(String(255))
    FormulaPrezzo6 = Column(String(255))
    FormulaPrezzo7 = Column(String(255))
    FormulaPrezzo8 = Column(String(255))
    FormulaPrezzo9 = Column(String(255))
    EcoContribNetto = Column(Numeric(18, 4))
    EcoContribIvato = Column(Numeric(18, 4))
    CodBarre = Column(String(50), unique=True)
    NumAltriCodBarre = Column(Integer, nullable=False, server_default=text("0"))
    IDFornitore = Column(ForeignKey('TAnagrafica.IDAnagr'), index=True)
    CodArticoloForn = Column(String(50), index=True)
    PrezzoNettoForn = Column(Numeric(18, 4))
    PrezzoIvatoForn = Column(Numeric(18, 4))
    NoteForn = Column(String(255))
    NumAltriForn = Column(Integer, nullable=False, server_default=text("0"))
    Url = Column(String(255))
    Produttore = Column(String(255))
    UdmDim = Column(String(50))
    DimNettaX = Column(Float)
    DimNettaY = Column(Float)
    DimNettaZ = Column(Float)
    DimImballoX = Column(Float)
    DimImballoY = Column(Float)
    DimImballoZ = Column(Float)
    UdmPeso = Column(String(50))
    PesoNetto = Column(Float)
    PesoLordo = Column(Float)
    GestMagazzino = Column(SmallInteger, server_default=text("0"))
    NumComponenti = Column(Integer, nullable=False, server_default=text("0"))
    NextLottoProdotto = Column(String(50))
    GgOrdine = Column(Integer, nullable=False, server_default=text("0"))
    OrdinaAMultipliDi = Column(Numeric(18, 4))
    QtaGiacenza_Import = Column(Numeric(18, 4))
    PrezzoMedioCarico = Column(Numeric(18, 4))
    PrezzoMedioScarico = Column(Numeric(18, 4))
    PrezzoUltimoCarico = Column(Numeric(18, 4))
    Extra1 = Column(String(255))
    Extra2 = Column(String(255))
    Extra3 = Column(String(255))
    Extra4 = Column(String(255))
    Note = Column(String(20000))
    PubblicaSuWeb = Column(SmallInteger, server_default=text("1"))
    PubblicaSuWeb2 = Column(SmallInteger, server_default=text("1"))
    PubblicaSuWeb3 = Column(SmallInteger, server_default=text("1"))
    PubblicaSuAppAgenti = Column(SmallInteger, nullable=False, server_default=text("1"))
    DescHtml = Column(Text)
    Taglie = Column(String(500))
    PathImmagine_Import = Column(String(255))
    MostraInTouch = Column(SmallInteger, server_default=text("1"))

    TClassiProvv = relationship('TClassiProvv')
    TIva = relationship('TIva')
    TAnagrafica = relationship('TAnagrafica')
    TCategorie = relationship('TCategorie')
    TSottocategorie = relationship('TSottocategorie')


class TImpegni(Base):
    __tablename__ = 'TImpegni'

    IDImpegno = Column(Integer, primary_key=True)
    DataOraInizio = Column(DateTime, nullable=False)
    DataOraFine = Column(DateTime, nullable=False)
    Oggetto = Column(String(255), nullable=False)
    Promemoria = Column(SmallInteger, server_default=text("0"))
    PromemoriaFatto = Column(SmallInteger, server_default=text("0"))
    Calendario = Column(ForeignKey('TCalendari.Calendario'), nullable=False)
    IDAnagr = Column(ForeignKey('TAnagrafica.IDAnagr'))
    NomeAnagr = Column(String(255))
    CellAnagr = Column(String(50))
    Note = Column(Text)

    TCalendari = relationship('TCalendari')
    TAnagrafica = relationship('TAnagrafica')


class TArticoliCodBarre(Base):
    __tablename__ = 'TArticoliCodBarre'

    IDArticolo = Column(ForeignKey('TArticoli.IDArticolo'), primary_key=True, nullable=False)
    CodBarre = Column(String(50), primary_key=True, nullable=False, unique=True)
    Qta = Column(Numeric(18, 4), nullable=False, server_default=text("1"))

    TArticoli = relationship('TArticoli')


class TArticoliColori(Base):
    __tablename__ = 'TArticoliColori'
    __table_args__ = (
        Index('TArticoliColori_I1', 'IDArticolo', 'CodColore', unique=True),
    )

    IDArticolo = Column(ForeignKey('TArticoli.IDArticolo'), primary_key=True, nullable=False)
    Colore = Column(String(255), primary_key=True, nullable=False)
    CodColore = Column(String(50), nullable=False)

    TArticoli = relationship('TArticoli')


class TArticoliForn(Base):
    __tablename__ = 'TArticoliForn'

    IDArticolo = Column(ForeignKey('TArticoli.IDArticolo'), primary_key=True, nullable=False)
    IDFornitore = Column(ForeignKey('TAnagrafica.IDAnagr'), primary_key=True, nullable=False)
    CodArticoloForn = Column(String(50), index=True)
    PrezzoNettoForn = Column(Numeric(18, 4))
    PrezzoIvatoForn = Column(Numeric(18, 4))
    NoteForn = Column(String(255))

    TArticoli = relationship('TArticoli')
    TAnagrafica = relationship('TAnagrafica')


class TArticoliMagazz(Base):
    __tablename__ = 'TArticoliMagazz'

    IDArticolo = Column(ForeignKey('TArticoli.IDArticolo'), primary_key=True, nullable=False)
    Magazz = Column(ForeignKey('TMagazz.Magazz'), primary_key=True, nullable=False)
    ScortaMin = Column(Numeric(18, 4), nullable=False, server_default=text("0"))
    Ubicazione = Column(String(255))
    QtaCaricata = Column(Numeric(18, 4), nullable=False, server_default=text("0"))
    QtaScaricata = Column(Numeric(18, 4), nullable=False, server_default=text("0"))
    QtaImpegnata = Column(Numeric(18, 4), nullable=False, server_default=text("0"))
    QtaInArrivo = Column(Numeric(18, 4), nullable=False, server_default=text("0"))
    DataPrimoCarico = Column(Date)
    DataUltimoCarico = Column(Date)
    DataUltimoScarico = Column(Date)

    TArticoli = relationship('TArticoli')
    TMagazz = relationship('TMagazz')


class TArticoliTaglie(Base):
    __tablename__ = 'TArticoliTaglie'

    IDArticolo = Column(ForeignKey('TArticoli.IDArticolo'), primary_key=True, nullable=False)
    Taglia = Column(String(255), primary_key=True, nullable=False)
    Ordinam = Column(Integer, nullable=False)

    TArticoli = relationship('TArticoli')


class TDiba(Base):
    __tablename__ = 'TDiba'

    IDArticolo = Column(ForeignKey('TArticoli.IDArticolo'), primary_key=True, nullable=False)
    IDDiba = Column(Integer, primary_key=True, nullable=False)
    IDComponente = Column(ForeignKey('TArticoli.IDArticolo'), nullable=False, index=True)
    Qta = Column(Numeric(18, 4), nullable=False, server_default=text("1"))
    Costo = Column(Numeric(18, 4))

    TArticoli = relationship('TArticoli', primaryjoin='TDiba.IDArticolo == TArticoli.IDArticolo')
    TArticoli1 = relationship('TArticoli', primaryjoin='TDiba.IDComponente == TArticoli.IDArticolo')


class TDocTestate(Base):
    __tablename__ = 'TDocTestate'
    __table_args__ = (
        ForeignKeyConstraint(['CodDest_IDAnagr', 'CodDest'], ['TAnagraficaDest.IDAnagr', 'TAnagraficaDest.CodDest']),
        Index('TDocTestate_I1', 'Data', 'TipoDoc', 'Num')
    )

    IDDoc = Column(Integer, primary_key=True)
    TipoDoc = Column(ForeignKey('TTipiDoc.TipoDoc'), nullable=False, index=True)
    IDAnagr = Column(ForeignKey('TAnagrafica.IDAnagr'), index=True)
    CodDest_IDAnagr = Column(Integer)
    CodDest = Column(String(255))
    Magazz = Column(ForeignKey('TMagazz.Magazz'))
    Data = Column(Date, nullable=False)
    Num = Column(Integer)
    Numeraz = Column(String(50))
    DataDoc = Column(Date, nullable=False)
    NumDoc = Column(String(50))
    DescDoc = Column(String(255))
    ContrPrev_Nome = Column(String(50))
    ContrPrev_Perc = Column(Float)
    ContrPrev_CodIva = Column(ForeignKey('TIva.CodIva'))
    ContrPrev_SoggettoRA = Column(SmallInteger, server_default=text("0"))
    ContrPrev_ImportoNetto = Column(Numeric(18, 4))
    ContrPrev_ImportoIvato = Column(Numeric(18, 4))
    Spese_Nome = Column(String(255))
    Spese_CodIva = Column(ForeignKey('TIva.CodIva'))
    Spese_ImportoNetto = Column(Numeric(18, 4))
    Spese_ImportoIvato = Column(Numeric(18, 4))
    TotNetto = Column(Numeric(18, 4), nullable=False, server_default=text("0"))
    TotIva = Column(Numeric(18, 4), nullable=False, server_default=text("0"))
    TotIvaDetr = Column(Numeric(18, 4), nullable=False, server_default=text("0"))
    TotDoc = Column(Numeric(18, 4), nullable=False, server_default=text("0"))
    TotIvaNonDovuta = Column(Numeric(18, 4), nullable=False, server_default=text("0"))
    TotIvaSplitPaym = Column(Numeric(18, 4), nullable=False, server_default=text("0"))
    RevCharge = Column(SmallInteger, nullable=False, server_default=text("0"))
    TotRitAcconto = Column(Numeric(18, 4), nullable=False, server_default=text("0"))
    TotRitVarie = Column(Numeric(18, 4), nullable=False, server_default=text("0"))
    TotDocNoRit = Column(Numeric(18, 4), nullable=False, server_default=text("0"))
    TotPrezzoAcquisto = Column(Numeric(18, 4), nullable=False, server_default=text("0"))
    TotGuadagno = Column(Numeric(18, 4), nullable=False, server_default=text("0"))
    ImportoSoggettoRA = Column(Numeric(18, 4), nullable=False, server_default=text("0"))
    PercRitAcconto = Column(Float, nullable=False, server_default=text("0"))
    PercRitAcconto2 = Column(Float, nullable=False, server_default=text("100"))
    DescRitVarie = Column(String(255))
    AnnoCompetenzaRitVarie = Column(Integer)
    TotEcoContribNetto = Column(Numeric(18, 4), nullable=False, server_default=text("0"))
    ScontiDefault = Column(String(50))
    IDListino = Column(String(50), nullable=False)
    UsaPrezzoIvato = Column(SmallInteger, server_default=text("0"))
    Includibile = Column(SmallInteger, server_default=text("1"))
    InclusoInIDDoc = Column(Integer, index=True)
    FattAcconto_IDDocSrc = Column(ForeignKey('TDocTestate.IDDoc'))
    NotaVariaz_IDDocSrc = Column(ForeignKey('TDocTestate.IDDoc'))
    FatturatoDaScorporare = Column(SmallInteger, server_default=text("0"))
    Pagamento = Column(ForeignKey('TPagamenti.NomePagamento'))
    Pagam_CoordBancarie = Column(String(255))
    Pagam_AccontoDaIncludere = Column(Numeric(18, 4))
    Pagam_AccontoFatturato = Column(SmallInteger, server_default=text("0"))
    Pagam_UltimaDataPagam = Column(Date)
    Pagam_ShowForzaSaldato = Column(SmallInteger, server_default=text("0"))
    Pagam_ForzaSaldato = Column(SmallInteger, server_default=text("0"))
    Pagam_Migrati = Column(SmallInteger, nullable=False, server_default=text("0"))
    Pagam_TotPagamenti = Column(Numeric(18, 4))
    Pagam_ImportoSaldato = Column(Numeric(18, 4))
    Pagam_ImportoDaSaldare = Column(Numeric(18, 4))
    Pagam_Saldato = Column(SmallInteger, server_default=text("0"))
    Vettore = Column(String(255))
    CausaleTrasporto = Column(String(255))
    AspettoBeni = Column(String(255))
    NumColli = Column(String(50))
    DataOraTrasporto = Column(String(50))
    Porto = Column(String(255))
    Trasp_Peso = Column(String(255))
    Trasp_CodSpedizione = Column(String(255))
    NoteInterne = Column(String(255))
    Extra1 = Column(String(255))
    Extra2 = Column(String(255))
    Extra3 = Column(String(255))
    Extra4 = Column(String(255))
    Note = Column(String(255))
    Anagr_Nome = Column(String(255))
    Anagr_Indirizzo = Column(String(255))
    Anagr_Cap = Column(String(50))
    Anagr_Citta = Column(String(255))
    Anagr_Prov = Column(String(50))
    Anagr_Nazione = Column(ForeignKey('TNazioni.NomeNazione'))
    Anagr_CodiceFiscale = Column(String(50))
    Anagr_PartitaIva = Column(String(50))
    Anagr_DestNome = Column(String(255))
    Anagr_DestIndirizzo = Column(String(255))
    Anagr_DestCap = Column(String(50))
    Anagr_DestCitta = Column(String(255))
    Anagr_DestProv = Column(String(50))
    Anagr_DestNazione = Column(ForeignKey('TNazioni.NomeNazione'))
    StatoOrdine = Column(String(50))
    DataPrevistaConclOrdine = Column(Date)
    Ord_InclusoInIDDoc_Last = Column(Integer)
    Ord_InclusoInIDDoc_Multi = Column(Integer)
    CausaleDoc = Column(String(255))
    Agente = Column(ForeignKey('TAgenti.Agente'))
    Agente_ImportoSoggettoProvv = Column(Numeric(18, 4))
    Agente_ImportoProvv = Column(Numeric(18, 4))
    Agente_DataLiquidazProvv = Column(Date)
    Rinnovo_Intervallo = Column(String(50), nullable=False, server_default=text("'Mesi_12'"))
    Rinnovo_Data = Column(Date, index=True)
    Rinnovo_Desc = Column(String(255))
    IvaPerCassa = Column(SmallInteger, server_default=text("0"))
    DescIvaPerCassa = Column(String(255))
    IvaDovutaEntroUnAnno = Column(SmallInteger, server_default=text("1"))
    DataIvaDovutaEntroUnAnno = Column(Date)
    TotIvaDovutaEntroUnAnno = Column(Numeric(18, 4))
    DataCompetenzaIva = Column(Date)
    Fidelity_EuroPerPunto = Column(Numeric(18, 4))
    Fidelity_ImportoIvato = Column(SmallInteger, server_default=text("0"))
    Fidelity_Punti = Column(Integer, nullable=False, server_default=text("0"))
    ContoVend = Column(ForeignKey('TContiVend.ContoVend'))
    TS_NoteComm = Column(String(68))
    Tmp_RicalcolaTotali = Column(SmallInteger, server_default=text("0"))
    Tmp_SyncTMovMagazz = Column(SmallInteger, nullable=False, server_default=text("0"))
    Tmp_DelMe = Column(SmallInteger, server_default=text("0"))
    DataOraStampa = Column(DateTime)
    NomeReport = Column(String(255))
    Ecr_CodLotteria = Column(String(8))
    Spes_ForzaComunica = Column(SmallInteger, server_default=text("0"))
    Spes_AcqIntraServizi = Column(SmallInteger, nullable=False, server_default=text("0"))
    Spes_AcqIntraBeni = Column(SmallInteger, nullable=False, server_default=text("0"))
    Spes_NonComunicare = Column(SmallInteger, server_default=text("0"))
    FE_TipoDoc = Column(String(4))
    FE_Causale = Column(String(200))
    FE_Bollo = Column(Numeric(18, 4))
    FE_Src_TipoDoc = Column(String(50))
    FE_Src_Num = Column(String(255))
    FE_Src_Data = Column(Date)
    FE_Src_Cig = Column(String(15))
    FE_Src_Cup = Column(String(15))
    FE_Src_Commessa = Column(String(100))
    FE_Src2_TipoDoc = Column(String(50))
    FE_Src2_Num = Column(String(255))
    FE_Src2_Data = Column(Date)
    FE_Src2_Cig = Column(String(15))
    FE_Src2_Cup = Column(String(15))
    FE_Src2_Commessa = Column(String(100))
    FE_Src3_TipoDoc = Column(String(50))
    FE_Src3_Num = Column(String(255))
    FE_Src3_Data = Column(Date)
    FE_Src3_Cig = Column(String(15))
    FE_Src3_Cup = Column(String(15))
    FE_Src3_Commessa = Column(String(100))
    FE_IDFepa = Column(Integer)
    FE_IDAgyoReg = Column(String(50), unique=True)
    FE_IDAgyo = Column(String(50), unique=True)

    TAgenti = relationship('TAgenti')
    TNazioni = relationship('TNazioni', primaryjoin='TDocTestate.Anagr_DestNazione == TNazioni.NomeNazione')
    TNazioni1 = relationship('TNazioni', primaryjoin='TDocTestate.Anagr_Nazione == TNazioni.NomeNazione')
    TAnagraficaDest = relationship('TAnagraficaDest')
    TContiVend = relationship('TContiVend')
    TIva = relationship('TIva', primaryjoin='TDocTestate.ContrPrev_CodIva == TIva.CodIva')
    parent = relationship('TDocTestate', remote_side=[IDDoc], primaryjoin='TDocTestate.FattAcconto_IDDocSrc == TDocTestate.IDDoc')
    TAnagrafica = relationship('TAnagrafica')
    TMagazz = relationship('TMagazz')
    parent1 = relationship('TDocTestate', remote_side=[IDDoc], primaryjoin='TDocTestate.NotaVariaz_IDDocSrc == TDocTestate.IDDoc')
    TPagamenti = relationship('TPagamenti')
    TIva1 = relationship('TIva', primaryjoin='TDocTestate.Spese_CodIva == TIva.CodIva')
    TTipiDoc = relationship('TTipiDoc')


class TGruppiArticoli(Base):
    __tablename__ = 'TGruppiArticoli'

    IDGruppo = Column(ForeignKey('TGruppi.IDGruppo'), primary_key=True, nullable=False)
    Ordinam = Column(Integer, primary_key=True, nullable=False)
    IDArticolo = Column(ForeignKey('TArticoli.IDArticolo'))
    Qta = Column(Numeric(18, 4), nullable=False, server_default=text("0"))

    TArticoli = relationship('TArticoli')
    TGruppi = relationship('TGruppi')


class TArticoliTaglieColori(Base):
    __tablename__ = 'TArticoliTaglieColori'
    __table_args__ = (
        ForeignKeyConstraint(['IDArticolo', 'Colore'], ['TArticoliColori.IDArticolo', 'TArticoliColori.Colore']),
    )

    IDArticolo = Column(Integer, primary_key=True, nullable=False)
    Colore = Column(String(255), primary_key=True, nullable=False)
    Taglia = Column(String(50), primary_key=True, nullable=False)
    CodBarre = Column(String(50), nullable=False, unique=True)

    TArticoliColori = relationship('TArticoliColori')


class TDocIva(Base):
    __tablename__ = 'TDocIva'

    IDDocIva = Column(Integer, primary_key=True)
    IDDoc = Column(ForeignKey('TDocTestate.IDDoc'), nullable=False)
    CodIva = Column(ForeignKey('TIva.CodIva'), nullable=False)
    ImportoNetto = Column(Numeric(18, 4), nullable=False, server_default=text("0"))
    Iva = Column(Numeric(18, 4), nullable=False, server_default=text("0"))
    IvaDetr = Column(Numeric(18, 4), nullable=False, server_default=text("0"))

    TIva = relationship('TIva')
    TDocTestate = relationship('TDocTestate')


class TDocRighe(Base):
    __tablename__ = 'TDocRighe'
    __table_args__ = (
        Index('TDocRighe_I2', 'IDDoc', 'IDDocRiga'),
    )

    IDDocRiga = Column(Integer, primary_key=True)
    IDDoc = Column(ForeignKey('TDocTestate.IDDoc'), nullable=False)
    IDArticoloScaricato = Column(ForeignKey('TArticoli.IDArticolo'), index=True)
    IDDocRigaIncluso = Column(ForeignKey('TDocRighe.IDDocRiga'), index=True)
    CodArticolo = Column(String(50))
    CodArticoloForn = Column(String(50))
    Desc = Column(String(2000))
    QtaShown = Column(Numeric(18, 4))
    Qta = Column(Numeric(18, 4))
    Udm = Column(String(50))
    Lotto = Column(String(50))
    DataScadenza = Column(Date)
    PrezzoNetto = Column(Numeric(18, 4))
    PrezzoIvato = Column(Numeric(18, 4))
    Sconti = Column(String(50))
    EcoContribNetto = Column(Numeric(18, 4))
    EcoContribIvato = Column(Numeric(18, 4))
    RitAcconto = Column(SmallInteger, server_default=text("0"))
    CodIva = Column(ForeignKey('TIva.CodIva'))
    ImportoNettoRiga = Column(Numeric(18, 4))
    IvaForzataRiga = Column(Numeric(18, 4))
    ImportoIvatoRiga = Column(Numeric(18, 4))
    EcoContribNettoRiga = Column(Numeric(18, 4))
    EcoContribIvatoRiga = Column(Numeric(18, 4))
    Conto = Column(ForeignKey('TConti.Conto'))
    MovMagazz = Column(SmallInteger, server_default=text("0"))
    QtaArrivata = Column(Numeric(18, 4))
    PercProvv = Column(Float)
    ImportoProvvRiga = Column(Numeric(18, 4))
    UdmPeso_Tmp = Column(String(255))
    Peso_Tmp = Column(Numeric(18, 4))
    PrezzoAcquisto = Column(Numeric(18, 4))
    ImportoAcquistoRiga = Column(Numeric(18, 4))
    GuadagnoRiga = Column(Numeric(18, 4))
    Note = Column(String(255))

    TIva = relationship('TIva')
    TConti = relationship('TConti')
    TArticoli = relationship('TArticoli')
    TDocTestate = relationship('TDocTestate')
    parent = relationship('TDocRighe', remote_side=[IDDocRiga])


class TPrimaNota(Base):
    __tablename__ = 'TPrimaNota'

    IDPrimaNota = Column(Integer, primary_key=True)
    IDGiroconto = Column(Integer, index=True)
    IDDoc = Column(ForeignKey('TDocTestate.IDDoc'), index=True)
    IDDocPrev = Column(ForeignKey('TDocTestate.IDDoc'))
    IsAcconto = Column(SmallInteger, server_default=text("0"))
    NomePagamDoc = Column(String(50))
    DataScad = Column(Date, nullable=False, index=True)
    DataPagam = Column(Date, nullable=False)
    Ordinam = Column(String(500), nullable=False)
    Risorsa = Column(ForeignKey('TRisorse.Risorsa'))
    CategPagamento = Column(String(50))
    Importo = Column(Numeric(18, 4), nullable=False, server_default=text("0"))
    IDAnagr = Column(ForeignKey('TAnagrafica.IDAnagr'))
    Desc = Column(String(255))
    RifPagam = Column(String(255))
    Saldato = Column(SmallInteger, server_default=text("0"))
    DataSollecito = Column(Date)
    DescSollecito = Column(String(255))
    Auto_Data = Column(Date)
    Auto_Importo = Column(Numeric(18, 4))
    ImportoIvaPerCassa = Column(Numeric(18, 4))
    Tmp_DelMe = Column(SmallInteger, server_default=text("0"))

    TAnagrafica = relationship('TAnagrafica')
    TDocTestate = relationship('TDocTestate', primaryjoin='TPrimaNota.IDDoc == TDocTestate.IDDoc')
    TDocTestate1 = relationship('TDocTestate', primaryjoin='TPrimaNota.IDDocPrev == TDocTestate.IDDoc')
    TRisorse = relationship('TRisorse')


class TMovMagazz(Base):
    __tablename__ = 'TMovMagazz'
    __table_args__ = (
        Index('TMovMagazz_I4', 'IDArticolo', 'Lotto'),
        Index('TMovMagazz_I5', 'IDArticolo', 'Magazz')
    )

    IDMovMagazz = Column(Integer, primary_key=True)
    IDArticolo = Column(ForeignKey('TArticoli.IDArticolo'), nullable=False, index=True)
    Magazz = Column(ForeignKey('TMagazz.Magazz'), nullable=False)
    Lotto = Column(String(50), index=True)
    DataScadenza = Column(Date)
    IDAnagr = Column(ForeignKey('TAnagrafica.IDAnagr'), index=True)
    Data = Column(Date, nullable=False, index=True)
    QtaCaricata = Column(Numeric(18, 4))
    QtaScaricata = Column(Numeric(18, 4))
    QtaImpegnata = Column(Numeric(18, 4))
    QtaInArrivo = Column(Numeric(18, 4))
    PrezzoNetto = Column(Numeric(18, 4))
    IDDocRiga = Column(ForeignKey('TDocRighe.IDDocRiga'), index=True)
    NumProduz = Column(Integer, index=True)
    Note = Column(String(255))
    Tmp_DelMe = Column(SmallInteger, server_default=text("0"))

    TAnagrafica = relationship('TAnagrafica')
    TArticoli = relationship('TArticoli')
    TDocRighe = relationship('TDocRighe')
    TMagazz = relationship('TMagazz')
