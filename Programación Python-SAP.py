print("¡Hola!")
print("¿Que información necesitas llevar a SAP?")
print("1. Aviso (IW21)")
print("2. Orden de mantenimiento (IW31)")
seleccion= input("Selecciona una opción (1 o 2):")
if seleccion == "1":
    print("Perfecto, vamos a redactar el aviso para SAP.")
    print("Recuerda que debes describir el problema de manera clara y concisa, sin errores ortograficos.")
    mac_o_mpl=input("¿El aviso es para un MAC (1) o un MPL(2)?:")
    if mac_o_mpl < "1" or mac_o_mpl > "2":
        print("Opción no valida. porfavor selcciona una opción valida.")
    if mac_o_mpl == "1":
        print("Seleccionaste MAC.")
    estacion_mac= input("¿Cuál es la estación de trabajo involucrada?:")
    print("Perfecto, la estación es", estacion_mac)
    print("¿En qué recinto se realizo el mantenimiento?")
    print("- SAF V1")
    print("- SAF V2")
    print("- SER")
    print("- Vías")
    recinto_mc= input("Selecciona una opción:")
    if recinto_mc != "SAF V1" and recinto_mc != "SAF V2" and recinto_mc != "SER" and recinto_mc != "Vías":
        print("Opción no valida. porfavor selecciona una opción valida.")
    else:
        print("Seleccionaste", recinto_mc)
    equipo_mac= input ("¿Cuál es el equipo involucrado?:")
    problema_mac= input("Describe el problema encontrado:")
    mantenimiento_equpo_mac= input("¿Qué tipo de mantenimiento se realizó?:")
    solucion_mac= input("¿Cuál fue la solución aplicada?:")
    inspectores_mac= input("¿Quién realizó la inspección?:")
    supervisor_mac= input("¿Quién es el supervisor a cargo?:")
    tecnicos_mac= input("¿Quiénes son los técnicos involucrados?:")
    empresa_contratista_mac= input("¿Cuál es la empresa contratisa?:")
    om_mac= input("¿Cuál es la orden de mantenimiento asociada (si aplica)?:")
    fecha_mac= input("¿Cuál es la fecha del aviso (DD/MM/AAAA)?:")
    hora_mac= input("¿Cuál es la hora del aviso (HH:MM)?:")
    semana_mac= input("¿Cuál es la semana del aviso (Número de semana)?:")
    turno_mac= input("¿Cuál es el turno del aviso (Mañana/Tarde/Noche)?:")
    actividad_mac= input("¿Cuál es la actividad realizada?:")
    observacion_mac= input("¿Se encuentran observaciones adicionales?:")
    print("¡Gracias! Has completado la información para el aviso en SAP.")
    print("Resumen del aviso:")
    print("Tipo de aviso: MAC")
    print("Estación de trabajo:", estacion_mac)
    print("Recinto:", recinto_mc)
    print("Equipo involucrado:", equipo_mac)
    print("Problema encontrado:", problema_mac)
    print("Tipo de mantenimiento realizado:", mantenimiento_equpo_mac)
    print("Solución aplicada:", solucion_mac)
    print("Inspector:", inspectores_mac)
    print("Supervisor a cargo:", supervisor_mac)
    print("Técnicos involucrados:", tecnicos_mac)
    print("Empresa contratista:", empresa_contratista_mac)
    print("Orden de mantenimiento asociada:", om_mac)
    print("Fecha del aviso:", fecha_mac)
    print("Hora del aviso:", hora_mac)
    print("¡Listo para ingresar el aviso en SAP!")

    #******************Informe final de Aviso A2 MAC******************************
    informe_aviso_mac = f"""
    Informe del Aviso para SAP - MAC    
    -----------------------------------
    Semana: {semana_mac}
    Fecha: {fecha_mac}
    Hora de inicio: {hora_mac}
    Hora de término: {hora_mac}
    Turno: {turno_mac}
    Actividad realizada: {actividad_mac}
    Estación de trabajo: {estacion_mac}
    Recinto: {recinto_mc}
    Equipo involucrado: {equipo_mac}
    Problema encontrado: {problema_mac}
    Inspector: {inspectores_mac}
    Empresa contratista: {empresa_contratista_mac}
    Supervisor a cargo: {supervisor_mac}
    Tecnicos involucrados: {tecnicos_mac}    
    Técnicos involucrados: {tecnicos_mac}
    Orden de mantenimiento asociada: {om_mac}

    ---------Resumen de la Inspección y Mantenimiento---------

    Se realiza inspección tecnica a {actividad_mac} en la estación {estacion_mac} ubicada en el recinto {recinto_mc}. 
    El supervisor a cargo de {empresa_contratista_mac} es {supervisor_mac} junto a {tecnicos_mac} técnicos.
    Los equipos inspeccionados son {equipo_mac}.
    Durante la inspección se detectó el siguiente problema: {problema_mac}.
    Se llevó a cabo un mantenimiento de tipo {mantenimiento_equpo_mac} y se aplicó la siguiente solución: {solucion_mac}.
    La OM asociada a este mantenimiento correctivo es {om_mac}

    -------------------Observaciones--------------------------
    {observacion_mac}
    ----------------------------------------------------------"""

    print("En que formato necesitas el informe?")
    seleccion_formato_mac=input("" \
    "1. Formato wWord" \
    "2. Formato PDF" \
    "Selecciona una opción (1 o 2):")
    if seleccion_formato_mac == "1":
        print("Generando informe en formato Word",informe_aviso_mac)
    elif seleccion_formato_mac == "2":
        print("Generando informe en formato PDF...")

    from docx import Document                    # Importar el informe a Word, este paso es similar para PDF
    document = Document()                            
    print("DEBUG:", informe_aviso_mac)
    document.add_paragraph(informe_aviso_mac)
    document.save('informe_aviso_mac.docx')         #Aca termina el proceso de generación de Word

    

   