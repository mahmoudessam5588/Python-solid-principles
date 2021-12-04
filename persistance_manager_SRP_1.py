from solid_SRP_0 import Journal


class Persistance_Manager:
    #seperation of concern from solid_srp.py file
    @staticmethod   
    def save_to_file(journal:str,filename:str):
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()
        