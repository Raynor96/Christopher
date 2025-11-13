-- Creación de la tabla base 'Mascota'
CREATE TABLE Mascota (
    id_mascota INT PRIMARY KEY,         
    edad INT,
    especie VARCHAR(255),
    historialMedico VARCHAR(255)
);

-- Creación de la tabla 'Perro' 
CREATE TABLE Perro (
    id_mascota INT PRIMARY KEY,          
    historialVacunas VARCHAR(255),
    FOREIGN KEY (id_mascota) REFERENCES Mascota(id_mascota)
);

-- Creación de la tabla 'Ave' como subclase de 'Mascota'
CREATE TABLE Ave (
    id_mascota INT PRIMARY KEY,          
    tipoJaula VARCHAR(255),
    controlVuelo BOOLEAN,
    FOREIGN KEY (id_mascota) REFERENCES Mascota(id_mascota)
);

-- Creación de la tabla 'Gato' 
CREATE TABLE Gato (
    id_mascota INT PRIMARY KEY,         
    esterilizado BOOLEAN,
    FOREIGN KEY (id_mascota) REFERENCES Mascota(id_mascota)
);


