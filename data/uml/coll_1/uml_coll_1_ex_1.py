from textwrap import dedent

from models.collection import SampleSolution
from models.uml import UmlClassDiagram, UmlMapping, UmlClass, UmlClassType, UmlAttribute, UmlMethod, UmlAssociation, \
    UmlImplementation, UmlMultiplicity, UmlExercise, UmlExerciseContent

sample: UmlClassDiagram = UmlClassDiagram(
    classes=[
        UmlClass(
            name='Kunde',
            attributes=[
                UmlAttribute(memberName='name', memberType='string'),
                UmlAttribute(memberName='kundennummer', memberType='int')
            ],
            methods=[UmlMethod(memberName='gesamtGuthaben', parameters='', memberType='float')]
        ),
        UmlClass(
            name='Konto',
            classType=UmlClassType.ABSTRACT,
            attributes=[
                UmlAttribute(memberName='kontonummer', memberType='int'),
                UmlAttribute(memberName='vertragsdauerInJahren', memberType='int'),
                UmlAttribute(memberName='zinssatz', memberType='float'),
                UmlAttribute(memberName='saldo', memberType='float')
            ],
            methods=[UmlMethod(memberName='einzahlen', parameters='double', memberType='void')]
        ),
        UmlClass(name='Sparkonto'),
        UmlClass(name='Girokonto'),
        UmlClass(name='Kreditkonto')
    ],

    associations=[
        UmlAssociation(
            firstEnd='Kunde', firstMult=UmlMultiplicity.SINGLE,
            secondEnd='Konto', secondMult=UmlMultiplicity.UNBOUND
        )
    ],
    implementations=[
        UmlImplementation(subClass='Girokonto', superClass='Konto'),
        UmlImplementation(subClass='Sparkonto', superClass='Konto'),
        UmlImplementation(subClass='Kreditkonto', superClass='Konto')
    ]
)

uml_coll_1_ex_1: UmlExercise = UmlExercise(
    id=1,
    collectionId=1,
    toolId='uml',
    title='Tutorial Konto',
    authors=['bje40dc'],
    text=dedent(
        """\
        Eine Bank verwaltet die Konten ihrer Kunden.
        Jedes Konto wird durch die Kontonummer identifiziert und speichert das momentane Saldo sowie die
        Vertragsdauer (in Jahren).
        Diese Konten können entweder ein Girokonto, ein Sparkonto oder ein Kreditkonto sein.
        Für jeden Typ von Konto gilt ein anderer Zinssatz: Für ein Girokonto gibt es keine Zinsen, für ein Sparkonto
        1 Prozent und für ein Kreditkonto 3 Prozent.
        Die Kunden der Bank werden durch ihre Kundennummer identifiziert.
        Es soll außerdem jeweils der komplette Name gespeichert werden.
        Jeder Kunde kann mehrere Konten besitzen und hat die Möglichkeit, sich das Gesamtsaldo aller Konten anzeigen
        zu lassen und Geld auf ein Konto einzuzahlen."""
    ).replace('\n', ' '),
    topics=[],
    difficulty=1,
    sampleSolutions=[SampleSolution(id=1, sample=sample)],
    content=UmlExerciseContent(
        mappings=[
            UmlMapping(key='Konten', value='Konto'),
            UmlMapping(key='Kunden', value='Kunde'),
            UmlMapping(key='Jahren', value='Jahr'),
            UmlMapping(key='Zinsen', value='Zins'),
        ],
        toIgnore=['Eine', 'Jedes', 'Diese', 'Für', 'Jeder', 'Es', 'Zudem', 'Die'],
    )
)
