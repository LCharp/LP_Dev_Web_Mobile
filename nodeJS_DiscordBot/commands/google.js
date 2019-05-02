// Instanciation des variables constantes
//Variable de raccourci à la fonctionnalité command
const Command = require("./command")

// Classe google permettant d'effectuer une recherche google à partir de la commande !google
module.exports = class google extends Command{

    //Fonction de vérification du message entrant
    static match(message){
        return message.content.startsWith("!google")
    }

    //Fonction d'envoi de la recherche google
    static action(message){
        let args = message.content.split(" ")
        args.shift()
        message.delete()
        message.reply("https://www.google.fr/#q=" + args.join("%20"))
    }

}