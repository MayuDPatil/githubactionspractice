#!/usr/bin/env python3
"""
Flask Web Application
A simple web app for GitHub Actions practice.
"""

from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder=".", static_folder="static")


def greet(name: str) -> str:
    """Return a greeting message."""
    return f"Hello, {name}!"


def calculate_sum(numbers: list[int]) -> int:
    """Calculate the sum of numbers."""
    return sum(numbers)


@app.route("/")
def home():
    """Render the home page."""
    return render_template("index.html")


@app.route("/api/greet", methods=["POST"])
def api_greet():
    """API endpoint to greet."""
    data = request.json
    name = data.get("name", "World")
    return jsonify({"message": greet(name)})


@app.route("/api/sum", methods=["POST"])
def api_sum():
    """API endpoint to calculate sum."""
    data = request.json
    numbers = data.get("numbers", [])
    result = calculate_sum(numbers)
    return jsonify({"result": result, "numbers": numbers})


if __name__ == "__main__":
    app.run(port=5000)
