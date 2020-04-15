from models.collection import Exercise, ExerciseContent, ExerciseFile, ExerciseState, SampleSolution, SemanticVersion, \
    load_text_from_file, base_res_path
from typing import List
from textwrap import dedent
from models.web import WebExTag, WebExerciseContent, WebSolution, HtmlTask, HtmlAttribute, JsTask, SiteSpec, JsAction, \
    JsCondition, JsActionType

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

web_coll_2_ex_1 = Exercise(
    id=1,
    collectionId=2,
    toolId='web',
    semanticVersion=SemanticVersion(major=1, minor=0, patch=0),
    title='Klickzähler',
    authors=['bje40dc'],
    text=load_text_from_file(base_res_path / 'web' / 'coll_2' / 'ex_1' / 'text.html'),
    tags=[],
    state=ExerciseState.APPROVED,
    difficulty=2,
    content=WebExerciseContent(
        files=[
            ExerciseFile(
                name='clickCounter.html',
                fileType='htmlmixed',
                editable=True,
                resourcePath='clickCounter.html'
            ),
            ExerciseFile(
                name='clickCounter.js',
                fileType='javascript',
                editable=True,
                resourcePath='clickCounter.js'
            )
        ],
        htmlText='Erstellen Sie zunächst den Rumpf der Seite in HTML.',
        jsText=dedent(
            """\
            Implementieren Sie nun die Funktion <code>increment()</code> die aufgerufen wird wenn auf den Knopf
            gedrückt wird. Sie soll den Inhalt (innerHTML) des Elementes mit der id 'theSpan' auslesen und um 1 erhöhen.
            Sie können die Funktion <code>parseInt(str)</code> verwenden um einen String in eine Ganzzahl umzuwandeln."""
        ),
        siteSpec=SiteSpec(
            fileName='clickCounter.html',
            htmlTasks=[
                HtmlTask(
                    id=1,
                    text=dedent(
                        """\
                        Erstellen Sie einen Button auf den geklickt wird. Dieser soll als Text 'Klick mich!' haben. Außerdem soll beim
                        Klick die Funktion 'increment()' aufgerufen werden."""
                    ),
                    xpathQuery='/html/body//button',
                    awaitedTagName='button',
                    attributes=[
                        HtmlAttribute(key='onclick', value='increment()')
                    ],
                    awaitedTextContent='Klick mich!'
                ),
                HtmlTask(
                    id=2,
                    text=dedent(
                        """\
                        Erstellen Sie einen Span mit der ID 'theSpan' in dem die Anzahl der Klicks angezeigt werden. Zu Anfang soll
                        dieser eine 0 anzeigen."""
                    ),
                    xpathQuery="""/html/body//span[@id='theSpan']""",
                    awaitedTagName='span',
                    awaitedTextContent='0'
                ),
                HtmlTask(
                    id=3,
                    text="""Binden Sie die Javascript - Datei 'clickCounter.js' ein.""",
                    xpathQuery='/html/head//script',
                    awaitedTagName='script',
                    attributes=[
                        HtmlAttribute(key='src', value='clickCounter.js')
                    ]
                )
            ],

            jsTasks=js_tasks,
            sampleSolutions=[
                SampleSolution(
                    id=1,
                    sample=WebSolution(
                        files=[
                            ExerciseFile(
                                name='clickCounter.html',

                                fileType='htmlmixed',
                                editable=False,
                                resourcePath='clickCounterSolution.html'
                            ),
                            ExerciseFile(
                                name='clickCounter.js',

                                fileType='javascript',
                                editable=False,
                                resourcePath='clickCounterSolution.js'
                            )
                        ]
                    )
                )
            ]
        )
    )
)
