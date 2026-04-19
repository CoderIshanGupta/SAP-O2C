def check_stock(material, qty):
    stock_db = {
        "LED-TV-1000": 500
    }

    if stock_db.get(material, 0) >= qty:
        return True
    return False