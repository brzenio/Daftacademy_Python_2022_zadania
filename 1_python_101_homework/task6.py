def lazy_scribe(sources: list):
    # W tym zadaniu wcielisz się w skrybe (a do tego lenia i plagiatora) ciągów znakowych.
    # Skryba dostał zadanie stworzenia nowego ciągu znakowego. Nie chce mu się poświęcać
    # na to zbyt dużo czasu więc postanowił wykorzystać ciągi znakowe ze swojej biblioteczki.
    # 
    # Skryba działa metodycznie i chce całkowicie wykorzystać potencjał swojej kolekcji ciągów.
    # Wypracował następujący schemat działania:
    # 1. Bierze pierwszy ciąg z bilioteczki
    # 2. Przepisuje pierwszy znak z pobranego z bilbioteczki ciągu do ciągu, który właśnie tworzy
    # 3. Zapamiętuje, że wykorzystał już pierwszy znak z pierwszego ciągu
    # 4. Przechodzi do kolejnego ciągu, wybiera go zgodnie z kolejnościa przechowywania ciągów w
    #    biblioteczce
    # 5. Kopiuje z pobranego ciągu pierwszy znak, którego jeszcze nie wykorzystał z danego ciągu i
    #    i zapamiętuje który znak wykorzystał
    # 6. Powtarza kroki 4 i 5, jeśli dojdzie do końca bilbioteczki to wraca na jej początek i powtarza
    #    proces tak długo, aż wykorzysta wszystkie znaki ze wszystkich dostępnych w bilbioteczce ciągów
    # 
    # Dodatkowo z racji tego, że jest leniwy, kompresuje w tworzonym ciągu powtarzające się znaki
    # zastępując je liczbą kolejnych wystąpień tego samego znaku połączoną z samym znakiem
    # np. "aaaaaaa" -> "7a"
    #
    # Przykład:
    # Skryba ma w swojej bilbioteczce (`sources`) następujące ciągi znakowe:
    # `sources = ["python", "java", "golang"]`
    #
    # Jego genialna i nowatorska metoda tworzenia nowych ciogów zaowocuje następującym ciągiem:
    # `result = "pjgyaotvlh2ao2ng"`
    #  
    # Pomóż skrybie zautomatyzowac ten proces! Rezultat przypisz do zmiennej `result`.
    
    # * W liście `sources` znajdują się ciągi znakowe które odpowiadają bilbioteczce skryby.
    # * Ciągi znakowe w 'sources' składają się wyłącznie ze znaków a-z.
    # * Znaki traktuj jako unikalne podmioty, wykorzystanie znaku 'a' z któregoś z ciągów z
    #   z biblioteczki nie oznacza, że nie można wykorzystać znaku 'a' znajdującego się
    #   dalej w tym samym ciągu

    result: str = ''
    if sources:
        
        max_len = len(max(sources, key=len))

        char_iterator = 0
        lista = []

        while char_iterator < max_len:
            for word in sources:
                if char_iterator < len(word):
                    lista.append(word[char_iterator])
                    #print(lista)
            char_iterator += 1


        count = 0
        lista_powtorzen = []
        for i in range(len(lista) - 1):
                if lista[i] == lista[i + 1]:
                    count += 2
                    lista[i] = str(count)
                count = 0


        string = ''
        string.join(lista)

        result = string.join(lista)


    return result


