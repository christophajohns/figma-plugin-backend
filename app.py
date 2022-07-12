"""Flask application for the link prediction project."""

from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
from link_prediction.utils.classes import Design
from link_prediction.models import TextSimilarityNeighborsClassifier
from utils import get_data_points

# Set up the Flask application
app = Flask(__name__)
CORS(app)

# Load the link prediction model
clf: TextSimilarityNeighborsClassifier = joblib.load(
    "models/TextSimilarityNeighborsClassifier.joblib"
)

# Define the route for the default URL, which returns the version number
@app.route("/")
def index():
    """Returns the version number."""
    return "'Suggested Links' Backend v0.1.0"


# Define the route for the /links endpoint, which returns the predicted links (incl. their scores)
@app.route("/links", methods=["POST"])
def predict():
    """Returns the predicted links."""
    # Get the input data (i.e., view hierarchies) from the request
    data = request.get_json()
    # Parse the view hierarchies into a Design object
    print("Constructing Design object...")
    design = Design.from_dict(data)
    # Create a list of DataPoint objects from the view hierarchies
    print("Constructing DataPoint objects...")
    data_points = get_data_points(design)
    # Make the predictions
    print("Generating predictions...")
    predictions = clf.predict(data_points)
    print("Generating scores...")
    scores = clf.decision_function(data_points)
    # Construct list of predictions
    predicted_links = [
        {
            "sourceId": data_point.source.id,
            "targetId": data_point.target_id,
            "score": score,
        }
        for data_point, prediction, score in zip(data_points, predictions, scores)
        if prediction == 1
    ]
    # Return the predictions
    print("Returning results...")
    return jsonify(links=predicted_links)
