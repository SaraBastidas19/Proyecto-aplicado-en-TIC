create schema core;

-- DISEÑO BASE DE DATOS

-- Tabla: Rol
create table core.rol
(
    rol_id              serial not null constraint rol_pk primary key,
    nombre		    	varchar(100) not null,
    descripcion			text not null
);

INSERT INTO core.rol (rol_id, nombre, descripcion)
VALUES (1, 'docente', 'dictan el curso');

INSERT INTO core.rol (rol_id, nombre, descripcion)
VALUES (2, 'estudiante', 'toman las clases');

INSERT INTO core.rol (rol_id, nombre, descripcion)
VALUES (3, 'administrativo', 'administran la información');


-- Tabla: Usuarios
create table core.usuarios
(
    usuario_id          serial not null constraint usuarios_pk primary key,
    nombre		    	varchar(100) not null,
    email				varchar(100) not null,
    contrasena			varchar(100),
    tipo_documento		varchar(50) not null,
    numero_documento	int not null,
    fecha_nacimiento	date not null,
    rol_id				int not null,
    
    foreign key (rol_id) references core.rol(rol_id)
);

-- ALTER TABLE core.usuarios
-- ADD CONSTRAINT unique_nombre UNIQUE (nombre);
INSERT INTO core.usuarios (nombre, email, tipo_documento, numero_documento, fecha_nacimiento, contrasena, rol_id)
values ('Lana Solarte', 'lsolarte@inder.com', 'Cédula de Ciudadanía (CC)', '1424542325', '1990-02-03', '$2b$12$qD54g17fHBKjHyQ9btLRvemPxLAO7WmIBq5IgqSgj9rUcXdtayEdy', 1),
	   ('Antonio Aguirre', 'aaguirre@inder.com', 'Cédula de Ciudadanía (CC)', '1342542335', '1989-05-25', '$2b$12$WpMebhCspTiK.42HbfLj2.Jd4eA85j34MoFuXDwhHBazxeSGbsNCq', 1),
	   ('Brandon Delgado', 'bdelgado@inder.com','Cédula de Ciudadanía (CC)', '1525622342', '1991-03-04', '$2b$12$iu8UTOqQqFyxUjTDOKqlauGk753ObQfvjmeNBpbsNeA1IajEV9Woi', 1);

-- Tabla: Docentes
create table core.docentes
(
    docente_id          serial not null constraint docentes_pk primary key,
    nombre		    	varchar(100) not null,
    tipo_documento		varchar(50) not null,
    numero_documento	int not null,
    especialidad		varchar(200) not null,
    usuario_id			int not null unique,
    
    
    foreign key (usuario_id) references core.usuarios(usuario_id)
);
INSERT INTO core.docentes (nombre, tipo_documento, numero_documento, especialidad, usuario_id)
values ('Lana Solarte', 'Cédula de Ciudadanía (CC)', '1424542325', 'Natación', (select usuario_id from core.usuarios where email = 'lsolarte@inder.com')),
	   ('Antonio Aguirre', 'Cédula de Ciudadanía (CC)', '1342542335', 'Baloncesto', (select usuario_id from core.usuarios where email = 'aaguirre@inder.com')),
	   ('Brandon Delgado', 'Cédula de Ciudadanía (CC)', '1525622342', 'Fútbol', (select usuario_id from core.usuarios where email = 'bdelgado@inder.com'));
		
-- alter table core.docentes add column    numero_documento	int 

-- Tabla: Curso
create table core.cursos
(
    curso_id            serial not null constraint cursos_pk primary key,
    nombre		    	varchar(100) not null,
    descripcion			varchar(200) not null,
    horario				varchar(100) not null,
    docente_id			int not null,
    
    foreign key (docente_id) references core.docentes(docente_id) 
);

INSERT INTO core.cursos (nombre, descripcion, horario, docente_id)
VALUES ('Baloncesto', 'Curso de baloncesto', 'Martes-Jueves 5.00 pm - 7.00 pm', (select docente_id from core.docentes where numero_documento = '1342542335')),
		('Natación', 'Curso de natación', 'Lunes-Miércoles 5.00 pm - 7.00 pm', (select docente_id from core.docentes where numero_documento = '1424542325')),
		('Fútbol', 'Curso de fútbol', 'Lunes-Viernes 5.00 pm - 7.00 pm', (select docente_id from core.docentes where numero_documento = '1525622342'));



-- Tabla: Matrícula
create table core.matriculas
(
    matricula_id        serial not null constraint matriculas_pk primary key,
    usuario_id		    int not null,
    curso_id			int not null,
    fecha				date not null,
    
    foreign key (usuario_id) references core.usuarios(usuario_id),
    foreign key (curso_id) references core.cursos(curso_id)
);

-- Tabla: Asistencia
create table core.asistencias
(
    asistencia_id       serial not null constraint asistencias_pk primary key,
    usuario_id		    int not null,
    curso_id			int not null,
    fecha				date not null,
    
    foreign key (usuario_id) references core.usuarios(usuario_id),
    foreign key (curso_id) references core.cursos(curso_id)
);

-- Tabla: Calificaciones
create table core.calificaciones
(
    calificacion_id     serial not null constraint calificaciones_pk primary key,
    usuario_id		    int not null,
    curso_id			int not null,
    evaluacion			varchar(100) not null,
    porcentaje			decimal(5,2) not null,
    calificacion		decimal(5,2) not null,
    
    
    foreign key (usuario_id) references core.usuarios(usuario_id),
    foreign key (curso_id) references core.cursos(curso_id)
);
