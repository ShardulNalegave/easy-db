
import json
import os

from collection import collectionClass


class EasyDB:

    class use:

        def __init__(self, dbName):

            if os.path.isdir("./data/{}".format(dbName)):

                def isCollectionThen_Else(dbName, collName):

                    if os.path.isfile("./data/{}/{}.json".format(dbName, collName)):
                        return collectionClass(dbName, collName + ".json")
                    else:

                        open("./data/{}/{}.json".format(dbName, collName),
                             "w").write('{ "docs": [] }')

                        return collectionClass(dbName, collName + ".json")

                self.collection = lambda coll: isCollectionThen_Else(
                    dbName, coll)

            else:
                os.mkdir("./data/{}".format(dbName))

                def isCollectionThen_Else(dbName, collName):

                    if os.path.isfile("./data/{}/{}.json".format(dbName, collName)):
                        return collectionClass(dbName, collName + ".json")
                    else:

                        open("./data/{}/{}.json".format(dbName, collName),
                             "w").write('{ "docs": [] }')

                        return collectionClass(dbName, collName + ".json")

                self.collection = lambda coll: isCollectionThen_Else(
                    dbName, coll)
