import os


def file_names_in_directory(directory):
    for entry in os.scandir(directory):
        if entry.is_file():
            yield entry.name


# given generator that returns data that should be inserted to the DB,
# this function executes a commit every commit_size objects
def commit_in_chunks(db_session, data_generator, commit_size):
    current_size = 0
    for data in data_generator:
        db_session.add(data)
        current_size += 1
        if current_size == commit_size:
            db_session.commit()
            current_size = 0
    if current_size > 0:
        db_session.commit()
