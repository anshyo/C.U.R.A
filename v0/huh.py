from filehandle import file as f
from cryptography.fernet import Fernet

def encrypt(text:str):
    return Fernet(Fernet.generate_key()).encrypt(text.encode())

if __name__ == "__main__":
    g = encrypt(f('v0/huh.py').data)
    print(Fernet(Fernet.generate_key()).decrypt("b'gAAAAABktnTHvxbway0ZQp3CJSpFOuyXuroeOKUBB_avK0W9B0rY0vc2ki_wcw_-CnMHw77tvx9IOMebD3HJbjnq4Qf2Lb7YdDSfnANRJmpEyOGTGss3fwMUXWWs9wZ4tDwJ7SSNgh1YCIQwCp0Ixv22kJncKty2sbeiS7u1LQg5gCa8ahx9gAqZRrmPz6j8lBpLz4rOIe0gF-tysEdFuvayFq_BJ2sUMti0-KiZ8TQROh23tjwXtL73U5DfLgahZEY6mF4wGdQjEXhpVV8oW7U2NBFwO33rUugwoR6IH6vaiF_fo-6H9g4DPDSEdFowNiTK0hqvcSfPAoZn3-9UtA1evZbPxCeR6owD-So4zNAvKqnVXvytGgAH8exX8wX_ZhHPTeVtdT_d'").decode())