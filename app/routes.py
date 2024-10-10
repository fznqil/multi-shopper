from app import app
from flask import render_template, request

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('query')

    if not query:
        return "No query provided", 400
    # Logic for search
    #return render_template('search.html', query=query)
    return f"Search results for: {query}"