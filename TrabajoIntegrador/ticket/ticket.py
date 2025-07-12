import sys, os, random , json

registros = "ticket/registrosTickets.json"

while True:
    menu_opcion_elegida = input("Menu:\n1. Generar un nuevo ticket\n2. Leer un ticket\n3. Salir\nSeleccione: ")
    if menu_opcion_elegida == "1":
        while True:

            ticket = {
                "Nombre": input("Ingrese el nombre: "),
                "Sector": input("Ingrese el sector: "),
                "Asunto": input("Ingrese el asunto: "),
                "Problema": input("Ingrese el problema: "),
                "N Ticket": random.randrange(1000, 9999) 
            }

            # Revisar existencia de tickets ingresados
            if os.path.isfile(registros) and os.path.getsize(registros) > 0:
                with open(registros, "r", encoding="utf-8") as f:
                    tickets = json.load(f)
            else:
                tickets = []

            # Agregar el nuevo ticket a la lista
            tickets.append(ticket)

            # Guardar la lista completa
            with open(registros, "w", encoding="utf-8") as f:
                json.dump(tickets, f, indent=4, ensure_ascii=False)


            formato_ticket = f"""
            ================================================================
                    Se genero el siguiente Ticket
            ================================================================
            Su nombre: {ticket['Nombre']}                 N° Ticket: {ticket['N Ticket']}
            Sector: {ticket['Sector']}
            Asunto: {ticket['Asunto']}

            Mensaje: {ticket['Problema']}
            ================================================================
            """
            print(formato_ticket)
            repetir = input("Desea generar un nuevo Ticket? (s/n): ")

            if repetir == "n":
                break

    elif menu_opcion_elegida == "2":
        while True:
            numero = int(input("Ingrese el número del ticket a buscar: "))
            with open(registros ,"r" , encoding="utf-8") as archivo:
                tickets = json.load(archivo)

                encontrado = []
                for ticket in tickets:
                    if ticket["N Ticket"] == numero:
                        encontrado.append(ticket) 

                if encontrado:
                    for ticket in encontrado:
                        print(f"----- Ticket N°{ticket["N Ticket"]}-----")
                        print(ticket)
                else:
                    print(f"No se encontro ningun ticket con el número {numero}")
                    
            repetir = input("Desea leer otro ticket? (s/n)")
            if repetir == "n":
                break


    elif menu_opcion_elegida == "3":
        confirmar = input("Desea cerrar el programa? (s/n)")
        if confirmar == "s":
            sys.exit()