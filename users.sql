DROP DATABASE IF EXISTS blogly;

CREATE DATABASE blogly;

\c blogly

CREATE TABLE users(
  user_id SERIAL PRIMARY KEY,
  first_name TEXT,
  last_name TEXT,
  image_url TEXT
);

INSERT INTO users (first_name, last_name, image_url)
VALUES 
('Layla', 'Peace', 'https://images.unsplash.com/photo-1658110260429-12a9865c9ee5?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwzNHx8fGVufDB8fHx8&auto=format&fit=crop&w=400&q=60'),
('Joe', 'Green', 'https://images.unsplash.com/photo-1568602471122-7832951cc4c5?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8bWFufGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=400&q=60'),
('Alan', 'Alden', 'https://images.unsplash.com/photo-1581803118522-7b72a50f7e9f?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTF8fG1hbnxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=400&q=60'),
('Jane', 'Smith', 'https://images.unsplash.com/photo-1514315384763-ba401779410f?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8Z2lybHxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=400&q=60'),
('Emery', 'Sun', 'https://images.unsplash.com/photo-1469334031218-e382a71b716b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MjB8fGdpcmx8ZW58MHx8MHx8&auto=format&fit=crop&w=400&q=60')
;



