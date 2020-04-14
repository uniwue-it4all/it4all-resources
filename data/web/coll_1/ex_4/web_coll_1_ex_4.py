from textwrap import dedent
from typing import List

from models.collection import Exercise, ExerciseFile, ExerciseState, SampleSolution, SemanticVersion, \
    load_text_from_file, base_res_path
from models.web import WebSolution, WebExerciseContent, HtmlAttribute, SiteSpec, HtmlTask

html_tasks: List[HtmlTask] = [
    HtmlTask(
        id=1,
        text=dedent(
            """\
            Erstellen Sie das Formular - Tag.
            Geben Sie für die Attribute 'action' und 'method' jeweils die Werte '/test.php' und 'post' an."""
        ).replace('\n', ' '),
        xpathQuery='/html/body//form',
        awaitedTagName='form',
        attributes=[
            HtmlAttribute(key='action', value='/test.php'),
            HtmlAttribute(key='method', value='post')
        ]
    ),
    HtmlTask(
        id=2,
        text="""Erstellen Sie ein Label mit dem Inhalt 'Email' für das Eingabefeld mit der ID 'email'.""",
        xpathQuery="""/html/body//form//label[@for ='email']""",
        awaitedTagName='label',
        awaitedTextContent='Email'
    ),
    HtmlTask(
        id=3,
        text=dedent(
            """\
            Erstellen Sie ein Feld zur Eingabe der Emailadresse.
            Benutzen Sie den in der Vorlesung gezeigten Typen und geben Sie den Attributen 'name' und 'id' jeweils den
            Wert 'email'.
            Die Eingabe soll eines Wertes soll außerdem verpflichtend sein."""
        ).replace('\n', ' '),
        xpathQuery="""/html/body//form//input[@type='email']""",
        awaitedTagName='input',
        attributes=[
            HtmlAttribute(key='name', value='email'),
            HtmlAttribute(key='id', value='email'),
            HtmlAttribute(key='required', value='true')
        ]
    ),
    HtmlTask(
        id=4,
        text="""Erstellen Sie ein Label mit dem Inhalt 'Passwort' für das Eingabefeld mit der ID 'passwort'.""",
        xpathQuery="""/html/body//form//label[@for='passwort']""",
        awaitedTagName='label',
        awaitedTextContent='Passwort'
    ),
    HtmlTask(
        id=5,
        text=dedent(
            """\
            Erstellen Sie ein Feld zur Eingabe des Passworts.Benutzen Sie den in der Vorlesung gezeigten Typen und
            geben Sie dem Attribut 'name' den Wert 'passwort'.Die Eingabe soll außerdem verpflichtend sein."""
        ).replace('\n', ' '),
        xpathQuery="""/html/body//form//input[@type='password']""",
        awaitedTagName='input',
        attributes=[
            HtmlAttribute(key='name', value='passwort'),
            HtmlAttribute(key='id', value='passwort'),
            HtmlAttribute(key='required', value='true')
        ]
    ),
    HtmlTask(
        id=6,
        text="""Erstellen Sie einen Knopf ('input', kein 'button') um das Formular abzusenden.""",
        xpathQuery="""/html/body//form//input[@type='submit']""",
        awaitedTagName='input'
    ),
    HtmlTask(
        id=7,
        text=dedent(
            """\
            Binden Sie die vorgegebene CSS - Datei 'loginStyle.css' ein.
            Die entsprechende Datei ist unter der URL 'loginStyle.css' zu finden.
            Setzen Sie auch den entsprechenden Wert für das Attribut'rel'."""
        ).replace('\n', ' '),
        xpathQuery='/html/head//link',
        awaitedTagName='link',
        attributes=[
            HtmlAttribute(key='rel', value='stylesheet'),
            HtmlAttribute(key='href', value='loginStyle.css')
        ]
    )
]

sampleSolution: SampleSolution[WebSolution] = SampleSolution(
    id=1,
    sample=WebSolution(
        files=[
            ExerciseFile(
                name='login.html',
                fileType='htmlmixed',
                editable=False,
                content=load_text_from_file(base_res_path / 'web' / 'coll_1' / 'ex_4' / 'sol_1' / 'login.html')
            )
        ]
    )
)

web_coll_1_ex_4: Exercise[WebExerciseContent] = Exercise(
    id=4,
    collectionId=1,
    toolId='web',
    semanticVersion=SemanticVersion(major=1, minor=0, patch=0),
    title='Login-Formular',
    authors=['bje40dc'],
    text=load_text_from_file(base_res_path / 'web' / 'coll_1' / 'ex_4' / 'text.html'),
    tags=[],
    state=ExerciseState.APPROVED,
    difficulty=3,
    content=WebExerciseContent(
        files=[
            ExerciseFile(
                name='login.html',
                fileType='htmlmixed',
                editable=True,
                content=load_text_from_file(base_res_path / 'web' / 'coll_1' / 'ex_4' / 'login.html')
            ),
            ExerciseFile(
                name='loginStyle.css',
                fileType='css',
                editable=False,
                content=load_text_from_file(base_res_path / 'web' / 'coll_1' / 'ex_4' / 'loginStyle.css')
            )
        ],
        siteSpec=SiteSpec(
            fileName='login.html',
            htmlTasks=html_tasks,
            jsTasks=[]
        ),
        sampleSolutions=[sampleSolution]
    )
)
