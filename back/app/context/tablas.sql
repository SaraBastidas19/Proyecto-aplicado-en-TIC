-- Crear esquema CORE
-- Creamos un esquema para almacenar todo el modelo de datos del dominio
create schema core;

-- crear el usuario con el que se implementará la creación del modelo
create user inde_app with encrypted password 'inde_app';

-- DISEÑO BASE DE DATOS

-- Tabla: Rol
create table core.rol
(
    rol_id              int not null constraint rol_pk primary key,
    nombre		    	varchar(100) not null,
    descripcion			text not null
);

INSERT INTO core.rol (rol_id, nombre, descripcion)
VALUES (3, 'administrativo', 'administran la información');


-- Tabla: Usuarios
create table core.usuarios
(
    usuario_id          int not null constraint usuarios_pk primary key,
    nombre		    	varchar(100) not null,
    email				varchar(100) not null,
    contraseña			varchar(100),
    tipo_documento		varchar(50) not null,
    numero_documento	int not null,
    fecha_nacimiento	date not null,
    rol_id				int not null,
    
    foreign key (rol_id) references core.rol(rol_id)
);

-- ALTER TABLE core.usuarios
-- ADD CONSTRAINT unique_nombre UNIQUE (nombre);


-- Tabla: Docentes
create table core.docentes
(
    docente_id          int not null constraint docentes_pk primary key,
    nombre		    	varchar(100) not null,
    especialidad		varchar(200) not null,
    
    foreign key (nombre) references core.usuarios(nombre)
);


-- Tabla: Curso
create table core.cursos
(
    curso_id            int not null constraint cursos_pk primary key,
    nombre		    	varchar(100) not null,
    descripcion			varchar(200) not null,
    horario				varchar(100) not null,
    docente_id			int not null,
    
    foreign key (docente_id) references core.docentes(docente_id) 
);


-- Tabla: Matrícula
create table core.matriculas
(
    matricula_id        int not null constraint matriculas_pk primary key,
    usuario_id		    int not null,
    curso_id			int not null,
    fecha				date not null,
    
    foreign key (usuario_id) references core.usuarios(usuario_id),
    foreign key (curso_id) references core.cursos(curso_id)
);

-- Tabla: Asistencia
create table core.asistencias
(
    asistencia_id       int not null constraint asistencias_pk primary key,
    usuario_id		    int not null,
    curso_id			int not null,
    fecha				date not null,
    
    foreign key (usuario_id) references core.usuarios(usuario_id),
    foreign key (curso_id) references core.cursos(curso_id)
);

-- Tabla: Calificaciones
create table core.calificaciones
(
    calificacion_id     int not null constraint calificaciones_pk primary key,
    usuario_id		    int not null,
    curso_id			int not null,
    evaluacion			varchar(100) not null,
    porcentaje			decimal(5,2) not null,
    calificacion		decimal(5,2) not null,
    
    
    foreign key (usuario_id) references core.usuarios(usuario_id),
    foreign key (curso_id) references core.cursos(curso_id)
);
