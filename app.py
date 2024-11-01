from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# In-memory storage for demonstration
students = []
next_id = 1

@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = next((s for s in students if s['id'] == student_id), None)
    if student is None:
        abort(404)
    return jsonify(student)

@app.route('/students', methods=['POST'])
def add_student():
    global next_id
    data = request.get_json()
    new_student = {
        'id': next_id,
        'name': data['name'],
        'grade': data['grade'],
        'email': data['email']
    }
    students.append(new_student)
    next_id += 1
    return jsonify(new_student), 201

@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    student = next((s for s in students if s['id'] == student_id), None)
    if student is None:
        abort(404)
    data = request.get_json()
    student['name'] = data.get('name', student['name'])
    student['grade'] = data.get('grade', student['grade'])
    student['email'] = data.get('email', student['email'])
    return jsonify(student)

@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    global students
    students = [s for s in students if s['id'] != student_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
