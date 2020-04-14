from textwrap import dedent
from typing import List

from models.collection import ExerciseFile, Exercise, SemanticVersion, load_text_from_file, base_res_path, \
    ExerciseState, SampleSolution
from models.web import WebExerciseContent, WebSolution, SiteSpec, HtmlTask, HtmlAttribute, WebExTag

html_tasks: List[HtmlTask] = [
    HtmlTask(
        id=1,
        text='Erstellen Sie das Grundtag für die Tabelle.',
        xpathQuery='/html/body//table',
        awaitedTagName='table'
    ),
    HtmlTask(
        id=2,
        text='Erstellen Sie die erste Zeile für die Überschriften.',
        xpathQuery='/html/body//table//tr[1]',
        awaitedTagName='tr'
    ),
    HtmlTask(
        id=3,
        text="""Erstellen Sie die erste Zelle für die Überschrift. Diese soll als Inhalt 'Jahr' haben.""",
        xpathQuery='html/body//table//tr[1]/th[1]',
        awaitedTagName='th',
        awaitedTextContent='Jahr'
    ), HtmlTask(
        id=4,
        text="""Erstellen Sie die zweite Zelle für die Überschrift. Diese soll als Inhalt 'Produktion' haben.""",
        xpathQuery='html/body//table//tr[1]/th[2]',
        awaitedTagName='th',
        awaitedTextContent='Produktion'
    ),
    HtmlTask(
        id=5,
        text='Erstellen Sie die zweite Zeile in der Tabelle',
        xpathQuery='/html/body//table//tr[2]',
        awaitedTagName='tr'
    ),
    HtmlTask(
        id=6,
        text="""Erstellen Sie die erste Zelle in der zweiten Zeile. Diese soll als Inhalt '1900' haben.""",
        xpathQuery='html/body//table//tr[2]/td[1]',
        awaitedTagName='td',
        awaitedTextContent='1900'
    ),
    HtmlTask(
        id=7,
        text="""Erstellen Sie die zweite Zelle in der zweiten Zeile. Diese soll als Inhalt '9504' haben.""",
        xpathQuery='html/body//table//tr[2]/td[2]',
        awaitedTagName='td',
        awaitedTextContent='9504'
    ),
    HtmlTask(
        id=8,
        text='Erstellen Sie die dritte Zeile in der Tabelle',
        xpathQuery='/html/body//table//tr[3]',
        awaitedTagName='tr'
    ),
    HtmlTask(
        id=9,
        text="""Erstellen Sie die erste Zelle in der dritten Zeile. Diese soll als Inhalt '1950' haben.""",
        xpathQuery='html/body//table//tr[3]/td[1]',
        awaitedTagName='td',
        awaitedTextContent='1950'
    ),
    HtmlTask(
        id=10,
        text="""Erstellen Sie die zweite Zelle in der dritten Zeile. Diese soll als Inhalt '10577426' haben.""",
        xpathQuery='html/body//table//tr[3]/td[2]',
        awaitedTagName='td',
        awaitedTextContent='10577426'
    ),
    HtmlTask(
        id=11,
        text='Erstellen Sie die vierte Zeile in der Tabelle.',
        xpathQuery='/html/body//table//tr[4]',
        awaitedTagName='td'
    ),
    HtmlTask(
        id=12,
        text="""Erstellen Sie die erste Zelle in der vierten Zeile. Diese soll als Inhalt '2000' haben.""",
        xpathQuery='html/body//table//tr[4]/td[1]',
        awaitedTagName='td',
        awaitedTextContent='2000'
    ),
    HtmlTask(
        id=13,
        text="""Erstellen Sie die zweite Zelle in der vierten Zeile. Diese soll als Inhalt '58374162' haben""",
        xpathQuery='html/body//table//tr[4]/td[2]',
        awaitedTagName='td',
        awaitedTextContent='58374162'
    ),
    HtmlTask(
        id=14,
        text=dedent(
            """\
            Binden Sie die vorgegebene CSS-Datei 'productionStyle.css' ein.
            Die entsprechende Datei ist unter der URL 'productionStyle.css' zu finden.
            Setzen Sie auch den entsprechenden Wert für das Attribut 'rel'."""
        ).replace('\n', ' '),
        xpathQuery='/html/head//link',
        awaitedTagName='link',
        attributes=[
            HtmlAttribute(key='href', value='productionStyle.css'),
            HtmlAttribute(key='rel', value='stylesheet')
        ]
    )
]

sampleSolution: SampleSolution[WebSolution] = SampleSolution(
    id=1,
    sample=WebSolution(
        files=[
            ExerciseFile(
                name='production.html',
                fileType='htmlmixed',
                editable=False,
                content=load_text_from_file(
                    base_res_path / 'web' / 'coll_1' / 'ex_2' / 'sol_1' / 'production.html'
                ),
            )
        ]
    )
)

web_coll_1_ex_2: Exercise[WebExTag, WebExerciseContent] = Exercise(
    id=2,
    collectionId=1,
    toolId='web',
    semanticVersion=SemanticVersion(major=1, minor=0, patch=0),
    title='Tabellen in Html',
    authors=['bje40dc'],
    text=load_text_from_file(base_res_path / 'web' / 'coll_1' / 'ex_2' / 'text.html'),
    tags=[],
    state=ExerciseState.APPROVED,
    difficulty=2,
    content=WebExerciseContent(
        files=[
            ExerciseFile(
                name='production.html',
                fileType='htmlmixed',
                editable=True,
                content=load_text_from_file(base_res_path / 'web' / 'coll_1' / 'ex_2' / 'production.html')
            ),
            ExerciseFile(
                name='productionStyle.css',
                fileType='css',
                editable=False,
                content=load_text_from_file(base_res_path / 'web' / 'coll_1' / 'ex_2' / 'productionStyle.css')
            )
        ],
        siteSpec=SiteSpec(
            fileName='production.html',
            htmlTasks=html_tasks,
            jsTasks=[]
        ),
        sampleSolutions=[sampleSolution]
    )
)
