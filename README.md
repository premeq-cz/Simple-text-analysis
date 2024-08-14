# Textovy-analyzator
Check if user is registered, select a text, basic analysis of chosen text

EVALUATION FROM A LECTOR #1:

Co se mi líbilo: 1. Přihlášení funkční, jednoduše řešeno
2. Kód je strukturovaný a čitelný
3. Hezky okomentováno vše


Co by jsi měl/a zlepšit: Co zlepšit:
1. Ošetření vstupu uživatele, při výběru textu: při zadání písmene, program spadne s chybou ValueError: invalid literal for int() with base 10: 's'. Nutno ošetřit, buď nechat uživatele napsat znovu s upozorněním, kde udělal chybu, nebo řízeně ukončit program.
2. Počítání statistik pro slova začínající velkým písmenem: zde je výstup There are 12 titlecase words. ['Situated', 'Kemmerer', 'Fossil', 'Butte', 'Twin', 'Creek', 'Valley', 'The', '30N', 'Union', 'Pacific', 'Railroad'] - slovo 30N nezačíná velkým písmenem. Koukni se jek funguje metoda istitle.
3. Univerzálnost kódu: řádek 42 - máš pevně dáno na 3 texty, když přidáme další texty, musíš podmínku upravit ručně. Nešlo by to udělat univerzálně, třeba použít délku seznamu. A to samé by šlo použít na řádku 36
4. Odstranění nežádoucích znaků: řádek 50, odstraníš jen čárky a tečky, když přidáme text, kde bude otazník apod. opět budeš muset ručně opravit.

Závěr: Kód má dobrý základ, je strukturovaný a snadno čitelný. Je potřeba implementovat výše uvedená zlepšení. Pokud budeš potřebovat něco dovysvětlit, určitě mi napiš. Budu se těšit na upravený kód.



EVALUATION FROM A LECTOR #2:

Co se mi líbilo: Pozitiva zůstávají stejná +
1. Ošetřeny uživatelské vstupy
2. Správné počítání statistik
3. Univerzálnost pro výběr textu

Co by jsi měl/a zlepšit: 

Závěr: Projekt je strukturovaný a funkční. Veškerá zlepšení byla implementována a projekt splňuje požadavky zadání. Gratuluji, projekt schválen.

