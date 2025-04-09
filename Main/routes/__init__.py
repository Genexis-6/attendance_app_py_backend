from .security import security

def reg_routes(app):
    app.include_router(security)