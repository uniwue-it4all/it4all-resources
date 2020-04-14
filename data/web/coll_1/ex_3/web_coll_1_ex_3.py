from textwrap import dedent

from models.collection import ExerciseState, SampleSolution, SemanticVersion, load_text_from_file, \
    base_res_path, ExerciseFile, Exercise
from models.web import WebExerciseContent, SiteSpec, HtmlTask, HtmlAttribute, WebSolution

html_tasks = [
    HtmlTask(
        id=1,
        text="""Erstellen Sie eine passende h1 - Überschrift, die 'Ford Mustang' enthält.""",
        xpathQuery='/html/body//h1',
        awaitedTagName='h1',
        awaitedTextContent='Ford Mustang'
    ),
    HtmlTask(
        id=2,
        text=dedent(
            """\
            Erstellen Sie den Link auf der Seite, der auf Wikipedia verweist.
            Geben Sie als Ziel die URL 'https=//de.wikipedia.org/wiki/Ford_Mustang' an."""
        ).replace('\n', ' '),
        xpathQuery='/html/body//a',
        awaitedTagName='a',
        attributes=[HtmlAttribute(key='href', value='https=//de.wikipedia.org/wiki/Ford_Mustang')]
    ),
    HtmlTask(
        id=3,
        text=dedent(
            """\
            Erstellen Sie im Link das Bild des Ford Mustang.
            Geben Sie als Quelle des Bildes die URL
            'https=//upload.wikimedia.org/wikipedia/commons/2/2d/1964_12_Ford_Mustang.jpg' und als alternative
            Beschreibung 'Ford Mustang' an.
            Geben Sie außerdem eine Breite von 250 und eine Höhe von 188 an, um das Bild zu skalieren."""
        ).replace('\n', ' '),
        xpathQuery='/html/body//a//img',
        awaitedTagName='img',
        attributes=[
            HtmlAttribute(
                key='src',
                value='https=//upload.wikimedia.org/wikipedia/commons/2/2d/1964_12_Ford_Mustang.jpg'),
            HtmlAttribute(key='alt', value='Ford Mustang'),
            HtmlAttribute(key='width', value='250'),
            HtmlAttribute(key='height', value='188')
        ]
    ),
    HtmlTask(
        id=4,
        text=dedent(
            """\
            Binden Sie die vorgegebene CSS - Datei 'mustangStyle.css' ein.
            Die entsprechende Datei ist unter der URL 'mustangStyle.css' zu finden.
            Setzen Sie auch den entsprechenden Wert für das Attribut 'rel'."""
        ).replace('\n', ' '),
        xpathQuery='/html/head//link',
        awaitedTagName='link',
        attributes=[
            HtmlAttribute(key='rel', value='stylesheet'),
            HtmlAttribute(key='href', value='mustangStyle.css')
        ]
    )
]

sampleSolution: SampleSolution[WebSolution] = SampleSolution(
    id=1,
    sample=WebSolution(
        files=[
            ExerciseFile(
                name='mustang.html',
                fileType='htmlmixed',
                editable=False,
                content=load_text_from_file(base_res_path / 'web' / 'coll_1' / 'ex_3' / 'sol_1' / 'mustang.html'),
            )
        ]
    )
)

web_coll_1_ex_3 = Exercise(
    id=3,
    collectionId=1,
    toolId='web',
    semanticVersion=SemanticVersion(major=1, minor=0, patch=0),
    title='Hyperlinks und Bilder in HTML',
    authors=['bje40dc'],
    text=load_text_from_file(base_res_path / 'web' / 'coll_1' / 'ex_3' / 'text.html'),
    tags=[],
    state=ExerciseState.APPROVED,
    difficulty=2,
    content=WebExerciseContent(
        files=[
            ExerciseFile(
                name='mustang.html',
                fileType='htmlmixed',
                editable=True,
                content=load_text_from_file(base_res_path / 'web' / 'coll_1' / 'ex_3' / 'mustang.html'),
            ),
            ExerciseFile(
                name='mustangStyle.css',
                fileType='css',
                editable=False,
                content=load_text_from_file(base_res_path / 'web' / 'coll_1' / 'ex_3' / 'mustangStyle.css'),
            )
        ],
        siteSpec=SiteSpec(
            fileName='mustang.html',
            htmlTasks=html_tasks,
            jsTasks=[]
        ),
        sampleSolutions=[sampleSolution]
    )
)
