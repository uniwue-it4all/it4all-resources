from pathlib import Path
from textwrap import dedent
from typing import List

from models.collection import ExerciseFile, SampleSolution, load_text_from_file, ex_resources_path
from models.web import WebSolution, HtmlTask, HtmlAttribute, JsTask, SiteSpec, JsAction, JsCondition, JsActionType, \
    WebExercise, WebExerciseContent

ex_res_path: Path = ex_resources_path('web', 2, 1)

html_tasks: List[HtmlTask] = [
    HtmlTask(
        id=1,
        text=dedent(
            """\
            Erstellen Sie einen Button mit dem Text 'Klick mich!'.
            Beim Klick die Funktion 'increment()' aufgerufen werden."""
        ).replace('\n', ' '),
        xpathQuery='/html/body//button',
        awaitedTagName='button',
        attributes=[HtmlAttribute(key='onclick', value='increment()')],
        awaitedTextContent='Klick mich!'
    ),
    HtmlTask(
        id=2,
        text=dedent(
            """\
            Erstellen Sie einen Span mit der ID 'theSpan', in dem die Anzahl der Klicks angezeigt werden.
            Zu Anfang soll dieser eine 0 anzeigen."""
        ).replace('\n', ' '),
        xpathQuery="""/html/body//span[@id='theSpan']""",
        awaitedTagName='span',
        awaitedTextContent='0'
    ),
    HtmlTask(
        id=3,
        text="""Binden Sie die Javascript - Datei 'clickCounter.js' ein.""",
        xpathQuery='/html/head//script',
        awaitedTagName='script',
        attributes=[HtmlAttribute(key='src', value='clickCounter.js')]
    )
]

js_tasks: List[JsTask] = [
    JsTask(
        id=i,
        text=f'Test {i}',
        preConditions=[
            JsCondition(
                id=1,
                xpathQuery="""/html/body//span[@id='theSpan']""",
                awaitedTagName='span',
                awaitedTextContent=f'{i - 1}'
            )
        ],
        action=JsAction(
            xpathQuery='/html/body//button',
            actionType=JsActionType.Click
        ),
        postConditions=[
            JsCondition(
                id=1,
                xpathQuery="""/html/body//span[@id='theSpan']""",
                awaitedTagName='span',
                awaitedTextContent=f'{i}'
            )
        ]
    ) for i in range(1, 5)
]

sampleSolution: SampleSolution[WebSolution] = SampleSolution(
    id=1,
    sample=WebSolution(
        files=[
            ExerciseFile(
                name='clickCounter.html',
                fileType='htmlmixed',
                editable=False,
                content=load_text_from_file(ex_res_path / 'sol_1' / 'clickCounter.html')
            ),
            ExerciseFile(
                name='clickCounter.js',
                fileType='javascript',
                editable=False,
                content=load_text_from_file(ex_res_path / 'sol_1' / 'clickCounter.js')
            )
        ]
    )
)

web_coll_2_ex_1: WebExercise = WebExercise(
    id=1,
    collectionId=2,
    toolId='web',
    title='Klickzähler',
    authors=['bje40dc'],
    text=load_text_from_file(ex_res_path / 'text.html'),
    topics=[],
    difficulty=2,
    content=WebExerciseContent(
        files=[
            ExerciseFile(
                name='clickCounter.html',
                fileType='htmlmixed',
                editable=True,
                content=load_text_from_file(ex_res_path / 'clickCounter.html')
            ),
            ExerciseFile(
                name='clickCounter.js',
                fileType='javascript',
                editable=True,
                content=load_text_from_file(ex_res_path / 'clickCounter.js')
            )
        ],
        htmlText='Erstellen Sie zunächst den Rumpf der Seite in HTML.',
        jsText=dedent(
            """\
            Implementieren Sie nun die Funktion <code>increment()</code> die aufgerufen wird wenn auf den Knopf
            gedrückt wird.
            Sie soll den Inhalt (innerHTML) des Elementes mit der id 'theSpan' auslesen und um 1 erhöhen.
            Sie können die Funktion <code>parseInt(str)</code> verwenden um einen String in eine Ganzzahl
            umzuwandeln."""
        ).replace('\n', ' '),
        siteSpec=SiteSpec(
            fileName='clickCounter.html',
            htmlTasks=html_tasks,
            jsTasks=js_tasks
        ),
        sampleSolutions=[sampleSolution]
    )
)
