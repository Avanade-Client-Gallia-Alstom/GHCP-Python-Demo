from flask import Flask, jsonify, request

#create a list of 5 sample books with title and author
books = [
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    {"title": "A Tale of Two Cities", "author": "Charles Dickens"},
    {"title" :  "The Catcher in the Rye", "author": "J.D. Salinger"},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee"},
    {"title": "1984", "author": "George Orwell"}
]

app = Flask(__name__)

# Create
@app.route('/books', methods=['POST'])
def create_book():
    new_book = request.get_json()
    books.append(new_book)
    return jsonify(new_book), 201

# Read
@app.route('/books', methods=['GET'])
def get_all_books():
    return jsonify(books)

@app.route('/books/<int:index>', methods=['GET'])
def get_book(index):
    if index < len(books):
        return jsonify(books[index])
    else:
        return jsonify({'error': 'Book not found'}), 404

# Update
@app.route('/books/<int:index>', methods=['PUT'])
def update_book(index):
    if index < len(books):
        updated_book = request.get_json()
        books[index] = updated_book
        return jsonify(updated_book)
    else:
        return jsonify({'error': 'Book not found'}), 404

# Delete
@app.route('/books/<int:index>', methods=['DELETE'])
def delete_book(index):
    try:
        if index < len(books):
            deleted_book = books.pop(index)
            return jsonify(deleted_book)
        else:
            return jsonify({'error': 'Book not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run()

