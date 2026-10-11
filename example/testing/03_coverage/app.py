def calculate_discount(price, discount):
    if price < 0:
        raise ValueError("Ціна не може бути від'ємною")
    if discount < 0 or discount > 100:
        raise ValueError("Знижка має бути від 0 до 100")
    return price * (1 - discount / 100)


def classify_number(number):
    if number > 0:
        return "positive"
    elif number < 0:
        return "negative"
    return "zero"