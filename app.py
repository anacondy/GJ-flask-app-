# app.py
# --- This is the complete and final version. Just copy and paste all of it. ---

from flask import Flask, render_template
import sqlite3
import os # We need this to find the file path.

# --- This is the "find things" part ---
# It gets the exact "street address" of your project folder.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# It then creates the full, exact path to your database file.
DB_PATH = os.path.join(BASE_DIR, 'jobs.db')

app = Flask(__name__)

# This function now connects to the database using its full, exact address.
# This prevents PyCharm from getting lost.
def get_db_connection():
    conn = sqlite3.connect(DB_PATH) # Use the full path here.
    conn.row_factory = sqlite3.Row
    return conn

# --- The rest of the code is the same, but it will now work correctly. ---

# This handles the main page.
@app.route('/')
def index():
    conn = get_db_connection()
    jobs = conn.execute('SELECT * FROM jobs').fetchall()
    conn.close()
    return render_template('index.html', jobs=jobs)

# This handles the details page.
@app.route('/details/<int:job_id>')
def details(job_id):
    conn = get_db_connection()
    job = conn.execute('SELECT * FROM jobs WHERE id = ?', (job_id,)).fetchone()
    job_details = conn.execute('SELECT * FROM job_details WHERE job_id = ?', (job_id,)).fetchall()
    job_cutoffs = conn.execute('SELECT * FROM job_cutoffs WHERE job_id = ? ORDER BY category', (job_id,)).fetchall()
    conn.close()
    return render_template('details.html', job=job, details=job_details, cutoffs=job_cutoffs)

# This line starts the server.
if __name__ == '__main__':
    app.run(debug=True)
