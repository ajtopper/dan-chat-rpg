import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
import os
import yaml


 # METODO CARREGANDO KEY PELO YAML
#with open('config.yaml', 'r') as config_file:
#    config = yaml.safe_load(config_file)
#os.environ['OPENAI_API_KEY'] = config['OPENAI_API_KEY']


# METODO PARA VALIDAR A CHAVE E NAO EXPOR
# Configurando a chave da API do OpenAI via st.secrets
os.environ['OPENAI_API_KEY'] = st.secrets['OPENAI_API_KEY']


if "OPENAI_API_KEY" in st.secrets and isinstance(st.secrets["OPENAI_API_KEY"], str):
    st.write("Chave encontrada e válida.")
else:
    st.error("Chave OPENAI_API_KEY ausente ou inválida. Verifique o arquivo secrets.toml.")


# Método para o user inserir a key
#with st.sidebar:
#    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
#    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"

#if not openai_api_key:
#    st.error("Please add your OpenAI API key to continue.")
#     st.stop()


# Inicializando o cliente OpenAI com try
#try:
#    openai = ChatOpenAI(
#        api_key=st.secrets["OPENAI_API_KEY"],
#        model_name='gpt-3.5-turbo',
#        temperature=0
#    )
#    st.success("ChatOpenAI inicializado com sucesso!")
#except Exception as e:
#    st.error(f"Erro ao inicializar ChatOpenAI: {e}")
    
    
    # Inicializando o cliente DeepSeek com try
try:
    openai = ChatOpenAI(
        api_key=st.secrets["OPENAI_API_KEY"],
        base_url="https://api.deepseek.com",
        temperature=0
    )
    st.success("DeepSeek inicializado com sucesso!")
except Exception as e:
    st.error(f"Erro ao inicializar DeepSeek: {e}")
    
    response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"},
    ],
    stream=False
)



template = '''
Você é um escritor de aventuras de RPG.
Escreva um relatório de aventura de RPG detalhado levando em consideração o gênero "{genero}" para uma mesa na temática {tema} para uma mesa com {jogador} jogadores.

O relatório dever ser sempre escrito em {idioma} e incluir a seguinte análise:

Qual bundles da Loot Studios são melhores para jogar determinada aventura? 
Evite ao máximo misturar bundles que não tem simalaridade entre si, porque senão a história ficará desconexa.

Traga um resultado total de 3 sugestões de bundles.
Traga um resumo dos Bundles escolhidas na sua análise e traga como o DM pode criar ganchos relacionados a cada bundle. 
Além disso leve em consideração que a mesa possui {jogador} jogadores.
Dê no mínimo 5 sugestões de ganchos para o DM.

Certifique-se de fornecer insights e conclusões para esta seção.


---------------------------------------------------------------------------------------

Pacotes de bundles da Loot com descrição se restrinja a somente esse conteúdo para embasar os bundles sugeridos:


 Forgotten Beasts
Doomsday Has Claws and Fangs!
In a strange, different reality, where the moon intercepted the gigantic meteor that would bring extinction to all dinosaurs, sentience was attained not by mankind, but rather, by a peculiar kind of reptiles. Their civilization spans all over the world, with a bellicose, and reckless culture. However, all is about to change, for the alignment of the planets is changing the behavior of all the fauna in the world, creating murderous monsters from once peaceful dinos! Now, it's do or die, and the Saurinax will meet this foretold doom with a weapon in hand, and a smile on the face!


Rise of Draconians
The glorious comeback of the Dragon Empress
Centuries ago, the Dragon Empress was sealed away by a group of heroes who used the power of the Orb of Dragonkind. The power of the orb has waned now, and those heroes are long gone. Her followers are finally ready to reconquer the land of Shaldrak. However, one of her dragon knights decided her actions were beyond any reasonable excuse and fled from the army, searching for souls brave enough to stand against certain doom. Who will answer the call for adventure? Who will choose to face the Empress against all odds? Who will save the land of Shaldrak from the Rise of Draconians?


Cryo Hazard
The alien horror is about to begin
One of the Pitblazers spaceships ended up crash landing in a world known as Hellplanet Typhoon, an inhospitable place barely unexplored by humanity. Once the crew awoke from cryosleep and identified where they were, they made a plan to keep themselves safe and broadcast a message asking for help. While setting this plan in motion, the Pitblazers crew realized they weren’t alone in the icy landscapes of Hellplanet Typhoon. Unfortunately, they only realized the unknown presence when an alien entity was already attacking their numbers.


Arthurian Tales
A tale retold!
Valorous knights from ancient tales gather to protect Albion from a winged tempest that threatens to destroy it. Relive and experience the beloved tales of the Knights of the Round Table, as well as the mythological creatures and fantastical artifacts that permeate the Arthurian mythos. Fight alongside Arthur against the traitorous Mordred, seek the counseling of the wizards Merlin and Nimue, outlast the invasion of Galehaut, hunt the Questing Beast, or quest for the Holy Grail alongside Galahad and Dindrane. Camelot awaits!


Bump in the Night
It's Time For a Killing Show!
Dear spectator, the time is right for a truly marvelous show! Sit back and relax, as you watch the Survivors try and outlast the murderous beings that I'll throw at them. Be it brute or rogue, flesh amalgam, or incorporeal shade, the Scream Team will haunt the rooms of the Ghastly Cabin while hunting their prey. Oh, but don't take me for a mere sadist, my dear! Each one of them can be defeated by the Survivors, should their wit guide them towards such knowledge. But hush now, my dear! The lights are dim, and the cinema's screen is lit by the projector. Let us watch a spectacle.


Abyssal Haze
Everything will turn into void when the haze comes
The city of Azmar was known to be a sanctuary, a place to help those in need, all thanks to the Chantry of Healing. Unknowingly, Lord Gaspard let loose the essence of the void, manifesting itself in a sickening haze that took over Azmar and nearby lands. The void couldn’t be controlled and, with the passing years, the abyssal haze began to spread itself further across the realm, infecting even more people. Many heroes tried to stop it and failed, but a group of hunters decided to give one last shot before everything is lost to the void.


Tysect Wars
The War Isn't Over
Pitblazer, the Authority has been lying to you! The situation on Erca is way worse than what they've briefed us for. With each passing day, the Tysects deploy new monstrous evolutions to destroy our troops. Worse still, some say they might even be following a higher form of conscience, as their tactics are nothing short of genius. There is, however, hope. I've managed to find an entrance that leads directly into the Heart of the Hive, whose destruction might finally put an end to this menace. Lock N' load, Pitblazer, we're going deep into the hive. For humanity!


Mystery in Panshaw
In a city of doppelgangers, who can you trust?
The Thieves’ Guild is causing chaos and mayhem. Rumors say they are able to get away with it by using doppelgangers as their agents and even the city guard is said to have been infiltrated. Magistrate Vurneg has hired a group of adventurers, rusted heroes of Panshaw who were away on a mission when the trouble started. The group needs to retrieve a magical artifact, the Gateway of Ahzora, to get a lead of where the Thieves’ Guild hideout and then defeat its leader, Cole Nightshade. However, not only are the thieves aware of their movements, but the City Guard is also on their heels.


Pitblazers Unleashed
Give 'em Hell!
Commander, The Authority need you to bring the light of freedom to the massive jungle planet of Erca, whose monstrous bug-like inhabitants don't seem to understand our right to take their bountiful world for ourselves. According to our reconnaissance teams, the resources present there will provide for our brethren's colonies for many decades. To subdue the creatures who stand in our path, thousands of Pitblazers will rain down fire and bullets in the name of freedom! Lock and load, check your Voxcomm, and command your troops toward victory!

Chaos in Haydale
A bloody ritual brings forth a terrible creature
The people of Panshaw knew there was something seriously wrong when shipments stopped arriving from Haydale, the southern settlement that feeds most of the region. When the city’s taverns started running dangerously low on ale, people started to worry. Rumors spread quickly but before panic sets in a group of adventurers is sent to investigate and report back. After a week’s journey, the heroes make their way to Haydale, only to discover that the village has been run over by Hobgoblins!


Clockwork Skyline
Metal and Flesh Clashes!
The megacity of Skyline used to be a utopia of flesh and metal, where mankind lived peacefully through the work of their creations. Now, the scales have turned. As the Avatar of Illumination seizes the reigns of the city, declaring martial law, automatons begin to oppress the people they once served. The time has come for brave rebels to stand their ground and strike against the heart of corruption, either uncovering the truth behind the Avatar's facade and saving the city, or dying trying.


The Undercaves
Monster crawl in the shadows of the Undercaves
When the Mindbreaker of the Cthulhufolk made his way to the Undercaves, the fragile peace was shattered. Most of the people perished in a deadly monstrous feast. However, even in this grim scenario, there is still hope. The few survivors left aside their differences to create a fragile alliance. Time is short because the Mindbreaker has achieved a terrifying feat: through psionic might he has the Ancient Rock Worm, the most feared creature from the Undercaves, under his control. Who will rise victorious, the mighty heroes or the monsters controlled by the Mindbreaker?


Primal Crisis
It’s the Past All Over Again!
The future is bright, for Wells Corp has created a space portal! Of sorts... Some unexpected results have happened on the island's test site, and monstrous creatures from Earth's ancient past now roam free, wreaking havoc and threatening to expose the corporation. To prevent such a scenario, the Desperate Measures were created, and a team of scientists and mercs were set to stop the chaotic machine and reclaim its blueprint. The machine, however, has given way to strange hominids, raising questions about the tech's true purposes. Alliances will be made, as unlikely heroes venture into the past to save the future!



Faewood Haven
A Wise Trunk Flower Pot
You don't need to tell anyone of your love for the fey if your plants grow like magic in a highly detailed Faewood flower pot. Show everyone you are a true defender of the little folk by 3D printing and painting this unique prop and home decor, the perfect vase to exhibit your gardening skills to all your friends!


Metal Maelstrom
Behold the era of the Blessed Ones!
In a devastated Earth, the Motor Gangs have fought for territory and resources for many decades. After a Kapillian spaceship falls into Wargod Tom’s territory, his gang takes over the alien cutting-edge technology. These new tools give life to the Wargod’s greatest desire: taking over all the scrub territory and becoming the ultimate leader. His new technology gave him the power to exterminate many of his enemies, however, people who already tasted the Wargod’s cruelty are willing to do anything to stop this explosive madness. Will their determination be enough to stop Wargod Tom’s savagery?



Scarlet Requiem
The Erntefest approaches, and Baron Voyd has set all the pieces in place
Inside the tomb-land of Rabennar, caravans and travelers venturing through the dark woods claim to have survived attacks by fanged people, surveying the land in search of something, leaving a trail of bodies in their wake, ever closer to human settlements. All the while, atop the Manor of Night, a shadowless figure watches from above, plotting. Still, a party of heroes arrives, defying the odds, eager to stand where many fell. The cards of the fortune tellers are set, but destiny is yet to be shaped by those who venture into darkness.


Horrors From Beyond
Welcome to Uncanny Valley
The cult of the Elder One lurks in the dark alleys of Uncanny Valley. For decades, Professor Murray kept the Elder Tome safe in his house… Until a group of children decides to use it as a Monster Guide to play their homebrew game of Catacombs & Cryptids. Unknowingly, the children release the servants of the Elder One into their town, and one of them unlocks eldritch powers she can barely control. Since none of the adults can be trusted, the children decide to take matters into their own hands and save Uncanny Valley themselves.


Phoenix Forge
Solaris' flames bring life and death to the Forge
Sudden accidents began to bring chaos to the Phoenix Forge. The leader of the Lavashaper dwarven clan, Durgon, claims everything is under control, but the kingdoms will not take him at his word. If the constructs continue to rampage, many more will die, but the Lavashapers refuse to reveal the secret workings of their machines. Amidst all the chaos, a group of heroes has decided to infiltrate the Phoenix Forge in search of answers. Will they find the truth about the Phoenix’s power, or will they face a gruesome death in the depths of the Forge?



Neon Shadows
The criminal underworld is coming out of the Shadows!
It's been several years now since the Vespilliacci Crime Family and the local yakuza chapter, the Sakura Clan, took over all crime in the city in a single night of bloodshed. They have rulled the underground together in an uneasy alliance, while the rest of the criminal elements have survived on the scraps the two crime syndicates leave on the table. But things have changed now, as a vulnerability presents itself at the Nodakys hotel and every low life in the city makes a play to exploit it. Who will come out on top as the underworld comes out of the shadows?


Reign of the Coldheart
A blizzard is coming
Surrounded by the tallest peaks, in the far kingdom of Ellendran, Zendel Coldheart, the Ice Queen, rules her domain with an iron fist. With her ice powers and her alliance with Hoarfrost, the Albino Dragon, she has created an eternal blizzard in the region that traps everything in ice that will never melt. The ones who are unlucky enough to live in Ellendran will do anything in their power to survive, and many make offerings in exchange for their lives. And yet somehow, the freezing nightmare is getting worse. The unnatural ice which plagues Ellendran is spreading across the land, and will soon reach many other villages beyond the mountains. In an attempt to stop this chaos, a group of heroes decided to bring an end to the eternal blizzard of the Ice Queen. Will they succeed and allow a new future to rise from the snow, or will they end up buried under it?


Planet of the Beasts
Cyberpug's Legacy awaits!
Cyberpug has been saving people and fighting injustice and tyranny for a long time, but he can't be everywhere at once. Good thing he had a couple of kids who could take up the torch and carry on the fight. Warpug has been leading the Liberty Brigade since his dad went of to save the galaxy and has been doing a crack job, freeing the enhanced animals from the clutch Royal Enterprises. Unfortunately some of his pals don't think "pacific resistance" is enough, and are trying to free the Cyberleviathan to wreak havoc on the human cities. Will Warpug be able to stop them, like his father would?


Curse of the Witchmire
Many lost their souls to the witch's curse
Greenvale used to be a peaceful town, until Agasyl, a malefic witch, began to put everyone’s safety in search of eternal life. House Gneeve banished Agasyl to the Witchmire Swamp, in hopes the witch would find her inevitable death. Agasyl not only survived but drew power from the curse and tamed the Cursed Giant. Yielding the foul magic from the Witchmire Swamp, Agasyl cursed whoever crossed her way. The heroes know they won’t find freedom while Agasyl keeps terrorizing innocents. Will they be able to end the horror who commands the Witchmire Swamp, or will they get crushed by the curse?



Starblade Chronicles
Beware the Forgotten Empress
The Wave, a matter from which all things are made, sings in unison. “Beware the Forgotten Empress, for we see the signs which foretell of her return.” The Empress was a powerful force that conquered and divided the galaxy thousands of years in the past, and her return could herald the coming of a great conflict. Now the race is on, the Order of Knight Supplicants rushes to stop her return, the Cliffants bring their armies to welcome their founder into a new age, and a crew of opportunistic scoundrels wants to offer their services to whoever will fill their pockets with the most Chalk.



Orcs of Butcherhold
Nobody is safe from the Nightstalker clan
The orc Ygash hungered for more power. In her journey to strengthen the clan, she defeated a giant and consumed his body and his power, becoming a giant herself. Ygash’s greed also grew to giant size, and her tactics became more aggressive. She and her clan went from town to town, threatening the population. There must be an end to this bloodshed. Heroes have risen to face the threat, but how will they bring this menace to an end? Will they have to end every single orc in the clan, or will they be able to change the orc’s mind and turn them all against Ygash?


The Titanomecha
A battle to decide Humanity's fate
For the last 80 year, the Titans have been all that matters. Thunderjaw were our response to their invasion, they are the pinnacle of our war machines, designed to be a match for the Titans. Our victories allowed humanity to live some good decades since, but in our hubris we've allowed ourselves to let our guard down, believing to be invincible. Now, the whole Earth is shaking again. The oceans part for another ascention, a final ascention with Titans larger than we've ever faced before coming to wipe us out. We can only hope that the Thunderjaw we have will be strong enough to take them down.



Flames of Wrath
War never changes and it may never end
Eve Fargrace has been through a lot to get here and is at the cusp of freeing herself from the Land of Sins, but this may be the worst of the realms yet. In the Warfields of Wrath angels and demons fight in an endless war for control of a powerful artifact that could break the stalemate and bring an end to this war, and these otherworldly beings will not hesitate to use the mortals who find themselves in this realm to tip the balance and achieve their goals. Only true heroes can see that things have gone too far and that the innocent will continue to suffer, unless someone breaks the cycle.




Z Outbreak Survivors
he Zombies are coming
No one expected Frank to die. We have no time for mourning though, the virus got to him and he returned as a Mastermind Infected bringing the horde with him to take us down. He's down there now, hundreds of zombies with him, some are special infected we've never even faced before, but he's a fool if he thinks we're doing down easy. Get ready Frank, if you're even in there anymore, we've got guns, traps and we're not pulling any stops. We'll be the ones surviving this attack.



Carnival of Lust
The Show Must Go On
The Death’s Whisper would never be the same again, but at least the survivors weren’t in danger anymore. After defeating the Ruling Sin of Envy, Eve set out to find a way forward. While searching through Irinia’s treasure she found a curious invitation from another of the sins, along with Tickets to the Carnival of Lust.

Instead of being hunted down by demons, Eve was greeted and well-received by the Ruling Sins of Lust, charming fiends as she had never met before. She wasn’t naive, Eve knew very well there is no free lunch with demons, but people seemed to have so much fun that she gave it a go, performing with her lute in front of such a warm audience… She never felt more welcomed in her life, so why not enjoy it a little more?
Many mortals end up drowned by the Carnival’s charms and their attractions, which makes any other entertainment savorless in comparison. Knife throwing, fire breathing, duels to the death… Each one of the acts is more dangerous than the last, and they often lead to someones death. It’s all part of the show, the sinners love the applause, even if it comes at the cost of their lives.

That’s just how the Carnival works, alluring people’s most narcissistic side and keeping them inebriated by ceaseless joy. However, how long can this bliss last before one is entirely consumed by the Ruling Sins of Lust?



Dino Doomsday
The Dinos have gone feral!
Constructed in the far future by the New Land Foundation Caretakers, the Yardblue is the park where all types of dinosaurs are studied to further humanity's knowledge about this great beast. Nathaniel Munde has a different vision for the park, however, and after he seized control of it, he has been trying to turn it into a theme park to be visited through the eyes of his Tourist Proxy. Now the Dinos have gone feral and only the Caretakers can stop them from harming themselves and everyone in the park.


Envious Tempest
Yo ho, yo ho, here comes the green tempest...
"Which sailor never heard about the Bottomless Sea? This mythical and dangerous place, surrounded by storms, from where only madmen have ever come back. Many say there is a powerful siren who rules these waters, the Ruling Sin of Envy Irinia, and the many sea creatures who obey her commands…

Captain Imor Jones dragged his crew in a suicidal journey to capture the Monstrous Serpent, but Irinia’s whispers made the crew turn against itself. Trapped alongside the only three crewmates still alive in the Death’s Whisper, Eve needs to find a way out yet again. "



Thundercoil Cities
As the Thundercoil Cities are gearing up for civil war, Katlin Dove, A-City Mayor's betrothed, has been captured by the horrible Dr. Alvus Wattson and his mob of reanimated thugs. Now Joules Voltamp, the genius scientist behind the Thundercoil Renaissance, will have to gather a team of specialists aboard the Daring Dove airship to go on a rescue mission to the wartorn streets of D-City. Little does he know, however, that Alvus plans to capture him and unleash his newest creation on the world, a reanimated flesh monstrosity who is ready to fight.


Voracious Sands
The winds of this desert carry the stench of death
"In the Ravenous Wastes, everything is food for Vorax. Eve finds herself in a new realm in the Land of Sins.The heirs to the great city Qarean wish to conquer their land back, following the orders of Sand King Antares. His followers believe Antares will defeat Vorax and set them free.

Eve learns about an old tale that might be just what she needs: an efreeti sorcerer capable of granting her heart’s desire. But every wish requires payment in something equivalent, a sacrifice consumed by fire.
And what better offering to the flames than the body of a Ruling Sin?"


Crimson Protocol
Vampires, werewolves and genetic experiments
The underworld of the city of Baygrave hides more than common criminals, it hides vampires and werewolves. To make things worse, a war is brewing between the two genetically modified factions that prowl in the shadows, Count Crimson controls his New Vampiric Court to recover the power he once had, while the Lycans follow Dominic Arcon in the path to destroy their mortal enemies.

The city's last hope has come in the form of three hunters who have been called in as a part of the Crimson Protocol and will stop at nothing to end the battle between the two factions.




Curse of Torpor
Dark nightmares are on the prowl
The underground of the Land of Sins is Desidia’s domain, the Ruling Sin of Sloth. This powerful fiend keeps all the mortals in her realm under the Curse of Torpor, a hex that keeps all sinners trapped in a devilish plane of horrors. Eve finds herself in this endless nightmare. Before being attacked by a nightmare monster, a group of rebel heroes saves her. They want to be free from the Dreamlands. To succeed on this path, and advance on her objective, Eve must defeat not only the worst nightmares from the depths of the sinners' minds, but also the Cult of Slumber.


Pact of Greed
Beware devils and their bargains
"Within the Plains of Endless Greed, very few are innocent. Here, cities crawl and devour each other, Emoria is being destroyed by the sibling's greed, and Avaritium, the Ruling Sin of Greed, is well on his way to mold the Plains of Endless Greed into the biggest realm in the Lands of Sins.

Amongst such disasters, no one has ever left these lands. But Eve Fargrace, in her quest to write the Song of Sins, is willing to try. Will the civil war in Emoria make the city succumb before Eve has her chance to free herself?"


Flaying Sands
A desert wasteland abandoned by the galaxy
After Faetor’s Doom, many people tried to escape Noubos, but not many found a way. The Doom infested the land with deadly radioactivity, that spread in the form of storms, known as Flaying Sands. Every village in Noubos has a sealed basement, in case a sandstorm rises in the horizon. Unfortunately, for the people of Noubos, this is not the only danger around. Faetor might have crumbled down, but it still exists beneath the sands, as a memorial to its own former glory. There, the AI still lives, protected by the Cult of Faetor.


Mark of the Hunter
Time to take a planet from the aliens, by any means necessary
The first encounter between the humans and the Vrak’thal was disastrous. Many were wounded or killed, leaving only a handful of survivors. Among them was Rambold Patton, a brave and resourceful military officer. He was able to inform the human HQ of what had happened and ask for support. Rambold’s plea was disregarded, as the leaders of the human race decided against escalating the conflict with the Vrak’thal. Hearing of what had transpired, Commander Patton, Rambold’s brother, couldn’t just let it be. He gathered his squad of elite soldiers and went after his brother.


Roar of the Everdeath
A dracolich roars and the dead rise
Sunathaer Caex’s final moment was facing the Triumvirate of Undeath, the trio of liches led by Vox’shax, the Everdeath. Archmage Savros had tricked all three and recruited Sunathaer Caex on the quest to end them before they could regenerate. Caex fell in battle against Vox’shax, as many adventurers have before, but only due to Savros’ betrayal.

Though the mission wasn’t a complete success, Kuat’ze and Barator would both regenerate at the same place as Vox’shax, creating the perfect opportunity to end the Triumvirate of Undeath once and for all. Now, new heroes will end what Sunathaer started.



Deep Space Madness
These aliens and their mad science need to burn, burn, burn!
Six weeks ago AlphaC-1, the research station in orbit of Proxima Centauri b, missed one of its scheduled data burst transmissions. The last transmissions received indicated no issues with the station itself or its personnel. Due to the sensitive nature of the research being conducted at AlphaC-1 and its importance to our government, the Gamma Squad be dispatched quickly, and rescue the head of research, Dr. Alvarez. Little do they know, however, the foes inside are the Shadowclaw, a treat larger than they have ever faced before.


Tales of Ryuboken
In a land far to the east, the sun rises!
A long time ago, onis plagued the land. Brave heroes climbed the mountain summit to meet the divine dragon, ZhongTian, and bring balance to their world, shutting the onis and evil spirits in their own realm. Peace reigned for hundreds of years, but now balance was disturbed once more and the dark spirits have returned. A pilgrimage to the mountain summit was needed, in order to appease the divine dragon. The trail will present our heroes with many trials, but this time they will find that appeasing ZhongTian will be the greatest of them all…


The Wild Frontier
Cowboys, gunslingers and terraformers
The fringes of humanity hold infinite possibilities, both good and bad. Regular folks fear this, for they cannot bear the thought of losing what they’ve already got and starting anew. Some people are wired differently, though. Their greed sees only the upside. A brave few have ventured beyond the edge of civilization to terraform Kepler-16785d. An intergalactic crisis led to a shortage of capital and supplies. Society has declined and the Terraworm have gone berserk, and they are about to level the last pocket of humanity on the planet.


Cursed Collector’s Curiosities
Behold, the menacing menagerie of monsters!
The retired monster hunter and collector Dr. Anderson has emitted a sending asking for help and warning of danger. The Wardens promptly sent their best squad available to take care of the matter, but when the party arrives at the scene they get trapped inside the tower's forcefield, a mechanism designed to keep the danger in, not out. Now they must go deeper into the mage’s tower, and discover which creature in the menagerie is the source of trouble. Could it be the doctor's prized protodragon? One thing is for sure though, many sounds can be heard, but none of them seem friendly.


Highway Slicers
Badass biker gangs take to the road one last time
The “Four Riders” successfully robbed over a billion dollars in their prime. However, their leader was killed, and with him went part of the secret code to find the money. The remaining three split up, suspicious of each other. Each of them now leads their own gang: the Wild Riders, Cyberbreath, and Leather Rebels. Years passed, and the broken trust was never mended. But now, things are different. The missing code was broadcast to them, and the missing fortune could finally be retrieved. Who could have sent the code? There’s no time to investigate; the race is on for their long-lost fortune!



Loxwort Academy
Magic, wonder, and a murderer on the loose
Loxwort Academy is the place where the brightest minds go to study magic under the tutelage of masters of magical crafts. However, when someone attempts to murder the school's headmaster, everyone becomes a suspect. Could it have been the professors vying to get his position? Or maybe the daring students trying to prove themselves capable? How do the draconic scales found in the crime scene tie into all of this? Alas, there is much to discover and it's up to our adventurers to investigate the mystery before the assassin comes back to finish what he started.



Ultimate Battle Machina
2 robots go in, 1 robot gets out!
Welcome to the 247th edition of the Ultimate Battle Machina, the greatest sporting event of all time! Combatants from all over the world face each other to find out who is the Ultimate Battle Machina. There will be sweat, tears, and oil flying about! Retired fighters return to fight new blood; sentient machines fight actual pilots in the flesh; even the military is coming out to show off their new tech! Tonight, you will witness one of the greatest editions of the UBM to this day. So get ready to fight.


Tenebris Infested
A new threat emerges from the Underworld
Tenebris' caves used to be a peaceful place, but that hasn’t been true for some time. The “children of Tithonus” have spread their poisonous taint and have almost dominated the vast underground. Now the titholoths have started venturing outside their caves and desperate nations have come together to offer rewards to whoever can defeat their queen. An unlikely group of heroes has joined forces, and if they’re able to partner with the natives of Tenebris, which include the durks, hags, and even a dragon, perhaps they’ll stand a chance!


Viva Los Loots
The craziest sci-fi heist you have ever seen
Los Loots is a land of wealth and status, of greed and violence. It is only fitting they would gather here for the Grand Gambling Series, at the The Silk Clover Resort and Casino. The players who come here want to show their influence, they come for an opportunity to display their resources, to casually bet small fortunes. It would be the perfect place for a grand heist if it wasn’t for the dangerous competitors. Still, that doesn’t preclude people from trying. There’s a daring group of thieves who have infiltrated the event. Will they succeed?


Lair of Liars
Sharp smiles and sharper blades
Have you heard about the Two-Faced Coin Tavern? Well, dear customer, while there may be shady dealings in our business, we assure you everything is real and high-quality. Maybe we need to bribe some guards to get cheaper goods, but that’s good for the customers, that gets better prices! Maybe we host some not-quite-law-abiding contests or entertainment… But you get to watch it all! If you happen to be adventurers, we might even have some unusual, lucrative activities… definitely fair, no double-crossing! Just dispose of the eye-devowering drake in our basement and we can all make a killing!


Overclock Crisis
What happens when your head can be hacked?
The ExoTech first allowed disabled people to walk again. It became so good that folks could be enhanced with it. The ExoForce, as they were coined, used exoskeletons to fight crime, reducing casualties in the force, as well as inhibiting criminals. Stocks were up, crime rates were down, everything was great. Until the “Overclock Virus” appeared. This malware lay dormant while spreading, at first, through the ExoForce. Although unintended, the Overclock Virus started to infect any user of ExoTech. The ExoForces now fights its former comrades who have gone mad with the Overclock Virus.


Kragudür Clan
Souls shattered by madness
The Kragudür were lost to corruption. On the Day of Thunder, they were in the deepest mines, and could not escape. They were bound to the Thunderstone and its unchecked power brought on the madness. Their cities sprawled on the scars of the mountain and they grew into something monstrous. These dwarves live in the deepest parts of Utgard and have been affected by the raw power of the Thunderstone in a way others cannot begin to fathom… You either die a dwarf or live long enough to become something else entirely… Although sometimes, even death is not enough to stop the spread of The Corruption.



Formate o relatório utilizando Markdown


'''

prompt_template = PromptTemplate.from_template(template=template)

generos = ['Suspense','Horror', 'Cosmic Horror', 'Action', 'Mystery', 'Romance','Terror']
temas = ['Sci-Fi','Medieval','Lovecraft','Steampunk','Space Opera','Cyberpunk','Anime','Wild West']
jogadores = ['1','2','3','4','5']
idiomas = ['English', 'Português', 'Español', 'Français', 'Deutsch', '中国人']

st.title('Which Loot´s Bundle fit in my Adventure?')

genero = st.sidebar.selectbox('Select the genre:', generos)
tema = st.sidebar.selectbox('Select the theme:', temas)
jogador = st.sidebar.selectbox('How many players?', jogadores)
idioma = st.sidebar.selectbox('Select the language:', idiomas)

if st.sidebar.button('Gerar Relatório para Aventura'):
    prompt = prompt_template.format(
        genero=genero,
        tema=tema,
        jogador=jogador,
        idioma=idioma
    )

    response = openai.invoke(prompt)

    st.subheader('Relatório Gerado:')
    st.write(response.content)






