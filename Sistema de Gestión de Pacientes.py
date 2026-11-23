class paciente:
    def __init__(self, nombre_completo, documento_numero_tipo, fecha_nacimiento, sexo, direccion, telefono, correo, eps, peso, estatura):
        self.nombre_completo = nombre_completo
        self.documento__numero_tipo = documento_numero_tipo
        self.fecha_nacimiento = fecha_nacimiento
        self.sexo = sexo
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.eps = eps
        self.peso = peso
        self.estatura = estatura

    def ingresar_datos(self):
        self.nombre_completo = input("Ingrese el nombre completo del paciente: ")
        self.documento__numero_tipo = input("Ingrese el número de documento y tipo: ")
        self.fecha_nacimiento = input("Ingrese la fecha de nacimiento: ")
        self.sexo = input("Ingrese el sexo del paciente: ")
        self.direccion = input("Ingrese la direccion: ")
        self.telefono = input("Ingrese el numero de telefono: ")
        self.correo = input("Ingrese el correo del paciente: ")
        self.eps = input("Ingrese la EPS del paciente: ")
        self.peso = input("Ingrese el peso del paciente: ")
        self.estatura = input("Ingrese la estatura del paciente: ")
        self.guardar_datos_paciente()

class contacto_emergencia:
    def __init__(self, nombre_familiar, parentesco, numero_telefono):
        self.nombre_familiar = nombre_familiar
        self.parentesco = parentesco
        self.numero_telefono = numero_telefono

    def ingresar_datos_contacto_emergencia(self):
        self.nombre_familiar = input("Ingrese el nombre del familiar: ")
        self.parentesco = input("Ingrese el parentesco: ")
        self.numero_telefono = input("Ingrese el numero de telefono del familiar: ")
        self.guardar_datos_contacto_emergencia()

class historia_clinico:
    def __init__(self, motivo_consulta, antecedentes_personales, antecedentes_familiares, alergias, medicamentos_actuales, cirugias, habitos):
        self.motivo_consulta = motivo_consulta
        self.antecedentes_personales = antecedentes_personales
        self.antecedentes_familiares = antecedentes_familiares
        self.alergias = alergias
        self.medicamentos_actuales = medicamentos_actuales
        self.cirugias = cirugias
        self.habitos = habitos

    def ingresar_datos_historia_clinica(self):
        self.motivo_consulta = input("Ingrese el motivo de la consulta: ")
        self.antecedentes_personales = input("Ingrese los antecedentes personales: ")
        self.antecedentes_familiares = input("Ingrese los antecedentes familiares: ")
        self.alergias = input("Ingrese las alergias: ")
        self.medicamentos_actuales = input("Ingrese los medicamentos actuales: ")
        self.cirugias = input("Ingrese las cirugías previas: ")
        self.habitos = input("Ingrese los hábitos del paciente: ")
        self.guardar_datos_historia_clinica()

class cita:
    def __init__(self, paciente, fecha, medico, orden_medica, consentimiento_familiar_firmado, consentimiento_firmado, valor_copago):
        self.paciente = paciente
        self.fecha = fecha
        self.medico = medico
        self.orden_medica = orden_medica
        self.consentimiento_familiar_firmado = consentimiento_familiar_firmado
        self.consentimiento_firmado = consentimiento_firmado
        self.valor_copago = valor_copago

    def ingresar_datos_cita(self):
        self.paciente = input("Ingresar el nombre del paciente: ")
        self.fecha = input("Ingresar la fecha de la cita: ")
        self.medico = input("ingresar el nombre del medico: ")
        self.orden_medica = input("Ingresar la orden medica: ")
        self.consentimiento_familiar_firmado = input("Ingresar si el familiar firmo el consentimiento (S/N): ")
        self.consentimiento_firmado = input("Ingresar si el paciente firmo el consentimiento (S/N): ")
        self.valor_copago = input("Ingresar el valor del copago: ")
        self.guardar_datos_cita()

while True:
    print("\n=== Sistema de Gestión de Pacientes ===")
    print("\n=== Ingreso de datos del paciente ===")
    print("\n1. Ingresar datos del paciente")
    print("2. Ingresar datos del contacto de emergencia")
    print("3. Ingresar datos de la historia clínica")
    print("4. Cita médica")
    opcion = input("\nSeleccione una opción: ")
    match opcion:
        case "1":
            paciente1 = paciente("", "", "", "", "", "", "", "", "", "")
            paciente1.ingresar_datos()
            print("Datos del paciente ingresados correctamente.")
        case "2":
            contacto_emergencia1 = contacto_emergencia("", "", "")
            contacto_emergencia1.ingresar_datos_contacto_emergencia()
            print("Datos del contacto de emergencia ingresados correctamente.")
        case "3":
            historia_clinica1 = historia_clinico("", "", "", "", "", "", "")
            historia_clinica1.ingresar_datos_historia_clinica()
            print("Datos de la historia clínica ingresados correctamente.")
        case "4":
            cita1 = cita("", "", "", "", "", "", "")
            cita1.ingresar_datos_cita()
            print("Datos de la cita ingresados correctamente.")
        case _:
            print("Opción no válida. Por favor, seleccione una opción válida.")
