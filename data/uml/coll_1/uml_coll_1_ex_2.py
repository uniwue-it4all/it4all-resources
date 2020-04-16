from textwrap import dedent

from models.collection import SampleSolution
from models.uml import UmlClass, UmlMethod, UmlAttribute, UmlClassDiagram, UmlMapping, UmlAssociation, \
    UmlImplementation, UmlClassType, UmlMultiplicity, UmlExercise

sample: UmlClassDiagram = UmlClassDiagram(
    classes=[
        UmlClass(
            classType=UmlClassType.ABSTRACT,
            name='Person',
            attributes=[
                UmlAttribute(memberName='id', memberType='int'),
                UmlAttribute(memberName='name', memberType='string')
            ]
        ),
        UmlClass(
            name='Doktor',
            methods=[UmlMethod(memberName='verschreiben', parameters='Patient', memberType='void')]
        ),
        UmlClass(
            name='Rezept',
            attributes=[UmlAttribute(memberName='id', memberType='int')]
        ),
        UmlClass(
            name='Patient',
            methods=[
                UmlMethod(memberName='entlassen', parameters='Station', memberType='void'),
                UmlMethod(memberName='aufnehmen', parameters='Station', memberType='void')
            ]
        ),
        UmlClass(name='Krankenschwester'),
        UmlClass(
            name='Station',
            attributes=[
                UmlAttribute(memberName='nummer', memberType='int')
            ]
        ),
        UmlClass(
            name='Medikament',
            attributes=[
                UmlAttribute(memberName='id', memberType='int'),
                UmlAttribute(memberName='name', memberType='string')
            ]
        ),
        UmlClass(
            name='Krankenhaus',
            attributes=[UmlAttribute(memberName='name', memberType='string')]
        )
    ],
    implementations=[
        UmlImplementation(subClass='Patient', superClass='Person'),
        UmlImplementation(subClass='Doktor', superClass='Person'),
        UmlImplementation(subClass='Krankenschwester', superClass='Person')
    ],
    associations=[
        UmlAssociation(
            firstEnd='Doktor', firstMult=UmlMultiplicity.SINGLE,
            secondEnd='Rezept', secondMult=UmlMultiplicity.UNBOUND),
        UmlAssociation(
            firstEnd='Station', firstMult=UmlMultiplicity.SINGLE,
            secondEnd='Patient', secondMult=UmlMultiplicity.UNBOUND),
        UmlAssociation(
            firstEnd='Station', firstMult=UmlMultiplicity.SINGLE,
            secondEnd='Krankenschwester',
            secondMult=UmlMultiplicity.UNBOUND),
        UmlAssociation(
            firstEnd='Station', firstMult=UmlMultiplicity.SINGLE,
            secondEnd='Doktor', secondMult=UmlMultiplicity.UNBOUND),
        UmlAssociation(
            firstEnd='Patient', firstMult=UmlMultiplicity.SINGLE,
            secondEnd='Rezept', secondMult=UmlMultiplicity.UNBOUND),
        UmlAssociation(
            firstEnd='Rezept', firstMult=UmlMultiplicity.UNBOUND,
            secondEnd='Medikament', secondMult=UmlMultiplicity.UNBOUND),
        UmlAssociation(
            firstEnd='Station', firstMult=UmlMultiplicity.UNBOUND,
            secondEnd='Krankenhaus', secondMult=UmlMultiplicity.SINGLE
        )
    ]
)

uml_coll_1_ex_2: UmlExercise = UmlExercise(
    id=2,
    collectionId=1,
    toolId='uml',
    title='Krankenhaus',
    authors=['bje40dc'],
    text=dedent(
        """\
        Ein Krankenhaus hat einen Namen und besteht aus Stationen mit einer eindeutigen Nummer.
        Jede Station hat einen oder mehrere Doktoren, Krankenschwestern und Patienten.
        Jede Person hat jeweils eine eindeutige Id und einen Namen.
        Ein Doktor kann dem Patienten ein Rezept mit einer eindeutigen Id verschreiben, das ein oder mehrere
        Medikamente beinhalten kann.
        Ein Medikament hat eine eindeutige Id und einen Namen und kann Patienten auf verschiedenen Rezepten
        verschrieben werden.
        Ein Patient wiederum kann in einer Station aufgenommen bzw. entlassen werden."""
    ).replace('\n', ' '),
    topics=[],
    difficulty=2,
    mappings=[
        UmlMapping(key='Stationen', value='Station'),
        UmlMapping(key='Doktoren', value='Doktor'),
        UmlMapping(key='Krankenschwestern', value='Krankenschwester'),
        UmlMapping(key='Patienten', value='Patient'),
        UmlMapping(key='Namen', value='Name'),
        UmlMapping(key='Medikamente', value='Medikament'),
        UmlMapping(key='Rezepten', value='Rezept')
    ],
    toIgnore=['Ein', 'Jede'],
    sampleSolutions=[SampleSolution(id=1, sample=sample)]
)
