#!/usr/bin/env python3
"""Module 9-insert_school: insert a document in MongoDB."""


def insert_school(mongo_collection, **kwargs):
    """Insert a new document in a collection.

    Args:
        mongo_collection: pymongo collection object
        **kwargs: fields to insert

    Returns:
        The _id of the newly created document
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
