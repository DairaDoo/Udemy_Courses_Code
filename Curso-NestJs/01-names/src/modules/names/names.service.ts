import { Body, Injectable, Post } from '@nestjs/common';

// El service es el que se encarga de responder las respuestas GET, POST y etc.
// El servicio se podría decir que se usa para hacer la lógica.

@Injectable() // que algo sea inyectable significa que lo podemos inyectar en otras clases.
export class NamesService { 

    // creamos el atributo names, que será un array de tipo string.
    // el guíon bajo (_) es para decir que es privado (no se puede acceder desde fuera).
    private _names: string[];


    // creamos un constructor vacío que inicializar el array vacío.
    constructor() {
        this._names = [];
    }


    // cuerpo del metodo @Get < createName
    createName(name: string) {

        // asignamos al valor nameFound name, si el nombre, convertido a lower, sacandole los espacios con el trim, es igual al pasado.
        const nameFound = this._names.find(n => n.toLowerCase().trim() == name.toLowerCase().trim());

        // si el nombre encontrado es indefinido, devuelve esto.
        if (!nameFound) {
            this._names.push(name); // agregamos un elemento al array _names
            console.log("Nombre: ", this._names); // mostramos en consola el nombre añadido
            
            return true; // devolvemos true para mostrar que funciono.
        } 

        else {
            return nameFound + " ya se encuentra";
        }
    }

    // metodo get name que recibe como parametro el query start, usando el signo de pregunta para represetar que es opcional.
    getNames(start?: string) { 
        // si no tiene valor (es indefinido)
        if (!start) {
            return this._names;
        } 

        else {
            // el metodo filter te devuelve un array con algo, si no contiene nada, devuelve uno vacio (tiene parecido con el find()).
            return this._names.filter(n => n.toLowerCase().trim().startsWith(start.toLowerCase().trim()));
        }
        
    }

    // Cuerpo del método @Put() updateName
    updateName(name: string, newName: string) {

        // Si el nombre se encuentra devolvera su indice, si no lo encuentra devuelve -1.
        // revisamos que name si exista en la lista (utilizando el parametro name)
        const indexNameFound = this._names.findIndex(n => n.toLowerCase().trim() == name.toLowerCase().trim());

        // revisamos si existe el nuevo nombre no existe en la lista (utilizando el parametro newName)
        const indexNewNameFound = this._names.findIndex(n => n.toLowerCase().trim() == newName.toLowerCase().trim());

        // si el indice es distinto de uno Y el indice del número a agregar es igual a -1, se ejecuta.
        if (indexNameFound != -1 && indexNewNameFound == -1) {
            this._names[indexNameFound] = newName;
            return true;

        } else {
            return false;
        }
    }

    // Cuerpo del metodo @Delete(':/name') deleteName() < usado para borrar un nombre en específico.
    deleteName(name: string) {
        const deletedBefore = this._names.length;
        this._names = this._names.filter(n => n.toLowerCase().trim() != name.toLowerCase().trim());
        const deleteAfter = this._names.length;

        // esta condición revisa que sean distinta la cantidad de elementos y devuelve true or false.
        return deletedBefore != deleteAfter;
    }

    // Cuerpo del metodo @Delete('clear') < usado para borrar todos los elementos de la lista
    clearNames() {
        this._names = [];  // reiniciamos la tabla con cero elementos.
        return true;
    }
}
