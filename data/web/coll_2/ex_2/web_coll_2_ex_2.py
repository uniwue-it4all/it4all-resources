from pathlib import Path
from textwrap import dedent
from typing import List

from models.collection import ExerciseFile, load_text_from_file, SampleSolution, ex_resources_path
from models.web import WebSolution, HtmlTask, HtmlAttribute, JsTask, JsAction, JsActionType, JsCondition, SiteSpec, \
    WebExercise, WebExerciseContent

ex_res_path: Path = ex_resources_path('web', 2, 2)

sampleSolution: SampleSolution[WebSolution] = SampleSolution(
    id=1,
    sample=WebSolution(
        files=[
            ExerciseFile(
                name='pwChecker.html',
                fileType='htmlmixed',
                editable=False,
                content=load_text_from_file(ex_res_path / 'sol_1' / 'branchesStrings.html'),
            ),
            ExerciseFile(
                name='pwChecker.js',
                fileType='javascript',
                editable=False,
                content=load_text_from_file(ex_res_path / 'sol_1' / 'branchesStrings.js'),
            )
        ]
    )
)

html_tasks: List[HtmlTask] = [
    HtmlTask(
        id=1,
        text="""Erstellen Sie ein Texteingabefeld mit der ID 'name'.""",
        xpathQuery="""/html/body//input[@id='name']""",
        awaitedTagName='input',
        attributes=[HtmlAttribute(key='type', value='text')]
    ),
    HtmlTask(
        id=2,
        text=dedent(
            """\
            Erstellen Sie ein Passworteingabefeld mit der ID 'password'.
            Bei Änderung des Passwortfeldes (onchange) soll die Funktion 'passwordStrength()' aufgerufen werden."""
        ).replace('\n', ' '),
        xpathQuery="""/html/body//input[@id='password']""",
        awaitedTagName='input',
        attributes=[
            HtmlAttribute(key='type', value='password'),
            HtmlAttribute(key='onchange', value='passwordStrength()')
        ]
    ),
    HtmlTask(
        id=3,
        text=dedent(
            """\
            Erstellen Sie einen Span mit der ID 'errors', der später anzeigen soll, wenn das Passwort zu schwach ist.
            Zu Anfang soll dieser leer sein."""
        ).replace('\n', ' '),
        xpathQuery="""/html/body//span[@id='errors']""",
        awaitedTagName='span'
    ),
    HtmlTask(
        id=4,
        text="""Binden Sie die Javascript-Datei 'pwChecker.js' ein.""",
        xpathQuery="""/html/head//script""",
        awaitedTagName='script',
        attributes=[
            HtmlAttribute(key='src', value='pwChecker.js')
        ]
    )
]

js_tasks: List[JsTask] = [
    JsTask(
        id=1,
        text="""Wenn das Passwort unter 8 Zeichen lang ist, setze den Fehlertext auf 'Zu kurz'.""",
        preConditions=[],
        action=JsAction(
            xpathQuery="""/html/body//input[@id='password']""",
            actionType=JsActionType.FillOut,
            keysToSend='123'
        ),
        postConditions=[
            JsCondition(
                id=1,
                xpathQuery="""/html/body//span[@id='errors']""",
                awaitedTagName='span',
                awaitedTextContent='Zu kurz'
            )
        ]
    ),
    JsTask(
        id=2,
        text="""Wenn das Passwort 'passwort' enthält, setze den Fehlertext auf 'Zu einfach'.""",
        preConditions=[],
        action=JsAction(
            xpathQuery="""/html/body//input[@id='password']""",
            actionType=JsActionType.FillOut,
            keysToSend='meinpasswort'
        ),
        postConditions=[
            JsCondition(
                id=1,
                xpathQuery="""/html/body//span[@id='errors']""",
                awaitedTagName='span',
                awaitedTextContent='Zu einfach'
            )
        ]
    ),
    JsTask(
        id=3,
        text="""Für alle anderen Passwörter soll das Fehlerfeld geleert (auf '' gesetzt) werden.""",
        preConditions=[],
        action=JsAction(
            actionType=JsActionType.FillOut,
            xpathQuery="""/html/body//input[@id='password']""",
            keysToSend='GanzGanzSicherUndGeheim'
        ),
        postConditions=[
            JsCondition(
                id=1,
                xpathQuery="""/html/body//span[@id='errors']""",
                awaitedTagName='span',
                awaitedTextContent=''
            )
        ]
    )
]

web_coll_2_ex_2: WebExercise = WebExercise(
    exerciseId=2,
    collectionId=2,
    toolId='web',
    title='Verzweigungen und Strings',
    authors=['alg81dm'],
    text=load_text_from_file(ex_res_path / 'text.html'),
    topics=[],
    difficulty=3,
    content=WebExerciseContent(
        files=[
            ExerciseFile(
                name='pwChecker.html',
                fileType='htmlmixed',
                editable=True,
                content=load_text_from_file(ex_res_path / 'branchesStrings.html')
            ),
            ExerciseFile(
                name='pwChecker.js',
                fileType='javascript',
                editable=True,
                content=load_text_from_file(ex_res_path / 'branchesStrings.js')
            )
        ],
        htmlText='Erstellen Sie zunächst den Rumpf der Seite in HTML.',
        jsText=dedent(
            """\
            Implementieren Sie nun die Funktion <code>passwordStrength()</code>, die bei Änderung des Felds aufgerufen
            wird.
            Sie soll den Inhalt (value) des Passwortfeldes auslesen und verschiedene Tests durchführen.
            Bei fehlgeschlagenen Tests soll der Inhalt des Elements mit der ID 'errors' auf den entsprechenden Text
            gesetzt werden.
            Es soll immer nur der erste fehlgeschlagene Test (in der Reihenfolge der Teilaufgaben) beachtet werden.
            Wenn kein Test fehlschlägt, soll der Fehlertext gelöscht werden (auf '' setzen).
            Wenn das Passwort unter 8 Zeichen lang ist, soll der Fehlertext 'Zu kurz' lauten.
            Wenn die Eingabe den Teilstring 'passwort' enthält, soll 'Zu einfach' gesetzt werden."""
        ).replace('\n', ' '),
        siteSpec=SiteSpec(
            fileName='pwChecker.html',
            htmlTasks=html_tasks,
            jsTasks=js_tasks
        ),
        sampleSolutions=[sampleSolution]
    )
)
