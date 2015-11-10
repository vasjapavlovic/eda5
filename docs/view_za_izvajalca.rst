.. _glossary:

Pogled za Izvajalca Del
=======================

IZVEDBA DEL : DELOVNI-NALOGI
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Statusi delovnega-naloga:
    - V ČAKANJU
    - V PLANU
    - V REŠEVANJU
    - ZAKLJUČENI   



V ČAKANJU
---------

.. glossary::

    Namen:
        - Čakanje na potrditev nosilca izvedbe-del po delovnem-nalogu.

    Polja:
        - delovni nalog (oznaka)
        - opravilo
        - rok izvedbe
        - nosilec
        - nadzor

    Posebnosti prikaza:
        - delovne-naloge vidi samo nosilec (opcijsko vključi v nastavitev)

    Aktivnosti:
        - kliknemo na delovni-nalog

        - vnesemo "planirani datum izvedbe del" po delovnem-nalogu
            - datum ne sme biti čez rok-izvedbe-opravila
            - razpon dni med datumom "v planu" in "rok izvedbe" ne sme biti večji od "št_dni" <-- definiraj v opravilih

        - možnost vpisa zaznamkov (posebnosti) za nadzor
        - potrditev s klikom na "POTRDI"
        - po uspešni potrditvi (validacija) se status delovnega-naloga spremeni = "V PLANU"


V PLANU
-------

Aktivnosti:
    - vnos prvega dela = sprememba statusa delovnega-naloga = "V REŠEVANJU"



V REŠEVANJU
-----------

Aktivnosti:
    - s pritiksom na zaključi delovni-nalog se status spremeni = "ZAKLJUČENO"
    - delovni-nalog se avtomatsko natisne. Kasnejše tiskanje je možno pod
    zaključeni delovni-nalogi

ZAKLJUČENI
----------

Podatki:
    - Podatki o OPRAVILU in DELOVNEM NALOGU
    - 
    -

Dodatne opcije:
    - možnost tiskanja delovnega naloga

