import requests
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

headers = {"x-api-key": os.getenv("REQRES_API_KEY")}

# --- Connect to MySQL ---
conn = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)
cursor = conn.cursor()

# --- Handle Pagination ---
page = 1
total_inserted = 0

while True:
    response = requests.get(
        f"https://reqres.in/api/users?page={page}",
        headers=headers
    )
    data = response.json()
    users = data["data"]
    total_pages = data["total_pages"]

    for user in users:
        cursor.execute("""
            INSERT INTO users (id, email, first_name, last_name, avatar)
            VALUES (%s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
                email=VALUES(email),
                first_name=VALUES(first_name),
                last_name=VALUES(last_name),
                avatar=VALUES(avatar)
        """, (user["id"], user["email"], user["first_name"], user["last_name"], user["avatar"]))
        total_inserted += 1

    print(f"✅ Page {page}/{total_pages} inserted ({len(users)} users)")

    if page >= total_pages:
        break
    page += 1

conn.commit()
cursor.close()
conn.close()

print(f"\n🎉 Done! Total {total_inserted} users inserted into MySQL.")