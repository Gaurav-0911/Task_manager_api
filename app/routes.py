from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from .models import Task
from .extensions import db

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return "Task Management API Running 🚀"

# CREATE TASK
@main.route("/tasks", methods=["POST"])
@jwt_required()
def create_task():
    user_id = int(get_jwt_identity())   # ✅ FIX

    data = request.json

    task = Task(
        title=data["title"],
        description=data["description"],
        created_by=user_id,
        assigned_to=int(data.get("assigned_to", user_id))  # ✅ FIX
    )

    db.session.add(task)
    db.session.commit()

    return jsonify({"msg": "Task created"}), 201


# GET TASKS (Pagination + Filtering)
@main.route("/tasks", methods=["GET"])
@jwt_required()
def get_tasks():
    user_id = int(get_jwt_identity())   # ✅ FIX

    page = int(request.args.get("page", 1))
    status = request.args.get("status")

    query = Task.query.filter_by(assigned_to=user_id)

    if status:
        query = query.filter_by(status=status)

    tasks = query.paginate(page=page, per_page=5)

    return jsonify([
        {
            "id": t.id,
            "title": t.title,
            "status": t.status
        } for t in tasks.items
    ])


# UPDATE TASK
@main.route("/tasks/<int:id>", methods=["PUT"])
@jwt_required()
def update_task(id):
    user_id = int(get_jwt_identity())   # ✅ FIX

    task = Task.query.get_or_404(id)

    # ✅ Flexible access (better)
    if task.assigned_to != user_id and task.created_by != user_id:
        return jsonify({"msg": "Unauthorized"}), 403

    data = request.json
    task.status = data.get("status", task.status)

    db.session.commit()

    return jsonify({"msg": "Updated"})


# DELETE TASK
@main.route("/tasks/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_task(id):
    user_id = int(get_jwt_identity())   # ✅ FIX

    task = Task.query.get_or_404(id)

    if task.created_by != user_id:
        return jsonify({"msg": "Unauthorized"}), 403

    db.session.delete(task)
    db.session.commit()

    return jsonify({"msg": "Deleted"})