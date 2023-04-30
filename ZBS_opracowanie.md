### Modele bezpieczeństwa

**Model CIA**
- *confidentiality* 
  - poufność - tylko uprawniona para podmiotów może odtajnić przekaz
  - przykładowo wiadomość do wielu odbiorców szyfrowana jest strumieniowo kluczem symetrycznym, a zawartość tego klucza podlega zaszyfrowaniu indywidualnie przez każdego z odbiorców
  - skutkuje to tym, że wysyłamy tą samą wiadomość dla każdego i nikt spoza grupy nie będzie mógł odczytać jej zawartości
  - populityczne bezpieczeństwo = poufność (duże uproszczenie)
- *integrity*
  - zasada integralności mówi, o tym, że modyfikacja przekazu jest wykrywalna
  - nie dysponujemy narzędziami, które zabronią modyfikacji wiadomości, ale nas o tym fakcie poinformuję, czyli dysponujemy narzędziami, które zasygnalizują nam sytuację, w które została naruszona integralność
  -  możliwe jest też nie być w stanie, czy integralność została zachowana - wówczas korzysta się z alertów systemowych, które to komunikują
  -  integralność można naruszyć poprzez oczekiwanie na nieprawidłową reakcję użytkownika na taki alert
- *availability*
  - dostępność - zasób jest dostępny w czasie ustalonym przez dostawcę
  - trzeba zwracać uwagę na monitorowanie i dostępność systemu

**Model Parkera** 
- *utility* 
  - użyteczność informacji po zastosowaniu mechanizmów bezpieczeństwa
  - często wymuszenie rozluźnienia mechanizmów bezpieczeństwa
  - im system jest bardziej zabezpieczony - tym mniej jest użyteczny
  - firma wprowadziła programik, który blokował ekran po 3 minutach nieużywania - pracownicy pobierali swój, który wirtualnym klawiszem zapobiegał blokadzie
  - w efekcie wprowadzenie mechanizmu bezpieczeństwa tak naprawdę je obniżyło
- *authenticity* 
  - my nabieramy przekonania, że to jest prawdziwa wiadomość i jesteśmy w stanie potwierdzić tożsamość źródła przekazu
  - przykładowo uwierzymy, że `mojaPG` nie wysyła fałszywych informacji 
- *posession/control*
  - przekaz znajduje się pod kontrolą dysponenta

**Modell IAS Octave**
- *confidentiality* - poufność
- *integrity* - integralność
- *availability* - dostępność
- *accountability* - rozliczalność
- *non repudiation* - niezaprzeczalność - operacje podmiotu w interakcji z systemem
- *auditability* - audytowalność - cecha systemu nabudowywująca dodatkowe atrybuty 
- *authenticity, trustworthiness* - autentyczność i wiarygodność
- *privacy* - prywatność, powinny dostarczać rozwiązań odseparowujących różne sektory np. ortopeda nie powinien mieć dostępu do danych stomatologicznych
```
audytowalność != niezaprzeczalność
```

**Kryteria klasyfikacji zagrożeń**
- naruszany  mechanizm bezpieczeństwa
- natura podatności
- umiejscowienie kompromitowanego elementu
- charakter zagrożenia
    - atak celowany (APT) - napastnik pozostaje długi czas w ukryciu
    - atak niecelowany 
- rozproszenie ataku

**Aktualne motywacje cyberataków**
- przejęcie i utrzymanie kontroli nad stacją roboczą
- szpiegostwo przemysłowe 
- handel danymi
- cyberterroryzm
- dewastacja

**Sieci BOTNET**
- sieć maszyn zombie, nad którymi przejęto kontrolę
- zyskuje na popularności z powodu rosnącej dostępności środków pozwalających przejąć kontrolę nad stację roboczą
- pozyskiwanie dużych sieci stacji roboczych
- zapewnia podziemny rynek adresów e-mail, kont użytkowników, pozycjonowania stron
- sieci `fast-flux` - między skradzionymi maszynami przepływa ukryta sieć z niedozwolonymi treściami

### Ataki DDOS

`DoS (Denial of Service)` - podzbiór ataków odmowy świadczenia usług, wyczerpanie zasobów dowolnego elementu składowego systemu w sposób prowadzący do odmowy świadczenia usług

`DDoS (Distributed DoS)` - w wyczerpaniu zasobów systemu angażowna jest relatywnie duża liczba węzłów sieci, rozproszenie znacznie wpływa na trudność walki z takimi atakami

Napastnika trudno zlokalizować, bo korzysta ze stacji przesiadkowych, po czym posługuje się agentami, by wytworzyć "komin" tego ruchu atakującego. Zbierane są one w rdzeń sieci, przez który atak jest transportowany do sieci ofiary za pośrednictwem jakichś sieci pośredniczących.  

Bezpośrednio ofiarami takiego ataku są właściciele atakowanej infrastruktury, administratorzy i pracownicy zdalni. Pośrednie ofiary to klienci danej usługi, a czasami właściciele wykorzystywanych do odbicia ataku. 

### Klasyfikacja ataków `DDOS`

**Warstwa architektury loficznej**
 - warstwa sieciowa/transportowa
   - ataki zalewania i wykorzystujące specyfikę danej warstwy modelu `ISO-OSI`
   - przykładowo wykorzystanie protokołów niewiarygodnych i jednocześnie podszywania czy `SYN-flood`, `Smurf`
 - warstwa aplikacji
   - ataki wykorzystujące podatności warstwa wyższych lub konsstrukcję aplikacji i współzależności tworzących ją komponentów
   - bardzo niewygodne i trudne zapytania do bazy za pomocą frontendu - skutkiem czego baza się zapycha, a front dalej działa i ciągle tej bazie dokłada
   - przykłady to ataki sesyjne, asymetryczne, powolne żądania/odpowiedzi
 
**Cel ataku**
 - *host*
    - wyczerpanie zasobów
    - przeciążanie/ wyłączanie mechanizmów komunikacyjnych
    - błądy krytyczne systemu, wymuszanie restartu
  - *urządzenia sieciowe*
    - wysycenie zasobów routera, firewalla, systemów IDS/IPS
    - zalewanie łącza - aplikacje działają bardzo wolno albo będą rzucać timeout
  - *infrastruktura*
    - główne serwery DNS - bez nich Internet po prostu by upadł 
    - rządzenia tworzące rdzeń sieci Internet (transoceaniczne, `tier-1`)
  - *aplikacja*
    - najbardziej precyzyjna forma ataku
    - trudno wykryć atak metodami pośrednimi, bo pozostałe usługi serwera pozostają sprawne i przepływność ruchu sieciowego w granicach normy
    - narzędzia monitorowania dostępności i zagrożenia muszą posiadać świadomość przynajmniej fragmentu funkcjonalności aplikacji
    - wykorzystywanie konstrukcji aplikacji i jej relacji z innymi podsystemami np. serwery bazodanowe czy uwierzytelniania

**Usprawnienie ataku**
- fałszowanie adresów `IP` poprzez wykorzystanie adresów globalnych, prywatnych lub zabronionych np. `127.0.0.1, 0.0.0.0`
- atak wykorzystujący wzmocnienie 
  - atakujący generuje zapytanie relatywnie małej wielkości w imieniu ofiary 
  - serwer generuje odpowiedź o dużo większym rozmiarze (zapytanie do bazy danych lub HTTP)
  - podszywamy się pod ofiarę i pytamy wszystkich na ziemii o adres DNS 
  - parametrem siły ataku jest współczynnik wzmocnienia odpowiedzi np. dla DNS to 53, a dla SNP jest to 600
  - ogólnie wykorzystuje się tu usługi działające z protokołami niewiarygodnymi (`DNS, NTP, SNMP`) czyli aplikacje zbudowane na `UDP`


**OpenResolver** 
- otwarte serwery nazw
- udziela dowolnemu hostowi odpowiedzi o dowolną nazwę na świecie
- jeśli `DNS` nie znajdzie odpowiedzi to sam stara się ustalić odpowiedź
- generalnie to jest złe, bo nie filtruje się komu udzielamy odpowiedzi
- powinno to być podzielone na jakieś strefy lokalne, w kórych nie powinno się skąpić odpowiedzi
- na zewnętrznych interfejsach (podłączonych do sieci Internet) powinniśmy co najwyżej odpowiadać na wewnętrzną strefę
- projekt `OpenResolver` mapował jak w przestrzeni adresowej `IPv4` się takie frywolne serwery zachowują i określał ich zagęszczenie
- później z niego zrezygnowano, bo zamiast pomagać to pokazywał jedynie łatwe cele dla napastników

**Podziemna Klasyfikacja Ataków**
1. Ataki wolumetryczne (zalewanie)
   - grupa najmniej wyrafinowanych ataków - plujemy jak najwięcej w stronę ofiary
   - zwykle symetryczne względem ruchu odbieranego przez ofiarę i generowanego łącznie przez napastnika
2. Ataki semantyczne (podatności)
   - wykorzystujące specyfikę atakowanego rozwiązania protokolarnego/sprzętowego
   - zazwyczaj dotyczą powolnych żądań i odpowiedzi
   - bardziej efektywne z punktu widzenia napastnika
3. Ataki rozmyte (blended)
   - ukierunkowane na osiągnięcie innego efektu niż bezpośrednia odmowa świadczenia usług, zazwyczaj na trudną eliminację zagrożenia
   - atakujemy zwykłym `DoS` by odwrócić uwagę od jakiegoś miejsca, w którym można się spokojnie i wyrafinowanie kompromitować jakieś inne usługi

**Detekcja ataków DDoS**
- bardzo prosta po stronie ofiary, z wyjątkiem ataków na aplikację
- bardzo trudna po stronie napastnika
  - przechwyczenie rozkazu rozpoczęcia ataku - `Botnet-hijacking`
- relatywnie trudna po stronie agentów 
  - w ogólności wymagane rozpoznawanie nietypowej charakterystyki ruchu
  - jakby ktoś usiadł na tym kompie w trakcie ataku i sprawdzał połączenie, to dla niego byłoby to zazwyczaj w pełni normalne połączenie
  - adresy źródłowe pojawiają się tam za całego świata

**Kierunki działań obronnych**
- dobre praktyki
- usługi i rynkowe rozwiązania - skuteczne dla podzbioru ataków, kosztowne
- badania naukowe - podejście metodyczne, duża koordynacja

### **Klasyfikacja metod obrony**

**Miejsce obrony** - ze wględu na konsumowanie wielu zasobów w górę strumienia ataku, korzystne byłoby powstrzymanie go możliwe jak najbliżej źródła tj. przy agentach

**Obrona w sieci ofiary**
- ze względu na rozproszony charakter ataku duża trudność w odróżnieniu ruchu zamówionego od niezamówionego
- nawet jeśli uda się go rozróżnić, to pojawia się problem wydajności 
- mechanizmy śledzenia wstecz - wykorzystują znakowanie interfejsów ruterów w celu określeniaa rzeczywistego adresu nadawcy w przypadku podszywania się, jednak jest to złożone i pochłaniające dużo zasobów rozwiązanie
- mechanizmy wykorzystujące MIB tj. wykorzystywanie dostępnych statystyk ruchu
- znakowanie i filtrowanie pakietów z wykorzystaniem takich danych jak:
  - historyczne adresy IP u odbiorcy
  - liczba przeskoków `hop count`
  - identyfikacja ścieżek `path-id`
- proaktywne usuwanie pakietów - ruch TCP jest elastyczny i doskonale toleruje sytuację utraty pakietów, czyli legalny ruch na tym nie utraci
- w ogólności mechanizmy te nie są w stanie właściwie wykryć ataku i zareagować zanim dotrze do ofiary

**Obrona w sieci źródłowej**
- obrona w sieci źródłowej jest nieefektywna i niewydajna
- istnieją mechanizmy w ruterach brzegowych albo dostępowych  
- przykłady takich mechanizmów to filtry wejściowe i wyjściowe, porównanie ruchu z wzorcami czy analiza oparta na założeniu symetrii ruchu w obrębie sieci źródłowej
- słabe strony to trudność w odróżnieniu legalnego ruchu od ataku oraz bardzo duży narzut pamięciowy i obliczeniowy

**Sieć pośrednicząca**
- filtracja oparta na trasach - legalny ruch pochodzi zazwyczaj ze skończonego zbioru adresów i pojawienie się nietypowego adresu może świadczyć o podszywaniu 
- wykrywanie i filtrowanie ruchu ze złośliwych ruterów - obserwatorzy wykrywają rutery, które usuwają lub kierują pakiety na błędne trasy, z wykorzystaniem zasady zachowania przepływu między punktami końcowymi i sąsiadami
- inne mechaizmy mogą być oparte na zaufaniu do ruterów dostępowych lub mogą wymagać spróbkowania całego ruchu przekazywanego dalej
- metody te znacznie obciążają rutery, ale trwają badania nad próbą zmniejszenia tego narzutu

**Kooperacyjne mechanizmy**
- decyzja podejmowana na podstawie skoordynowanych działań w różnych miejscach sieci
- wykorzystanie sposobu nawiązania połączenia do otrzymywania uprawnień
- wykorzystanie autoryzacji źródeł ruchu w oparciu o kryptografię symetryczną 
- połączenie rozwiązań w sieci atakującego i rdzeniu - filtrowanie i indetyfikacja interfejsów, pozwala dotrzeć jedynie do agentów 
- aproksymacja topologii bronionej sieci i znalezienia drzewa ataku z pniem w węźle ofiary w oparciu o sieć nakładkową w modelu `P2P`
- zapobieganie fałszowaniu adresów `IP` i filtracja sygnaturowa 
- 

**Dobre praktyki**

1. Odłączenie ofiary od sieci i analiza off-line
   - niedostępność usługi dla użytkowników
   - ochrona innych zasobów
   - eliminacja nieprawidłowo obsługiwanych żądań
   - eliminacja sytuacji wyścigu
   - zmniejszenie szansy powodzenia ataku rozmytego
   - lepiej przeczekać niż naprawić
2. Blackholing
   - dostawca bierz na klatę ten atak
   - odfiltrowanie ruchu należącego do tatku wcześniej w górę strumieniana ruterach o wystarczających zasobach
   - efekt podobny do odłączenia ofiary, ale pozwalający funkcjonować pozostałej części usług
3. Stosowanie krótkich czasów życia wpisów DNS - przeniesienie nazwy domenowej pod inny adres `IP` 

**Usługi i rozwiązania rynkowe**

1. Rozwiązania sprzętowe
   - opierają się na prawidłowej implementacji stosu `IP` do poziomu warstwy aplikacji włącznie
   - najczęściej dedykowane dla aplikacji webowych
   - chronią przed atakami semantycznymi

2. Usługi ochrony przed atakami `DDoS`
   - typowo opierają się o techniki `Anycast` i rozproszenie geograficzne zasobów
   - dodatkowo zakładają znaczne przewymiarowanie sieci w celu oddalenia punktu wysycenia warstw

### Metryki zagrożeń

**Identyfikator CVE** 
- każde współczesne zagrożenie zmaterializowane w postaci podatności dotykającej dużej grupy systemów orzymuje identyfikator CV
- jest to system do klasyfikacji zagrożeń
- jak w gazetach pojawi się informacją, że w jakiejś firmie wykryto dużą lukę, to otrzymuje ona pewien numerek
- zadaniem tej organizacji jest rozstrzyganie jednoznacznościu tych numerów
- `CVSS` to stopień podatności, poziom zagrożenia w rzeczywistym środowisku, gdzie wartości są z przedziału od 0 do 10
- istnieją 3 wskaźniki `CVSS`
  - bazowy
  - chwilowy - odzwierciedla np. zmianę występowania gotowych exploitów w czasie 
  - środowiskowy - są to po prostu modyfikatory bazowego
- *exploitability* - jak trudno wykorzystać podatność 
  - access vector - wektor dostępu, przykładowo czy można wbić z sieci WAN
  - access complexity - czy wywołanie ruchu jest trudne
  - authentication - czy trzeba się uwierzytelnić i jak bardzo
- *impact metrics* - co dzieje się w momencie ataku
  - confidentiality - poufność
  - integrity - integralność
  - availability - dostępność

**Identyfikator CWSS**
- `CWSS` to niezależne od `CVSS` metryka przyznawana zagrożeniom
- wartości są w przedziale od 0 do 100, jest kilkaset kategorii
- odzwierciedla podatności niekoniecznie implementacyjne (w przeciwieństwie do `CVSS`) ale raczej słabości
- operuje na wyższym poziomie abstrakcji i ma pozwalać na przewidywanie materializacji zagrożeń

**Metryka CWRAS** - metryka zagrożenia z uwzględnieniem ryzyka

### **Rodzaje ataków**

**Atak statystyczny** 
- atak na szyfrowanie symetryczne z liniową operacją odzworowania ciągu jawnego w szyfrogram
- na podstawie częstości występowania znaków alfabetu kryptogramu i przy znajomości statystycznych właściwości alfabetu tekstu jawnego można odtajnić wiadomość znajdując odwzorowanie najczęściej występujących znaków 

**Atak siłowy (brute force)**
- klasa ataków na poufność i autentyczność, która polega na próbowaniu wszystkich kombinacji i sprawdzaniu rezultatu
- pesymistycznie próbujemy całą przestrzeń kombinacji, a statystycznie połowę
- atakowi siłowemu opierają się szyfry z kluczem jednorazowym, których długość stanowi największą wadę praktycznego stosowania

**Atak ze znanym tekstem jawnym**
- atak na poufność
- prowadzi do metodycznego odtajnienia sposobu w jaki deterministycznie szyfrowana jest wiadomość np. atak na enigme
- dotyczy szyfrów strumieniowych
- przyczynił się do znacznego przyspieszenia ataków na szyfrowanie `WEP` zmniejszając o kilka rzędów wielkość wymaganej próbki ruchu
- aktualnie ma znaczenie historyczne, bo większość algorytmów nosi cechy charakterystyczne dla kodów jednorazowych 

**Atak podsłuchiwania**
- atak na poufność
- polega na przejęciu informacji podczas aktu komunikacji charakteryzującej stan wiedzy jednej ze stron
- wymaga fizycznego dostępu do kanału komunikacyjnego w dowolnym fragmencie

**Atak powtórzenia**
- atak na autentyczność
- jeden z najbardziej popularnych ataków na stałą wartość pozwalającą uwierzytelnić jedną ze stron 
- przesyłana informacja uwierzytelniająca może być nawet zaszyfrowana, a jej odszyfrowanie niemożliwe - ale jest za to możliwe naruszenie jej autentyczności
- wymaga fizycznego dostępu do kanału komunikacyjnego w dowolnym fragmencie

**Atak podszywania**
- atak na autentyczność
- na podstawie znajomości informacji tajnych jednej ze stron przekazu można oszukać jedną ze stron komunikacji
- informację można albo przechwycić albo pozyskać kompromitując inne mechanizmy zabezpieczeń
- przykłady:
  - kradzież loginu lub hasła
  - podszywanie się pod adres `MAC/IP`
  - podszywanie pod sesję `HTTP` - kradzież cookie

**Atak dnia urodzin**
- atak na autentyczność - połączenie ataku podszywania i siłowego
- w celu zmaksymalizowania szansy ataku siłowego napstnik najpierw podszywa się pod ofiarę w celu wygenerowania żądań bardzo zbliżonych do oryginalnego ofiary
- żądania obsługiwane przez drugą komunikującą się stronę generują odpowiedzi dla wszystkich zapytań, spośród których wystarcza skompromitować jedno
- nazwa pochodzi od paradoksu dnia urodzin - dla 30 osób mamy 70% szans na to, że są dwie osoby, które mają urodziny tego samego dnia 

**Atak *Man in the middle***
- atak na autentyczność, który polega na realizacjia trzech składanych ataków:
  - podszywanie się pod stronę A
  - podszywanie się pod stronę B
  - podsłuchiwanie odszyfrowanej komunikacji w obu kierunkach
- wymaga dostępu do kanału komunikacyjnego w sposób, który pozwala zabronić legalnej komunikacji tj przerwać dany kanał komunikacyjny

### **Koncepcyjne rozwiązania bezpieczeństwa**

- mechanizmy proaktywne
  - sposób poświadczania tożsamości
  - zarządzanie tożsamością
  - filtrowanie ruchu
  - ochrona przed DDoS
- mechanizmy reaktywne
  - wykrywanie włamań
  - sygnaturowe rozpoznawanie zagrożeń (Spam)
  - korelacja zdarzeń
  - ochrona fizyczna

**Challenge Response**
- mechanizm zabezpieczający proces potwierdzenia autentyczności (uwierzytelniania)
- pozwala zabezpieczyć komunikację przed atakiem powtórzenia
- zamiast przesyłać nawet najbardziej zaszyfrowane dane, które jednoznacznie identyfikują jedną ze stron, przesyła się jej wyzwanie, które musi zostać przetworzone z użyciem współdzielonego sekretu
- strona weryfikująca tożsamość wykonuje analogiczną operację po swojej stronie - jeżeli odesłana wartość jest taka sama, nastąpiło poprawne uwierzytelnienie
- istotne jest zmienianie wartości wyzwania przy każdym uwierzytelnieniu

**Mechanizm  TOFU**
- trust on first use - zabezpiecza proces potwierdzania autentyczności 
- koncepcja oparta o powtarzalność procesu uwierzytelniania
- pierwsze uwierzytelnienie wymaga zaufania lub odrębnego kanału potwierdzania tożsamości
- każde następne korzysta z faktu wystąpienia poprawnego uwierzytelnienia za pierwszym razem

**Protokół SSH**
- bezpieczna alternatywa dla protokołu Telnet
- aktualnie rozbudowany protokół, pozwala na:
  - wykonywanie poleceń bez interaktywnej powłoki
  - przekierowywanie portów TCP
  - tunelowanie ruchu IP
  - uwierzytelnianie w oparciu o X.509
- pozwala korzystać z kryptografii asymetrycznej RSA, DSA i krzywych eliptycznych

**Infrastruktura klucza publicznego**

- wykorzystuje mechanizmy:
  - integralności - funkcja skrótu
  - autentyczności - podpis cyfrowy
  - poufności - szyfrowanie blokowe
- dostarcza mechanizmów wzajemnego uwierzytelniania
- pozwala bezpiecznie wymieniać klucze sesyjne i szyfrować komunikację
- pozwala zweryfikować tożsamość nieznanego serwera w oparciu o zaufaną trzecią stronę komunikacji
- implementowana w postaci standardu ITU-T X.509 
- zastosowanie:
  - szyfrownaie komunikacji
  - uwierzytelnianie komunikujących się podmiotów
  - podpis cyfrowy
  - znakowanie czasem (złożone obliczeniowo)

**Certyfikata PKI**
- standard X.509 definiuje pojęcie certyfikatu, który stanowi formę dokumentu elektronicznego podpisanego cyfrowo
- dokument zawiera
  - tożsamość zapisaną w sformalizowany sposób
  - czas ważności i przeznaczenie certyfikatu
  - podpis cyfrowy podmiotu poświadczającego tożsamość (CA)
  - adres, pod którym można zweryfikować listę odwoła certyfikatów z danego CA
- ścieżka certyfikacji
  - główny urząd podpisuje urząd podrzędny
  - urząd podrzędny podpisuje nam certyfikat
  - ścieżka weryfikacji idzie od nas do głównego urzędu certyfikacji
- aktualność certyfikatów
  - oprócz potwierdzenia spójności ścieżki certyfikatu należy sprawdzić także czas ważności i stan odwołania certyfikatu
  - stan odwołania można zweryfikować dzięki udostępnianym publicznie listom odwołań publikowanym przez Certificate Revocation Lists
  - status certyfikatu można zweryfikować samodzielnie lub z wykorzystaniem protokołów OSCP, PRQP, SCVP
- weryfikowanie certyfikatu
  - integralność - czy dane w certyfikacie nie uległy modyfikacji, weryfikacja podpisu nadrzędnego CA
  - występowanie w magazywnie certyfikatu głównego CA lub czy sam certyfikat jest znany i oznaczony jako zaufany
  - autentyczność - weryfikacja danych opisujących podmiot
  - przeznacznie, data ważności i stan odwołania certyfikatu
- zarządzanie certyfikatami
  - mechanizmy automatycznego wystawiania certyfikatów
  - uzyskiwanie certyfikatów dla witryn internetowych od podmiotów zewnętrznych nie bazuje na standardzie
- standardy PKCS
  - [7] format zapisu certyfikatów 
  - [10] standard żądania certyfikatu
  - [11] uogólniony interfejs dla tokenów
  - [12] przenoszenie materału kryptograficznego
- dodatkowe mechanizmy PKI to ponowne wykorzystywanie pary kluczy lub odzyskiwanie certyfikatów

**Podatności PKI**

- istotne jest dochowanie bezpieczeństwa podczas dostarczania certyfikatów głównych urzędów certyfikacji
- operowanie zbiorem zaufanych głównych urzędów certyfikacji proawdzi do nierozróżnialności prawidłowych łańcuchów certyfikacji
- rozwiązaniem może być wykorzystanie wspóloty agentów rozproszonych geograficznych
- w protokole `SSL/TLS` jednocześnie odbywają się dwa rodzaje negocjacji 
  - weryfikacja za pomocą loginu i hasła
  - przeglądarka weryfikuje tożsamość serwera
- weryfikacja polega na sprawdzeniu w odpowiedzi zgodności z nazwą domeny
- przebieg komunikacji w `SSL/TLS`
  - zgłoszenie do serwera
  - odpowiedź z certyfikatem
  - weryfikacja
  - wygenerowanie klucza symetrycznego
  - identyfikacja klienta
  - weryfikacja i odszyfrowanie klucza symetrycznego
  - szyfrowanie symetryczne
  
**SPAM i ochrona**

- problem polega na wysyłaniu wiadomości poprzez wykorzystywanie serwerów `open-replay` lub takich, które uwierzytelniają użytkownika, bez jego wiedzy
- wiadomości są wysyłane masowo i najczęściej z sfałszowanym adresem nadawcy
- rozwiązania ochrony przed spamem to: SPF, Sender ID, DK, DKIM
- `DMARC` to standard, który wspomaga sygnalizacją na potrzeby `SPF` i `DKIM` - wykorzystuje (nadużywa) cechy systemy DNS
  - działa w oparciu o rekordy TXT systemu DNS
  - rekordy sa publikowane przez właścicieli domen, który chcą zapewnić możliwość potwierdzenia autentyczności wiadomości pochodzącej z tej domeny
  - standaryzuje zapisy w polach TXT
  - dla określonej domeny dodawana jest subdomena _dmarc
  - jakie środki serwer odbiorcy powinien podjąć, jeśli było podszywanie się pod nadawcę (np serwery outlooka)


![image](../img/ZBS_02.PNG)

**SPF Secure Policy Framework**
- strasznie zacinało, nie dało rady słuchać

**DKIM**
- mechanizm będący rozszerzeniem standardu Domain Keys
- wymaga orkiestracji szeregu czynników w celu uwiarygodnienia nadawcy poczty e-mail
- składniki to:
  - rekordy DNS z informacjami o domenie nadawcy
  - nagłówki wysyłanych wiadomości z bezpiecznej domeny
  - komplety kluczy RSA, które pozwalają zweryfikować podpis w nagłówkach wiadomości z kluczami publikowanymi w DNS
- przebieg procesu:
  - jako właściciel domeny generujemy klucz prywatny i odpowiadający mu klucz publiczny
  - klucz publiczny publikujemy w DNS
  - dla każdej wysyłanej wiadomości wykonujemy operacje kryptograficzne z użyciem klucza prywatnego, które może weryfikować odbiorca wiadomości
  - odbiorca orientuje się, że w wiadomości są zawarte dodatkowe nagłówki 
  - potem udaje się do DNS po klucz publiczny i patrzymy czy podpis się zgadza
  - jeśli wszystko się zgodzi, to wiadomość ląduje w skrzynce odbiorczej
 
**Szyrowanie poczty elektronicznej**

- dobrą praktykę jest oddzielenie kluczy stosowanych dod szyfrowania i podpisu 
- wymagane dostarczenie kluczy i certyfikatów, żeby mogły być stosowane do podpisu i szyfrowania
  - szyfrowanie przebiega z użyciem klucza publicznego odbiorcy i własnego 
  - podpis przebieg z wykorzystaniem włąsnego klucza prywatnego
- aby zaszyfrowanie lub weryfikacja podpisu była możliwa wymagane jest zastosowanie mechanizmu udostępniania odpowiednich certyfikatów z kluczami publicznymi użytkowników
- po prostu musi być wiadome, gdzie szukać danego klucza publicznego
- wysyłanie tej samej wiadomości do kilku osób jednocześnie
  - nie szyfrujemy każdej wiadomości osobno 
  - najpierw generujemy klucz symetryczny i nim szyfrujemy wiadomość
  - potem klucz symetryczny zostaje zaszyfrowany kluczami publicznymi odbiorców
  - wysyłamy szyfrogram wiadomości wraz z szyfrogramami kluczy
  - odbiorca najpierw odszyfrowuje klucz symetryczny z wykorzystaniem swojego klucza prywatnego, a następnie tym symetrycznym samą już wiadomość

**Znakowanie czasem**

- jedna bardziej wymagających funkcjonalności realizowanych w oparciu o PKI
- możliwe funkcjonowanie w modelu rozproszonym lub scentralizowanym
- w modelu rozproszonym dodatkowym zabezpieczeniem jest włącznie poprzednio złożonego znacznika czasu do kolejnego
- tworzony jest w ten sposób weryfikowalny łańcuch następstwa czasowego operacji związanych ze znakowaniem czasem dokumentów

**PGP, OpenPGP i GPG**

- alternatywa dla hierarchicznej struktury PKI - `całkiem dobra prywatność`
- `PGP` jest rozwiązaniem komercyjnym
- oryginalnym zastosowaniem jest szyfrowanie poczty elektronicznej
- aktualnie wykorzystywane także do szyfrowania dysku 
- `PGP` pozwala tworzyć relacja zaufania nie tylko hierachicznie
- funkcjonalnie jest tworzona sieć zaufania, której cechą jest możliwość podpisania tożsamości innego podmiotu
- weryfikacja przebiega w oparciu o odtwarzanie łańcucha zaufania w postaci rozumowania
  - ja zweryfikowałem, że X to X i podpisałem jego klucz
  - X zweryfikował, że Y to Y i podpisał jego klucz 
- domyślne konfiguracje zakładają że jeśli utworzyłem relację zaufania z jakimś podmiotem, to ufam także podmiotom, którym on ufa bezpośrednio
- PGP może tworzyć struktury dowolne (nawet hierarchiczne), zatem można powiedzieć PKI zawiera się w PGP

### **Zasady bezpieczeństwa**

- zasada najmniejszego uprzywilejowania
  - podmiot otrzymuje minimalne prawa wymagane do wykonania okeślonego zadania
  - lista czynności także powinna podlegać zarządzaniu
  - przykłądem może być ograniczone liczba komend sudo w systemie linux lub brak uprawnień administratora na stacji roboczej windows
- obrona w głąb
  - wiele niezależnych od siebie warstw zabezpieczeń
  - przykładem może być dwuskładnikowe logowanie do systemu, antywirus, firewall korporacyjny, zapamiętane hasło w przeglądarce
- bezpieczeństwo przez niejawność 
  - niezalecana, krytykowana, ale praktykowana zasada
  - bezpieczeństwo oparte na niejawności rozwiązania, często konstrukcji
  - przykład to projekty closed-source vs open source lub steganografia
  - oparcie się na tym, że nikt nie wie jak działa algorytm/procedura
  - im więcej osób patrzy na rozwiązanie, tym staje się ono bardziej bezpieczne
- secure by design
  - rozwiązanie, którego podatności architektoniczne nie występują, albo zmniejszona jest ich relatywna liczba
  - w odniesieniu do systemów kryptograficznych funkcjonuje zasada Kerckhoffsa - *system powinien być bezpieczny także wtedy, gdy znane są wszystkie szczegóły jego działania, oprócz materiału kryptograficznego (kluczy)*
  
### **Podstawowe narzędzia bezpieczeństwa part 1**
- użytkownicy - zarządzanie katalogami
  - podstawowe zarządzanie grupami zasobów i użytkowników
  - uwierzytelnianie użytkownika do zbioru zasobów
  - hierarchiczne przydzielanie uprawnień
  - zakaz lub prawo do dziedziczenia uprawnień
  - kosztem jest trudność w teoretycznym określeniu uprawnień, niederministyczne zachowanie katalogu  
  - przykład to `Microsoft Active Directory`
- dane - szyfrowanie
  - mechanizmy autoryzacji oparte o tożsamość użytkownika
  - granularne przydzielanie uprawnień pojedynczym użytkownikom lub grupom
  - pierwsza wersja to szyfrowanie danych podczas transmisji
    - uwierzytelnianie użytkowników
    - zarządzanie kluczami szyfrującymi
  - druga wersja to szyfrowanie danych podczas przechowywania
    - wymagana znajomość strumieniowego klucza szyfrującego do odszyfrowania danych
    - klucz wprowadzany przez użytkownika lub zapisany na dysku
    - uzyskanie kluczy jako rezultat wzajmnego uwierzytelnienia w komunikacji międzysystemowej
  - `uwierzytelnienie` - sprawdzanie z kim mamy do czynienia 
  - `autoryzacja` - jeśli wiemy, z kim mamy do czynienia, to przydzielenie mu praw
- dane - centralne zarządzanie dostępem
  - zarządzanie na większą skalę wymaga:
    - centralnych mechanizmów uwierzytelniania
    - zadbania o wydajność serwerów uwierzytelniania
    - możliwości pracy z federacjami serwerów uwierzytelniających
    - możliwości delegacji zarządzania fragmentem infrastruktury 
  - protokół, który specyfikuje różnorodne możliwości uwierzytelniania, autoryzacji i rozliczania jest `IEEE 802.1x`

**Protokół 802.1X, RADIUS i EAP**
- specyfikuje jakie komponenty powinny brać udział w uwierzytelnianiu oraz relacje między tymi komponentami
- specyfikuje jakie protokoły, rozwiązania będą przydatne na styku tych komponentów
- ogólnie ustala relacje między składowymi mechanizmów uwierzytelniania, autoryzacji i rozliczania (`AAA`) niekoniecznie sam dostarczając rozwiązań
- działanie oparte głównie na protokole EAP, który podlega tunelowaniu w szeregu innych rozwiązań
- wykorzystuje się tutaj nie ramki `IP` tylko ramki `EAP over LAN` 
- popularne rozwiązanie to protokół RADIUS, który występuje między serwerem a suplikantem i składa się z serwera RADIUS oraz punktu dostępowego (przełącznika)
  - mamy tutaj 3 strony biorące udział w komunikacji
  - suplikant - podmiot, który podlega uwierzytelnianiu i autoryzacji
  - klient protokołu RADIUS - zezwala, zabrania albo doprecyzowuje zasady na podstawie których suplikant może uzyskać dostęp do sieci
  - serwer protokołu RADIUS - on tak naprawdę realizuje AAA względem suplikanta
  - opcjonalny jest jeszcze serwer usług uwierzytelniania LDAP
- `EAP` - rozszerzalny protokół uwierzytelniania, który pozwala na zastosowanie szeregu metod i protokołów uwierzytelniania i autoryzacji
  - podmioty serwera i suplikanta uwierzytelniają się wzajemnie
  - sposób uwierzytelniania każdej ze stron może być odmienny
  - niektóre korzystają z `X.509`, inne z loginu i hasła
- serwer RADIUS odpowiada za dispatchowanie, delegowanie procesu uwierzytelniania i odesłanie do tego, kto już może uwierzytelnić
- funkcjonalność rozliczania 
  - w protokole RADIUS nie przewidziano komunikacji inicjowanej od strony serwera
  - konieczne jest częste autoryzowanie suplikanta
  - serwer RADIUS nie może nikogo *wykopać* z usługi i trzeba projektować rozwiązania  typu *jak zajmuje łącze 5 minut, to ktoś go musi wykopać*
- protokół RADIUS definiuje szereg atrybutów, które podlegają wymianie z serwerem uwierzytelniania
- `MAC Authentication Bypass`
  - polega na uwierzytelnianiu w oparciu o adres MAC
  - pozwala uwierzytelniać IEE 802.1X na każdym porcie Ethernet
  - `NAS` uwierzytelnia je samoczynnie urządzenia za pomocą adresu MAC w przypadku, gdy nie obsługują one 802.1X
  - wymaga utrzymywania bazy adresów MAC
  - pozwala napastnikowi ominąć uwierzytelnianie poprzez podszycie się pod adres MAC

**Podstawowe narzędzia bezpieczeństwa part 2**
- aplikacje - skanowanie aplikacji
  - wykrywanie luk w istniejącym oprogramowaniu
  - skanowanie automatyczne (kod) vs testy penetracyjne (ludzie)
  - skanery podatności - z czasem się uniewrażliwiają i mogą przepuszczać stare wirusy
- infrastruktura - ochrona antywirusowa
  - oprogramowanie antywirusowe działa głównie w oparciu o sygnatury- jeśli ktoś kiedyś wykrył daną sygnaturę, to wtedy antywirus zadziała)
  - typowa konfiguracja firewall stanowych pozwala utrzymanie kontroli z sieci Internet nad stacją z firewallem
  - systemy `IDS/IPS` ewoluują w kiruneku *Deep Packet Inspection* oraz analizy behawioralnej
- infrastruktura - firewall
  - firewall bezstanowy
    - zawartość datagramu wystarcza do decyzji o przeznaczeniu pakietu
    - listy kontroli dostępu, to co było na pierwszej laborce
  - firewall stanowy
    - zawartość datagramu plus ruch sieciowy wcześniej przechodzący przez firewall
    - ruch przechodzący może być w przeciwnym kierunku
    - dwie zagregowane polityki (otwarta i zamknięta)
  - firewall aplikacyjny (zaawansowane rozwiązanie)
    - śledzenie sesji aplikacji np. ciastek w HTTP
    - interpretacja i filtrowanie zależne od funkcjonalności aplikacji
- `VPN` i rodzaje przenoszonych protokołów
  - L3 - tylko protokół IP
    - PPTP, L2TP, SSTP
    - WireGuard, IPsec
  - L3 + L2 - protokół IP i ruch Ethernet
    - OpenVPN
    - SoftEther
    - L2omGRE, DMVPN

**Standard IPsec** 
- rodzina standardów zabezpieczania komunikacji protokołem IP/IPv6
- protokoły bezpieczeństwa (transportowe) ESP i AH
- algorytmy uwierzytelniania (rozumianego jako integralność) i szyfrowania
- rozwiązania zarządzania kluczami - IKE
- bazowy komponent - security associations - mówią o tym co się dzieje, czy też dlaczego coś się dzieje z datagramami tego tunelu IPsec
- podstawowe drzewo decyzyjne

![img](../img/ZBS_03.PNG)
- protokół AH (Authentication Header, warstwa transportowa)
  - zapewnia uwierzytelnianie stron i przekazu
  - pod względem transportowym pozwala zapewnić integralność danych, ale nie poufność
- protokół ESP (Encapsulation Security Payload, warstwa transportowa )
  - zapewnia możliwość uwierzytelniania stron
  - pod względem transportowym pozwala zapewnić integralność i poufność danych
- tryb transportowy 
  - można utożsamiać go z trybem punkt-punkt
  - ograniczone zastosowanie, jeden z wariantów obejmuje zabezpieczenie komunikacji wewnętrznej
  - pozwala zabezpieczyć komunikacją między dwoma węzłami (nie segmentami)
  - nie są dodawane dodatkowe nagłówki protokołu IP
  - komunikacja odbywa się bezpośrednio między dwoma węzłami
- tryb tunelowy 
  - można go wykorzystać w komunikacji charakterystycznej dla rozwiązań VPN
  - można go wykorzystać do połączenia dwóch sieci LAN lub przykładowo do podłączenia komputera do sieci korporacyjnej 
  - pozwala zabezpieczyć komunikację między dwoma segmentami Ethernet
  - dodawane są nowe, dodatkowe nagłówki protokołu IP, co pozwala zabezpieczyć lub ukryć prawdziwe używane adresy, najczęściej prywatne
  - komunikacja odbywa się z użyciem koncentratorów VPN (urządzenia realizujące tunel VPN)

**IPsec - Security Association**
- dla zabezpieczenia komunikacji w protokole IPsec wykorzystywane jest tzw. SA
- SA jest jednokierunkowe
  - potrzeba dwóch SA, żeby zabezpieczyć dowolny dwukierunkowy kanał komunikacyjny
  - w szczególnym przypadku można wynegocjować różne zabezpieczenia w obu kierunkach
- właściwości CA 
  - jest identyfikowane przez SPI (Security Parameters Index)
  - podczas zestawiania SA uzgadniane są algorytmy kryptograficzne integralności (oraz poufności w przypadku ESP)
  - konkretne SA oznacza także konkretny wykorzystany klucz uwierzytelniający, który może podlegać wymianie
  - SA towarzyszy także numer sekwencyjny, który ma zapobiegać atakom powtórzenia
- na potrzeby zarządzania kluczami standard przeiwduje wykorzystanie następujących protokołów
  - IKE Internet Key Exchange (wersja 1 i 2)
  - ISAKMP - potencjalnie opcjonalny protokół zarządzania hierarchią kluczy, pozwala wygenerować sekret na sesję
- ponadto wykorzystywane są opcjonalnie protokoły, które nabudoują dodatkowe cechy negocjacji
  - Oakley - właściwość Perfect Forward Secrecy za sprawą negocjacji Diffie-Hellman
  - SKEME - szybka wymiana kluczy, anonimowosć
- alternatywa dla powyższych jest protokół KINK
  - możliwość negocjowania sekretów symetrycznych w oparciu o inne sekrety symetryczne
  - możliwość wykorzystywania kryptosystemu kerberos do centralnego zarządzania uwierzytelnianiem i negocjacją kluczy
  - rzadko stosowany
- podsumowujac IPSec może korzystać z
  - KINK (Kerberos)
  - IKE
    - ISAKMP - Oakley/SKEME
  - 

**IPsec - zarządzanie kluczami i uwierzytelnianie**
- w protokole ESP i AH całość zabezpieczeń SA opiera się na wynegocjowanym w bezpieczny sposób kluczu symetrycznym, znanym obu stronom
- w AH pełi rolę sekretu eliminującego możliwosćpodszywania i fałszowania pakietów
- w ESP oprócz tej samej roli pozwala dodatkowo utajnić przekaz (po stronie odbiorczej najpierw realizowane jest sprawdzenie integralności, następnie odszyfrowanie)
- klucz może być wynegocjowany jednorazowo (złe rozwiązanie) lub zarządzany z użyciem protokołu ISAKMP
- ISAKMP to protokół, który wykorzystuje komunikację po porcie 500/udp lub w przypadku NAT-T po porcie 4500/udp
- węzły które zestawiają połączenie IPsec mogą być identyfikowane na różne sposoby 
  - adres IP
  - nazwa domenowa
  - adres e-mail
  - identyfikacja może być nawet nie obowiązkowa
- IPsec pozwala wykorzystywać szereg rozwiązań do uwierzytelniania stron
  - PSK (Pre Shared Key) - klucz symetryczny
  - klucze RSA - strony muszą wzajemnie wymienić się swoimi kluczami publicznymi
  - certyfikaty X.509
  - a w szczególności rozwiązania protokołu EAP 

**IPsec - Protokoły IKE**
- Internet Key Exchange
- protokół wykorzystywany do uwierzytelniania stron od uzgodnienia wspólnego sekretu
- niezależnie od wersji działa w dwóch fazach:
  - main mode, profile
    - dotyczy parametrów samego protokołu IKE, sposobu uwierzytelniania stron negocjowania algorytmów itegralności i szyfrowania kluczy
    - nie wszystkie parametry mogą być negocjowane, część musi być uzgodniona poza protokołem
  - quick mode, proposal
    - dotyczy parametrów zabezpieczania danych w połączaniu VPN 
    - szyfrowanie, integralność, uwierzytelnianie źródła informacji (opcja w ESP)
- podczas zestawiania faz pierwszej i drugiej ustalany jest szereg parametrów, gdzie punktu widzenia bezpieczeństwa negocjowane są
  - algorytmy uwierzytelniania
  - długości kluczy symetrycznych
  - algorytm uzgadniania klucza symetrycznego
  - sam w sobie klucz symetryczny
- wśród najważniejszych parametrów uzgadanianych przez obie strony jest tzw. Traffic Selectors (TS)
  - TS oznacza jakiego ruchu będzie dotyczyła transformacja
  - typowo wskazuje podsieć źródłową i docelową w SA
  - czasami negocjowany dla transformacji punkt-punkt, co pozwala bardziej elastycznie zarządzać ruchem trafiającym do tunelu
    - jest to kompromis bezpieczeństwa
    - potencjalnie w tunelu może znaleźć się niepożącany ruch
  - ustaleniom podlega czas życia kluczy w fazach 1 i 2 
  - opcją może być obsługa DPD, gdzie strony dzielą się na inicjującą i odpowiadającą, co umożliwia i ułatwia detekcję awarii tunelu
- Protokół XAuth
  - w typowej eksploatacji IPsec występują dwa ograniczenia związane z obsługą scenariuszy *client to site*, bo był projektowany pod *site to site*
    - konieczność znajomości pary adresów IP po obu stronach
    - brak możliwości przydzielania adresów IP podczas zestawiania połączenia - czego skutkiem jest fakt, że trudno wyłonić traffic selector
  - jednym z rozwiązań tych problemów jest protokół XAuth

**IPsec - podsumowanie**
- zestawienie komunikacji IPsec typowo nie powoduje tworzenia nowego interfejsu w systemie
  - istnieją rozszerzenia, które pozwalają to obejść]
  - niedogodność może być rozumiana jako brak elastyczności tunelu 
- ruch podlega zabezpieczaniu na podstawie tzw. transformacji
  - transformacja wymaga klasyfikatora ruchu, który musi być zgodny po obu stronach
  - transformacja dotyczy wskazanych relacji IP np. w trybie tunelowym są to łączone tunelem podsieci IP
  - wewnętrznie w kernelu IPsec ma wyższy priorytet niż typowy routing, dlatego zanim datagram zostanie wysłany, podlega transformacji z użyciem sekretu charakterystycznego dla Security Association w tym kierunku
- jeśli mamy po obu stronach inną konfigurację IPsec, to jest przy stawianiu tunelu jest kupa roboty
  - złożoność rozwiązania
  - trudności w przenoszeniu i negocjowaniu ruchu zarządzającego (DHCP, DNS)
  - rozbieżności implementacyjne - przy zestawianiu dochodzi do tego, że urządzenia reaguje na banner drugiej strony i odpowiednio modyfikuje swoje zachowanie
  - przeznaczenie głównie pod *site to site*, a nie *client to site*

**Standard DNSsec**

- DNSSEC – Domain Name System Security Extensions - ochrona styku z siecią
- Rozszerzenie funkcjonalności protokołu DNS, które pozwala potwierdzić autentyczność odpowiedzi
  - wykorzystuje łańcuch zaufania odzwierciedlający hierarchiczną strukturę systemu DNS
  - wykorzystuje podpisy cyfrowe, nie korzysta z X.509
  - docelowo ma na celu eliminację możliwości podszywania w protokole DNS
    - napastnik musiałby znać/złamać klucz prywatny RSA, aby prawidłowo podpisać fałszywą odpowiedź
    - eliminowana jest możliwość wprowadzania nieistniejących wpisów
  - działa przy założeniu wartości rekordów DNS podpisanych zawczasu - serwery DNS nie są obciążane podpisywaniem każdej odpowiedzi osobno
- wszystkie informacje potrzebn do uwiarygodnienia będą przygotowywane *za wczasu*
- operuje zestawem kluczy
  - ZSK – klucz podpisujący rekordy w obrębie strefy
  - KSK – klucz podpisujący ZSK (jego fingerprint jest publikowany m. in. w domenie nadrzędnej) p
  - KSK podpisuje ZSK, więc jest *more important*
- Wprowadza dodatkowe rekordy:
  - DS – Delegation Signer - przechowuje skrót klucza publicznego KSK dla domeny delegowanej (podrzędnej)
  - RRSIG - Resource Record Signature - przechowuje podpisane rekordy DNS
  - DNSKEY - przechowuje klucze KSK (257) i ZSK (256) dla danej domeny
  - NSEC – Next Secure (historyczny)
    - przechowuje informacje o następnym zabezpieczanym rekordzie
    - odpowiada za spójność strefy
    - odpowiada za autorytatywną odpowiedź, że danego wpisu nie ma w strefie
    - umożliwiał pobranie wszystkich rekordów DNS strefy (!)
  - NSEC3 – następca rekordu NSEC
    - funkcjonuje podobnie, ale zwraca skrót wartości następnego rekordu, a nie samą wartość
    - nie eliminuje zgadywania i upewnienia się, że więcej
    wpisów w domenie nie ma
- do obsługi DNSsec zostały utworzone flagi do sprawdzania odpowiedzi
  - Flaga `AD`
    - Authenticated Data
    - flaga w odpowiedzi
    - potwierdza, że serwer sprawdził spójność danych w odpowiedzi
  - Flaga `DO`
    - DNSsec Ok
    - flaga w odpowiedzi od serwera
    - informuje klienta, że serwer obsługuje DNSSEC
  - Flaga `CD`
    - Checking Disabled
    - flaga w zapytaniu
    - informuje serwer, że klient akceptuje niesprawdzone odpowiedzi

**Podstawowe narzędzia bezpieczeństwa part 3**
- zarządzanie logami, raportowanie zgodności i regulacji
- Security intelligence -> bezpieczeństwo podstawowe
- Manualne przeglądanie dzienników zdarzeń (logów) - bardzo kosztowna
- Cykliczna analiza oprogramowaniem automatycznym - sprawdzanie np. czy jakiś port nie jest otwarty
- Cykliczne audyty bezpieczeństwa
  - pozwalają wychwycić niezgodność z polityką bezpieczeństwa
  - pozwalają wyłapać zagrożenia o niskim priorytecie z punktu widzenia bezpieczeństwa operacyjnego, np. nieużywane konta
  - zaniedbania na tym poziomie są częstym wektorem ataków celowanych (APT)

### **Zaawansowane narzędzi bezpieczeństwa**

**Użytkownicy**
- provisioning/deprovisioning - aktywacja pewnych zasobów na potrzeby pewnych akcji np. zestawienie i rozłączenie VPN
  - Funkcjonalność odpowiedzialna za zmapowanie usługi dostarczanej użytkownikowi na zasoby biorące udział w jej dostarczeniu
  - W przypadku sieci komputerowej może oznaczać np. rezerwację zasobów lub zestawianie kanału, np. VPN
  - Deprovisioning jest związany za zwalnianiem zasobów w sytuacji, kiedy nie są one już potrzebne
  - Najczęściej dotyczy usuwania obiektów w przypadku kiedy żaden użytkownik nie korzysta z określonej usługi np. rozłączenie łącza do Internetu
- zarządzanie dostępem i silne uwierzytelnianie
  - Rozwiązania SSO – Single Sign-on
  - Uwierzytelnianie dwu- i wieloskładnikowe
  - Uwierzytelnianie wielopoziomowe
  - rozwiązania IDM – Identity Management
    - opracowywanie szablonów uprawnień odpowiadających większości funkcji w korporacji
    - zarządzanie tożsamością na większej gamie urządzeń
  - wykorzystanie infrastruktury klucza publicznego (PKI)
- zarządzanie tożsamością
  - zarządzanie prawami dostępu do zasobów informacyjnych
    - kto może mieć dostęp do zasobów informacyjnych
    - jakie prawa są należne w systemach
  - systemy nadzorujące realizację tych ustaleń
  - zakres dostępu powinien być minimalny, ale zarazem wystarczający do pełnienia wyznaczonych obowiązków 
  - określenie zadań (ról) pracownika – przełożony
  - określenie wymaganych systemów i aplikacji – właściciel biznesowy
  - określenie uprawnień w systemach – właściciel biznesowy
  - nadanie uprawnień – administratorzy systemów
  - weryfikacja uprawnień – komórka bezpieczeństwa


**Dane**
- DAM (Database Activity Monitoring)
  - zewnętrzny mechanizm analizowania operacji zlecanych bazie danych
  - monitorowanie aplikacji, użytkowników uprzywilejowanych i wzorców ataku, np. SQLi
  - DAMP – DAM and Protection – zapobieganie wykonania pewnych operacji
- DLP systemy zapobiegania kradzieży lub wycieku danych
  - blokada portów we/wy
  - filtrowanie załączników
  - wykrywanie słów kluczowych i wzorców
  - ostrzeganie przed wykonaniem operacji lub blokowanie możliwości jej wykonania
  - zaglądają we wszystko co opuszcza aplikacje i sprawdzają, czy to jest dobra operacja
**Aplikacje**
- analiza kodu źródłowego
  - dopełnienie testów penetracyjnych black- i gray-box
- firewall aplikacyjny
  - WAF Web Application Firewall
  - znakomita większość usług działa w oparciu o protokoły HTTP/HTTPS
  - typowe filtrowanie ruchu nie pozwala rozróżnić aplikacji
  - operowanie bardzo granularnym rozróżnianiem aplikacji – możliwe np. udostępnienie GMail, ale nie np. Google Docs
  - wadą jest wymóg znajomości aplikacji w celu efektywnego jej odróżnienia
  - w przypadku HTTPS wymagane tzw. lawful interception – uprawnione podsłuchiwanie (inspekcja SSL); w Polsce wymagane powiadomienie użytkowników o stosowaniu tej praktyki, nie jest wymagana zgoda użytkowników
**Infrastruktura**
- bardziej elastyczne metody zarządzania aktywami przedsiębiorstwa
  - pełniejsze wykorzystanie ich potencjału
  - dostosowywanie możliwości infrastruktury do zmieniających się potrzeb biznesowych
  - zarządzania aktywami, konserwacją oraz łańcuchami dostaw zasobów i części
- zarządzanie bezpieczeństwem sieci
  - zintegrowane systemy filtrowania ruchu i reagowania na incydenty bezpieczeństwa
  - propagowanie sygnatur do wielopunktowej infrastruktury styku sieci
  - rozwiązania UTM – antywirus, antyspam, IDS, WAF w jednym
- standard IEEE 802.1AE - MACsec
  - Standard, który funkcjonalnie rozszerza standard IEEE 802.1X i jest wykorzystywany do uwierzytelniania i uzgodnienia wspólnego sekretu
  - Odpowiada za szyfrowanie ruchu sieciowego na poziomie każdej ramki (Ethernet)
  - wymaga zarządzania materiałem kryptograficznym w każdej pojedynczej domenie rozgłoszeniowej (hop-by-hop) - inaczej niż w szeregu rozwiązań End-to-end
  - ochrona na poziomie warstwy łącza danych
- MDM Mobile Data Management
  - MDM – Mobile Data Management
    - rozwiązania dla urządzeń mobilnych
    - pozwalają na provisioning aplikacji i lokalne źródła aplikacji
    - pozwalają na kontrolowanie funkcjonalności terminala mobilnego
    - zapewniają bezpieczeństwo data-in-motion oraz data-at-rest
    - funkcjonalność zdalnego usunięcia danych
  - terminale mobilne jako cienki klient
  - firewalle dedykowane dla środowisk wirtualnych
  - garbage-collectory – czyszczenie zwalnianych zasobów przed przydzieleniem ich innym maszynom
**Security Intelligence**
- SIEM - System Information and Event Management
  - gromadzenie informacji z dzienników zdarzeń w jednym miejscu
  - możliwość analizowania dzienników z wielu systemów
  - historia zdarzeń, korelowanie zdarzeń
  - za sprawą agentów następuja akwizycja i unifikacja zdarzeń
  - typowo oferowane są predefiniowane reguły korelacyjne, np. nieużywane konta w systemach (wykrywanie zdarzenia logowania występującego później niż zadany próg), wiele nieudanych prób logowania i następnie udana, logowanie na jedno konto z wielu adresów IP
  - możliwość tworzenia własnych reguł korelacyjnych
  - Przykłady: ArcSight (HP), QRadar (IBM), Splunk (OpenSource)
- gromadzenie śladu w ruchu sieciowym
  - pomoże nam to, gdy chcemy dotrzeć do wektora inicjującego atak malware 
  - Dopełnienie funkcjonalne systemów SIEM
  - Możliwość analizy wstecznej anomalii
  - Rozwiązanie problemu zaszyfrowanych informacji
  - Możliwość ograniczania inspekcji ruchu szyfrowanego np. z instytucjami finansowymi

### **Zoptymalizowane narzędzi bezpieczeństwa**
- użytkownicy
  - analityka ról
  - kontrola użytkowników (zwłaszcza uprzywilejowanych) 
  - ład w zarządzaniu tożsamością
- dane
  - analiza przepływu danych
  - ład w zarządzaniu danymi
- aplikacje
  - bezpieczne budowanie aplikacji
  - detekcja nadużyć
- infrastruktura
  - zaawanowane monitorowanie sieci
  - gromadzenie i analiza śladu
  - utwardzanie systemów
- security intelligence
  - zaawansowane wykrywanie zagrożeń
  - detekcja anomalii
  - predykcja w zarządzaniu ryzykiem

**Monitorowanie sesji uprzywilejowanych**
- dotyczy ruchu sieciowego związanego z zarządzaniem systemami informatycznymi
- rozwiązania pozwalają monitorować zarówno ruch przeszukiwalny, jak i inny
- obserwacja ruchu sieciowego z metadanymi systemu - może to być tekstowa lub graficzna 

### **Zarządzanei bezpieczeństwem**

**Cykl Deminga**
- bezpieczeństwo traktujemy jako proces
- `zaplanuj` -> `wykonaj` -> `sprawdź` -> `popraw`
- iteracyjny proces, który rozwiązuje takie problemy jak to, że klucze mogą być zbyt krótkie, poświadczenia mogły zaginąć
- na nim opiera się norma ISO 27000 

**Obszary w standardzie ISO 27000**
1. Polityka bezpieczeństwa
  - w skrócie - jak kategoryzujemy nasze zasoby na ważne (chronione) i ważniejsze (bardziej chronione)
  - zbiór spójnych, precyzyjnych reguł i procedur, według których dana organizacja buduje, zarządza oraz udostępnia systemy teleinformatyczne i dane
  - informacje, które zasoby i w jaki sposób mają być chronione
  - elementy składowe
    - model bezpieczeństwa
      - otwarty - można robić wszystko, co nie zostało zabronione, nowy zasób jest domyślnie `accept` 
      - zamknięty - można robić tylko to, co nie zostało zakazane, nowy zasób jest domyślnie `closed`
      - firewall agreguje oba modele - polityka zamknięta dla ruchu inicjowanego z sieci Internet i otwarta dla ruchu inicjowanego z wewnątrz
    - mechanizmy kontroli dostępu
    - poziomy uprawnień
    - mechanizmy identyfikacji i zapewnienie autentyczności (fizyczne i informatyczne)
    - śledzenie zdarzeń w systemie 
2. Organizacja bezpieczeństwa informacji
  - poziomy niejawności dokumentów zgodnie z ustawą o ochronie informacji niejawnych
    - ściśle tajne - lustracja, dużo rzeczy podlega pytaniu
    - tajne - rozbudowana kontrola
    - niejawne - krótka weryfikacja
    - jawne  
  - osoby muszą być poinformowane, że mają styczność z danymi niejawnymi np. znaki wodne
  - aktualnie trwają prace nad formalizacją tajemnicy przedsiębiorstwa
3. Bezpieczeństwo zasobów ludzkich
  - zapewnienie, by proces zapewniania bezpieczeństwa był na dobrym poziomie 
  - jeśli brakuje ludzi, to prowadzi się szkolenia umiejętności twardych
  - alternatywne źródło zasilania
  - włączenie zasobów do infrastrktury krytycznej
4. Bezpieczeństwo fizyczne i środowiskowe
  - redundancja światłowodów (struktura grafowa)
  - jeśli jakiś z nich padnie, to trafia do klienta inną drogą
  - należy unikać węzłów wysokiego stopnia
5. Kontrola dostępu
  - kamery muszą być instalowane parami
  - fuzja dwóch firm, które maja różne systemy autoryzacji
  - po takiej fuzji SA musi przepuszczać też pakiety z drugiego SA
6. Zarządzanie ciągłością działania
  - BCM - Business Continuity Management
  - dotyczy firm, których celeme dostarczanie jakiegoś medium, treści w sposób nieprzerwany
  - kategoryzowanie procesów pod względem krytyczności działania 
  - polityka ciągłości działania
    - odnosi się ściśle do organizacji, pozwala określić procesy krytyczne
    - elementem jest analiza ryzyka
  - strategia zachowania ciągłości działania
    - definiuje sposób postępowania organizacji w przypadku wystąpienia sytuacji kryzysowej
    - określa czasy odtwarzania do poziomu minimalnego i nominalnego (pełna funkcjonalność)
    - definiuje zakres akceptowalnej funkcjonalności minimalnej pozwalającej zachować ciągłość działania
  - plan ciągłości działania
    - struktura zarządzania kryzysowego
    - zasady postępowania w sytucjach kryzysowych
    - procedury i instrukcje awaryjne
    - pomijalna jest informacja o przyczynie awarii/ataku
  - planowanie ciągłości działania
    - podzbiór BCM, który realizowany jest w oparciu o ISO 22301
    - analiza ryzyka - kiedy podejmujemy ryzyko i ile nas ono kosztuje
    - analiza procesów biznesowych - co wchodzi w skład ścieżki kytycznej, kiedy jesteśmy w stanie pełnić usługę
    - identyfikacja kluczowych procesów - kiedy ludzie przestaną od nas kupowac, kiedy stracimy reputacę
    - utworzenie planów ciągłości działania  
    - wdrożenie PCD (BCP) 
    - testy wdrożonych systemów i procedur
    - szkolenia - podnoszą świadomośc i kulturę bzpieczeństwa na każdym etapie funkcjonowania systemów informatycznych
  - odwrócony paradygmat bezpieczeństwa - robimy aplikację tak głupią, że nie jest w stanie nic zepsuć
  - bezpieczne rozwijanie kodu
    - metodyki `OWASP`, `MISRA C`,`Microsoft Security Development Lifecycle`
    - `Common Weakness Enumeration` 
      - mówi o przypadkach wystąpienia danego zagrożenia oraz o błędzie jakim popełniono
      - bardzo dużo opisanych sytuacji wraz z przykładami
    - zautomatyzwane testowanie oprogramowania np. `Selenium`
    - narzędzia do statyczne i dynamicznej inspekcji kodu
7. Pozyskiwanie, rozwój i utrzymanie systemów informatycznych - częste aktualizowanie oprogramowania
8. Zarządzanie incydentami związanymi z bezpieczeństwem informacji
9. Zgodność z wymaganiami prawnymi i własnymi standardami
10. Zarządzanie aktywami, systemami i sieciami

**Standardy bezpieczeństwa**

- `PCI DSS` - Payment Card Industry Data Security Standard
  - specyfikuje zbiór działań, które należy przedsięwziąć
  - w ogólności interpretacja w niektórych przypadkach pozostaje niedoprecyzowana
  - dwanaście wymagań zebranych w sześć grup:
    - Build and Mantain a Secure Network and Systems
    - Protect Cardholder Data - ochraniaj dane właścicieli kart płatniczych
    - Maintain a Vulnerability Management Program - zarządzaj podatnościami tj. licz, sprawdzaj, eliminuj
    - Implement Strong Acces Control Measures - wdróż silne mechanizmy uwierzytelniania
    - Reguralrly Monitor and Test Networks - kto jest powiadamiany, do kogo do spływa 
    - Maintan an Information Security Policy
- `Common Criteria` - w polsce jest to norma ISO 15408
  - zalecenia mające na celu wprowadzeie ujednoliconego sposobu oceny systemów infrmatycznych pod względem szeroko rozumianego bezpieczeństwa
  - mówiątylko o tym, co należy zrobić, a nie w jaki sposób
  - mogą być stosowane zarowno doprduktów programowych, jak i sprzętowych
  - certyfikat stanowi dokument określający jedno z poniższych
    - zgodność tego systemu z określonym profilem zabezpieczenia
    - spełnienie wymagań bezpieczeństwa określonych w zadaniach zabezpieczenia 
    - przypisanie do konkretnego poziomu uzasadnionego zaufania EAL (4+ oznacza niszczenie danych w przypadku ataku)
  - poziomy uzasadnionego zaufania EAL
    - EAL4+ - *Methodically Designed, Tested and Reviewed*, odnosi się do sposobu zorganizowania dostępu do kluczy prywatnych, jest zapisem nieformalnym stosowanym przez producentów 
    - EAL5 - *Semiformally Designed and Tested*, karty chipowe, wybrane moduły HSM
    - EAL7 - *Formally Verified Design and Tested*, oprogramowae wybranej seri kart chipowych Gemalto

**Testy penetracyjne**

- audyt - sprawdzenie, czy rzeczywisty sposób działania lub uzyskiwania dostępu jest zgodny z założonym
- test penetracyjny - przełamanie zabezpieczeń informatycznych wynikające ze specyfiki systemu lub zastosowanych uniwersalnych rozwiązań
  - zwykle pozwala odkryć nieszablonowe podatności systemu jako całości
  - odróżnia się od skanowania podatności narzędziami automatycznymi
- metodologia prowadzenia testów penetracyjnych (analogia do procedury ataku)
  - określenie celu
    - zdefiniowanie wymagań klienta
    - podpisanie umów o poufości i biznesowej
    - okreśenie charakteru testów (white/black/gray)
    - określenie jawności - informowanie osób odpowiedzialnych za utrzymanie systemów o testach
    - zasięg testów - decyzja podejmowana w zakresie testów technikami inżynierii społecznej 
  - zbieranie informacji
    - pasywne zbieranie informacji
    - publicznie dostępne źródła
    - czynności nie noszą znamion przestępstwa komputerowego
    - często wykonywane jeszcze przed rozpoczęciem testów penetracyjnych
  - odkrywanie celu
    - pół pasywne zbieranie informacji
    - poznawanie celów wyszczególnionych w umowie
    - identyfikacja podsieci
    - rodzaj używanej architektury
    - określanie używanych systemów operacyjnych
    - wykonywane czynności ingerują w testowane zasoby w sposób nie budzący podejrzeń np. odwiedzenie strony, pasywne identyfikowanie systemów operacyjnych
  - enumeracja zasobów
    - pierwszy etap, który może wpłynąć na działanie systemu
    - aktywne zbieranie informacji
    - odkrywanie usług sieciowych
    - odkrywanie topologii sieci
      - aktywne urządzenia sieciowe
      - rodzaj urządzeń
    - informacje zebrane na tym etapie traktowane są jako punkt wyjścia do dalszych działań 
  - mapowanie podatności
    - etap odpowiedzialny za wykrywanie podatności w zindetyfikowanych systemach
    - testowanie
      - znanych podatności
      - nieznanych podatności - black box, analiza dynamiczna
      - podatności wynikających z konstrukcji systemu - analiza statyczna
    - OWASP ZAP, nmap NSE i OpenVAS
  - inżynieria społeczne
    - opcjonalny etap sprawdzania świadomości bezpieczeństwa pracowników firmy
    - można wykorzystywać zgromadzone do tej pory informacje o firmie
    - przygotowanie ukierunkowanego ataku socjotechnicznego
    - zwykle etap ma dość silnie zindywidualizowan charakter
    - kluczowe jest żeby target nie czuł się gorzej niż po wykonaniu analizy
  - kompromitacja celu
    - wykonanie penetracji wybranego systemu informatycznego
      - wybór wektora ataku
      - pokonanie występujących zabezpieczeń
    - cel kompromitacji
      - zdobycie wrażliwych danych osobowych
      - odcięcie systemu od sieci zewnętrznej
      - przerwanie ciągłości działania
      - *pivoting* - zdobycie maszyny, przygotowanie do etapu eskalacji uprawnień
  - eskalacja uprawnień
    - etap zwiększenia uprawnień w systemie, który został do tej pory skompromitowany
    - celem mogą być:
      - informacje w danym systemie
      - przejęcie kolejnego systemu
      - przygotowanie *pivot point* - miejsce utrzymania dostępu zdalnego
    - może angażować np. odzyskiwanie haseł z postaci niejawnej lub elewację uprawnień z konta nieuprzywilejowanego do uprzywilejowanego
  - utrzymanie dostępu
    - etap odpowiedzialny za skrócenie czasu dostępu do skompromitowanego systemu informatycznego
    - jeśli wektor ataku zakładał przejęcie kolejno kilku systemów, etap będzie odpowiadał za pozostawienie ukrytego wejścia do systemu z prawami już uprzywilejowanego użytkownika
      - ustanowienie połączenia zwrotnego
      - webshell
      - opcjonalnie wykorzystanie narzedzi ukrywania tunelu w innym ruchu sieciowym
  - dokumentacja i raportowanie
    - kluczowy etap testów penetracyjnych
    - typowo dwa rodzaje raportów - techniczny i dla kadry zarządzającej
    - zwykle związana z odpowiednim sposobem poinformowanie o znalezionych podatnościach
    - zbiór podatności powinien być możliwie duży
    - potencjalnie występuje ryzyko ograniczenia do przyjętego przez firmę realizującę test wektora ataku
    - dobrą praktykę jest kategoryzacja podatności zgodnie z określonym modelem 

**Automatyczne systemy testowanie bezpieczeństwa**

- OpenVAS 
  - darmowa platforma zarządzania bezpieczeństwem
  - możliwość pracy z podatnościami
  - możliwość zmiany priorytetów podatności
  - opóźnienie w feedzie podatności względem rozwiązań komercyjnych
- Nessus
  - komercyjne, popularne narzędzie
  - posiada wersję próbną i taką do zastosowań edukacyjnych
  - teoretycznie ma te same funkcjonalności co OpenVAS

**Bezpieczeństwo podstawowych usług IP**
- protokół ARP
  - możliwość podszywania - dowolna stacja może stwierdzić że to ona posiada dany adres IP
  - sytuacja wyścigu
  - możliwość nadpisywania wpisów w już istniejącej tablicy po stronie ofiary
  - obrona:
    - statyczne tablice/pojedyncze wpisy ARP 
    - monitorowanie zapytań - odpowiedzi ARP
    - MACsec - złożone rozwiązanie
- protokół DNS
  - ograniczona możliwość podszywania - w ogólności napastnik musi przewidzieć numer ID zapytania, które wysłał klient
  - możliwość generowania nazw domenowych podobnych do prawdziwych
  - obrona:
    - statyczne wpisy DNS - trudne zarządzanie
    - DNSsec - rozwiązuje problem narażając serwer na atak DoS
 - protokół DHCP
  - możliwość podszywania pod odpowiedzi (sytuacja wyścigu)
  - możliwość ataku DoS - można wydzierżawić wszystkie adresy IP
  - obrona:
    - autorskie rozwiązania konfiguracji serwera
    - DHCP snooping - nikt w sieci nie może odpowiadać na zapytania DHCP
 - ruting SLAAC IPv6 
  - SLAAC - mechanizm automatycznej konfiguracji lokalnego adresu IP i samoczynnego ogłaszania ruterów rozgłoszeniowymi multicast
  - możliwość ogłoszenia w sieci jednego lub więcej złośliwych ruterów (rogue)
  - obrona:
    - samodzielne konfigurowane filtrowanie komunikacji multicast
    - wykorzystanie DHCPv6 z zastrzeżeniami DHCP do IPv4










