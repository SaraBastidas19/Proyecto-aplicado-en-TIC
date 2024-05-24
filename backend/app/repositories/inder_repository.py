from backend.app.context.db_connection import Session
from backend.app.models.inder import Rol, Usuario, Docente, Curso, Matricula, Asistencia, Calificacion
from datetime import date

class InderRelationalRepository:

    def __init__(self):
        self.session = Session().session

    # 1. Obtener todos los roles existente
    def get_all_roles(self):
        results = self.session.query(Rol).all()
        response = []
        for result in results:
            response.append(self.model_as_dict(result))
        return response

    # 1. Obtener todos los cursos disponibles
    def get_all_cursos(self):
        results = self.session.query(Curso).all()
        response = []
        for result in results:
            response.append(self.model_as_dict(result))
        return response
    
    # 2. Crear un nuevo curso
    def create_curso(self, curso: dict):
        curso_item = {
            'curso_id': curso['curso_id'],
            'nombre': curso['nombre'],
            'descripcion': curso['descripcion'],
            'horario': curso['horario'],
            'docente_id': curso['docente_id']
        }
        curso_object = Curso(**curso_item)
        self.session.add(curso_object)
        self.session.commit()
        return {'message': 'El curso ha sido creado con éxito'}
        
    # 3. Actualizar un curso existente
    def update_curso(self, curso: dict, curso_id: int):
        curso_item = {
            'curso_id': curso['curso_id'],
            'nombre': curso['nombre'],
            'descripcion': curso['descripcion'],
            'horario': curso['horario'],
            'docente_id': curso['docente_id']
        }
        old_curso = self.session.query(Curso).filter(Curso.curso_id == curso_id).first()
        for key, value in curso_item.items():
            setattr(old_curso, key, value)
        self.session.commit()
        return {'message': f'el curso con id {curso_id} fue actualizado con éxito',
                'curso': {"id":curso_id, **curso}}
    
    # 4. Eliminar un curso existente.
    def delete_curso_by_id(self, id: int):
        curso = self.session.query(Curso).filter(Curso.curso_id == id).first()
        self.session.delete(curso)
        self.session.commit()
        return {'message': f'El curso con id {id} fue eliminado con éxito'}

    # 5. Obtener Docentes registrados   
    def get_all_docentes(self):
        results = self.session.query(Docente).all()
        response = []
        for result in results:
            response.append(self.model_as_dict(result))
        return response
    
    # 6. Crear un nuevo docente
    def create_docente(self, docente: dict):
        user = self.session.query(Usuario).filter(Usuario.numero_documento == docente['numero_documento']).first()
        docente_item = {**docente, 'usuario_id': user.usuario_id if user is not None else None}
        docente_object = Docente(**docente_item)
        self.session.add(docente_object)
        self.session.commit()
        return {'message': 'El docente ha sido creado con éxito'}
    
    # 7. Actualizar un docente existente
    def update_docente(self, docente: dict, docente_id: int):
        user = self.session.query(Usuario).filter(Usuario.numero_documento == docente['numero_documento']).first()
        docente_item = {**docente, 'usuario_id': user.usuario_id if user is not None else None}
        old_docente = self.session.query(Docente).filter(Docente.docente_id == docente_id).first()
        for key, value in docente_item.items():
            setattr(old_docente, key, value)
        self.session.commit()
        return {'message': f'el curso con id {docente_id} fue actualizado con éxito',
                'curso': {"id":docente_id, **docente}}

    # 8. Eliminar un docente existente.
    def delete_docente_by_id(self, id: int):
        docente = self.session.query(Docente).filter(Docente.docente_id == id).first()
        self.session.delete(docente)
        self.session.commit()
        return {'message': f'El docente con id {id} fue eliminado con éxito'}
    
    # 9. Obtener usuarios registrados   
    def get_all_usuarios(self):
        results = self.session.query(Usuario).all()
        response = []
        for result in results:
            response.append(self.model_as_dict(result))
        return response

    # Crear un nuevo usuario
    def create_usuario(self, usuario: dict):
        docente = self.session.query(Docente).filter(Docente.tipo_documento == usuario['tipo_documento'], 
                                                     Docente.numero_documento == usuario['numero_documento']).first()
        rol = 'estudiante'
        if docente is not None:
            rol = 'docente'
        rol_object = self.session.query(Rol).filter(Rol.nombre == rol).first()
            
        usuario_item = {
            'nombre': usuario['nombre'],
            'email': usuario['email'],
            'tipo_documento': usuario['tipo_documento'],
            'numero_documento': usuario['numero_documento'],
            'fecha_nacimiento': usuario['fecha_nacimiento'],
            'contrasena': usuario['contrasena'],
            'rol_id': rol_object.rol_id
        }
        usuario_object = Usuario(**usuario_item)
        self.session.add(usuario_object)
        self.session.commit()
        return {'message': 'El usuario ha sido creado con éxito'}
    
    # Get Usuario
    def get_usuario_by_email(self, email: str):
        usuario = self.session.query(Usuario).filter(Usuario.email == email).first()
        if usuario is None:
            return {}
        return usuario.as_dict()
    
    # Crear matrícula
    def create_matricula(self, new_matricula:dict):
        try:
            new_matricula = self.remove_leftover_spaces(new_matricula)
            curso = self.session.query(Curso).filter(Curso.nombre == new_matricula["curso"]).first()
            user = self.session.query(Usuario).filter(Usuario.email == new_matricula["correo"]).first()
            matricula_item = {
                "usuario_id": user.usuario_id if user is not None else None,
                "curso_id": curso.curso_id if curso is not None else None,
                "fecha": date.today().strftime("%Y-%m-%d")
            }
            check_matricula = self.session.query(Matricula).filter(Matricula.usuario_id == matricula_item["usuario_id"], Matricula.curso_id == matricula_item["curso_id"]).first()
            if check_matricula:
                return "Exists"
            self.session.add(Matricula(**matricula_item))
            self.session.commit()
            return matricula_item
        except Exception:
            return matricula_item

    # Funcion para transformar objeto de un modelo a diccionario 
    def model_as_dict(self, object):
        return {attr.key: getattr(object, attr.key) for attr in object.__mapper__.attrs}
    
    def get_where_location_conditions(self, rol: str):
        where_conditions = []
        if rol:
            where_conditions.append(
                Rol.nombre == rol
            )
        return where_conditions

    def get_full_query(self):
        return self.session.query(Usuario, Rol.rol_id).join(
            Rol, Usuario.rol_id == Rol.rol_id, isouter=True
            )

    def remove_leftover_spaces(self, item:dict):
        return {key: value.strip() if isinstance(value, str) else value for key, value in item.items()}