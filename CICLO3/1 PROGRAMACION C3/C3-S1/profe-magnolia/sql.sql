



CREATE TABLE Alumnos
(
    IdAlumno
    Nombres varchar not null (45),
    Apellidos varchar not null (45),
    Edad int not null,
    Direccion_Residencia varchar (50)
);

CREATE TABLE Materias
(
    idMaterias int primary not null,
    Nombre varchar not null (45),
    profesor varchar not null (60),
    grado varchar (10),
    IdAlumno int,
);