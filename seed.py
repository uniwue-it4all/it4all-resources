from dataclasses import asdict as dataclasses_asdcit

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

users_coll_name = 'users'
lessons_coll_name = 'lessons'
collections_coll_name = 'exercise_collections'
exercises_coll_name = 'exercises'

username = 'root'
password = '1234'

new_username = 'it4all'
new_password = password

colorama_init()

client: MongoClient = MongoClient(f'mongodb://{username}:{password}@localhost:27017/')

db: Database = client.get_database(db_name)

print(Fore.WHITE)

print(f'connected to database {db_name}...')

db.command('createUser', new_username, pwd=new_password, roles=["readWrite"])

# Create collection and index for Users
users_coll: Collection = db.get_collection(users_coll_name)
users_unique_index_name = users_coll.create_index([('username', ASCENDING)], unique=True)

print(f'Created unique index on {users_coll.name}: {users_unique_index_name}')

# Create collection and index for Lessons
lessons_coll: Collection = db.get_collection(lessons_coll_name)
lessons_unique_index_name = lessons_coll.create_index([('toolId', ASCENDING), ('lessonId', ASCENDING)], unique=True)

print(f'Created unique index on {lessons_coll.name}: {lessons_unique_index_name}')

# Create collection and index for ExerciseCollections
collections_coll: Collection = db.get_collection(collections_coll_name)
collections_unique_index_name: str = collections_coll.create_index(
    [('toolId', ASCENDING), ('collectionId', ASCENDING)], unique=True
)

print(f'Created unique index on {collections_coll.name}: {collections_unique_index_name}')

# Create collection and index for Exercises
exercises_coll: Collection = db.get_collection(exercises_coll_name)

exercises_unique_index_name: str = exercises_coll.create_index(
    [('toolId', ASCENDING), ('collectionId', ASCENDING), ('exerciseId', ASCENDING)], unique=True
)

print(f'Create unique index on {exercises_coll.name}: {exercises_unique_index_name}')

# Insert all collections and exercises

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
