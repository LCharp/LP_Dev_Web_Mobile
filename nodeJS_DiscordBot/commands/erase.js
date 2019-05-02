// Classe erase permettant d'effacer un message textuel, en laissant un message d'avertissement sur le canal du message, puis
//avertissant l'auteur du message par message privé.
module.exports = class erase{
	static deleteYourSoul(message){
        //Instanciation des variables
		var theAuthor = message.author.tag
        var theContent = message.content
        var theGuild = message.guild.name
        var theChannel = message.channel.name
        //suppression des messages
        message.delete()
        //ouverture d'un canal de discussion privé, pour envoyer un message d'avertissement directement à l'auteur du message
        message.author.createDM().then(function(channel){
			channel.send(theAuthor+", apprends à jouer noob, tu as fail sur le serveur "+theGuild+", arrête d'écrire sur "+theChannel+", merci.")
        })
        //ajout du message d'avertissement sur le canal de discussion du message
        return message.reply("Je vous présente le noob "+theAuthor+", il n'a écrit que du texte sur ce chan'. Honte à lui.")
	}
}