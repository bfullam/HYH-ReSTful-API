from flask import Flask, jsonify, request #import objects from the flask model
app = Flask(_name_) #define app using flask

@app.route('/', methods=['GET'])
def test():
    return jsonify({'message' : 'It works!'})

if _name_ == '_main_':
    app.run(debug=True, port=8000) #run app on port 8000 in debug mode
