# Datastore Setup

## Choice: MongoDB

MongoDB is a flexible, schema-less NoSQL database ideal for structured but evolving data. I also happenend to
have a MongoDB quiz around the same time I got this assignment. Two birds one stone. Using Python client (`pymongo`) 
for quick setup and querying.

## Why MongoDB?
- Simple to set up locally or in Docker
- No need to define rigid schemas
- Works well with Python

I hold an opinion that document based models are superior to schema based ones. I know this is a strong opinion but 
I know I shall hold it loosely. *wink wink 


## Setup

We use a Docker container for MongoDB and connect using Python with `pymongo`.

To start MongoDB, run:

```bash
docker-compose up -d
```

The `datastore_setup.py` file ensures the `linq_data` collection exists.
