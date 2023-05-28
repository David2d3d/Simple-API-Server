# Cats API

This is a simple Cats API built using Flask, a Python web framework. The API allows you to perform basic CRUD operations (Create, Read, Update, Delete) on a collection of cat objects.

## Getting Started

To get started with the Cats API, follow the instructions below.

### Prerequisites

Make sure you have the following installed:

- Python (version 3.7 or higher)
- Flask (version 2.0.0 or higher)

### Installation

1. Clone the repository or download the source code.
2. Open a terminal and navigate to the project directory.
3. Install the required dependencies by running the following command:
   ```
   pip install -r requirements.txt
   ```

### Usage

1. Run the API by executing the following command:
   ```
   python app.py
   ```
2. Once the API is running, you can send HTTP requests to interact with the cats collection.

## Endpoints

The Cats API exposes the following endpoints:

### GET /cats

Retrieve a list of all cats.

#### Example Request

```
GET /cats
```

#### Example Response

```json
[
  {
    "id": 0,
    "name": "Daisy",
    "race": "Siamese",
    "age": 4
  },
  {
    "id": 1,
    "name": "Bailey",
    "race": "Siamese",
    "age": 2
  },
  {
    "id": 2,
    "name": "Babie",
    "race": "British Shorthair",
    "age": 3
  }
]
```

### GET /cats/{id}

Retrieve a cat by its ID.

#### Example Request

```
GET /cats/1
```

#### Example Response

```json
{
  "id": 1,
  "name": "Bailey",
  "race": "Siamese",
  "age": 2
}
```

### POST /cats

Add a new cat to the collection.

#### Example Request

```
POST /cats

Body:
{
  "id": 3,
  "name": "Charlie",
  "race": "Persian",
  "age": 5
}
```

#### Example Response

```
Cat added
```

### DELETE /cats

Delete the entire cats collection.

#### Example Request

```
DELETE /cats
```

#### Example Response

```
List deleted
```

### DELETE /cats/{id}

Delete a cat by its ID.

#### Example Request

```
DELETE /cats/2
```

#### Example Response

```
Cat was successfully removed
```

### PUT /cats/{id}

Update a cat by its ID.

#### Example Request

```
PUT /cats/0

Body:
{
  "id": 0,
  "name": "Daisy",
  "race": "Siamese",
  "age": 5
}
```

#### Example Response

```
Cat updated
```

## Conclusion

The Cats API provides a simple interface to manage a collection of cats. Feel free to explore the endpoints and use them in your applications or projects.