from flask import Flask, request, jsonify
import pymongo
import os
from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__)

myclient = pymongo.MongoClient(os.getenv("MONGO_DB_URI"))
mydb = myclient["lalle"]
mycol = mydb["books"]


@app.route("/")
def hello():
    return "Hello Kams!"


@app.route("/books")
def get_book():
    books = []
    for values in mycol.find():
        values["_id"] = str(values["_id"])
        books.append(values)
    return jsonify(lalle=books)


@app.route("/books/insert", methods=["POST"])
def insert_book():
    if request.method == "POST":
        lalle = request.json
        book_name = lalle["name"]
        book_category = lalle["category"]
        book_read = lalle["read"]
        book_to_insert = {
            "name": book_name,
            "category": book_category,
            "read": book_read,
        }
        x = mycol.insert_one(book_to_insert)
        return "Successfully added -> {}".format(
            book_to_insert,
        )


if __name__ == "__main__":
    app.run(debug=True)
