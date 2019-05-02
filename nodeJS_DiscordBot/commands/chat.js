// Instanciation des variables constantes
//utilisation de chat.json pour les différentes entrées.
const jsonFile = "commands/chat.json"
const fs = require("fs")
const lowerCase = require('lower-case')

// Classe de chat permettant au bot d'activer sa fonction de chat ou non
module.exports = class chat{

    static matchJoin(message){
        return message.content.startsWith("!jc")
    }

    static matchLeave(message){
        return message.content.startsWith("!lc")
    }
    
    static action(message){
            let rawdata = fs.readFileSync(jsonFile)
            let res = JSON.parse(rawdata)
            if(res[lowerCase(message)] != undefined){
                message.reply(res[lowerCase(message)])
            }else{
                var traitement = true
                var tmp = message.content.split(" ")
                var len = tmp.length - 1
                tmp.pop()
                var msg = tmp.join(" ") 
                while(len > 0 && traitement){
                    if(res[lowerCase(msg)] != undefined){
                        traitement = false
                        message.reply(res[lowerCase(msg)])
                    }else{
                        tmp = msg.split(" ")
                        tmp.pop()
                        msg = tmp.join(" ")
                    }
                    len = len-1
                }
                msg = message.content.split(" ")
                var len2 = msg.length
                if(len == 0 && traitement){
                    if(len2 >= 2){
                        var j = 0
                        while(j < len2-1 && traitement){
                            if(res[lowerCase(msg[j])+" "+lowerCase(msg[j+1])] != undefined){
                                traitement = false
                                message.reply(res[lowerCase(msg[j])+" "+lowerCase(msg[j+1])])
                            }else{
                                j++
                            }
                        }
                    }
                }
                if(len == 0 && traitement){
                    var i = 0
                    while( i < len2 && traitement){
                        if(res[lowerCase(msg[i])] != undefined){
                            traitement = false
                            message.reply(res[lowerCase(msg[i])])
                        }else{
                            i++
                        }
                    }
                }
                if(len == 0 && res[lowerCase(message)] == undefined && traitement ){
                    message.reply(res["!default"])
                }
            }

    }

    static chatWithBot(message){
        message.delete()
        if(message.content.startsWith("!jc")){
            message.reply("Chat bot join da way !")
            message.reply("Chat bot can read da way whitout '!jc'")
            message.reply("Chat bot can leave da way whit '!lc'")
        }
        if(message.content.startsWith("!lc")){
            message.reply("Chat bot leave da way !")
            message.reply("Chat bot can join da way with '!jc'")
        }
    }
}