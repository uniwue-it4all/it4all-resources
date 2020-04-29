from dataclasses import asdict as dataclasses_asdcit
from typing import List

# noinspection Mypy
from colorama import init as colorama_init, Fore
# noinspection Mypy
from pymongo import MongoClient, ASCENDING
# noinspection Mypy
from pymongo.collection import Collection
# noinspection Mypy
from pymongo.database import Database

from all_data import all_tools
from models.collection import ExerciseCollection, ExCollKey, ExKey

db_name = 'it4all'

collections_coll_name = 'exercise_collections'
exercises_coll_name = 'exercises'

username = 'root'
password = '1234'

colorama_init()

client: MongoClient = MongoClient(f'mongodb://{username}:{password}@localhost:27017/')

db: Database = client.get_database(db_name)

print(Fore.WHITE + f'connected to database {db_name}...')

existing_collections: List[str] = db.list_collection_names()

collections_coll: Collection
if collections_coll_name not in existing_collections:
    collections_coll = db.create_collection(collections_coll_name)

    print(f'Created collection {collections_coll.name}')

    collections_unique_index_name: str = collections_coll.create_index(
        [('toolId', ASCENDING), ('collectionId', ASCENDING)], unique=True
    )

    print(f'Created unique index on {collections_coll.name}: {collections_unique_index_name}')
else:
    collections_coll = db.get_collection(collections_coll_name)

exercises_coll: Collection
if exercises_coll_name not in existing_collections:
    exercises_coll = db.create_collection(exercises_coll_name)

    print(f'Create collection {exercises_coll.name}')

    exercises_unique_index_name: str = exercises_coll.create_index(
        [('toolId', ASCENDING), ('collectionId', ASCENDING), ('exerciseId', ASCENDING)], unique=True
    )

    print(f'Create unique index on {exercises_coll.name}: {exercises_unique_index_name}')
else:
    exercises_coll = db.get_collection(exercises_coll_name)

for tool_values in all_tools.values():
    for collectionsAndExes in tool_values.collectionAndExes.values():
        exercise_collection: ExerciseCollection = collectionsAndExes.collection

        coll_key: ExCollKey = exercise_collection.key()

        collections_coll.replace_one(coll_key, dataclasses_asdcit(exercise_collection), upsert=True)
        print(f'Inserted collection for key {coll_key}')

        for exercise in collectionsAndExes.exercises.values():
            ex_key: ExKey = exercise.key()

            exercises_coll.replace_one(ex_key, dataclasses_asdcit(exercise), upsert=True)

            print(f'Inserted exercise for key {ex_key}')

client.close()

print('collection closed')
