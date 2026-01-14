print("¡Hola!")
print("¿Que información necesitas llevar a SAP?")
print("1. Aviso (IW21)")
print("2. Orden de mantenimiento (IW31)")
seleccion= input("Selecciona una opción (1 o 2):")
if seleccion == "2":
    print("Perfecto, vamos a redactar la orden para SAP.")
    print("Recuerda que debes describir el problema de manera clara y concisa, sin errores ortograficos.")
    mac_o_mpl=input("¿La orden es para un MAC (1) o un MPL(2)?:")
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
        problema_mac= input ("¿Cuál es el problema encontrado anteirormente por el equipo?:")
        mantenimiento_equipo_mac= input("¿Qué tipo de mantenimiento se realizó?:")
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
        sistema_mac= input("¿El sistema es entregado en  conformidad? (si/no);")
        if sistema_mac.lower() == "si":
            conformidad_mac= input("El sistema es entregado en coformidad.")
        else:
            conformidad_mac= input("El sistema no es entregado en conformidad.")
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
        print(conformidad_mac)
        print("¡Listo para ingresar el aviso en SAP!")
        resumen_mac = input ("Resume la inspección, esto aparecera como el resumen general de la orden en SAP:")

        #******************Informe final de Aviso A3 MAC******************************
        from textwrap import dedent

        informe_aviso_mac = dedent(f"""\
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
        Técnicos involucrados: {tecnicos_mac}
        Orden de mantenimiento asociada: {om_mac}

        ---------Resumen de la Inspección y Mantenimiento---------
        {resumen_mac}

        -------------------Observaciones--------------------------
        {observacion_mac}
        ----------------------------------------------------------
        """)

        print(informe_aviso_mac)
    elif mac_o_mpl == "2":
        print("Seleccionaste MPL.") 
        estacion_mpl= input("¿Cuál es la estación de trabajo involucrada?:")
        print("Perfecto, la estación es", estacion_mpl)
        print ("¿En qué recinto se realizo el mantenimiento?")
        print("- SAF V1")
        print("- SAF V2")
        print("- SER")
        print("- Vías")
        recinto_mpl= input("Selecciona una opción:")
        if recinto_mpl != "SAF V1" and recinto_mpl != "SAF V2" and recinto_mpl != "SER" and recinto_mpl != "Vías":
            print("Opción no valida. porfavor selecciona una opción valida.")
        else:
            print("Seleccionaste", recinto_mpl)
            semana_mpl = input("¿Cuál es la semana de mantenimiento? (Si es del 1 al 9, debe escribir 0 antes):")
            dia_mpl = input("¿Cuál es el dia del mantenimiento?:")
            fecha = input ("¿Cuál es la fecha del mantenimiento (DD/MM/AAAA)?:")
            hora_inicio_mpl= input("¿Cuál es la hora de inicio del mantenimiento (HH:MM)?:")
            hora_termino_mpl= input("¿Cuál es la hora de término del mantenimiento (HH:MM)?:")
            turno_mpl= input("¿Cuál es el turno del mantenimiento (Mañana/Tarde/Noche)?:")
            manteniminto_mpl = input("¿Cuál es el mantenimiento realizado?:")
            equipo_mpl= input ("¿Cuál(es)  es o son los equipos involucrado(s)?:")
            orden_mpl= input("¿Cuál es la orden de mantenimiento asociada (si aplica)?:")
            empresa_mpl= input("¿Cuál es la empresa contratista?:")
            supervisor_mpl= input("¿Quién es el supervisor a cargo?:")
            tecnicos_mpl= input("¿Quiénes son los técnicos involucrados en numeros?:")
            inspectores_mpl = input("¿Quién realizó la inspección?:")
            resumen_mpl= input ("Resume la inspección, esto aparecera como el resumen general de la orden en SAP:")
            observacion_mpl= input("¿Se encuentran observaciones adicionales?:")
            print("¡Gracias! Has completado la información para el aviso en SAP.")

            #************************Informe final de orden OM5 MPL******************************
            from textwrap import dedent
            informe_orden_mpl = dedent(f"""\
            Informe de la Orden de Mantenimiento para SAP - MPL
            -----------------------------------
            Semana: {semana_mpl}
            Día: {dia_mpl}
            Fecha: {fecha}
            Hora de inicio: {hora_inicio_mpl}
            Hora de término: {hora_termino_mpl}
            Turno: {turno_mpl}
            Actividad realizada: {manteniminto_mpl} 
            Estación de trabajo: {estacion_mpl} 
            Recinto: {recinto_mpl}
            Equipo(s) involucrado(s): {equipo_mpl}
            Inspector: {inspectores_mpl}
            Empresa contratista: {empresa_mpl}
            Supervisor a cargo: {supervisor_mpl}
            Técnicos involucrados: {tecnicos_mpl}
            Orden de mantenimiento asociada: {orden_mpl}
            ---------Resumen de la Inspección y Mantenimiento---------
            {resumen_mpl}   
            -------------------Observaciones--------------------------
            {observacion_mpl}
            ----------------------------------------------------------
            """)
            print(informe_orden_mpl)

elif seleccion == "1":
    print("Perfecto, vamos a redactar el aviso para SAP.")
    print("Recuerda que debes describir el problema de manera clara y concisa, sin errores ortograficos. Este aviso puede ser para MAC o MPL.")
    estacion_aviso= input("¿Cuál es la estación de trabajo involucrada?:")
    print("Perfecto, la estación es", estacion_aviso)
    equipo_aviso= input ("¿Cuál es el equipo involucrado?:")
    resumen_aviso= input ("Resume el aviso, esto aparecera como el resumen general del aviso en SAP:")
    print("¡Gracias! Has completado la información para el aviso en SAP.")
    print("Resumen del aviso:")
    print("Estación de trabajo:", estacion_aviso)
    print("Resumen del aviso:", resumen_aviso)
    print("Equipo involucrado:", equipo_aviso)
    print("¡Listo para ingresar el aviso en SAP!")

    #*******************Informe final de Aviso IW21******************************
    from textwrap import dedent
    informe_aviso = dedent(f"""\
    Informe del Aviso para SAP
    -----------------------------------
    Estación de trabajo: {estacion_aviso}
    Equipo involucrado: {equipo_aviso}
    ---------Resumen del Aviso---------
    {resumen_aviso}
    ----------------------------------------------------------
    """)
    print(informe_aviso)

else:
    print("Opción no valida. porfavor selecciona una opción valida.")



