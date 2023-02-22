SELECT Product.name AS product_name, Product.price, Category.name AS category_name FROM Product
LEFT JOIN Category ON Product.category_id=Category.id;
