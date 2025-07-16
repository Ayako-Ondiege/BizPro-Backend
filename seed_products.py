# seed_products.py

import random
from faker import Faker
from app import create_app
from app.extensions import db
from app.models.product import Product

fake = Faker()
app = create_app()

# Top 60+ construction materials (looped to reach 200)
construction_products = [
    "Cement 50kg", "Iron Rod 12mm", "Steel Mesh", "PVC Pipe 3m", "River Sand (Ton)",
    "Ballast (Ton)", "Hardcore (Ton)", "Binding Wire", "Roofing Nails", "BRC Mesh",
    "Timber 2x4", "Timber 2x6", "Flush Door", "Door Frame", "Window Frame",
    "Wall Tiles 30x60", "Floor Tiles 60x60", "Tile Adhesive", "Wall Screed",
    "Emulsion Paint (5L)", "Gloss Paint (5L)", "Undercoat", "Primer (1L)",
    "Paint Roller", "Brush Set", "Roof Sheets", "Reinforcement Bars", "Sika Waterproof",
    "Welding Rods", "Concrete Blocks", "Hollow Blocks", "Paving Blocks",
    "Manhole Cover", "Grout", "Waterproof Membrane", "Chisel", "Trowel",
    "Spirit Level", "Plumb Line", "Shovel", "Hammer", "Hand Saw", "Wheelbarrow",
    "Electric Drill", "Angle Grinder", "Generator 3kVA", "Concrete Mixer",
    "Scaffolding Pipe", "Scaffolding Coupler", "Safety Boots", "Safety Helmet",
    "Reflective Jacket", "Gloves", "Dust Mask", "Goggles", "Toolbox Set",
    "Electric Cable", "Extension Cable", "Fuse Box", "Switch Socket", "LED Floodlight",
    "Water Tank 1000L", "Toilet Set", "Basin Tap", "Sink Mixer", "PVC Elbow", "PVC Tee"
]

def seed_products(n=200):
    with app.app_context():
        products_seeded = 0
        while products_seeded < n:
            name = random.choice(construction_products)
            price = round(random.uniform(100, 10000), 2)
            stock = random.randint(20, 500)
            description = fake.sentence(nb_words=10)

            # Add variation to avoid duplicates
            variant = f" ({fake.word().capitalize()})" if random.random() < 0.3 else ""
            unique_name = name + variant

            # Check if name already exists
            existing = Product.query.filter_by(name=unique_name).first()
            if existing:
                continue

            product = Product(
                name=unique_name,
                price=price,
                stock=stock,
                description=description
            )
            db.session.add(product)
            products_seeded += 1

        db.session.commit()
        print(f"{n} construction products seeded successfully.")

if __name__ == "__main__":
    seed_products()
