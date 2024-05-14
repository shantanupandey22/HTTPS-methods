from flask import Flask,jsonify,request

app=Flask(__name__)

books = [
    {"id":1,"name":"book_1","author":"author_1"},
    {"id":2,"name":"book_2","author":"author_2"},
    {"id":3,"name":"book_3","author":"author_3"},
    {"id":4,"name":"book_4","author":"author_4"},
]

#This is our home page 
@app.route('/home',methods=['GET'])
def home_page():
    return "This is my home page"

#This page will show all books data.
@app.route('/home/books',methods=['GET'])
def all_books():
    return jsonify(books)

#It will show one book data.
@app.route('/home/books/<int:book_id>',methods=['GET'])
def book_data(book_id):
    for book in books:
        if book['id'] == book_id:
            return jsonify(book)
        return jsonify({'message':'Book not found'})
    
#Adding new data with post method.
@app.route('/home/books',methods = ['POST'])
def add_books():
    new_book = {
            'id' : request.json['id'],
            'name' : request.json['name'],
            'author' : request.json['author']
        }
    books.append(new_book)
    return jsonify({'messgae':'Book added successfully'})

#This will update and existing book data.
@app.route('/home/books/<int:book_id>',methods=['PUT'])
def update_book(book_id):
    for book in books:
        if book['id']== book_id :
            book['name'] = request.json['name']
            book['author'] = request.json['author']
            return jsonify({'message':'Book updated Successfully'})
        return jsonify({'message':'Book not found'})

#This will delete an existing book data.
@app.route('/home/books/<int:book_id>',methods=['DELETE'])
def delete_book(book_id):
    for book in books:
        if book['id']== book_id :
            books.remove(book)
            return jsonify({'message':'Book deleted Successfully'})
        return jsonify({'message':'Book not found'})

if __name__ == ('__main__'):
    app.run(debug=True,port=3000)