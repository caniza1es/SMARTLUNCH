CREATE TABLE Usuario (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50),
    usuario VARCHAR(50) UNIQUE,
    contrasena TEXT,
    email VARCHAR(60)UNIQUE
);
