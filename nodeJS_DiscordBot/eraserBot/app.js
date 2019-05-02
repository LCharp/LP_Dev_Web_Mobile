// Instanciation des variables constantes
//Appel de l'API
const fs = require("fs")
const Discord = require("discord.js")
const Bot = new Discord.Client()

//Variables de raccourci aux autres fonctionnalités
const Chat = require("../commands/chat")
const Google = require("../commands/google")
const AddChat = require("../commands/addChat")
const Erase = require("../commands/erase")

//Token de l'API
const rawdata = fs.readFileSync("token.json")
const TOKEN = JSON.parse(rawdata)

//  Instanciation variables non constantes
let chatPlay = false
let com = false

//  Vérification connexion du bot
Bot.on("ready", function () {
  console.log("BOT connecté !")
})

//  Message de bienvenue aux nouveaux membres du serveur
Bot.on("guildMemberAdd", function(member){
  member.createDM().then(function (channel){
    return channel.send("Bienvenue sur le channel "+ member.displayName)
  }).catch(console.error)
})

//  Actions du bot lors de la reception d'un message
Bot.on("message", function (msg) {
  //Si le message n'est pas envoyé par un bot
  if(!msg.author.bot){
    //Si la fonction de chat est activée, vérifier si c'est une commande de désactivation de chat, sinon faire discuter le bot.
    if(chatPlay){
      if(Chat.matchLeave(msg)){
        Chat.chatWithBot(msg)
        chatPlay = false
      }else{
        let actionUsed = Chat.action(msg)
      }
    }else{
      //Si la fonction de chat est désactivée, activer la fonction de chat si c'est demandé
      if(Chat.matchJoin(msg)){
        Chat.chatWithBot(msg)
        chatPlay = true
      }else{
        let commandUsed =  Google.parse(msg) || AddChat.parse(msg)
        let commandTmp = !commandUsed
        //Si dans tous les cas ce n'est pas une demande au bot, activer la function d'effacement (erase), car ce message ne doit exister
        if(msg.embeds[0] == null && msg.attachments.get((msg.attachments.firstKey())) == undefined && commandTmp){
			    Erase.deleteYourSoul(msg)
		    }
      }
    }
  } else {
    //Si le message est un message de bot, l'effacer au bout d'une minute
		if(msg.embeds[0] == null && msg.attachments.get((msg.attachments.firstKey())) == undefined){
			msg.delete(60000);
		}
  }
})

//LUCAS WORK : 
// créer une constante channelTextuel vide, que l'utilisateur pourra instancier, afin que le bot ne puisse pas erase
// dans ce chan, et renvoyer les noobs sur ce chan (par message), quand ils écrivent sur le mauvais chan.


Bot.login(TOKEN["Token"])  