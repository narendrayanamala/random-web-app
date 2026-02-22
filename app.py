from flask import Flask, render_template_string, request
import random

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Random Number Generator</title>

    <!-- Bootstrap CDN -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">

    <style>
        body {
            background: linear-gradient(to right, #667eea, #764ba2);
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .card {
            border-radius: 20px;
            box-shadow: 0px 10px 30px rgba(0,0,0,0.3);
        }
        .result-box {
            font-size: 2rem;
            font-weight: bold;
        }
    </style>
</head>

<body>

<div class="card p-5 text-center" style="width: 400px;">
    <h2 class="mb-4">🎲 Random Number Generator</h2>

    <form method="POST">
        <div class="mb-3">
            <input type="number" name="start" value="{{ start }}" 
                   class="form-control" placeholder="Start Number" required>
        </div>

        <div class="mb-3">
            <input type="number" name="end" value="{{ end }}" 
                   class="form-control" placeholder="End Number" required>
        </div>

        <button type="submit" class="btn btn-primary w-100">
            Generate
        </button>
    </form>

    {% if error %}
        <div class="alert alert-danger mt-3">
            {{ error }}
        </div>
    {% endif %}

    {% if result is not none %}
        <div class="alert alert-success mt-4 result-box">
            Generated Number: {{ result }}
        </div>
    {% endif %}

</div>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    error = None
    start = ""
    end = ""

    if request.method == "POST":
        try:
            start = request.form["start"]
            end = request.form["end"]

            start_int = int(start)
            end_int = int(end)

            if start_int > end_int:
                error = "Start number must be less than End number"
            else:
                result = random.randint(start_int, end_int)

        except:
            error = "Invalid Input"

    return render_template_string(
        HTML,
        result=result,
        error=error,
        start=start,
        end=end
    )

if __name__ == "__main__":
    app.run(debug=True)