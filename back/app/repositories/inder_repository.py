from back.app.context.db_connection import Session
from back.app.models.inder import Rol, Usuario, Docente, Curso, Matricula, Asistencia, Calificacion

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
        docente_item = {
            'docente_id': docente['docente_id'],
            'nombre': docente['nombre'],
            'especialidad': docente['especialidad']
        }
        docente_object = Docente(**docente_item)
        self.session.add(docente_object)
        self.session.commit()
        return {'message': 'El docente ha sido creado con éxito'}
    
    # 7. Actualizar un docente existente
    def update_docente(self, docente: dict, docente_id: int):
        docente_item = {
            'docente_id': docente['docente_id'],
            'nombre': docente['nombre'],
            'especialidad': docente['especialidad']
        }
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
            'usuario_id': usuario['usuario_id'],
            'nombre': usuario['nombre'],
            'email': usuario['email'],
            'tipo_documento': usuario['tipo_documento'],
            'numero_documento': usuario['numero_documento'],
            'fecha_nacimiento': usuario['fecha_nacimiento'],
            'rol_id': rol_object.rol_id
        }
        usuario_object = Usuario(**usuario_item)
        self.session.add(usuario_object)
        self.session.commit()
        return {'message': 'El usuario ha sido creado con éxito'}
    
    # Get Usuario
    def get_usuario_by_email(self, email: str):
        return self.session.query(Usuario).filter(Usuario.email == email).first().as_dict()
















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

    # # 2. Obtener un reactor por Id
    # def get_reactor_by_id(self, id: int):
    #     result = self.session.query(Reactor, Estado.estado, Ubicacion.ciudad, Pais.pais, TipoReactor.tipo).join(
    #         Estado, Reactor.id_estado == Estado.id, isouter=True).join(
    #             TipoReactor, Reactor.id_tipo_reactor == TipoReactor.id, isouter=True
    #         ).join(
    #             Ubicacion, Reactor.id_ubicacion == Ubicacion.id, isouter=True
    #         ).join(
    #             Pais, Ubicacion.id_pais == Pais.id, isouter=True
    #         ).filter(Reactor.id == id).first()
    #     return {
    #         **self.model_as_dict(result[0]),
    #         'estado': result[1],
    #         'ciudad': result[2],
    #         'pais': result[3],
    #         'tipo': result[4]
    #     }

    
    # # 4. Actualizar un reactor existente.
    # def update_reactor(self, reactor: dict, reactor_id: int):
    #     reactor_item = self.get_reactor_foreign_keys(reactor)
    #     old_reactors = self.session.query(Reactor).filter(Reactor.id == reactor_id).first()
    #     for key, value in reactor_item.items():
    #         setattr(old_reactors, key, value)
    #     self.session.commit()
    #     return {'message': f'el reactor con id {reactor_id} fue actualizado con éxito',
    #             'reactor': {"id":reactor_id, **reactor}}
    
    # # 5. Eliminar un reactor existente
    # def delete_reactor_by_id(self, id: int):
    #     reactor = self.session.query(Reactor).filter(Reactor.id == id).first()
    #     self.session.delete(reactor)
    #     self.session.commit()
    #     return {'message': f'El reactor con id {id} fue eliminado con éxito'}
    
    # # 6. Obtener tipos de reactores registrados
    # def get_all_reactor_types(self):
    #     results = self.session.query(TipoReactor).all()
    #     response = []
    #     for result in results:
    #         response.append(self.model_as_dict(result))
    #     return response
    
    # # 7. Obtener tipo de reactor por Id. Respuesta incluye todos los reactores asociados al tipo.
    # def get_reactors_with_same_reactor_type_by_id(self, reactor_id:int):
    #     reactor = self.session.query(TipoReactor.id).join(
    #         Reactor, 
    #         TipoReactor.id == Reactor.id_tipo_reactor,
    #         isouter=True
    #         ).filter(Reactor.id == reactor_id).first()
    #     full_query = self.get_full_query()
    #     results = full_query.filter(Reactor.id_tipo_reactor == reactor[0]).all()
    #     response = []
    #     for result in results:
    #         response.append(
    #             {
    #                 **self.model_as_dict(result[0]),
    #                 'estado': result[1],
    #                 'ciudad': result[2],
    #                 'pais': result[3],
    #                 'tipo': result[4]
    #             }
    #         )
    #     return response
    
    # # 8. Obtener Ubicaciones Registradas
    # def get_all_locations(self):
    #     results = self.session.query(Ubicacion.ciudad, Pais.pais).join(Pais, Ubicacion.id_pais == Pais.id, isouter=True).all()
    #     response = []
    #     for result in results:
    #         response.append(
    #             {
    #                 'ciudad': result[0],
    #                 'pais': result[1]
    #             }
    #         )
    #     return response
    
    # # 9. Obtener Ubicación por Id.
    # def get_reactors_with_same_location_by_id(self, reactor_id:int):
    #     reactor = self.session.query(Ubicacion.id).join(
    #         Reactor, 
    #         Ubicacion.id == Reactor.id_ubicacion,
    #         isouter=True
    #         ).filter(Reactor.id == reactor_id).first()
    #     full_query = self.get_full_query()
    #     results = full_query.filter(Reactor.id_ubicacion == reactor[0]).all()
    #     response = []
    #     for result in results:
    #         response.append(
    #             {
    #                 **self.model_as_dict(result[0]),
    #                 'estado': result[1],
    #                 'ciudad': result[2],
    #                 'pais': result[3],
    #                 'tipo': result[4]
    #             }
    #         )
    #     return response
    
    # # 10. Obtener Reactores registrados por Ubicación
    # def get_reactors_by_location(self, country: str, city: str):
    #     where_conditions = self.get_where_location_conditions(country, city)

    #     if len(where_conditions) > 0:
    #         full_query = self.get_full_query()
    #         results = full_query.filter(*where_conditions).all()
    #         response = []
    #         for result in results:
    #             response.append(
    #                 {
    #                     **self.model_as_dict(result[0]),
    #                     'estado': result[1],
    #                     'ciudad': result[2],
    #                     'pais': result[3],
    #                     'tipo': result[4]
    #                 }
    #             )
    #         return response
    #     return self.get_all_reactors()
    

    # # Funciones Auxiliares
    # def get_reactor_foreign_keys(self, reactor: dict):
    #     pais = self.session.query(Pais).filter(Pais.pais == reactor['pais']).first()
    #     pais_obj = Pais(pais=reactor['pais'])
    #     estado_obj = Estado(estado=reactor['estado'])
    #     tipo_obj = TipoReactor(tipo=reactor['tipo'])
    #     if pais is None:
    #         self.session.add(pais_obj)
    #         self.session.commit()
    #         pais = pais_obj
    #     ubicacion = self.session.query(Ubicacion).filter(Ubicacion.ciudad==reactor['ciudad'], Ubicacion.id_pais == pais.id).first()
    #     ubicacion_obj = Ubicacion(ciudad=reactor['ciudad'], id_pais=pais.id if pais is not None else pais_obj.id)
    #     if ubicacion is None:
    #         self.session.add(ubicacion_obj)
    #         self.session.commit()
    #         ubicacion = ubicacion_obj
    #     estado = self.session.query(Estado).filter(Estado.estado == reactor['estado']).first()
    #     if estado is None:
    #         self.session.add(estado_obj)
    #         self.session.commit()
    #         estado = estado_obj
    #     tipo = self.session.query(TipoReactor).filter(TipoReactor.tipo == reactor['tipo']).first()
    #     if tipo is None:
    #         self.session.add(tipo_obj)
    #         self.session.commit()
    #         tipo = tipo_obj
    #     reactor_item = {
    #         'nombre': reactor['nombre'],
    #         "potencia_termica": reactor['potencia_termica'],
    #         "primera_fecha_reaccion": reactor['primera_fecha_reaccion'],
    #         "id_tipo_reactor": tipo.id,
    #         "id_ubicacion": ubicacion.id,
    #         "id_estado": estado.id
    #     }
    #     return reactor_item
    

    # def get_full_query(self):
    #     return self.session.query(Reactor, Estado.estado, Ubicacion.ciudad, Pais.pais, TipoReactor.tipo).join(
    #         Estado, Reactor.id_estado == Estado.id, isouter=True).join(
    #             TipoReactor, Reactor.id_tipo_reactor == TipoReactor.id, isouter=True
    #         ).join(
    #             Ubicacion, Reactor.id_ubicacion == Ubicacion.id, isouter=True
    #         ).join(
    #             Pais, Ubicacion.id_pais == Pais.id, isouter=True
    #         )

    # def get_where_location_conditions(self, country: str, city: str):
    #     where_conditions = []
    #     if country:
    #         where_conditions.append(
    #             Pais.pais == country
    #         )
    #     if city:
    #         where_conditions.append(
    #             Ubicacion.ciudad == city
    #         )
    #     return where_conditions
    

    # # Funcion para transformar objeto de un modelo a diccionario 
    # def model_as_dict(self, object):
    #     return {attr.key: getattr(object, attr.key) for attr in object.__mapper__.attrs}