# Summary of the document Lekcja kursu AI_Devs, S03L03 — Wyszukiwanie i bazy wektorowe

### Notatka

Sesja 3, Lekcja 3 z kursu AI_Devs skupia się na wykorzystaniu LLM (długoterminowej pamięci modelu) do budowania systemów **z hiper-personalizacją** i **częściowo autonomicznymi zachowaniami**.

Bazą do tego jest wykorzystanie **baz wektorowych**. Bazy te służą do przechowywania i przeszukiwania informacji, które zostały przekształcone na wektory przy użyciu technik tokenizacji i embeddingu. Przykładem takiego procesu jest porównanie wektorów za pomocą metody **cosine similarity**. 

Krótko mówiąc, bazy wektorowe przeprowadzają dla nas obliczenia związane z podobieństwem wektorów, zwracając nam wyniki z "similarity score". Na podstawie tego wyniku możemy wybrać tylko te wpisy, które są najbardziej zbliżone znaczeniem do zapytania. 

Przykładowy obrazek procesu znajduje się [w tej lokalizacji](https://cloud.overment.com/store-e4ff3078-b.png), pokazuje on proces dodawania danych do indeksu takiej bazy. Zaznacza też wagę metadanych, które zapisujemy razem z wektorem. W metadanych zawieramy między innymi identyfikator wpisu i inne dane szczegółowe dotyczące dokumentu. 

W lekcji omówiono również zasady funkcjonowania **Similarity Search**, czyli wyszukiwania poprzez podobieństwo. Możemy to robić za pomocą baz wektorowych. Schemat takiego wyszukiwania prezentuje się [tak](https://cloud.overment.com/similarty-1695814767.png). W skrócie, wynik wyszukiwania to lista embeddingów i score pokazujący, jak bardzo są one zbliżone do wprowadzonego zapytania.

W lekcji znajduje się również kod **21_similarity**, który pokazuje jak zbudować dynamiczny kontekst na podstawie wprowadzanych przez użytkownika danych. Wykorzystuje on bibliotekę **HNSWLib** jako in-memory vector store. Kontekst budowany jest na podstawie podobnych dokumentów znalezionych na podstawie zapytania. 

W dalszych lekcjach planowane jest omówienie tematów związanych z pracą z bazami wektorowymi przy użyciu podejścia no-code.

# Notatka z S03L03 kursu AI_Devs, Wyszukiwanie i bazy wektorowe

W tej części kursu rozmawiamy o przeszukiwaniu i bazach wektorowych. Szczególnie skupiamy się na wykorzystaniu **Hybrid Search and Retrieval Augmented Generation** i metadanych w procesie wyszukiwania.

Najważniejsze fakty:

- Metadane są kluczowe dla skojarzenia danych. Eksperymentuj z differentującymi poziomami topK (liczba zwracanych rekordów) dla uzyskania więcej informacji do przefiltrowania.
  
- Filtry mogą być używane podczas samego procesu wyszukiwania. 

- Wyszukiwanie hybrydowe to zestawienie różnych technik wyszukiwania dla otrzymania maksymalnej efektywności. Jest zwykle wykorzystywane we LLM pod nazwą HSRAG. 

- Podział dłuższych tekstów na małe fragmenty (długie na tyle, by zawierały pełne informacje i nie zaburzały kontekstu) jest kluczowy dla efektywnego wyszukiwania.

- Budując bazę wiedzy, należy unikać mieszania języków. Instrukcje do bazy powinny być kierowane w języku, w którym baza jest zbudowana. 

- Fragmentacja to problem, który często występuje, gdy interesujące informacje są podzielone na kilka fragmentów. Można mu przeciwdziałać zwiększając limit wyszukiwania dokumentów, ale powoduje to również wzrost niepełnych wyników. 

- W kolejnych lekcjach dowiemy się więcej o radzeniu sobie z fragmentacją.  

- Praca z różnymi formatami plików jest wymagająca. Kluczową koncepcją, którą powinniśmy wykorzystać, jest uniwersalność i dowolność.

Kolejne cele:

- Zastosowanie wiedzy z poprzednich lekcji do pracy z różnymi formatami plików. 

- Budowa zestawu danych na podstawie informacji o nas, twórcach AI_Devs, bezpośrednio ze strony aidevs.pl.

Ressource: 

- Przykład "11_docs", wykorzystywanie metadanych do opisania danych
- Przykład "22_simple", zebranie trzech dokumentów w jednym programie
- Przykład "23_fragmented", podejście do problemu fragmentacji
- Przykład "24_files", organizacja i dostosowanie danych

Zdjęcia użyte w lekcji:

- ![chunks-2033514e-7](https://cloud.overment.com/chunks-2033514e-7.png)
- ![simple-2adcdec1-f](https://cloud.overment.com/simple-2adcdec1-f.png)
- ![miss-12acc7c6-f](https://cloud.overment.com/miss-12acc7c6-f.png)
- ![fragmented-500ae0cc-c](https://cloud.overment.com/fragmented-500ae0cc-c.png)
- ![instructors-6f5f8bbc-1](https://cloud.overment.com/instructors-6f5f8bbc-1.png)

**Podsumowanie Lekcji S03L03 - Wyszukiwanie i bazy wektorowe z kursu AI_Devs**

Podczas tej lekcji dowiedzieliśmy się o przetwarzaniu danych HTML oraz o tym, jak zamieniać je na składnię Markdown. Możemy do tego wykorzystać ready-made narzędzia jak na przykład [node-html-markdown](https://www.npmjs.com/package/node-html-markdown). Zrozumiałeś, że informacje muszą być podzielone na jednostki niosące pewien sens i tym sposobem stworzyć dokumenty opisane metadanymi. Do wypreparowania i podziału konkretnych fragmentów tekstu rzeczywiście pomocne jest umiejętne korzystanie z wyrażeń regularnych. 

Później lekcja przechodzi do tematu przetwarzania długich dokumentów. Wszak wiele razy będziesz musiał się zmierzyć z sytuacją, kiedy informacji jest po prostu za dużo by pomieścić je w jednym kontekście. Sprawa dotyczy takich przypadków jak przetwarzanie całych długich dokumentów czy też klasyfikacja dużych zestawów danych. 

Podsumowując, umiejętność wyszukiwania właściwych informacji i ich odpowiedniego przetwarzania jest kluczowa w kontekście korzystania z modeli języka.

![Przykład przetwarzania danych](https://cloud.overment.com/processing-f7af380e-4.png)

Na ilustracji widzisz przykład tego, jak można przetwarzać dane z wykorzystaniem omówionych technik.


Tutaj jest szybki przegląd pracy wykonanej na Lekcji 3, Sezon 3 kursu AI_Devs, skupiający się na wyszukiwaniu i bazach wektorowych:

- Osoba prowadząca kurs przedstawia scenariusz, w którym **webhook* stosowany jest jako sposób przesyłania plików do przetworzenia.
- Pliki są przekształcane na mniejsze fragmenty, które są przesyłane do OpenAI do przetłumaczenia na język angielski.
- W przypadku, gdy OpenAI nie odpowiada, jest wypróbowywana metoda naprawy obejmująca czekanie i wznowienie działania.
- Z przetworzonych fragmentów, tworzy się nowy dokument, który jest zapisywany na Google Drive, z generowanym linkiem do jego pobrania.
- Link do pliku jest następnie zwracany jako odpowiedź.
  
Co warto zauważyć:

- Cały scenariusz jest koncepcyjnie "**izolowany**", co oznacza, że może być wywołany na różne sposoby.
- Można dodać informacje kontekstowe, które mogą modyfikować instrukcje systemowe.
- Możliwe są zastosowania zarówno dla krótkich, jak i długich form tekstów.
- Forki to unikalne operacje uzależnione od Make.com, stąd dla długich tekstów warto rozważyć przekładanie logiki na kod.

Poniżej zamieszczam przykładowy obrazek uzupełniony kodem CURL do przetestowania działania scenariusza. Należy jednak pamiętać o zmianie nazwy pliku i adresu webhooka:

![](https://cloud.overment.com/curl-2d752ffc-b.png)

[Dodatkowo, jest blueprint](https://cloud.overment.com/aidevs_watch_folder-1695994706.json), który można pobrać, ale pamiętaj o podmianie adresu Webhooka na własny.

