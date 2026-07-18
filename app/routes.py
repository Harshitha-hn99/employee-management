from flask import Blueprint, request, jsonify

from app.database import db
from app.models import Employee

# Create Blueprint
employee_bp = Blueprint("employee", __name__)


# ==========================
# CREATE Employee
# ==========================
@employee_bp.route("/employees", methods=["POST"])
def create_employee():

    data = request.get_json()

    employee = Employee(
        name=data["name"],
        email=data["email"],
        department=data["department"],
        salary=data["salary"]
    )

    db.session.add(employee)
    db.session.commit()

    return jsonify({
        "message": "Employee created successfully"
    }), 201


# ==========================
# READ All Employees
# ==========================
@employee_bp.route("/employees", methods=["GET"])
def get_employees():

    employees = Employee.query.all()

    result = []

    for emp in employees:
        result.append({
            "id": emp.id,
            "name": emp.name,
            "email": emp.email,
            "department": emp.department,
            "salary": emp.salary
        })

    return jsonify(result)


# ==========================
# READ One Employee
# ==========================
@employee_bp.route("/employees/<int:id>", methods=["GET"])
def get_employee(id):

    employee = Employee.query.get_or_404(id)

    return jsonify({
        "id": employee.id,
        "name": employee.name,
        "email": employee.email,
        "department": employee.department,
        "salary": employee.salary
    })


# ==========================
# UPDATE Employee
# ==========================
@employee_bp.route("/employees/<int:id>", methods=["PUT"])
def update_employee(id):

    employee = Employee.query.get_or_404(id)

    data = request.get_json()
    employee.name = data["name"]
    employee.email = data["email"]
    employee.department = data["department"]
    employee.salary = data["salary"]
    
    db.session.commit()

    return jsonify({
        "message": "Employee updated successfully"
    })


# ==========================
# DELETE Employee
# ==========================
@employee_bp.route("/employees/<int:id>", methods=["DELETE"])
def delete_employee(id):

    employee = Employee.query.get_or_404(id)

    db.session.delete(employee)
    db.session.commit()

    return jsonify({
        "message": "Employee deleted successfully"
    })
