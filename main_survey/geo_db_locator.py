import sqlite3
from . import geodecoder
import time
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "dati.sqlite")

def anagrafe_milano_piu_vicina(address):

    db_connection = sqlite3.connect(db_path)
    lista = db_connection.execute("SELECT titolo, lat, long, indirizzo, tel FROM anagrafe_milano")

    distanza_min = None

    if (lista is None):
        print("Errore db per anagrafe_milano")
    else:
        for anagrafe in lista:
            anag_corrente = (anagrafe[1], anagrafe[2])
            coord_indirizzo = geodecoder.from_address_to_coords(address)
            distanza = geodecoder.meters_from_two_addresses(coord_indirizzo, anag_corrente)
            if (distanza_min is None):
                distanza_min = distanza
            if (distanza<distanza_min):
                distanza_min = distanza
                municipio = anagrafe[0]
                indirizzo_municipio = anagrafe[3]
                tel_municipio = anagrafe[4]

    db_connection.close()

    stringa = "Il municipio più vicino è il {}, in {}, telefono: {}\n".format(municipio, indirizzo_municipio, tel_municipio)

    print(stringa)

    return stringa



def valori_bollati_milano_piu_vicini(address):

    db_connection = sqlite3.connect(db_path)
    lista = db_connection.execute("SELECT nome, lat, long, via, civico, telefono FROM valoribollati_milano")

    distanza_min = None

    if (lista is None):
        print("Errore db per valoribollati_milano")
    else:
        for lottomatica in lista:
            lott_corrente = lottomatica[1], lottomatica[2]
            distanza = geodecoder.meters_from_two_addresses(address, lott_corrente)
            if (distanza_min is None):
                distanza_min = distanza
            if (distanza<distanza_min):
                distanza_min = distanza
                lottomatica_selezionata = lottomatica[0]
                indirizzo_lottomatica = str(lottomatica[3])+", "+str(lottomatica[4])
                tel_lottomatica = lottomatica[5]

    db_connection.close()

    stringa = "Puoi acquistare la marca da bollo presso {}, in {}, telefono: {}\n".format(lottomatica_selezionata, indirizzo_lottomatica, tel_lottomatica)

    print(stringa)

    return stringa



def idoneita_abitativa_vicina_milano(address):

    db_connection = sqlite3.connect(db_path)
    lista = db_connection.execute("SELECT municipio, indirizzo, servizio, giorni_e_ore, tel FROM idoneitaabitativa_milano")
    servizio_ufficio = ""
    num_ufficio = ""
    indirizzo_ufficio = ""
    aperture_ufficio = ""
    tel_ufficio = ""
    distanza_min = None

    if (lista is None):
        print("Errore db per idoneitaabitativa_milano")
    else:
        for ufficio in lista:
            temp_addr = ufficio[1]
            stringa_ind_ufficio = "milano, {}".format(temp_addr)
            coord_indirizzo = geodecoder.from_address_to_coords(address)
            coord_ufficio = geodecoder.from_address_to_coords(stringa_ind_ufficio)
            distanza = geodecoder.meters_from_two_addresses((coord_indirizzo),( coord_ufficio))
            if distanza_min is None:
                distanza_min = distanza
            if (distanza<distanza_min):
                distanza_min = distanza
                num_ufficio = ufficio[0]
                indirizzo_ufficio = ufficio[1]
                servizio_ufficio = ufficio[2]
                aperture_ufficio = ufficio[3]
                tel_ufficio = ufficio[4]

    db_connection.close()

    stringa = "puoi recarti presso {} del Municipio {}, in {}, aperto {}, telefono: {}\n".format(servizio_ufficio, num_ufficio, indirizzo_ufficio, aperture_ufficio, tel_ufficio)

    print(stringa)

    return stringa


def info_ambasciata(paese):
    db_connection = sqlite3.connect(db_path)
    info = db_connection.execute("SELECT sede, indirizzo, telefonisedi, faxsedi, sitoweb, email FROM ambasciate WHERE paese = ?",(paese.upper(),))
    output = list(info.fetchone())
    for elem in info:
        output.append(elem)
    print(output)
    return output



def info_consolato(paese):
    db_connection = sqlite3.connect(db_path)
    info = db_connection.execute("SELECT sede, indirizzo, telefonisedi, faxsedi, sitoweb, email FROM consolati WHERE paese = ?",(paese.upper(),))
    output = list(info.fetchone())
    for elem in info:
        output.append(elem)
    print(output)
    return output


def sindacati_e_patronati(address):

    db_connection = sqlite3.connect(db_path)
    lista = db_connection.execute("SELECT ufficio, indirizzo, telefono FROM sindacatipatronati WHERE citta=?",("MILANO",))

    distanza_min = None

    if (lista is None):
        print("Errore db per idoneitaabitativa_milano")
    else:
        for sindacato_temp in lista:
            temp_addr = sindacato_temp[1]
            stringa_ind_ufficio = "milano, {}".format(temp_addr)
            coord_sindacato = geodecoder.from_address_to_coords(stringa_ind_ufficio)
            coord_indirizzo = geodecoder.from_address_to_coords(address)
            try:
                distanza = geodecoder.meters_from_two_addresses((coord_indirizzo),(coord_sindacato))
                if distanza_min is None:
                    distanza_min = distanza
                if (distanza<distanza_min):
                    distanza_min = distanza
                    nome_ufficio = sindacato_temp[0]
                    indirizzo_ufficio = sindacato_temp[1]
                    tel_ufficio = sindacato_temp[2]
            except ValueError:
                print("Errore parsing indirizzo, saltato..")

    db_connection.close()

    stringa = "\n{},\nindirizzo: {},\ntelefono: {}\n".format(nome_ufficio, indirizzo_ufficio, tel_ufficio)

    print(stringa)

    return stringa






if __name__ == '__main__':
    main()
