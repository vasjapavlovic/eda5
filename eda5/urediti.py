##### EDA5 Project #####

'eda5.arhiv'#########################################################
    Arhiviranje --> Relacije na račune, zahtevke itd je prenesti v ArhivMesto!
'eda5.core'#########################################################
'eda5.deli'#########################################################
'eda5.delovninalogi'#########################################################
    #1 opravilo_create : uredi, da se da dodajati elemente many-to-many
    #2 vnos delovnega naloga za INTERVENCIJSKA DELA (ročni vpis podatkov, ko je čas)
    - opravilo from vzorec opravila :  rok izvedbe naj se izdela kot zadnje izdelan + perioda

'eda5.skladisce'#########################################################
'eda5.etaznalastnina'#########################################################
'eda5.katalog'#########################################################
'eda5.import'#########################################################
'eda5.lastnistvo'#########################################################
'eda5.moduli'#########################################################
'eda5.narocila'#########################################################
- seznam naročil
- detail naročila
- novo naročilo ustno
- novo naročilo naročilnica/pogodba
'eda5.partnerji'#########################################################
'eda5.predaja_lastnine'#########################################################
'eda5.planiranje'#########################################################
'eda5.posta'#########################################################
    # aktivnost
        ''' Ibira Prejeta Pošta ali Izdana Pošta. Kasneje ni pravilna rešitev.
        Popraviti je:   nastavitev podjetja v globalnih nastavitvah. Če je pri naslovnik pošte podjetje
        gre za prejeto pošto. Če je pošiljatelj nastavljeno podjetje gre za izdano pošto '''

'eda5.pomanjkljivosti'#########################################################
'eda5.predpisi'#########################################################
'eda5.racunovodstvo'#########################################################
'eda5.razdelilnik'#########################################################
'eda5.stevci'#########################################################
'eda5.users'#########################################################


'eda5.zahtevki'#########################################################
    #1 Povpraševanje
    #2 Analiza
    #3 ŠkodniDogodki
        # mogoče dodaj pisanje dnevnika reševanja
        # Dodati opis poškodovanih stvari
    #4 Sestanek
        # podzahtevkom omogoči dodajanje udeležencev (glej ZahtevekSestanekCreateView)
    - zahtevek predaja v posest
    - zahtevek predaja v najem

- Urediti filtriranje <option> v horizontal filter. Sedaj je uporabljen navaden MultipleSelection
- filtriranje pri izdelavi zahtevek izvedba del

'eda5.zaznamki'#########################################################


### DODATNE APLIKACIJE ###

# - zavarovanja
#    *Sklenjena zavarovanje
#    *DelStavbe je lahko zavarovan po sklenjeni zavarovalni polici
# lokacije
# vnos pomankljivosti
# 
