#!/usr/bin/env python3
"""Module 8-all: list all documents in a MongoDB collection."""


def list_all(mongo_collection):
    """Return a list of all documents in `mongo_collection`.

    Args:
        mongo_collection: a pymongo collection object.

    Returns:
        A list of documents (empty list if the collection has no documents).
    """
    return list(mongo_collection.find())
