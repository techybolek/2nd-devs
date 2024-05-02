# Summary of the document Lekcja kursu AI_Devs, S03L03 — Wyszukiwanie i bazy wektorowe

Lekcja **S03L03** kursu AI_Devs dotyczyła wyszukiwania i baz wektorowych, które pozwalają przechowywać oraz przeszukiwać dane pochodzące z lmu (długoterminowej pamięcie dla modelu). Dwa główne zastosowania to możliwość hiper-personalizacji doświadczeń, polegające na połączeniu wiedzy o nas z dostępem do usług i urządzeń. Drugi powód to możliwość budowania częściowo autonomicznych zachowań, które przekładają się na unikalne zastosowania, np. wyobraź sobie, że GPT-4 wykonuje zadanie samodzielnie, posiadając zdolność dobrania niezbędnych danych do jego wykonania. 

Bazy wektorowe, o których już rozmawialiśmy w lekcji **C01L02**, to miejsce gdzie przechowujemy i przeszukujemy dane. Możesz zobaczyć uproszczoną wizualizację wielowymiarowych danych, przedstawionych w przestrzeni 3D [tutaj](https://projector.tensorflow.org). Dzięki nim możliwe jest określenie podobieństwa pomiędzy danymi, na przykład, za pomocą metody cosine similarity. Na wykresie poniżej widać, które słowa są najbliżej słowa "komputer".

Budowanie dynamicznego kontekstu dla LLM polega na dodawaniu danych do indeksu bazy wektorowej z uwzględnieniem odpowiednich metadanych, takich jak treść dokumentu, kategorie, tagi, źródło lub  inne dane, które mogą być istotne. Ważne jest również, aby pamiętać o aktualizacji danych, ponieważ przynajmniej część z nich będzie zmieniać się w czasie. Na przykład, generowanie embeddingów kosztuje i zajmuje czas, więc musimy pamiętać o synchronizacji danych między źródłem danych a bazą wektorową.

Na koniec, wyszukiwanie podobności (similarity search) jest procesem, w którym nasze wielowymiarowe zapytanie jest wzbogacane, modyfikowane i opisane, a następnie zwraca nam listę embeddingów i, zwykle, przypisany do nich score, pokazujący, jak bardzo są one podobne do naszego zapytania. Schemat działania baz wektorowych wygląda podobnie, o czym przekonasz się w dalszych lekcjach. W przykładzie **21_similarity** znajdziesz kod, który realizuje właśnie te schematy, które omówione zostały przez Adama.

W S03L03 kursu AI_Devs omawiane są zagadnienia związane z wyszukiwaniem i bazami wektorowymi, konkretnie - przetwarzanie danych dotyczących autorów strony aidevs.pl przedstawione jest jako prawdziwy projekt. Długie pliki HTML czy innego formatu mogą zostać zrozumiane przez model, ale zawierają wiele niepotrzebnego szumu. Możemy usunąć zbędne sekcje przy użyciu narzędzi dostępnych dla kodu HTML, takich jak [cheerio](https://www.npmjs.com/package/cheerio). Często potrzebujemy nie tylko tekstu, ale także formatowania, linków i obrazów, dlatego dobrym podejściem jest konwersja kodu na składnię Markdown, na przykład przy użyciu [node-html-markdown](https://www.npmjs.com/package/node-html-markdown). Dokumenty musimy podzielić na mniejsze fragmenty, opisać za pomocą metadanych i przenieść linki do metadanych, zamiast używać pełnych adresów w treści. GPT-4 może pomagać w pisaniu wyrażeń regularnych, które mogą być użyte do podziału tekstu i znalezienia linków. Poniżej przedstawiam różne zastosowania przetwarzania długich dokumentów, takie jak korekta, tłumaczenie, klasyfikacja, wzbogacanie, kompresja czy interakcja z treścią za pomocą czatbota lub w celu wyszukiwania zewnętrznych informacji. Kolejną sugestią jest wypróbowanie [blueprinta scenariusza](https://cloud.overment.com/aidevs_process_file-1695994995.json), który można łatwo testować na krótkich plikach, zwracając uwagę na koszty przetwarzania długich treści. ![](https://cloud.overment.com/processing-f7af380e-4.png)

Scenariusz zaczyna się od **webhooka**, który umożliwia wysyłanie plików za pomocą zapytań **HTTP**. Następnie pliki te są dzielone na mniejsze fragmenty, które następnie są przekazywane do **OpenAI** do przetłumaczenia na język angielski. W przypadku błędu, próba jest przeprowadzana ponownie po krótkim czasie. Tłumaczenia są zapisywane na **Google Drive** i udostępniane za pomocą linku do pobrania.

Uwaga, scenariusz ten może być uruchomiony na różne sposoby, co czyni go bardzo elastycznym. Może być uruchamiany na żądanie, według harmonogramu, lub w odpowiedzi na jakieś zdarzenie. Dodatkowe informacje kontekstowe mogą również być przesyłane wraz z plikami, zwiększając użyteczność tego narzędzia.

Dla długiego dokumentu, tłumaczenia muszą być dopasowane do kontekstu. Może to obejmować przekazywanie nazwy pliku lub innych informacji, które pomagają w tłumaczeniu. Poniżej znajduje się obrazek z przykładowym interfejsem użytkownika. 

![Przykład interfejsu użytkownika](https://cloud.overment.com/prompt-e7738b20-3.png)

Możesz przetestować tę funkcję za pomocą poniższego CURL'a lub z jakimkolwiek innego rodzaju zapytania HTTP.

![Test CURL](https://cloud.overment.com/curl-2d752ffc-b.png)

Dodatkowo, można zasugerować utworzenie oddzielnego folderu na **Google Drive** (np. 'Do przetłumaczenia'), który będzie obserwowany przez scenariusz.

![Przykład drugiego interfejsu użytkownika](https://cloud.overment.com/process-e7445b93-a.png)

Następnie, czekamy na odpowiedź na podłączony adres webhook. Może to chwilę potrwać.

