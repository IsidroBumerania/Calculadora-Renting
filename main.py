#-------- IMPORTS -----------


#---------------------------- Variables -----------------------------

#-------- TRAMOS --------
tramos = [1,2,3,4,5,6]

#-------- Plazos en meses --------------

plazos = [12,24,36,48,60,72]

#--------- Coeficientes ----------------

                #---------- Números de posiciones en lista --------------------------------------

                #--- 0 -------- 1------ 2----------- 3 ----- 4 ----------- 5--------
coeficientes = [0.0937352, 0.0478192, 0.0342056, 0.0266032, 0.0229008, "No hay plazo",

                #--- 6 -------- 7------ 8 ---------- 9 ----- 10 -------- 11------ 12 ------ 13 ----
                0.0229112, 0.0194168, 0.0934232, 0.047632, 0.033904, 0.0263952, 0.022568,  0.01924,

                #--- 14 ----- 15 ----- 16 ------- 17 ----- 18 ------- 19 ----- 20 -------
                0.0933192, 0.04732, 0.033696, 0.026312, 0.02236, 0.0191048, 0.047216,

                #--- 21 ---- 22 ------ 23 ----- 24 -------- 25 -------
                0.033592, 0.026208, 0.022048, 0.0191152, "Consultar"]

#----------- Se crea la variable del coeficiente que será utilizado --------------

coeficiente_final = 0.00


#----------- Se crea la variable del valor_introducido (se resetea el valor) ------------------


valor_introducido = 0.00


#----------- Determinación de tramos ---------------------------------------------------------

#------ Se pide el valor que se ha introducido para determinar en que tramo se encuentra
def determinacion_tramo (valor_intro):

    #--------- Si es menor a 500
    if valor_intro <= 500:
        return tramos[0]

    #--------- Si es mayor de 500 pero menor de 3 mil
    if valor_intro > 500 and valor_intro <= 3000:
        return tramos[1]

    # --------- Si es mayor de 3 mil pero menor de 6 mil
    if valor_intro > 3000 and valor_intro <= 6000:
        return tramos[2]

    # --------- Si es mayor de 6 mil pero menor de 15 mil
    if valor_intro > 6000 and valor_intro <= 15000:
        return tramos[3]

    # --------- Si es mayor de 15 mil pero menor de 50 mil
    if valor_intro > 15000 and valor_intro <= 50000:
        return tramos[4]

    # --------- Si es mayor de 50 mil
    if valor_intro > 50000:
        return tramos[5]


#---------- Determinación de los coeficientes ------------------------------------------------

#--- Se pide el tramo y el plazo seleccionados
def determinacion_coeficiente (tramo, plazo):

#----- Clasificador de coeficientes según el tramo -------------------

    #----------- Tramo 1 ----------------------
    if tramo == 1:

        print(plazos[0])
        if plazo == plazos[0]:
            coeficiente_final = coeficientes[0]
            return  coeficiente_final
        elif plazo == plazos[1]:
            coeficiente_final = coeficientes[1]
            return coeficiente_final
        elif plazo == plazos[2]:
            coeficiente_final = coeficientes[2]
            return coeficiente_final
        elif plazo == plazos[3]:
            coeficiente_final = coeficientes[3]
            return coeficiente_final
        elif plazo == plazos[4]:
            coeficiente_final = coeficientes[4]
            return coeficiente_final

        #------ CASO ESPECIAL QUE DEVUELVE "No hay plazo" -----------
        elif plazo == plazos[5]:
            coeficiente_final = coeficientes[5]
            return coeficiente_final

    # ----------- Tramo 2 ----------------------
    if tramo == 2:
        if plazo == plazos[0]:
            coeficiente_final = coeficientes[0]
            return  coeficiente_final
        elif plazo == plazos[1]:
            coeficiente_final = coeficientes[1]
            return coeficiente_final
        elif plazo == plazos[2]:
            coeficiente_final = coeficientes[2]
            return coeficiente_final
        elif plazo == plazos[3]:
            coeficiente_final = coeficientes[3]
            return coeficiente_final
        elif plazo == plazos[4]:
            coeficiente_final = coeficientes[6]
            return coeficiente_final
        elif plazo == plazos[5]:
            coeficiente_final = coeficientes[7]
            return coeficiente_final

    # ----------- Tramo 3 ----------------------
    if tramo == 3:
        if plazo == plazos[0]:
            coeficiente_final = coeficientes[8]
            return  coeficiente_final
        elif plazo == plazos[1]:
            coeficiente_final = coeficientes[9]
            return coeficiente_final
        elif plazo == plazos[2]:
            coeficiente_final = coeficientes[10]
            return coeficiente_final
        elif plazo == plazos[3]:
            coeficiente_final = coeficientes[11]
            return coeficiente_final
        elif plazo == plazos[4]:
            coeficiente_final = coeficientes[12]
            return coeficiente_final
        elif plazo == plazos[5]:
            coeficiente_final = coeficientes[13]
            return coeficiente_final

    # ----------- Tramo 4 ----------------------
    if tramo == 4:
        if plazo == plazos[0]:
            coeficiente_final = coeficientes[14]
            return  coeficiente_final
        elif plazo == plazos[1]:
            coeficiente_final = coeficientes[15]
            return coeficiente_final
        elif plazo == plazos[2]:
            coeficiente_final = coeficientes[16]
            return coeficiente_final
        elif plazo == plazos[3]:
            coeficiente_final = coeficientes[17]
            return coeficiente_final
        elif plazo == plazos[4]:
            coeficiente_final = coeficientes[18]
            return coeficiente_final
        elif plazo == plazos[5]:
            coeficiente_final = coeficientes[19]
            return coeficiente_final

    # ----------- Tramo 5 ----------------------
    if tramo == 5:
        if plazo == plazos[0]:
            coeficiente_final = coeficientes[14]
            return  coeficiente_final
        elif plazo == plazos[1]:
            coeficiente_final = coeficientes[20]
            return coeficiente_final
        elif plazo == plazos[2]:
            coeficiente_final = coeficientes[21]
            return coeficiente_final
        elif plazo == plazos[3]:
            coeficiente_final = coeficientes[22]
            return coeficiente_final
        elif plazo == plazos[4]:
            coeficiente_final = coeficientes[23]
            return coeficiente_final
        elif plazo == plazos[5]:
            coeficiente_final = coeficientes[24]
            return coeficiente_final

    # ----------- Tramo 6 ----------------------

    #----- CASO ESPECIAL QUE DEVUELVE "CONSULTAR" -------
    if tramo == 6:
        coeficiente_final = coeficientes[25]
        return coeficiente_final

#----------------------------- Calculo de las cuotas SIN IVA ----------------------------------

#----- Se piden el coeficiente determinado y el valor introducido ------
def calculo_renting (coeficiente_determinado, valor_intro):

    #----- Se verifica que el coeficiente no se uno de los dos casos especiales --------
    if not isinstance(coeficiente_determinado, str):

        # ----- Calculo de la cuota SIN iva
        cuota_SIN_iva = coeficiente_determinado * valor_intro

        # ----- Se redondea a 2 decimales
        cuota_total_SIN_iva_redondeada = round(cuota_SIN_iva,2)

        return cuota_total_SIN_iva_redondeada

    else:

        #----- Se devuelve el valor especial del coeficiente en caso especial -------

        return coeficiente_determinado





#-------------------------------------------- MAIN ------------------------------------------------------------
if __name__ == '__main__':

    #-------------- TEST -------------------------------------

    valor_introducido = input("Por favor, ingresa un importe: ")
    valor_intro = float(valor_introducido)

    tramo = determinacion_tramo(valor_intro)

    plazo = input('''Por favor, seleccione la cantidad de cuotas:
    
                    {} cuotas
                    {} cuotas
                    {} cuotas
                    {} cuotas
                    {} cuotas
                    {} cuotas
                    
                    '''.format(plazos[0], plazos[1], plazos[2], plazos[3], plazos[4], plazos[5]))

    plazo_intro = int(plazo)

    coeficiente_final = determinacion_coeficiente(tramo,plazo_intro)


    cuota_total_sin_iva = calculo_renting(coeficiente_final, valor_intro)



    print('''Usted introdujo el valor:  {}
             Cantidad de cuotas seleccionadas: {}
             coeficiente seleccionado: {}
             cuota_total_sin_iva: {}
             '''.format(valor_intro, plazo_intro, coeficiente_final,cuota_total_sin_iva) )