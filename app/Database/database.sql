CREATE TABLE Usuario (
    id SERIAL,
    nombre VARCHAR(50) ,
    usuario VARCHAR(50) UNIQUE,
    contraseña VARCHAR(15),
    email VARCHAR(30) UNIQUE
);
