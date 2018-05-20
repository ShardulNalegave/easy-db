
# EasyDB
Take it easy, **EasyDB** is here to help.


## What is EasyDB?
**EasyDB** is a experimental, **No-SQL** DataBase written in Python 3. Its main aim is to make it easy to use a DataBase.


## Features
As this project is experimental it has less features now. Some of them are:-

- Creating A Database
- Creating Collections
- Adding Documents To A Collection
- Getting Documents From A Collection
- Getting Documents From A Collection By A Given Query


## Usage
**EasyDB** is very easy to use. It has a very easy to understand syntax compared to others.

These are some things you can do using **EasyDB**:-

#### Creating A Database
EasyDB has a function called as `use` to use a DataBase if it exists already or to create and use a DataBase if it doesn't exist. The function takes one argument which is `dbName` ( Name of the Database ). The syntax for the function is:-

````python

    # Initialize EasyDB
    Easy = EasyDB()

    # Create A DataBase Named `Test`
    testDB = Easy.use("test")

````

#### Creating Collections
If you have used **MongoDB** first then you should already know what it is, but if you don't then, collection is a group of documents, a collection can contain infinite documents. In EasyDB you can create a collection if it doesn't exist or use an existing one with function `collection`. It takes one argument which is `collectionName` the name of the collection you want to use. The syntax is:-

````python

    testColl = testDB.collection("test")

````

#### Adding Documents To A Collection
As described before collections contain documents and in EasyDB you can just run one function to add an document to a collection. The function is `insert` and takes on argument `doc` which is the document. **Note:-** The argument passed should be of type `dict`. The syntac is:-

````python

    testColl.insert({
        "name": "Python",
        "type": "Programming Language",
        "desc": "General Purpose Programming Language"
    })

````

#### Getting Documents Back
Now as you have stored documents in a collection you can get it back with a function `get`. It takes no arguments. The data returned is in the form of a list so that you can iterate over it. The syntax for the function is:-

````python

    docs = testColl.get()
    print(docs)

    # Expected Output:-
    # [{
    #    "name": "Python",
    #    "type": "Programming Language",
    #    "desc": "General Purpose Programming Language"
    # }]
    #

````

#### Getting Documents Back By A Given Query
We can get documents back using the `get` function but it returns all the documents present. To get documents filtered by a given query we use the `doc` function. The `doc` function takes on argument `query`. The data returned back is in the form of list. The syntax is like:-

````python

    testColl.doc({
        "name": "Python"
    })

````


##### A Project By [Shardul Nalegave](https://shardul.netlify.com)
##### Licensed Under The [MIT License](./LICENSE)