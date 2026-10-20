
import sqlite3
from pathlib import Path

from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = "change-this-development-key"

BASE_DIR = Path(__file__).resolve().parent
DATABASE = BASE_DIR / "products.db"


def get_db_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():
    with get_db_connection() as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT NOT NULL,
                price REAL NOT NULL CHECK (price >= 0),
                category TEXT NOT NULL
            )
        """)


def read_form():
    name = request.form.get("name", "").strip()
    description = request.form.get("description", "").strip()
    category = request.form.get("category", "").strip()
    price_text = request.form.get("price", "").strip()

    if not name or not description or not category or not price_text:
        raise ValueError("Please fill in all fields.")

    try:
        price = float(price_text.replace(",", "."))
    except ValueError:
        raise ValueError("Enter a valid price.")

    if price < 0 or not 0 <= price < float("inf"):
        raise ValueError("Price must be a non-negative number.")

    return name, description, price, category


@app.route("/")
def home():
    with get_db_connection() as connection:
        products = connection.execute(
            "SELECT * FROM products ORDER BY id DESC"
        ).fetchall()

    return render_template("index.html", products=products, editing=None)


@app.route("/create", methods=["POST"])
def create_product():
    try:
        name, description, price, category = read_form()

        with get_db_connection() as connection:
            connection.execute(
                """
                INSERT INTO products (name, description, price, category)
                VALUES (?, ?, ?, ?)
                """,
                (name, description, price, category),
            )

        flash("Product added successfully.", "success")

    except ValueError as error:
        flash(str(error), "error")

    return redirect(url_for("home"))


@app.route("/edit/<int:product_id>", methods=["GET", "POST"])
def edit_product(product_id):
    with get_db_connection() as connection:
        product = connection.execute(
            "SELECT * FROM products WHERE id = ?",
            (product_id,),
        ).fetchone()

    if product is None:
        flash("Product not found.", "error")
        return redirect(url_for("home"))

    if request.method == "POST":
        try:
            name, description, price, category = read_form()

            with get_db_connection() as connection:
                connection.execute(
                    """
                    UPDATE products
                    SET name = ?, description = ?, price = ?, category = ?
                    WHERE id = ?
                    """,
                    (name, description, price, category, product_id),
                )

            flash("Product updated successfully.", "success")
            return redirect(url_for("home"))

        except ValueError as error:
            flash(str(error), "error")

    return render_template(
        "index.html",
        products=[],
        editing=product,
    )


@app.route("/delete/<int:product_id>", methods=["POST"])
def delete_product(product_id):
    with get_db_connection() as connection:
        result = connection.execute(
            "DELETE FROM products WHERE id = ?",
            (product_id,),
        )

    if result.rowcount:
        flash("Product deleted successfully.", "success")
    else:
        flash("Product not found.", "error")

    return redirect(url_for("home"))


initialize_database()


if __name__ == "__main__":
    app.run(debug=True)
