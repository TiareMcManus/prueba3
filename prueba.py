import json 

def agregarCategoria( parNombre:int):
    with open ("biblioteca.json", mode= "r") as lecturajson: 
        archivojson = json.load (lecturajson)

        categoria_nueva= {
            "Id": len (archivojson["Autor"]) +1, 
            "Nombre": parNombre,
        

             }
        archivojson["Categoria"].append(categoria_nueva)
    
        with open ("biblioteca.json",mode="w") as escribirjson:
         json.dump(archivojson,escribirjson, indent=4)


def editarCategoria(parId: int):
     with open ("biblioteca.json", mode="r") as lecturajson:
         archivojson= json.load(lecturajson)
         contador= 0

         for i in archivojson ["Categoria"]: 
              if i ["CategoriaID"] ==parId:
                   print ("Lo Encontre") 
                   break 
              contador += 1
              print (contador)

              archivojson["categoria"][contador]["nombre"] = parNombre

              with open ("biblioteca.json", mode= "w") as escribirjson : 
                json.dump(archivojson,escribirjson, indent=4)
                    

def eliminarCategoria(parId: int): 
    with open("biblioteca.json", mode ="r") as lecturajson: 
        archivojson = json.load (lecturajson)
        for categoria in archivojson["Categoria"]: 
            if categoria ["CategoriaID"] == parId: 
                archivojson["Categoria"].remove (categoria)
                print (f"categoria con ID {parId} eliminado")
                break
        else:
            print (f"categoria con ID {parId} no encontrado")

            with open ("biblioteca.json", mode= "w") as escribirjson : 
                json.dump(archivojson,escribirjson, indent=4)

def listarTodasLasCategoria():
     with open("biblioteca.json", mode ="r") as lecturajson: 
        archivojson = json.load (lecturajson)
        print ("CategoriaID               Nombre            ")
        print ("")
        for i in archivojson["Categoria"]:
            print (i["CategoriaID"],"  ", i["Nombre"] )
            
listarTodasLasCategoria()















