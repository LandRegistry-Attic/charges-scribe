from app.key import service as key_service


def all_keys():
    return key_service.all()
