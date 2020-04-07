from textwrap import dedent

from models.web import WebExerciseContent

ex_1: WebExerciseContent = {
    'html_text': None,
    'js_text': None,
    'files': [
        {
            'name': 'carList.html',
            'resource_path': 'carList.html',
            'file_type': 'htmlmixed',
            'editable': True
        },
        {
            'name': 'carListStyle.css',
            'resource_path': 'carListStyle.css',
            'file_type': 'css',
            'editable': False
        }
    ],
    'site_spec': {
        'file_name': 'carList.html',
        'html_tasks': [
            {
                'id': 1,
                'text': """Erstellen Sie eine passende h1 - Überschrift, die das Wort 'Autohersteller' enthält.""",
                'xpath_query': '/html/body//h1',
                'awaited_tag_name': 'h1',
                'awaited_text_content': 'Autohersteller'
            },
            {
                'id': 2,
                'text': dedent("""\
                    Erstellen Sie eine ungeordnete Liste auf der Seite, die dann die einzelnen Hersteller
                    enthalten wird.
                    """),
                'xpath_query': '/html/body//ul',
                'awaited_tag_name': 'ul'
            },
            {
                'id': 3,
                'text': """Erstellen Sie ein Listenelement mit dem Text 'Audi'.""",
                'xpath_query': """/html/body//ul/li[contains(text(), 'Audi')]""",
                'awaited_tag_name': 'li',
                'awaited_text_content': 'Audi',
            },
            {
                'id': 4,
                'text': """Erstellen Sie ein Listenelement mit dem Text 'BMW'.""",
                'xpath_query': """/html/body//ul/li[contains(text(), 'BMW')]""",
                'awaited_tag_name': 'li',
                'awaited_text_content': 'BMW'
            },
            {

                'id': 5,
                'text': """Erstellen Sie ein Listenelement mit dem Text 'Mercedes'.""",
                'xpath_query': """/html/body//ul/li[contains(text(), 'Mercedes')]""",
                'awaited_tag_name': 'li',
                'awaited_text_content': 'Mercedes'
            },
            {
                'id': 6,
                'text': """Erstellen Sie ein Listenelement mit dem Text 'Volkswagen'.""",
                'xpath_query': """/html/body//ul/li[contains(text(), 'Volkswagen')]""",
                'awaited_tag_name': 'li',
                'awaited_text_content': 'Volkswagen'
            },
            {
                'id': 7,
                'text': dedent("""\
                    Binden Sie die vorgegebene Style - Datei 'carListStyle.css' ein.
                    Die entsprechende Datei ist unter der URL 'carListStyle.css' zu finden.
                    Setzen Sie auch den entsprechenden Wert für das Attribut 'rel'!
                    """),
                'xpath_query': '/html/head/link',
                'awaited_tag_name': 'link',
                'attributes': [
                    {'key': 'href', 'value': 'carListStyle.css'},
                    {'key': 'rel', 'value': 'stylesheet'}
                ]
            }

        ],
        'js_tasks': []
    },
    'sample_solutions': [
        {'id': 1, 'sample': []}
    ]
}
