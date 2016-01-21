##### EDA5 Project #####

'eda5.arhiv'#########################################################
- Dodati arhiv in osnovna arhivska mesta:  01:Arhiv,   RAC:Računovodstvo, NAR:Naročilnice
- Dodati -->  Arhiviral == current_user

'eda5.core'#########################################################
'eda5.deli'#########################################################

Prostor 8000:
- stene_01
- strop_01
- tlak_01
- razsvetljava
- vtičnice, stikala, termostati


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
- urediti filtriranje pri izbiri naročilnice po izbrani vrsti dokumenta (email, naročilnica, pogodba)
'eda5.partnerji'#########################################################
'eda5.predaja_lastnine'#########################################################
'eda5.planiranje'#########################################################
'eda5.posta'#########################################################
    # aktivnost

'eda5.pomanjkljivosti'#########################################################
'eda5.predpisi'#########################################################
'eda5.racunovodstvo'#########################################################
    class Likvidiranje računov --> samo računovodska dokumentacija "RAC". Popravi, da je vsa racunovodska 
    dokumentacija v skupini RAC
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

- Urediti filtriranje <option> v horizontal filter. Sedaj je uporabljen navaden MultipleSelection
- filtriranje pri izdelavi zahtevek izvedba del
- v najem se predaja samo prosto etažne lastnino - Uredi pri predaja_lastnine
- uredi PickDate pri dodajanju predaje lastnine

'eda5.zaznamki'#########################################################


### DODATNE APLIKACIJE ###

# - zavarovanja
#    *Sklenjena zavarovanje
#    *DelStavbe je lahko zavarovan po sklenjeni zavarovalni polici
# lokacije
# vnos pomankljivosti
# 
