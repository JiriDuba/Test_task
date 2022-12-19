# ****Testové zadání na pozici Service owner v České spořitelně****


## Úkol č. 1

### **Pokyny k vypracování:**

Složka obsahuje níže uvedené soubory:
* ***1.txt***
* ***2.txt***
* ***3.txt***

Je potřeba je spojit do jednoho souboru s názvem merget_files.txt dle následujících požadavků:

1. sloučení souborů by mělo být realizováno prostřednictvím Pythonu,
2. pořadí zápisu do souboru merged_files.txt určuje počet řádků v jednotlivých souborech (tzn. soubor s nejmenším počtem řádků by měl být do finálního souboru zapsán jako první a soubor s největším počtem řádků jako poslední),
3. při sloučení souboru vždy uveďte jeho název a počet řádků.


### **Finální soubor merget_files.txt by měl vypadat následovně:**

```
3.txt
3
The Zen of Python
Beautiful is better than ugly.
Explicit is better than implicity.

1.txt
6
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.

2.txt
11
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those! 
```


## Úkol č. 2
Jeden z nejužitečnějších webů pro programátory je [stackoverflow](https://stackoverflow.com/), který má veřejné [API](https://api.stackexchange.com/docs). 
Je třeba napsat program, jehož výstupem bude seznam otázek s tagem "Python", za poslední dva dny.
Tato úloha nevyžaduje token.

### **Příklad výstupu**
```
Otázka číslo: 1; 2022-11-05 16:59:09
['python', 'search', 'artificial-intelligence', 'breadth-first-search']
Implementation of Breadth First Search for solving Puzzle
https://stackoverflow.com/questions/74329743/implementation-of-breadth-first-search-for-solving-puzzle

Otázka číslo: 2; 2022-11-05 16:58:11
['python', 'list', 'numpy']
Load custom dataset of with multiple categories into training and testing sets?
https://stackoverflow.com/questions/74329731/load-custom-dataset-of-with-multiple-categories-into-training-and-testing-sets
...
```

## Úkol č. 3

### **Pokyny k vypracování:**

1. Pomocí regulárních výrazů a Pythonu vytvořte přehledný adresář ve formátu CSV. 
2. Kontaktní údaje pro práci s adresářem najdete v souboru ```phonebook_raw.csv```.
3. Výstupní soubor pojmenujte dle libosti. 
4. Vycházejte z předpokladu, že každý člověk má pouze jedno telefonní číslo a jeden e-mail. 
2. Telefonní čísla uvádějte ve formátu ```+3 (123)-XXX-XX-XX```. 
3. Duplicitní záznamy je třeba sloučit do jednoho.


***Na výstupu by měl vzniknout nový CSV soubor s následující strukturou:***

```
LASTNAME   FIRSTNAME  SECONDNAME  ORGANIZATION  POSITION                                       PHONE                EMAIL
Coganj     Nina       Elisabeth   Amazon        Trade and Foreign Direct Investment advisory   +3 (123)-913-04-78   opendata@hotmail.com

Robertson  David      Ashton      Google                                                       +3 (123)-913-00-37 

Moore      Maria      Alison      Google                                                       +3 (123)-913-01-68 

Dunlop     Olena      Helen       Avast         Technical Manager

Briani     Massimo    Marc        TechNet                                                      +3 (123)-983-36-99   massimo.briani@gmail.com

Campbell   Marisa     Anna        TechNet                                                      +3 (123)-748-49-73   1248@hotmail.com

Lewis      Martin     Edward      NowRisk       Designer                                       +3 (123)-913-11-11   Martin.Lewis@gmail.com
```


---

### **Obecné informace k úkolům:**

1. inicializujte lokální Git repozitář na svém PC,
2. naklonujte si potřebné soubory z [GitHub](https://github.com/CSAS-TestoveZadani/Testove_zadani),
3. vytvořte veřejný repozitář na GitHubu a propojte ho s lokálním, 
4. odkaz na GitHub s vypracovaným zadáním pošlete na email: ***EBannikova@csas.cz***.
