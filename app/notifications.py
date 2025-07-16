def notify_suppliers(notifications):
    # This function simulates sending notifications to suppliers
    for note in notifications:
        product = note.get("product")
        stock = note.get("stock")
        message = f"Stock Alert: '{product}' stock is low ({stock} left). Please restock immediately."

        # Simulate email or in-app notification
        print(f"📬 Notification to suppliers: {message}")

    return True
