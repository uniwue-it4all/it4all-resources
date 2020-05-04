from pathlib import Path
from textwrap import dedent
from typing import List

from models.basics import ExerciseFile, SampleSolution, ex_resources_path, load_text_from_file
from models.web import WebSolution, HtmlTask, JsTask, HtmlAttribute, JsActionType, JsCondition, JsAction, SiteSpec, \
    WebExercise, WebExerciseContent

ex_res_path: Path = ex_resources_path('web', 2, 3)

html_tasks: List[HtmlTask] = [
    HtmlTask(
        id=1,
        text=dedent(
            """\
            Erstellen Sie ein Zahlen-Eingabefeld mit der ID 'number'.
            Bei Änderung des Feldes (onchange) soll die Funktion 'fakultaet()' aufgerufen werden."""
        ).replace('\n', ' '),
        xpathQuery="""/html/body//input[@id='number']""",
        awaitedTagName='input',
        attributes=[
            HtmlAttribute(key='type', value='number'),
            HtmlAttribute(key='onchange', value='fakultaet()')
        ]
    ),
    HtmlTask(
        id=2,
        text=dedent(
            """\
            Erstellen Sie einen Span mit der ID 'result', in dem das Ergebnis der Berechnung stehen soll.
            Zu Anfang soll dieser leer sein."""
        ).replace('\n', ' '),
        xpathQuery="""/html/body//span[@id='result']""",
        awaitedTagName='span'
    ),
    HtmlTask(
        id=3,
        text="""Binden Sie die Javascript-Datei 'factorial.js' ein.""",
        xpathQuery='/html/head//script',
        awaitedTagName='script',
        attributes=[HtmlAttribute(key='src', value='factorial.js')]
    )
]

js_tasks: List[JsTask] = [
    JsTask(
        id=1,
        text='Fakultät von 1 muss 1 sein.',
        preConditions=[],
        action=JsAction(
            actionType=JsActionType.FillOut,
            xpathQuery="""/html/body//input[@id='number']""",
            keysToSend='1'
        ),
        postConditions=[
            JsCondition(
                id=1,
                xpathQuery="""/html/body//span[@id='result']""",
                awaitedTagName='span',
                awaitedTextContent='1'
            )
        ]
    ),
    JsTask(
        id=2,
        text='Fakultät von 3 muss 6 sein.',
        preConditions=[],
        action=JsAction(
            actionType=JsActionType.FillOut,
            xpathQuery="""/html/body//input[@id='number']""",
            keysToSend='3'
        ),
        postConditions=[
            JsCondition(
                id=1,
                xpathQuery="""/html/body//span[@id='result']""",
                awaitedTagName='span',
                awaitedTextContent='6'
            )
        ]
    ),
    JsTask(
        id=3,
        text='Fakultät von 6 muss 720 sein.',
        preConditions=[],
        action=JsAction(
            actionType=JsActionType.FillOut,
            xpathQuery="""/html/body//input[@id='number']""",
            keysToSend='6'
        ),
        postConditions=[
            JsCondition(
                id=1,
                xpathQuery="""/html/body//span[@id='result']""",
                awaitedTagName='span',
                awaitedTextContent='720'
            )
        ]
    ),
    JsTask(
        id=4,
        text='Fakultät von 10 muss 3628800 sein.',
        preConditions=[],
        action=JsAction(
            actionType=JsActionType.FillOut,
            xpathQuery="""/html/body//input[@id='number']""",
            keysToSend='10'
        ),
        postConditions=[
            JsCondition(
                id=1,
                xpathQuery="""/html/body//span[@id='result']""",
                awaitedTagName='span',
                awaitedTextContent='3628800'
            )
        ]
    )
]

sampleSolution: SampleSolution[WebSolution] = SampleSolution(
    id=1,
    sample=WebSolution(
        files=[
            ExerciseFile(
                name='factorial.html',
                fileType='htmlmixed',
                editable=False,
                content=load_text_from_file(ex_res_path / 'sol_1' / 'factorial.html')
            ),
            ExerciseFile(
                name='factorial.js',
                fileType='javascript',
                editable=False,
                content=load_text_from_file(ex_res_path / 'sol_1' / 'factorial.js')
            )
        ]
    )
)

web_coll_2_ex_3: WebExercise = WebExercise(
    exerciseId=3,
    collectionId=2,
    toolId='web',
    title='Schleifen',
    authors=['alg81dm'],
    text=load_text_from_file(ex_res_path / 'text.html'),
    difficulty=2,
    topicAbbreviations=[],
    content=WebExerciseContent(
        files=[
            ExerciseFile(
                name='factorial.html',
                fileType='htmlmixed',
                editable=True,
                content=load_text_from_file(ex_res_path / 'factorial.html')
            ),
            ExerciseFile(
                name='factorial.js',
                fileType='javascript',
                editable=True,
                content=load_text_from_file(ex_res_path / 'factorial.js')
            )
        ],
        htmlText='Erstellen Sie zunächst den Rumpf der Seite in HTML.',
        jsText=dedent(
            """\
            Implementieren Sie nun die Funktion <code>fakultaet()</code>, die bei Änderung des Felds aufgerufen wird.
            Sie soll den Inhalt (value) des Eingabefeldes auslesen, die Fakultät davon berechnen und den
            Inhalt (textContent) des Elements mit der ID 'result' auf das Ergebnis setzen."""
        ).replace('\n', ' '),
        siteSpec=SiteSpec(
            fileName='factorial.html',
            htmlTasks=html_tasks,
            jsTasks=js_tasks
        ),
        sampleSolutions=[sampleSolution]
    )
)
