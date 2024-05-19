from pydantic import BaseModel
from typing import Union
from datetime import datetime, date


class CursosResponseModel(BaseModel):
    curso_id:              int
    nombre:                str
    descripcion:           str
    horario:               str
    docente_id:            int

class DocenteResponseModel(BaseModel):
    docente_id:            int
    nombre:                str
    especialidad:          str

class UsuarioResponseModel(BaseModel):
    usuario_id:         int
    nombre:             str
    email:              str
    tipo_documento:     str
    numero_documento:   int
    fecha_nacimiento:   date
    rol_id:             int

class RolesResponseModel(BaseModel):
    rol_id:             Union[int, None]
    nombre:             str
    descripcion:        str

