from flask_sqlalchemy import SQLAlchemy


DEFAULT_IMAGE = "https://tinyurl.com/demo-cupcake"

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)


class Cupcake(db.Model):
    """Cupcake Model."""

    __tablename__ = "cupcakes"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flavor = db.Column(db.Text, nullable=False)
    size = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image = db.Column(db.String, nullable=False, default=DEFAULT_IMAGE)

    def serialize(self):
        """Create JSON of single todo by serializing"""

        return {
            "id": self.id,
            "flavor": self.flavor,
            "size": self.size,
            "rating": self.rating,
            "image": self.image,
        }

    def __repr__(self):
        """Show info about cupcake."""

        c = self
        return f"<Cupcake {c.id}: Flavor: {c.flavor}, Size: {c.size}, Rating: {c.rating}, Image: {c.image}"