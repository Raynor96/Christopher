import bcrypt
#paso 1. Obtener contraseña en piano
incoming_password = input("Ingresa tu contraseña: ").encode("UTF-8")
#paso 2. Crear un pedazo de sal
salt = bcrypt.gensalt(rounds=12)
#paso 3. Hashear la contraseña en plano y dar una sal al hasheo
hashed_password = bcrypt.hashpw(password=incoming_password, salt=salt)
print("contraseña hasheada", hashed_password)

#Paso 4. Ingresar de nuevo la contraseña
confirm_password = input("Ingresar nuevamente la contraseña: ").encode("UTF-8")
#Paso 5. comparar contraseñas
if bcrypt.checkpw(confirm_password, hashed_password):
    print("Contraseña correcta")
else:
    print("Contraseña incorrecta")