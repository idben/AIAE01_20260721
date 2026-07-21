TRUNCATE products, users, categories RESTART IDENTITY;

INSERT INTO categories (name) VALUES
    ('3C 電子'),
    ('辦公家具'),
    ('文具用品');

INSERT INTO products (name, price, stock, category_id) VALUES
    ('藍牙耳機', 1290, 50, 1),
    ('機械鍵盤', 2490, 30, 1),
    ('無線滑鼠', 590, 120, 1),
    ('USB 集線器', 890, 200, 1),
    ('人體工學椅', 6800, 15, 2),
    ('升降桌', 9500, 8, 2),
    ('螢幕支架', 1580, 45, 2),
    ('原子筆', 25, 500, 3),
    ('筆記本', 89, 300, 3),
    ('螢光筆', 45, 150, 3);

INSERT INTO users (username, email) VALUES
    ('alice', 'alice@example.com'),
    ('bob', 'bob@example.com'),
    ('carol', 'carol@example.com');
