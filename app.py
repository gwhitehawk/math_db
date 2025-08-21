from flask import Flask, jsonify, g, render_template
import sqlite3

app = Flask(__name__)
DATABASE = 'math_problems.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/list', methods=['GET'])
def list_problems():
    cur = get_db().cursor()
    cur.execute('SELECT id, title FROM problems')
    problems = [{'id': row[0], 'title': row[1]} for row in cur.fetchall()]
    # If client accepts HTML, render template
    if 'text/html' in (g.get('accept', '') or ''):
        return render_template('list.html', problems=problems)
    return jsonify(problems)

@app.route('/problems/<int:problem_id>', methods=['GET'])
def get_problem(problem_id):
    cur = get_db().cursor()
    cur.execute('SELECT id, title, statement FROM problems WHERE id = ?', (problem_id,))
    row = cur.fetchone()
    if row:
        problem = {'id': row[0], 'title': row[1], 'statement': row[2]}
        # If client accepts HTML, render template
        if 'text/html' in (g.get('accept', '') or ''):
            return render_template('problem.html', problem=problem)
        return jsonify(problem)
    else:
        return jsonify({'error': 'Problem not found'}), 404

@app.before_request
def detect_accept_header():
    g.accept = (getattr(g, 'accept', None) or 
                (getattr(getattr(g, 'request', None), 'headers', {}).get('Accept', '') if hasattr(g, 'request') else ''))
    # Fallback for Flask request
    try:
        from flask import request
        g.accept = request.headers.get('Accept', '')
    except Exception:
        pass

if __name__ == '__main__':
    app.run(debug=True)
