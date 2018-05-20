
import os
import json


class collectionClass:

    def __init__(self, dbName, collName):

        parsedJSON = json.loads(
            open("./data/{}/{}".format(dbName, collName), "r").read())["docs"]

        self.dict = parsedJSON
        self.json = open("./data/{}/{}".format(dbName, collName), "r").read()

        def get():

            return parsedJSON

        self.get = get

        def doc(query):

            returnValue = []

            for doc in parsedJSON:

                lenQueries = len(list(query))
                matches = 0

                for key, value in query.items():

                    try:

                        if doc[key] == value:
                            matches += 1
                        else:
                            break

                    except KeyError:
                        return None

                if matches == lenQueries:
                    returnValue.append(doc)

            return returnValue

        self.doc = doc

        def insert(doc):

            parsedJSON.append(doc)
            JSON_To_Write = json.loads(
                open("./data/{}/{}".format(dbName, collName), "r").read())
            JSON_To_Write["docs"] = parsedJSON
            JSON_To_Write = json.dumps(JSON_To_Write)

            with open("./data/{}/{}".format(dbName, collName), "w") as file:
                file.write(JSON_To_Write)

        self.insert = insert
