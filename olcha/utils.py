import json

# JSON data for 50 phone products
data = [
    {"title": "Samsung Galaxy S21", "description": "Yangi model, yuqori sifatli kamera", "price": 999.99, "quantity": 50, "discount": 10, "category": 1},
    {"title": "iPhone 13", "description": "Ajoyib iPhone, uzun batareya muddati", "price": 1099.99, "quantity": 30, "discount": 5, "category": 1},
    {"title": "Xiaomi Redmi Note 10", "description": "Kuchli texnik xususiyatlar va arzon narx", "price": 299.99, "quantity": 100, "discount": 0, "category": 1},
    {"title": "OnePlus 9 Pro", "description": "Tezkor zaryadlash va kuchli texnik xususiyatlar", "price": 999.99, "quantity": 20, "discount": 15, "category": 1},
    {"title": "Google Pixel 6", "description": "Yaxshi kamera va tezkor ishlash", "price": 799.99, "quantity": 25, "discount": 10, "category": 1},
    {"title": "Samsung Galaxy Note 20", "description": "Zo'r dizayn va kuchli texnik xususiyatlar", "price": 899.99, "quantity": 40, "discount": 8, "category": 1},
    {"title": "iPhone 12", "description": "Apple telefonlarining ajoyib modeli", "price": 849.99, "quantity": 60, "discount": 7, "category": 1},
    {"title": "Xiaomi Mi 11", "description": "Tezkor ishlash va ajoyib kamera", "price": 749.99, "quantity": 35, "discount": 5, "category": 1},
    {"title": "OnePlus 8T", "description": "Yuqori tezlikda ishlash va tezkor zaryadlash", "price": 699.99, "quantity": 45, "discount": 0, "category": 1},
    {"title": "Oppo Reno 5", "description": "Kuchli kamera va zamonaviy dizayn", "price": 499.99, "quantity": 50, "discount": 10, "category": 1},
    {"title": "Realme GT", "description": "Yuqori tezlikda ishlash va quvvatli batareya", "price": 599.99, "quantity": 55, "discount": 5, "category": 1},
    {"title": "Nokia 8.3", "description": "Oson ishlash va yaxshi kamera", "price": 499.99, "quantity": 70, "discount": 0, "category": 1},
    {"title": "Sony Xperia 1 II", "description": "Ajoyib ekran va kuchli kamera", "price": 1199.99, "quantity": 15, "discount": 12, "category": 1},
    {"title": "Huawei P40 Pro", "description": "Zamonaviy dizayn va kuchli ishlash", "price": 899.99, "quantity": 40, "discount": 10, "category": 1},
    {"title": "LG Velvet", "description": "Yuqori sifatli ekran va dizayn", "price": 649.99, "quantity": 60, "discount": 8, "category": 1},
    {"title": "Asus ROG Phone 5", "description": "Gaming telefon, kuchli protsessor", "price": 999.99, "quantity": 25, "discount": 15, "category": 1},
    {"title": "Xiaomi Poco X3 Pro", "description": "Tezkor ishlash va yaxshi narx", "price": 349.99, "quantity": 80, "discount": 0, "category": 1},
    {"title": "Samsung Galaxy Z Fold 3", "description": "Foldable ekran va kuchli texnik xususiyatlar", "price": 1799.99, "quantity": 10, "discount": 5, "category": 1},
    {"title": "iPhone SE (2020)", "description": "Kichik va kuchli iPhone", "price": 399.99, "quantity": 90, "discount": 10, "category": 1},
    {"title": "Xiaomi Mi 10T Pro", "description": "Yuqori tezlikda ishlash va quvvatli kamera", "price": 799.99, "quantity": 40, "discount": 8, "category": 1},
    {"title": "OnePlus Nord", "description": "O'rta narxdagi yuqori sifatli telefon", "price": 499.99, "quantity": 60, "discount": 12, "category": 1},
    {"title": "Samsung Galaxy A52", "description": "Zamonaviy dizayn va kuchli kamera", "price": 450.99, "quantity": 70, "discount": 5, "category": 1},
    {"title": "iPhone 11", "description": "Ajoyib kamera va batareya", "price": 649.99, "quantity": 50, "discount": 7, "category": 1},
    {"title": "Realme 8 Pro", "description": "Yuqori tezlik va kuchli kamera", "price": 299.99, "quantity": 100, "discount": 0, "category": 1},
    {"title": "Nokia 7.2", "description": "Yaxshi narx va uzoq batareya muddati", "price": 299.99, "quantity": 85, "discount": 5, "category": 1},
    {"title": "Oppo F19 Pro", "description": "Yuqori sifatli ekran va kamera", "price": 449.99, "quantity": 60, "discount": 10, "category": 1},
    {"title": "Motorola Edge Plus", "description": "Kuchli ekran va ajoyib dizayn", "price": 999.99, "quantity": 25, "discount": 8, "category": 1},
    {"title": "Vivo V21", "description": "Tezkor ishlash va ajoyib dizayn", "price": 399.99, "quantity": 90, "discount": 0, "category": 1},
    {"title": "Infinix Zero 8", "description": "Yuqori tezlik va kuchli kamera", "price": 299.99, "quantity": 70, "discount": 5, "category": 1},
    {"title": "Vivo X60 Pro", "description": "Kuchli kamera va tezkor ishlash", "price": 999.99, "quantity": 30, "discount": 12, "category": 1},
    {"title": "LG G8X ThinQ", "description": "Dubbli ekran va kuchli ishlash", "price": 749.99, "quantity": 40, "discount": 10, "category": 1},
    {"title": "Honor 30 Pro", "description": "Ajoyib kamera va kuchli protsessor", "price": 899.99, "quantity": 50, "discount": 0, "category": 1},
    {"title": "Asus Zenfone 8", "description": "Yuqori tezlikda ishlash va uzun batareya muddati", "price": 799.99, "quantity": 50, "discount": 8, "category": 1},
    {"title": "Huawei Mate 40 Pro", "description": "Yuqori darajadagi telefon", "price": 1099.99, "quantity": 20, "discount": 5, "category": 1},
    {"title": "Xiaomi Mi Mix 4", "description": "Zamonaviy dizayn va kuchli ekran", "price": 799.99, "quantity": 60, "discount": 7, "category": 1},
    {"title": "Oppo Find X3 Pro", "description": "Tezkor ishlash va yuqori sifatli ekran", "price": 1099.99, "quantity": 30, "discount": 12, "category": 1},
    {"title": "iPhone 6S", "description": "Kichik va arzon iPhone", "price": 349.99, "quantity": 100, "discount": 0, "category": 1},
    {"title": "Samsung Galaxy A32", "description": "Yuqori sifatli kamera va uzoq batareya muddati", "price": 399.99, "quantity": 50, "discount": 5, "category": 1},
    {"title": "Google Pixel 5", "description": "Yuqori kamera va yaxshi ishlash", "price": 699.99, "quantity": 40, "discount": 8, "category": 1},
    {"title": "Xiaomi Poco M3", "description": "Arzon narx va yaxshi kamera", "price": 149.99, "quantity": 100, "discount": 0, "category": 1},
    {"title": "Huawei Y7a", "description": "Zo'r dizayn va quvvatli batareya", "price": 199.99, "quantity": 90, "discount": 5, "category": 1},
    {"title": "Samsung Galaxy M32", "description": "Yuqori darajadagi ekran va texnik xususiyatlar", "price": 249.99, "quantity": 80, "discount": 10, "category": 1},
    {"title": "Realme Narzo 30 Pro", "description": "Yuqori darajadagi ishlash va batareya", "price": 199.99, "quantity": 100, "discount": 0, "category": 1},
    {"title": "iPhone 8 Plus", "description": "Yuqori sifatli ekran va kamera", "price": 499.99, "quantity": 60, "discount": 7, "category": 1},
    {"title": "Motorola Moto G Power", "description": "Arzon narx va uzoq batareya muddati", "price": 149.99, "quantity": 90, "discount": 5, "category": 1},
    {"title": "Vivo V19", "description": "Tezkor ishlash va yuqori sifatli kamera", "price": 349.99, "quantity": 100, "discount": 8, "category": 1},
    {"title": "Oppo A74", "description": "Yuqori tezlikda ishlash va kuchli kamera", "price": 279.99, "quantity": 100, "discount": 5, "category": 1},
    {"title": "Xiaomi Redmi Note 9 Pro", "description": "Arzon narx va yaxshi ishlash", "price": 249.99, "quantity": 70, "discount": 10, "category": 1},
    {"title": "OnePlus Nord 2", "description": "Zamonaviy dizayn va kuchli kamera", "price": 499.99, "quantity": 60, "discount": 0, "category": 1}
]

# Save the data to a JSON file


with open('data.json', "w") as file:
    json.dump(data, file, indent=4)

