from textwrap import dedent

from models.collection import ExerciseFile, Exercise, SemanticVersion, load_text_from_file, base_res_path, \
    ExerciseState, SampleSolution
from models.web import WebExerciseContent, WebSolution, SiteSpec, HtmlTask, HtmlAttribute

web_coll_1_ex_2: Exercise[WebExerciseContent] = Exercise(
    id=2,
    collection_id=1,
    tool_id='web',
    semantic_version=SemanticVersion(major=1, minor=0, patch=0),
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
                file_type='htmlmixed',
                editable=True,
                content=load_text_from_file(base_res_path / 'web' / 'coll_1' / 'ex_2' / 'production.html')
            ),
            ExerciseFile(
                name='productionStyle.css',
                file_type='css',
                editable=False,
                content=load_text_from_file(base_res_path / 'web' / 'coll_1' / 'ex_2' / 'productionStyle.css')
            )
        ],
        site_spec=SiteSpec(
            file_name='production.html',
            html_tasks=[
                HtmlTask(
                    id=1,
                    text='Erstellen Sie das Grundtag für die Tabelle.',
                    xpath_query='/html/body//table',
                    awaited_tag_name='table'
                ),
                HtmlTask(
                    id=2,
                    text='Erstellen Sie die erste Zeile für die Überschriften.',
                    xpath_query='/html/body//table//tr[1]',
                    awaited_tag_name='tr'
                ),
                HtmlTask(
                    id=3,
                    text="""Erstellen Sie die erste Zelle für die Überschrift. Diese soll als Inhalt 'Jahr' haben.""",
                    xpath_query='html/body//table//tr[1]/th[1]',
                    awaited_tag_name='th',
                    awaited_text_content='Jahr'
                ), HtmlTask(
                    id=4,
                    text=dedent(
                        """\
                        Erstellen Sie die zweite Zelle für die Überschrift.
                        Diese soll als Inhalt 'Produktion' haben."""
                    ),
                    xpath_query='html/body//table//tr[1]/th[2]',
                    awaited_tag_name='th',
                    awaited_text_content='Produktion'
                ),
                HtmlTask(
                    id=5,
                    text='Erstellen Sie die zweite Zeile in der Tabelle',
                    xpath_query='/html/body//table//tr[2]',
                    awaited_tag_name='tr'
                ),
                HtmlTask(
                    id=6,
                    text="""Erstellen Sie die erste Zelle in der zweiten Zeile. Diese soll als Inhalt '1900' haben.""",
                    xpath_query='html/body//table//tr[2]/td[1]',
                    awaited_tag_name='td',
                    awaited_text_content='1900'
                ),
                HtmlTask(
                    id=7,
                    text="""Erstellen Sie die zweite Zelle in der zweiten Zeile. Diese soll als Inhalt '9504' haben.""",
                    xpath_query='html/body//table//tr[2]/td[2]',
                    awaited_tag_name='td',
                    awaited_text_content='9504'
                ),
                HtmlTask(
                    id=8,
                    text='Erstellen Sie die dritte Zeile in der Tabelle',
                    xpath_query='/html/body//table//tr[3]',
                    awaited_tag_name='tr'
                ),
                HtmlTask(
                    id=9,
                    text="""Erstellen Sie die erste Zelle in der dritten Zeile. Diese soll als Inhalt '1950' haben.""",
                    xpath_query='html/body//table//tr[3]/td[1]',
                    awaited_tag_name='td',
                    awaited_text_content='1950'
                ),
                HtmlTask(
                    id=10,
                    text=dedent(
                        """\
                        Erstellen Sie die zweite Zelle in der dritten Zeile.
                        Diese soll als Inhalt '10577426' haben."""
                    ),
                    xpath_query='html/body//table//tr[3]/td[2]',
                    awaited_tag_name='td',
                    awaited_text_content='10577426'
                ),
                HtmlTask(
                    id=11,
                    text='Erstellen Sie die vierte Zeile in der Tabelle.',
                    xpath_query='/html/body//table//tr[4]',
                    awaited_tag_name='td'
                ),
                HtmlTask(
                    id=12,
                    text="""Erstellen Sie die erste Zelle in der vierten Zeile. Diese soll als Inhalt '2000' haben.""",
                    xpath_query='html/body//table//tr[4]/td[1]',
                    awaited_tag_name='td',
                    awaited_text_content='2000'
                ),
                HtmlTask(
                    id=13,
                    text=dedent(
                        """\
                        Erstellen Sie die zweite Zelle in der vierten Zeile.
                        Diese soll als Inhalt '58374162' haben"""
                    ),
                    xpath_query='html/body//table//tr[4]/td[2]',
                    awaited_tag_name='td',
                    awaited_text_content='58374162'
                ),
                HtmlTask(
                    id=14,
                    text=dedent(
                        """\
                        Binden Sie die vorgegebene CSS-Datei 'productionStyle.css' ein.
                        Die entsprechende Datei ist unter der URL 'productionStyle.css' zu finden.
                        Setzen Sie auch den entsprechenden Wert für das Attribut 'rel'."""
                    ),
                    xpath_query='/html/head//link',
                    awaited_tag_name='link',
                    attributes=[
                        HtmlAttribute(key='href', value='productionStyle.css'),
                        HtmlAttribute(key='rel', value='stylesheet')
                    ]
                )
            ],
            js_tasks=[]
        ),
        sample_solutions=[
            SampleSolution(
                id=1,
                sample=WebSolution(
                    files=[
                        ExerciseFile(
                            name='production.html',
                            file_type='htmlmixed',
                            editable=False,
                            content=load_text_from_file(
                                base_res_path / 'web' / 'coll_1' / 'ex_2' / 'sol_1' / 'production.html'
                            ),
                        )
                    ]
                )
            )
        ]
    )
)
