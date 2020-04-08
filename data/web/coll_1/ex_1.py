from textwrap import dedent

from models.collection import Exercise, SemanticVersion, ExerciseState, load_text_from_file, base_res_path, \
    SampleSolution
from models.web import WebExerciseContent, ExerciseFile, SiteSpec, HtmlTask, HtmlAttribute, WebSolution

web_coll_1_ex_1: Exercise[WebExerciseContent] = Exercise(
    id=1,
    collection_id=1,
    tool_id='web',
    semantic_version=SemanticVersion(major=1, minor=0, patch=0),
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
                file_type='htmlmixed',
                editable=True,
                content=load_text_from_file(base_res_path / 'web' / 'coll_1' / 'ex_1' / 'carList.html'),
            ),
            ExerciseFile(
                name='carListStyle.css',
                file_type='css',
                editable=False,
                content=load_text_from_file(base_res_path / 'web' / 'coll_1' / 'ex_1' / 'carListStyle.css'),
            )
        ],
        site_spec=SiteSpec(
            file_name='carList.html',
            html_tasks=[
                HtmlTask(
                    id=1,
                    text="""Erstellen Sie eine passende h1 - Überschrift, die das Wort Autohersteller enthält.""",
                    xpath_query='/html/body//h1',
                    awaited_tag_name='h1',
                    awaited_text_content='Autohersteller'
                ),
                HtmlTask(
                    id=2,
                    text=dedent("""\
                    Erstellen Sie eine ungeordnete Liste auf der Seite, die dann die einzelnen Hersteller
                    enthalten wird.
                    """),
                    xpath_query='/html/body//ul',
                    awaited_tag_name='ul'
                ),
                HtmlTask(
                    id=3,
                    text="""Erstellen Sie ein Listenelement mit dem Text Audi.""",
                    xpath_query="""/html/body//ul/li[contains(text(), Audi)]""",
                    awaited_tag_name='li',
                    awaited_text_content='Audi',
                ),
                HtmlTask(
                    id=4,
                    text="""Erstellen Sie ein Listenelement mit dem Text BMW.""",
                    xpath_query="""/html/body//ul/li[contains(text(), BMW)]""",
                    awaited_tag_name='li',
                    awaited_text_content='BMW'
                ),
                HtmlTask(
                    id=5,
                    text="""Erstellen Sie ein Listenelement mit dem Text Mercedes.""",
                    xpath_query="""/html/body//ul/li[contains(text(), Mercedes)]""",
                    awaited_tag_name='li',
                    awaited_text_content='Mercedes'
                ),
                HtmlTask(
                    id=6,
                    text="""Erstellen Sie ein Listenelement mit dem Text Volkswagen.""",
                    xpath_query="""/html/body//ul/li[contains(text(), Volkswagen)]""",
                    awaited_tag_name='li',
                    awaited_text_content='Volkswagen'
                ),
                HtmlTask(
                    id=7,
                    text=dedent("""\
                    Binden Sie die vorgegebene Style - Datei carListStyle.css ein.
                    Die entsprechende Datei ist unter der URL carListStyle.css zu finden.
                    Setzen Sie auch den entsprechenden Wert für das Attribut rel!
                    """),
                    xpath_query='/html/head/link',
                    awaited_tag_name='link',
                    attributes=[
                        HtmlAttribute(key='href', value='carListStyle.css'),
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
                            name='carList.html',
                            file_type='htmlmixed',
                            editable=False,
                            content=load_text_from_file(
                                base_res_path / 'web' / 'coll_1' / 'ex_1' / 'sol_1' / 'carList.html'
                            )
                        )
                    ]
                )
            )
        ]
    )
)
