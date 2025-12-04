
CREATE TABLE Mascota (
    id_mascota       NUMBER PRIMARY KEY,
    nombre           VARCHAR2(100),
    edad             NUMBER,
    especie          VARCHAR2(50),
    historialMedico  VARCHAR2(500)
);


CREATE TABLE Perro (
    id_mascota       NUMBER PRIMARY KEY,
    historialVacunas VARCHAR2(500),
    
    CONSTRAINT fk_perro_mascota 
        FOREIGN KEY (id_mascota) 
        REFERENCES Mascota(id_mascota)
);


CREATE TABLE Gato (
    id_mascota   NUMBER PRIMARY KEY,
    esterilizado CHAR(1) CHECK (esterilizado IN ('S','N')),
    
    CONSTRAINT fk_gato_mascota 
        FOREIGN KEY (id_mascota) 
        REFERENCES Mascota(id_mascota)
);


CREATE TABLE Ave (
    id_mascota   NUMBER PRIMARY KEY,
    tipoJaula    VARCHAR2(100),
    controlVuelo CHAR(1) CHECK (controlVuelo IN ('S','N')),
    
    CONSTRAINT fk_ave_mascota 
        FOREIGN KEY (id_mascota) 
        REFERENCES Mascota(id_mascota)
);

