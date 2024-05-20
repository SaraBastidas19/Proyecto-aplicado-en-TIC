from back.app.repositories.inder_repository import InderRelationalRepository
from passlib.context import CryptContext


class InderService:
    def __init__(self):
        self.cipher = CryptContext(schemes=['bcrypt'], deprecated=['auto']) #Cifrado strings (hash)
        self.repository = InderRelationalRepository()

    # 1. Obtener roles disponibles.
    def get_all_roles(self):
        return self.repository.get_all_roles()
    
    # 2. Obtener cursos registrados.
    def get_all_cursos(self):
        return self.repository.get_all_cursos()
    
    # 2. Crear nuevo curso
    def create_curso(self, curso: dict):
        return self.repository.create_curso(curso)
    
    # 3. Actualizar un curso existente
    def update_curso(self, curso: dict, curso_id: int):
        return self.repository.update_curso(curso, curso_id)

    # 4. Eliminar un curso existente.
    def delete_curso_by_id(self, curso_id: int):
        return self.repository.delete_curso_by_id(curso_id)
    
    # 5. Obtener Docentes registrados
    def get_all_docentes(self):
        return self.repository.get_all_docentes()

    # 6. Crear un nuevo docente
    def create_docente(self, docente: dict):
        return self.repository.create_docente(docente)

    # 7. Actualizar un docente existente
    def update_docente(self, docente: dict, docente_id: int):
        return self.repository.update_docente(docente, docente_id)
    
    # 8. Eliminar un docente existente.
    def delete_docente_by_id(self, docente_id: int):
        return self.repository.delete_docente_by_id(docente_id)
    
    # 9. Obtener Estudiantes registrados
    def get_all_usuarios(self):
        return self.repository.get_all_usuarios()
    
    # 10. Crear un nuevo usuario
    def create_usuario(self, usuario: dict):
        usuario['contrasena'] = self.cipher.hash(usuario['contrasena'])
        return self.repository.create_usuario(usuario)
    
    # Metodo Login
    def login(self, form_data: dict):
        usuario = self.repository.get_usuario_by_email(form_data['correo'])
        if len(usuario.keys()) == 0:
            return 'No existe un usuario con este correo'
        if not self.cipher.verify(form_data['contrasena'], usuario['contrasena']):
            return 'Contraseña Incorrecta'
        return usuario










    
    # def get_reactor_by_id(self, id: int):
    #     return self.repository.get_reactor_by_id(id)
    
    # def get_all_reactor_types(self):
    #     return self.repository.get_all_reactor_types()

    # def get_all_locations(self):
    #     return self.repository.get_all_locations()

    # def get_reactors_with_same_reactor_type_by_id(self, reactor_id: int):
    #     return self.repository.get_reactors_with_same_reactor_type_by_id(reactor_id)
    
    # def get_reactors_with_same_location_by_id(self, reactor_id:int):
    #     return self.repository.get_reactors_with_same_location_by_id(reactor_id)
    
    # def get_reactors_by_location(self, country: str, city: str):
    #     return self.repository.get_reactors_by_location(country, city)
    

    
    # def update_reactor(self, reactor: dict, reactor_id: int):
    #     return self.repository.update_reactor(reactor, reactor_id)
    
    # def delete_reactor_by_id(self, reactor_id: int):
    #     return self.repository.delete_reactor_by_id(reactor_id)
    
