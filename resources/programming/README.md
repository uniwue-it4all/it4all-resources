# Aufgaben Programmierung für it4all

Aufgaben sind in Sammlungen geordnet, die in der Datei [`collections.yaml`](collections.yaml) verwaltet werden.
Zu jeder Sammlung gibt es eine Datei mit dem Namen `<id>-<shortName>.yaml`, in die Aufgaben dieser Sammlung 
verwaltet werden und einen Ordner `<id>-<shortName>/`, in der zusätzliche Ressourcen zu den Aufgaben abgelegt
werden.

Es empfiehlt sich, dieses Repository zu klonen und z. B. in PyCharm zu öffnen, da dort durch die Verwendung
einer Schemadatei (`prog_ex.schema.json`) Hilfestellungen wie z. B. Autovervollständigung, Validitäts- und
Gültigkeitsprüfung bei den YAML-Dateien gegeben werden kann.

## Test First

Die Programmieraufgaben in `it4all` sollen im 'Test first'-Ansatz bearbeitet werden. Das heißt, dass die Nutzer
zuerst passende Tests zur der Aufgabe schreiben sollen und erst dann die eigentliche Implementierung durchführen
sollen.

Es gibt in `it4all` zwei Möglichkeiten, Tests durchzuführen:

1. Die Ausführung von 'normalen' Unittests
2. Die Ausführung von 'vereinfachten' Unittests (für unerfahrene Nutzer), die die Komplexität reduzieren sollen,
   indem keine echten Unittest ausgeführt werden und die Ergebnisse der Testläufe entsprechend aufbereitet werden.

## YAML

Die Metadaten der Aufgaben und der Sammlungen werden in [YAML](https://de.wikipedia.org/wiki/YAML) verwaltet.
YAML ist eine Obermenge von JSON, d. h. jedes JSON-Dokument ist auch ein YAML-Dokument.

Im Gegensatz zu JSON können viele Steuerzeichen wie geschweifte und eckige Klammern bei Objekten und Arrays und
Anführungszeichen bei Strings weggelassen werden. Außerdem ist es möglich, Strings mit den Steuerzeichen `>`
(Zeilenumbrüche werden entfernt) und `|` (Zeilenumbrüche werden beachtet) mehrzeilig im Dokument zu schreiben.

### Beispiel YAML vs. JSON

Gültig in JSON und YAML:

```json
{
  "id": 1,
  "long_string": "This is a long string which goes on for a long time. It is displayed in a single line.",
  "boolean_field": true,
  "subObject": {
    "name": "Test",
    "value": 3.14152963
  },
  "list": [
    "object1",
    "object2",
    "object3"
  ]
}
```

Entsprechung in 'reinem' YAML:

```yaml
id: 1
longString: >
  This is a long string which goes on for a long time.
  In Yaml, it can be broken down on multiple lines.
subObject:
  name: Test
  value: 3.14152963
list:
  - object1
  - object2
  - object3
```

## Format `ExerciseFile`

In der Aufgabendefinition werden Dateien benötigt. Diese werden mit folgenden Metadaten beschrieben:

* `path`: Dateiname bei der Korrektur (z. B. `fibonacci.py`)
* `resourcePath`: Pfad, an dem die Definition der Datei liegt. Diese Angabe muss relativ zu einem in `it4all` 
  existierenden Rootfolder `programming` liegen, der dem Root dieses Projekts entspricht, also z. B.
  `programming/1-number/4-fibonacci/fibonacci.py`
* `fileType`: Typ der Datei, normalerweise `python`
* `editable`: Gibt an, ob die Datei editierbar sein soll oder nicht

## Definition einer Sammlung

Eine Sammlungen besteht aus folgenden Werten:

* `id`: Eindeutige Ganzzahl
* `title`: Titel der Sammlung, wird bei Auswahl angezeigt
* `author`: Autor
* `text`: Nicht benutzt
* `state`: Status der Sammlung. Eine Sammlung ist nur mit dem Status `APPROVED` für Nutzer sichtbar
* `shortName`: Kurzname der Sammlung. Wird u. a. zum Finden der Aufgabendatei benötigt

## Aufgabendefinition

Prinzipiell sollten für eine Aufgabe zwei Dateien existieren:

* Eine Musterlösung

* Eine Datei mit einem Unittest, der die Korrektheit der Aufgabe 'sicherstellt'

Die Metadaten einer Aufgaben bestehen aus folgenden Werten:

* `id`: In der Sammlung eindeutige ID der Aufgabe, Ganzzahl
* `semanticVersion`: Versionierung einer Aufgabe, für neue Aufgaben 0.0.1
* `title`: Titel der Aufgabe
* `author`: Autor
* `text`: Beschreibung der Aufgabe, wird bei Implementierung angezeigt
* `status`: siehe Sammlung


* `functionname`: Name der zu implementierenden Funktion
* `filename`: Name der Musterlösungsdatei ohne Endung (z. B. `fibonacci` für Datei `fibonacci.py`),
  normalerweise `functionname
* `foldername`: Name des Ordners, in dem die Ressourcen zur Aufgabe verwaltet werden, normalerweise `functionname`

* `unitTestPart`: Definitionen für den Aufgabenteil 'Erstellung des Unittests' (siehe unten)

* `implementationPart`: Definitionen für den Aufgabenteil `Erstellung der Implementierung' (siehe unten)

* `sampleSolutions`: Musterlösungen (siehe unten)

* `sampleTestData`: Beispieltestdaten für Ausführung von vereinfachten Unittests

### Teil 'Erstellung von Unittests'

Beim Teil 'Erstellung von Unittests' wird der vom Nutzer erstellte Unittest gegen mehrere "Lösungen" getestet.
Unter diesen Lösungen ist eine Musterlösung, bei der alle Tests erfolgreich ("grün") sein sollen.
Alle anderen Lösungen beinhalten Fehler, die Lerner eventuell machen könnten und bei denen mindestens ein Teil
der Unittests fehlschlagen **muss**. Solche Fehler können u. a. sein

* Keine Überprüfung der Inputparameter (z. B. Zahlen, die größer als 0 sein sollen oder insbesondere bei Python
  die Typen der Argumente)
  
* [Off-by-one-Fehler](https://de.wikipedia.org/wiki/Off-by-one-Error) bei Schleifen

* generelle Programmierfehler, die zu falschen Ergebnissen führen

Das Object `unitTestPart` besteht aus folgenden Attributen:

* `unitTestType`: Legt den Typ fest (siehe oben), `Normal` für Version 1, `Simplified` für Version 2
* `unitTestsDescription`: Beschreibung (in HTML) der vollen Funktionalität der Funktion, die durch die Unittests
   abgeprüft werden soll. Wird bei der Erstellung der Unittests gerendert.
* `unitTestFiles`: Dateien (im Format [ExerciseFile](#format-exercisefile)), die bei der Bearbeitung dieses
  Teils angezeigt werden sollen. Es sollten mindestens zwei Dateien definiert sein:
  * Eine Datei mit der Definition der zu implementierenden Funktion (mit `pass` als Rumpf) (Wert `editable`
    auf `false)
  * Die Datei `test.py` für den Unittest mit der Basisdefinition des Unittests (bearbeitbar)
* `unitTestTestConfigs`: Dieses Objekt definiert die Lösungen, gegen die der Unittest getestet wird.
  Diese Konfigurationen haben wiederum folgende Attribute:
  
  * `id`: Eindeutige ID (Konvention: 0 für korrekte Lösung)
  * `shouldFail`: boolescher Wert, der angibt, ob die Unittests fehlschlagen sollen
  * `description`: Eine Beschreibung, was in der Lösung falsch ist
  * `cause`: Nicht genutzt, String 
  
  Für jede Konfiguration **muss** eine Datei im Ordner 
  `<collection.id>-<collection.shortName>/<ex.id>-<ex.foldername>/unit_test_sols` existieren, gegen die der
  Unittest ausgeführt wird.

#### Erstellen der 'defekten' Lösungen

Zum Erstellen verschiedener defekter Lösungen eignen sich die Paket `mutpy` und `mutmut`, das eigentlich für *Mutation
Testing* in Python entwickelt wurde. Dabei werden geringfüge Änderungen (zum Beispiel ändern von `+` in `*`)
in eine Implementierung eingeführt und überprüft, ob die Unittests fehlschlagen.

Folgender Aufruf mit einer Musterlösung und einem **vollständigen** Test erzeugt die Mutationen und zeigt sie an:

```bash
mut.py -t solution.py -u test_solution.py -m

mutmut run --paths-to-mutate solution.py --runner "python -m unittest"

# Anzeigen von Mutanten
mutmut show X
```

Aus der Konsolenausgabe sind sind die erzeugten Mutationen sichtbar und können erstellt werden.
 
### Teil 'Erstellung der Implementierung'

Beim Teil 'Erstellung der Implementierung' wird die vom Nutzer erstellte Implementierung gegen einen gegebenen
Unittest ausgeführt.

Das Objekt `implementationPart` besteht aus folgenden Attributen:

* `base`: Basisdeklaration der Implementierung, wird für vereinfachte Unittestmethode benutzt, kann leer 
  gelassen werden
* `files`: Dateien, die bei der Bearbeitung im 'normalen' Modus angezeigt werden, als Typ 
  [ExerciseFile](#format-exercisefile). Es sollten mindestens folgende Dateien angezeigt werden:
  
  * `test.py` mit dem Unittest
  * Eine Datei mit einem Rumpf der zu implementierenden Funktionalität (z. B. `ficonacci.py`)
  
### Musterlösungen

Musterlösungen werden dem Nutzer angezeigt. Theoretisch können mehrere Musterlösungen angegeben werden,
meist reicht jedoch eine aus.

Eine Musterlösung besteht aus folgenden Attributen:

* `id`: Eindeutige ID der Musterlösung
* `files`: Für jede zu implementierende Datei (sowohl Erstellung der Unittests als auch Erstellung der 
  Implementierung) sollte in der Musterlösung eine Lösungsdatei im Format [ExerciseFile](#format-exercisefile)
  exisiteren.

### Mustertestdaten

Werden nur im Modus 'vereinfachte Tests' benötigt, können ansonsten als leeres Array (wie in JSON: `[]`)
definiert werden.
