

def membro_da_equipe(user):
    membro = False
    if user.is_staff:
        membro = True
    return membro

def usuario_comum(user):
    comum = False
    if user.last_name == 'usuariocomum':
        comum = True
    return comum


def isnumber(value):
    try:
         float(value)
    except ValueError:
         return False
    return True