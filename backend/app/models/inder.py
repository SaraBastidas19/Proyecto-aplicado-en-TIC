from sqlalchemy import Column, String, Integer, Numeric, ForeignKey, DateTime, Float
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Rol(Base):
    __tablename__ = 'rol'
    __table_args__ = {'schema': 'core'}

    rol_id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(String(200), nullable=False)

class Usuario(Base):
    __tablename__ = 'usuarios'
    __table_args__ = {'schema': 'core'}

    usuario_id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    contrasena = Column(String(100), nullable=False)
    tipo_documento = Column(String(50), nullable=False)
    numero_documento = Column(Integer, nullable=False)
    fecha_nacimiento = Column(DateTime, nullable=False)
    rol_id = Column(Integer, ForeignKey('core.rol.rol_id'))
    rol = relationship(Rol, backref='usuario')
    def as_dict(self):
        result = {attr.key: getattr(self, attr.key) for attr in self.__mapper__.attrs}
        return {**result, 'rol': getattr(self.rol, 'nombre')}


class Docente(Base):
    __tablename__ = 'docentes'
    __table_args__ = {'schema': 'core'}

    docente_id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    tipo_documento = Column(String(50), nullable=False)
    numero_documento = Column(Integer, nullable=False)
    especialidad = Column(String(200), nullable=False)
    usuario_id = Column(Integer, ForeignKey('core.usuarios.usuario_id'))

class Curso(Base):
    __tablename__ = 'cursos'
    __table_args__ = {'schema': 'core'}

    curso_id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(String(200), nullable=False)
    horario = Column(DateTime, nullable=False)
    docente_id = Column(Integer, ForeignKey('core.docentes.docente_id'))

class Matricula(Base):
    __tablename__ = 'matriculas'
    __table_args__ = {'schema': 'core'}

    matricula_id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('core.usuarios.usuario_id'))
    curso_id = Column(Integer, ForeignKey('core.cursos.curso_id'))
    fecha = Column(DateTime, nullable=False)

class Asistencia(Base):
    __tablename__ = 'asistencias'
    __table_args__ = {'schema': 'core'}

    asistencia_id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('core.usuarios.usuario_id'))
    curso_id = Column(Integer, ForeignKey('core.cursos.curso_id'))
    fecha = Column(DateTime, nullable=False)    

class Calificacion(Base):
    __tablename__ = 'calificaciones'
    __table_args__ = {'schema': 'core'}

    calificacion_id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('core.usuarios.usuario_id'))
    curso_id = Column(Integer, ForeignKey('core.cursos.curso_id'))
    evaluacion = Column(String(100), nullable=False)
    porcentaje = Column(Float, nullable=False)
    calificacion = Column(Float, nullable=False)