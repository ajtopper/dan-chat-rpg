import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
import os
import yaml

with open('config.yaml', 'r') as config_file:
    config = yaml.safe_load(config_file)
os.environ['OPENAI_API_KEY'] = config['OPENAI_API_KEY']

openai = ChatOpenAI(
    model_name='gpt-3.5-turbo',
    temperature=0
    )

template = '''
Você é um escritor de aventuras de RPG.
Escreva um relatório de aventura de RPG detalhado levando em consideração o gênero "{genero}" para uma mesa na temática {tema} para uma mesa com {jogador} jogadores.

O relatório dever ser escrito em {idioma} e incluir a seguinte análise:
Qual bundles da Loot Studios são melhores para jogar determinada aventura.
Qual plot e Lore as aventuras escolhidas pelo sistema e como o DM pode criar ganchos para as suas aventuras baseadas nele, além disso leve em consideração a quantidades de jogadores.
Dê no mínimo 5 a 10 sugestões de ganchos para o DM.

Certifique-se de fornecer insights e conclusões para esta seção.

Pacotes de bundles da Loot com descrição se restrinja a somente esse conteúdo para embasar os bundles sugeridos:


Bundle: Forgotten Beasts
Descrição: Doomsday Has Claws and Fangs!
In a strange, different reality, where the moon intercepted the gigantic meteor that would bring extinction to all dinosaurs, sentience was attained not by mankind, but rather, by a peculiar kind of reptiles. Their civilization spans all over the world, with a bellicose, and reckless culture. However, all is about to change, for the alignment of the planets is changing the behavior of all the fauna in the world, creating murderous monsters from once peaceful dinos! Now, it's do or die, and the Saurinax will meet this foretold doom with a weapon in hand, and a smile on the face!


Bundle: Rise of Draconians
Descrição: The glorious comeback of the Dragon Empress
Centuries ago, the Dragon Empress was sealed away by a group of heroes who used the power of the Orb of Dragonkind. The power of the orb has waned now, and those heroes are long gone. Her followers are finally ready to reconquer the land of Shaldrak. However, one of her dragon knights decided her actions were beyond any reasonable excuse and fled from the army, searching for souls brave enough to stand against certain doom. Who will answer the call for adventure? Who will choose to face the Empress against all odds? Who will save the land of Shaldrak from the Rise of Draconians?


Bundle: Cryo Hazard
Descrição: The alien horror is about to begin
One of the Pitblazers spaceships ended up crash landing in a world known as Hellplanet Typhoon, an inhospitable place barely unexplored by humanity. Once the crew awoke from cryosleep and identified where they were, they made a plan to keep themselves safe and broadcast a message asking for help. While setting this plan in motion, the Pitblazers crew realized they weren’t alone in the icy landscapes of Hellplanet Typhoon. Unfortunately, they only realized the unknown presence when an alien entity was already attacking their numbers.


Bundle: Arthurian Tales
Descrição: A tale retold!
Valorous knights from ancient tales gather to protect Albion from a winged tempest that threatens to destroy it. Relive and experience the beloved tales of the Knights of the Round Table, as well as the mythological creatures and fantastical artifacts that permeate the Arthurian mythos. Fight alongside Arthur against the traitorous Mordred, seek the counseling of the wizards Merlin and Nimue, outlast the invasion of Galehaut, hunt the Questing Beast, or quest for the Holy Grail alongside Galahad and Dindrane. Camelot awaits!


Bundle: Bump in the Night
Descrição: It's Time For a Killing Show!
Dear spectator, the time is right for a truly marvelous show! Sit back and relax, as you watch the Survivors try and outlast the murderous beings that I'll throw at them. Be it brute or rogue, flesh amalgam, or incorporeal shade, the Scream Team will haunt the rooms of the Ghastly Cabin while hunting their prey. Oh, but don't take me for a mere sadist, my dear! Each one of them can be defeated by the Survivors, should their wit guide them towards such knowledge. But hush now, my dear! The lights are dim, and the cinema's screen is lit by the projector. Let us watch a spectacle.


Bundle: Abyssal Haze
Descrição: Everything will turn into void when the haze comes
The city of Azmar was known to be a sanctuary, a place to help those in need, all thanks to the Chantry of Healing. Unknowingly, Lord Gaspard let loose the essence of the void, manifesting itself in a sickening haze that took over Azmar and nearby lands. The void couldn’t be controlled and, with the passing years, the abyssal haze began to spread itself further across the realm, infecting even more people. Many heroes tried to stop it and failed, but a group of hunters decided to give one last shot before everything is lost to the void.


Bundle: Tysect Wars
Descrição: The War Isn't Over
Pitblazer, the Authority has been lying to you! The situation on Erca is way worse than what they've briefed us for. With each passing day, the Tysects deploy new monstrous evolutions to destroy our troops. Worse still, some say they might even be following a higher form of conscience, as their tactics are nothing short of genius. There is, however, hope. I've managed to find an entrance that leads directly into the Heart of the Hive, whose destruction might finally put an end to this menace. Lock N' load, Pitblazer, we're going deep into the hive. For humanity!


Bundle: Mystery in Panshaw
Descrição: In a city of doppelgangers, who can you trust?
The Thieves’ Guild is causing chaos and mayhem. Rumors say they are able to get away with it by using doppelgangers as their agents and even the city guard is said to have been infiltrated. Magistrate Vurneg has hired a group of adventurers, rusted heroes of Panshaw who were away on a mission when the trouble started. The group needs to retrieve a magical artifact, the Gateway of Ahzora, to get a lead of where the Thieves’ Guild hideout and then defeat its leader, Cole Nightshade. However, not only are the thieves aware of their movements, but the City Guard is also on their heels.


Bundle: Pitblazers Unleashed
Descrição: Give 'em Hell!
Commander, The Authority need you to bring the light of freedom to the massive jungle planet of Erca, whose monstrous bug-like inhabitants don't seem to understand our right to take their bountiful world for ourselves. According to our reconnaissance teams, the resources present there will provide for our brethren's colonies for many decades. To subdue the creatures who stand in our path, thousands of Pitblazers will rain down fire and bullets in the name of freedom! Lock and load, check your Voxcomm, and command your troops toward victory!

Bundle: Chaos in Haydale
Descrição: A bloody ritual brings forth a terrible creature
The people of Panshaw knew there was something seriously wrong when shipments stopped arriving from Haydale, the southern settlement that feeds most of the region. When the city’s taverns started running dangerously low on ale, people started to worry. Rumors spread quickly but before panic sets in a group of adventurers is sent to investigate and report back. After a week’s journey, the heroes make their way to Haydale, only to discover that the village has been run over by Hobgoblins!


Bundle: Clockwork Skyline
Descrição: Metal and Flesh Clashes!
The megacity of Skyline used to be a utopia of flesh and metal, where mankind lived peacefully through the work of their creations. Now, the scales have turned. As the Avatar of Illumination seizes the reigns of the city, declaring martial law, automatons begin to oppress the people they once served. The time has come for brave rebels to stand their ground and strike against the heart of corruption, either uncovering the truth behind the Avatar's facade and saving the city, or dying trying.


Bundle: The Undercaves
Descrição: Monster crawl in the shadows of the Undercaves
When the Mindbreaker of the Cthulhufolk made his way to the Undercaves, the fragile peace was shattered. Most of the people perished in a deadly monstrous feast. However, even in this grim scenario, there is still hope. The few survivors left aside their differences to create a fragile alliance. Time is short because the Mindbreaker has achieved a terrifying feat: through psionic might he has the Ancient Rock Worm, the most feared creature from the Undercaves, under his control. Who will rise victorious, the mighty heroes or the monsters controlled by the Mindbreaker?


Bundle Primal Crisis
Descrição: It’s the Past All Over Again!
The future is bright, for Wells Corp has created a space portal! Of sorts... Some unexpected results have happened on the island's test site, and monstrous creatures from Earth's ancient past now roam free, wreaking havoc and threatening to expose the corporation. To prevent such a scenario, the Desperate Measures were created, and a team of scientists and mercs were set to stop the chaotic machine and reclaim its blueprint. The machine, however, has given way to strange hominids, raising questions about the tech's true purposes. Alliances will be made, as unlikely heroes venture into the past to save the future!



Bundle: Faewood Haven
Descrição: A Wise Trunk Flower Pot
You don't need to tell anyone of your love for the fey if your plants grow like magic in a highly detailed Faewood flower pot. Show everyone you are a true defender of the little folk by 3D printing and painting this unique prop and home decor, the perfect vase to exhibit your gardening skills to all your friends!


Bundle: Metal Maelstrom
Descrição: Behold the era of the Blessed Ones!
In a devastated Earth, the Motor Gangs have fought for territory and resources for many decades. After a Kapillian spaceship falls into Wargod Tom’s territory, his gang takes over the alien cutting-edge technology. These new tools give life to the Wargod’s greatest desire: taking over all the scrub territory and becoming the ultimate leader. His new technology gave him the power to exterminate many of his enemies, however, people who already tasted the Wargod’s cruelty are willing to do anything to stop this explosive madness. Will their determination be enough to stop Wargod Tom’s savagery?



Bundle: Scarlet Requiem
Descrição:The Erntefest approaches, and Baron Voyd has set all the pieces in place
Inside the tomb-land of Rabennar, caravans and travelers venturing through the dark woods claim to have survived attacks by fanged people, surveying the land in search of something, leaving a trail of bodies in their wake, ever closer to human settlements. All the while, atop the Manor of Night, a shadowless figure watches from above, plotting. Still, a party of heroes arrives, defying the odds, eager to stand where many fell. The cards of the fortune tellers are set, but destiny is yet to be shaped by those who venture into darkness.






'''
#Formate o relatório utilizando Markdown

prompt_template = PromptTemplate.from_template(template=template)

generos = ['Suspense','Horror', 'Horror Cósmico', 'Ação', 'Mistério', 'Romance','Terror']
temas = ['Sci-Fi','Medieval','Lovecraftiano','Steampunk','Space Opera','Cyberpunk','Anime']
jogadores = ['1','2','3','4','5','6','7','8']
idiomas = ['Português', 'Inglês', 'Espanhol', 'Francês', 'Alemão', 'Chinês']

st.title('Gerador de Aventuras de RPG - Loot Studios')

genero = st.selectbox('Selecione o gênero:', generos)
tema = st.selectbox('Selecione o tema:', temas)
jogador = st.selectbox('Selecione a quantidade de jogadores', jogadores)
idioma = st.selectbox('Selecione o idioma:', idiomas)

if st.button('Gerar Relatório para Aventura'):
    prompt = prompt_template.format(
        genero=genero,
        tema=tema,
        jogador=jogador,
        idioma=idioma
    )

    response = openai.invoke(prompt)

    st.subheader('Relatório Gerado:')
    st.write(response.content)






