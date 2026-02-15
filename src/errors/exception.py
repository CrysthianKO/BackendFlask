class UserAlreadyExistsError(Exception):
    """Lançado quando tenta criar usuário duplicado"""
    pass

class InvalidCpfError(Exception):
    """Lançado quando o CPF é inválido"""
    pass

class ResourceNotFound(Exception):
    """Lançado quando não acha algo no banco"""
    pass