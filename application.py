from flask import Flask, request, jsonify
from workouts import Workout
import werkzeug

application= Flask(__name__)

@application.route("/")
def index():
    # This will return Hello World in an h1 tag when you go to localhost:5000
    return '<h1>Hello W orld</h1>'
@application.route('/biceps', methods=['GET', 'POST'])
def CountBiceps():
    # Post request
    if request.method == 'POST':
        videoFile = request.files['workoutVideo']  # Important key
        videoName = werkzeug.utils.secure_filename(videoFile.filename)
        videoFile.save(videoName)
        workout = Workout()
        result = workout.workout_detection(number=1, video=videoName)
        return jsonify({
            "message": str(result)
        })
    return jsonify({
        "message": "Hello biceps"
    })


@application.route('/shoulders', methods=['GET', 'POST'])
def CountShoulders():
    # Post request
    if request.method == 'POST':
        videoFile = request.files['workoutVideo']  # Important key
        videoName = werkzeug.utils.secure_filename(videoFile.filename)
        videoFile.save(videoName)
        workout = Workout()
        result = workout.workout_detection(number=2, video=videoName)
        return jsonify({
            "message": str(result)
        })
    return jsonify({
        "message": "Hello shoulders"
    })


@application.route('/squats', methods=['GET', 'POST'])
def CountSquats():
    # Post request
    if request.method == 'POST':
        videoFile = request.files['workoutVideo']  # Important key
        videoName = werkzeug.utils.secure_filename(videoFile.filename)
        videoFile.save(videoName)
        workout = Workout()
        result = workout.workout_detection(number=3, video=videoName)
        return jsonify({
            "message": str(result)
        })
    return jsonify({
        "message": "Hello squats"
    })


if __name__ == "__main__":
    application.run()
