from flask import jsonify


def get_user():
    return jsonify({'message': 'get user success'})


def add_user():
    return jsonify({'message': 'add user success'})


def edit_user():
    return jsonify({'message': 'edit user success'})


def delete_user():
    return jsonify({'message': 'delete user success'})
