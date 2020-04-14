from textwrap import dedent
from typing import List

from models.collection import ExerciseFile, ExerciseState, Exercise, SampleSolution, SemanticVersion, \
    load_text_from_file, base_res_path
from models.web import WebSolution, WebExerciseContent, HtmlTask, HtmlAttribute, SiteSpec, WebExTag

sampleSolution = SampleSolution(
    id=1,
    sample=WebSolution(
        files=[
            ExerciseFile(
                name='audio.html',
                fileType='htmlmixed',
                editable=False,
                content=load_text_from_file(base_res_path / 'web' / 'coll_1' / 'ex_5' / 'sol_1' / 'audio.html')
            )
        ]
    )
)

html_tasks: List[HtmlTask] = [
    HtmlTask(
        id=1,
        text="""Erstellen Sie eine passende h1-Überschrift die 'Deutsche Nationalhymne' enthält.""",
        xpathQuery='/html/body//h1',
        awaitedTagName='h1',
        awaitedTextContent='Deutsche Nationalhymne'
    ),
    HtmlTask(
        id=2,
        text=dedent(
            """\
            Erstellen Sie das Grundelement für die Audiodatei und aktivieren Sie die Kontrollelement.
            Falls der Browser keine Audiodateien unterstützt, soll der Text 'Ihr Browser unterstützt kein Audio!'
            ausgegeben werden."""
        ).replace('\n', ' '),
        xpathQuery='/html/body//audio',
        awaitedTagName='audio',
        awaitedTextContent='Ihr Browser unterstützt kein Audio!',
        attributes=[
            HtmlAttribute(key='controls', value='true')
        ]
    ),
    HtmlTask(
        id=3,
        text=dedent(
            """\
          Erstellen Sie das Element für die Quelldatei. Diese ist vom Typ 'audio/ogg' und befindet sich an der URL
          'https=//upload.wikimedia.org/wikipedia/commons/c/cb/National_anthem_of_Germany_-_U.S._Army_1st_Armored_Division_Band.ogg'"""
        ).replace('\n', ' '),
        xpathQuery='/html/body//audio/source',
        awaitedTagName='source',
        attributes=[
            HtmlAttribute(key='type', value='audio/ogg'),
            HtmlAttribute(
                key='src',
                value='https=//upload.wikimedia.org/wikipedia/commons/c/cb/National_anthem_of_Germany_-_U.S._Army_1st_Armored_Division_Band.ogg'
            )
        ]
    )
]

web_coll_1_ex_5: Exercise[WebExTag, WebExerciseContent] = Exercise(
    id=5,
    collectionId=1,
    toolId='web',
    semanticVersion=SemanticVersion(major=1, minor=0, patch=0),
    title='Audio in HTML 5',
    authors=['bje40dc'],
    text=load_text_from_file(base_res_path / 'web' / 'coll_1' / 'ex_5' / 'text.html'),
    tags=[],
    state=ExerciseState.APPROVED,
    difficulty=1,
    content=WebExerciseContent(
        files=[
            ExerciseFile(
                name='audio.html',
                fileType='htmlmixed',
                editable=True,
                content=load_text_from_file(base_res_path / 'web' / 'coll_1' / 'ex_5' / 'audio.html')
            )
        ],
        siteSpec=SiteSpec(
            fileName='audio.html',
            htmlTasks=html_tasks,
            jsTasks=[]
        ),
        sampleSolutions=[sampleSolution]
    )
)
