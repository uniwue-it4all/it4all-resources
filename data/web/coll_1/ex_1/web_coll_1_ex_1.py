from pathlib import Path
from textwrap import dedent
from typing import List

from models.collection import load_text_from_file, SampleSolution, ex_resources_path
from models.web import ExerciseFile, SiteSpec, HtmlTask, HtmlAttribute, WebSolution, WebExercise, WebExerciseContent

ex_res_folder: Path = ex_resources_path('web', 1, 1)

html_tasks: List[HtmlTask] = [
    HtmlTask(
        id=1,
        text="""Erstellen Sie eine passende h1 - Überschrift, die das Wort Autohersteller enthält.""",
        xpathQuery='/html/body//h1',
        awaitedTagName='h1',
        awaitedTextContent='Autohersteller'
    ),
    HtmlTask(
        id=2,
        text="""Erstellen Sie eine ungeordnete Liste, die dann die einzelnen Hersteller enthalten wird.""",
        xpathQuery='/html/body//ul',
        awaitedTagName='ul'
    ),
    HtmlTask(
        id=3,
        text="""Erstellen Sie ein Listenelement mit dem Text Audi.""",
        xpathQuery="""/html/body//ul/li[contains(text(), Audi)]""",
        awaitedTagName='li',
        awaitedTextContent='Audi',
    ),
    HtmlTask(
        id=4,
        text="""Erstellen Sie ein Listenelement mit dem Text BMW.""",
        xpathQuery="""/html/body//ul/li[contains(text(), BMW)]""",
        awaitedTagName='li',
        awaitedTextContent='BMW'
    ),
    HtmlTask(
        id=5,
        text="""Erstellen Sie ein Listenelement mit dem Text Mercedes.""",
        xpathQuery="""/html/body//ul/li[contains(text(), Mercedes)]""",
        awaitedTagName='li',
        awaitedTextContent='Mercedes'
    ),
    HtmlTask(
        id=6,
        text="""Erstellen Sie ein Listenelement mit dem Text Volkswagen.""",
        xpathQuery="""/html/body//ul/li[contains(text(), Volkswagen)]""",
        awaitedTagName='li',
        awaitedTextContent='Volkswagen'
    ),
    HtmlTask(
        id=7,
        text=dedent(
            """\
            Binden Sie die vorgegebene Style - Datei carListStyle.css ein.
            Die entsprechende Datei ist unter der URL carListStyle.css zu finden.
            Setzen Sie auch den entsprechenden Wert für das Attribut rel!"""
        ).replace('\n', ' '),
        xpathQuery='/html/head/link',
        awaitedTagName='link',
        attributes=[
            HtmlAttribute(key='href', value='carListStyle.css'),
            HtmlAttribute(key='rel', value='stylesheet')
        ]
    )
]

sampleSolution: SampleSolution[WebSolution] = SampleSolution(
    id=1,
    sample=WebSolution(
        files=[
            ExerciseFile(
                name='carList.html',
                fileType='htmlmixed',
                editable=False,
                content=load_text_from_file(ex_res_folder / 'sol_1' / 'carList.html')
            )
        ]
    )
)

web_coll_1_ex_1: WebExercise = WebExercise(
    id=1,
    collectionId=1,
    toolId='web',
    title='Listen in Html',
    authors=['bje40dc'],
    text=load_text_from_file(ex_res_folder / 'text.html'),
    topics=[],
    difficulty=1,
    sampleSolutions=[sampleSolution],
    content=WebExerciseContent(
        files=[
            ExerciseFile(
                name='carList.html',
                fileType='htmlmixed',
                editable=True,
                content=load_text_from_file(ex_res_folder / 'carList.html'),
            ),
            ExerciseFile(
                name='carListStyle.css',
                fileType='css',
                editable=False,
                content=load_text_from_file(ex_res_folder / 'carListStyle.css'),
            )
        ],
        siteSpec=SiteSpec(
            fileName='carList.html',
            htmlTasks=html_tasks,
            jsTasks=[]
        ),
    )
)
