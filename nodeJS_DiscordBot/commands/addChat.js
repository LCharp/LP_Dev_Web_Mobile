// Instanciation des variables constantes
//utilisation de chat.json pour les différentes entrées.
const jsonFile = "commands/chat.json"
const fs = require("fs")
const lowerCase = require('lower-case')

//  Classe de chat permettant au bot de discuter avec un utilisateur
module.exports = class addChat{

    static parse(message){
        if(this.match(message)){
            let args = message.content.split(" ")
            args.shift()
            let tmp = args.join(" ")
            args = tmp.split("] [")
            if(args.length == 2 ){
                if(args[0].startsWith("[") && args[1].endsWith("]")){
                    let cle = args[0].slice(1)
                    let val = args[1].slice(0, -1)
                    this.action(message, cle, val)
                    return true
                }else{
                    message.reply("La commande doit contenir deux arguments entre [ ] '!addChat [clé] [valeur]' avec clé le message que le bot devra interpreter et valeur la valeur qu'il retournera après interpretation du message")
                    return true
                }
            }else{
                message.reply("La commande doit contenir deux arguments entre [ ] '!addChat [clé] [valeur]' avec clé le message que le bot devra interpreter et valeur la valeur qu'il retournera après interpretation du message")
                return true
            }
        }
        return false
    }

    static match(message){
        return message.content.startsWith("!addChat")
    }

    static action(message, cle, val){
        message.delete()
        let rawdata = fs.readFileSync("commands/chat.json")
        let res = JSON.parse(rawdata)
        res[cle] = val
        fs.writeFileSync("commands/chat.json", JSON.stringify(res, null, 4))
    }

}