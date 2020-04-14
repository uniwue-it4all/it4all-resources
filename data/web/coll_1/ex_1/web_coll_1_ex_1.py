from textwrap import dedent
from typing import List

from models.collection import Exercise, SemanticVersion, ExerciseState, load_text_from_file, base_res_path, \
    SampleSolution
from models.web import WebExerciseContent, ExerciseFile, SiteSpec, HtmlTask, HtmlAttribute, WebSolution

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
                content=load_text_from_file(
                    base_res_path / 'web' / 'coll_1' / 'ex_1' / 'sol_1' / 'carList.html'
                )
            )
        ]
    )
)

web_coll_1_ex_1: Exercise[WebExerciseContent] = Exercise(
    id=1,
    collectionId=1,
    toolId='web',
    semanticVersion=SemanticVersion(major=1, minor=0, patch=0),
    title='Listen in Html',
    authors=['bje40dc'],
    text=load_text_from_file(base_res_path / 'web' / 'coll_1' / 'ex_1' / 'text.html'),
    tags=[],
    state=ExerciseState.APPROVED,
    difficulty=1,
    content=WebExerciseContent(
        files=[
            ExerciseFile(
                name='carList.html',
                fileType='htmlmixed',
                editable=True,
                content=load_text_from_file(base_res_path / 'web' / 'coll_1' / 'ex_1' / 'carList.html'),
            ),
            ExerciseFile(
                name='carListStyle.css',
                fileType='css',
                editable=False,
                content=load_text_from_file(base_res_path / 'web' / 'coll_1' / 'ex_1' / 'carListStyle.css'),
            )
        ],
        siteSpec=SiteSpec(
            fileName='carList.html',
            htmlTasks=html_tasks,
            jsTasks=[]
        ),
        sampleSolutions=[sampleSolution]
    )
)
