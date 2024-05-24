from typing import List
from fastapi import FastAPI, status, Path, Query, Body, Depends
from backend.app.models.inder_schema import CursosResponseModel, DocenteResponseModel, UsuarioResponseModel, RolesResponseModel
from backend.app.services.inder_service import InderService
from backend.app.exceptions.exceptions import Exceptions

app = FastAPI()

app.add_exception_handler(Exception, handler=Exceptions().base_error)

# 1. Obtener roles existentes
@app.get(
        path='/roles',
        status_code=status.HTTP_200_OK,
        response_model=List[RolesResponseModel],
)
async def get_all_roles():
    return InderService().get_all_roles()


# 1. Obtener cursos registrados.
@app.get(
        path='/cursos',
        status_code=status.HTTP_200_OK,
        response_model=List[CursosResponseModel],
)
async def get_all_cursos():
    return InderService().get_all_cursos()

# 2. Crear un nuevo curso.
@app.post(
        path='/cursos',
        status_code=status.HTTP_201_CREATED,
)
async def create_curso(curso: CursosResponseModel=Body(...)):
    return InderService().create_curso(curso.model_dump())

# 3. Actualizar un curso existente
@app.put(
        path='/cursos/{id}',
        status_code=status.HTTP_200_OK,
)
async def update_curso(curso: CursosResponseModel=Body(...), id: int = Path(...)):
    return InderService().update_curso(curso.model_dump(), id)

# 4. Eliminar un curso existente.
@app.delete(
        path='/cursos/{id}',
        status_code=status.HTTP_200_OK,
)
async def delete_curso_by_id(id: int = Path(...)):
    return InderService().delete_curso_by_id(id)

# 9. Obtener Usuarios registrados
@app.get(
        path='/usuarios',
        status_code=status.HTTP_200_OK,
        response_model=List[UsuarioResponseModel],
)
async def get_all_usuarios():
    return InderService().get_all_usuarios()

# 6. Crear un nuevo usuario
@app.post(
        path='/usuarios',
        status_code=status.HTTP_201_CREATED,
)
async def create_usuario(estudiante: UsuarioResponseModel=Body(...)):
    return InderService().create_usuario(estudiante.model_dump())

# 5. Obtener Docentes registrados
@app.get(
        path='/docentes',
        status_code=status.HTTP_200_OK,
        response_model=List[DocenteResponseModel],
)
async def get_all_docentes():
    return InderService().get_all_docentes()

# 6. Crear un nuevo docente
@app.post(
        path='/docentes',
        status_code=status.HTTP_201_CREATED,
)
async def create_docente(docente: DocenteResponseModel=Body(...)):
    return InderService().create_docente(docente.model_dump())

# 7. Actualizar un docente existente
@app.put(
        path='/docentes/{id}',
        status_code=status.HTTP_200_OK,
)
async def update_docente(docente: DocenteResponseModel=Body(...), id: int = Path(...)):
    return InderService().update_docente(docente.model_dump(), id)

# 8. Eliminar un docente existente.
@app.delete(
        path='/docentes/{id}',
        status_code=status.HTTP_200_OK,
)
async def delete_docente_by_id(id: int = Path(...)):
    return InderService().delete_docente_by_id(id)






















# 6. Obtener tipos de reactores registrados.
# @app.get(
#         path='/reactors/types',
#         status_code=status.HTTP_200_OK,
#         response_model=List[ReactorTypeResponseModel],
# )
# async def get_all_reactor_types():
#     return ReactorService().get_all_reactor_types()

# # 8. Obtener Ubicaciones Registradas.
# @app.get(
#         path='/reactors/locations',
#         status_code=status.HTTP_200_OK,
#         response_model=List[LocationResponseModel],
# )
# async def get_all_locations():
#     return ReactorService().get_all_locations()

# # 7. Obtener tipo de reactor por Id. Respuesta incluye todos los reactores asociados al tipo.
# @app.get(
#         path='/reactors/types/{id}',
#         status_code=status.HTTP_200_OK,
#         response_model=List[ReactorResponseModel],
# )
# async def get_reactors_with_same_reactor_type_by_id(id: int):
#     return ReactorService().get_reactors_with_same_reactor_type_by_id(id)

# # 10. Obtener Reactores registrados por Ubicación
# @app.get(
#         path='/reactors/location',
#         status_code=status.HTTP_200_OK,
#         response_model=List[ReactorResponseModel],
# )
# async def get_reactors_by_location(country: str = Query(default=None), city: str = Query(default=None)):
#     return ReactorService().get_reactors_by_location(country, city)

# # 9. Obtener Ubicación por Id.
# @app.get(
#         path='/reactors/location/{id}',
#         status_code=status.HTTP_200_OK,
#         response_model=List[ReactorResponseModel],
# )
# async def get_reactors_with_same_location_by_id(id: int):
#     return ReactorService().get_reactors_with_same_location_by_id(id)

# # 2. Obtener un reactor por Id.
# @app.get(
#         path='/reactors/{id}',
#         status_code=status.HTTP_200_OK,
#         response_model=ReactorResponseModel,
# )
# async def get_reactor_by_id(id: int):
#     return ReactorService().get_reactor_by_id(id)


# # 4. Actualizar un reactor existente.
# @app.put(
#         path='/reactors/{id}',
#         status_code=status.HTTP_200_OK,
# )
# async def update_reactor(reactor: ReactorCreateModel=Body(...), id: int = Path(...)):
#     return ReactorService().update_reactor(reactor.model_dump(), id)

# # 5. Eliminar un reactor existente.
# @app.delete(
#         path='/reactors/{id}',
#         status_code=status.HTTP_200_OK,
# )
# async def delete_reactor_by_id(id: int = Path(...)):
#     return ReactorService().delete_reactor_by_id(id)