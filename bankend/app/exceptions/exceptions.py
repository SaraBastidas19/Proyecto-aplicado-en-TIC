from fastapi import Request, status
from fastapi.responses import JSONResponse

class Exceptions:

    def base_error(self, request: Request, exception: Exception):
        return JSONResponse(content=f'Ha ocurrido un error en {request.url.path}: {str(exception)}',
                             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)