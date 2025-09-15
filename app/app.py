from flask import Flask, jsonify
import os, psycopg2

app = Flask(__name__)

def get_db_conn():
    return psycopg2.connect(
        host=os.environ.get("DB_HOST"),
        database=os.environ.get("DB_NAME"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASSWORD"),
        connect_timeout=3
    )

@app.route("/health")
def health():
    return jsonify(status="ok"), 200

@app.route("/")
def index():
    try:
        with get_db_conn() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT 'PI-Credit running on EKS' as msg;")
                row = cur.fetchone()
        return jsonify(message=row[0]), 200
    except Exception as e:
        return jsonify(error=str(e)), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "8080")))
