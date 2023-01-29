import random
import time

rekord_lahko = "ni podatka"
rekord_srednje = "ni podatka"
rekord_tezko = "ni podatka"
rekord_zelo_tezko = "ni podatka"

print("Kako vam je ime?")
ime = input()



def ponovna_igra():
    




    print("Izberite tezavnost igre (lahko/srednje/tezko/zelo tezko/david) ce zelite videti statistiko (statistika)")
    tezavnost = input()

    global rekord_lahko
    global rekord_srednje
    global rekord_tezko
    global rekord_zelo_tezko

    if tezavnost == "lahko":
        stevilo_moznih_ugibanj = 4
        st_tezavnosti = 10

    if tezavnost == "srednje":
        stevilo_moznih_ugibanj = 5
        st_tezavnosti = 20

    if tezavnost == "tezko":
        stevilo_moznih_ugibanj = 6
        st_tezavnosti = 50
    
    if tezavnost == "zelo tezko":
        stevilo_moznih_ugibanj = 7
        st_tezavnosti = 100

    if tezavnost == "david":
        stevilo_moznih_ugibanj = 8
        st_tezavnosti = 1000

    if tezavnost == "statistika":
        print("rekord lahko: ", rekord_lahko)
        print("rekord srednje: ", rekord_srednje)
        print("rekord tezko: ", rekord_tezko)
        print("rekord zelo tezko: ", rekord_zelo_tezko)
        time.sleep(5)
        print("Izberite tezavnost igre (lahko/srednje/tezko/zelo tezko)")
        tezavnost = input()

        if tezavnost == "lahko":
            stevilo_moznih_ugibanj = 4
            st_tezavnosti = 10

        if tezavnost == "srednje":
            stevilo_moznih_ugibanj = 5
            st_tezavnosti = 20

        if tezavnost == "tezko":
            stevilo_moznih_ugibanj = 6
            st_tezavnosti = 50
    
        if tezavnost == "zelo tezko":
            stevilo_moznih_ugibanj = 7
            st_tezavnosti = 100

    

    

    stevilo_ugibanj = 0

    stevilo = random.randint(1, st_tezavnosti)
    print(ime + " ugani število med 1 in " , st_tezavnosti)
    while stevilo_ugibanj < stevilo_moznih_ugibanj:
        time.sleep(0.5)
        ugibanje = input()
        ugibanje = int(ugibanje)

        stevilo_ugibanj += 1

        if ugibanje < stevilo:
            time.sleep(0.2)
            print("premalo")
            print("Imate se " , stevilo_moznih_ugibanj - stevilo_ugibanj , " ugibanj")
    
        if ugibanje > stevilo:
            time.sleep(0.2)
            print("prevec")
            print("Imate se " , stevilo_moznih_ugibanj - stevilo_ugibanj , " ugibanj")

        if tezavnost == "lahko":
            rekord_lahko = stevilo_ugibanj

        if tezavnost == "srednje":
            rekord_srednje = stevilo_ugibanj

        if tezavnost == "tezko":
            rekord_tezko = stevilo_ugibanj

        if tezavnost == "zelo tezko":
            rekord_zelo_tezko = stevilo_ugibanj

        if ugibanje == stevilo:
            print("Bravo " + ime + " uganili ste v " + str(stevilo_ugibanj) + " poskusih")
            se_enkrat = input("Ali bi igrali se enkrat? (da/ne) ")
            if se_enkrat == "da":
                ponovna_igra()
            if se_enkrat == "ne":
                print("hvala za igro!")
                break
        if ugibanje != stevilo and stevilo_ugibanj == stevilo_moznih_ugibanj:
            print("Narobe. " + "Pravilno število je bilo " + str(stevilo))
            se_enkrat = input("Ali bi igrali se enkrat? (da/ne) ")
            if se_enkrat == "da":
                ponovna_igra()
            if se_enkrat == "ne":
                print("hvala za igro!")
                break
            time.sleep(3)
    
ponovna_igra()
 
time.sleep(1)
