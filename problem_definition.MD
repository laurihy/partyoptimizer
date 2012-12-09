Määrittelydokumentti 
====================

Lauri Hynynen / 013890647
lauri.hynynen@helsinki.fi
laurihy @ ircnet
+358 40 835 8689

1. Ongelmakuvaus
----------------

Ongelmana on Sitsi-juhlien optimaalinen istumajärjestys. Pöytäseurueella on merkittävä vaikutus juhlijan viihtyvyyteen ja toisaalta istumajärjestyksen laatiminen aiheuttaa paljon työtä järjestäjille. Hyvässä istumajärjestyksessä esimerkiksi ystävykset ja samoista asioista kiinnostuneet istuvat lähekkäin. 

Järjestäjillä on usein tietoa osallistujien taustoista ja toisaalta rakenteellisesti yhtenäistä tietoa voisi kerätä esimerkiksi yhdistämällä Facebook-profiilin suoraan ilmoittautumiseen. Yksinkertaistetaan ongelmaa kuitenkin olettamalla, että kyseinen tieto annettuna, eli sen hakemisesta ei tarvitse tässä algoritmissa välittää.

Ongelma voidaan näin ollen jakaa kahteen osaan. Ensinnäkin, miten yksittäistä istumajärjestystä arvioidaan olemassaolevien tietojen perusteella ja toisaalta miten tämän pohjalta pohjalta löydetään optimaalinen istumajärjestys.

2. Syöte ja tuloste
-------------------
Algoritmi ottaa syötteekseen pöytäkartan ja listan osallistujista. Tulosteena on istumajärjestys. Kaikki JSON-muodossa.


*2.1. Pöytäkartta*

Pöytäkartta voidaan kuvata verkkona, jossa vierekkäisten ja vastakkaisten istumapaikkojen välillä on kaaret. Jokainen istumapaikka on numeroitu. Verkon ei välttämättä tarvitse olla yhtenäinen, vaan verkon eri osat voivat kuvata eri pöytiä. Vieraisiin pöytiin ei huudella, joten verkko ei ota kantaa pöytien keskinäiseen sijoitteluun. 

Alla oleva verkko kuvaa kahta 6-paikkaista pöytää:

'0--1--2  6--7--8  
|  |  |  |  |  |
3--4--5  9--10-11'

Sama vieruslistaesityksenä ensimmäisen pöydän osalta:

'
0: [1, 3],
1: [0, 2, 4],
2: [1, 5],
3: [0, 4],
4: [1, 3, 5],
5: [2, 4]
...
'

*2.2. Osallistujat*

Osallistujat annetaan seuraavanlaisena listana, jossa avaimena id ja attribuutteina lista kavereiden id:istä, kiinnostuksen kohteista, avecin id ja sukupuoli:

'
1: {
	id: 1,
	kaverit: [3,4,5],
	kiinnostukset: ['ruoka','algoritmit','kalja'],
	avec: 5,
	sukupuoli: 'mies'
},
2: {
	id: 2,
	kaverit: [3,4],
...
'

2.3. Istumajärjestys

Istumajärjestys on lista, jossa indeksinä on istumapaikan numero (solmu verkossa) ja arvona siinä istuvan osallistujan id. 

1: 3,
2: 1,
3: 2,
...




3. Ratkaisutapa
---------------

Algoritmissa on 2 pääfunktiota. Ensimmäinen hakee parasta mahdollista istumajärjestystä ja toinen arvioi yksittäisen istumajärjestyksen sopivuuden. Alla karkea kuvaus molemmista. Voi tosin olla, että kehitystyön aikana suunnitelma muuttuu ja tarkentuu vielä.


3.1. Paras istumajärjestys.

Paras istumajärjestys löytyisi toki suoraan kokeilemalla kaikkia vaihtoehtoja. Kuitenkin, eri vaihtoehtoja on osallistujamäärän kertoman verran, eli pienilläkin sitseillä paljon, n = 10, 10! = 3628800. Ongelmasta muodostettava lineaarinen yhtälöryhmä olisi erittäin monimutkainen, ja näin ollen epäkäytännöllinen.

Järkevää onkin käyttää geneettistä algoritmia. Populaation alkioina ovat yksittäiset istumajärjestykset ja jokaisella iteraatiolla niistä valitaan sopivimmat. Parhaiden pohjalta muodostetaan uusi populaatio ja iteroidaan eteenpäin. Kun on käyty läpi tietty määrä iteraatioita tai löydetään alkio jonka sopivuus ylittää tietyn kynnyksen, keskeytetään ja palautetaan sopivin istumajärjestys.

Tämän algoritmin haasteena on toteuttaa hyvä tapa muodostaa vanhojen pohjalta uusi populaatio ja löytää sopivat arvot populaation koolle, iteraatioiden määrälle ja sopivuuskynnykselle.


3.2. Istumajärjestyksen sopivuus

Istumajärjestyksen sopivuus arvioi, miten hyvä yksittäinen istumajärjestys on.  Se ottaa syötteekseen pöytäkartan, osallistujien tiedot ja istumajärjestyksen. Paluuarvona on liukuluku välillä 0 ja 1. 

Sopivuutta varten jokaiselle osallistujalle lasketaan henkilökohtainen sopivuus, joiden pohjalta istumajärjestyksen sopivuus muodostetaan. Yksi isoimmista haasteista onkin löytää sopiva tapa arvioida näitä.

Yksittäisen osallistujan sopivuus voidaan joko laskea määrittämällä sopivuus erikseen jokaisen naapurin suhteen, tai muodostaa niistä jokin kokonaisuus. Esimerkiksi kolmen kaverin vieressä istuminen saattaisi saada huonommat pisteet, kuin kahden kaverin ja yhden sellaisen, joka on molempien kavereiden kaveri.

Toisaalta laskettaessa kokonaisuuden sopivuutta, on mahdollista keskittyä joko pelkästään keskiarvoon, tai esimerkiksi minimoida huonointa tapausta.

Olennaista on myös tehdä funktiosta riittävän nopea. Se suoritetaan hyvin monta kertaa haettaessa parasta mahdollista istumajärjestystä, joten sen tehokkuus vaikuttaa ratkaisevasti kokonaisuuteen.

Sopivuuden arviointiin liittyy paljon heuristiikkaa, eikä absoluuttisesti oikeaa ratkaisua ole olemassa. Olennaista onkin, että heuristinen osa on eriytetty optimoivasta osasta (istumajärjestyksen sopivuus vs. paras istumajärjestys), jolloin molempia voidaan kehittää erikseen.