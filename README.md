##EPGP Singularity 

Singularity will be switching to an EPGP loot system for Legion. This is a loot system that allows us to best reward being on time, consistent attendace, and performance. It is a point based system based on the formula Priority = (Effort Points) / (Gear Points), or simply: PR = EP/GP.

The idea behind the system is that your effort is measured against the amount of gear you have already recieved, and then a score is generated. The person with the highest score wins the next piece of loot. For more information on the loot system our EPGP will be based on, please see: http://www.epgpweb.com/help/system

##Effort Points
At the begining of this first tier (Emerald Nightmare) every raider will begin with the same amount of Effort Points, or EP. Effort points will then subsequently be rewarded for a variety of things. These could include, as an example, things such as:

1. Being on time for raid

2. Time spent progressing and wiping on a boss

3. Progression kills

4. Farm killls

5. Helping the guild through donation of herbs, enchanting materials, ect. 

6. Time spent riding the bench, but being availible

None of these are set in stone as of now, and the values associated with them will be finalized soon. But the basic idea is that we can award people for doing things that we have struggled with in the past (like starting raid on time). 

###Effort Point Decay
Another reason that EPGP is going to be the loot system of choice is because of EP decay. Instead of having a system that incentivizes people to not take gear upgrades and hoarding points/their position, (dkp/ksk) EPGP has a built in decay function. This means that every raid week your total effort points (and everyone elses) will decay by a certain amount. This means nothing for a consitent raider other than that they cannot hoard their points hoping for a trinket from the last boss. This does mean that people who show up inconsistently will not be able to keep their position as higher than someone who is on time and attends regularly. By including decay we incentivize taking gear that you need, and not skipping out on raid. 

###Effort Point Threshold
Another great thing this loot system has is an EP threshold system. In order to even be considered for loot your EP will have to be above a certain threshold. For a frequent raider this means absolutely nothing, you will always be above this threshold just by showing up to raid. What this does mean is that a new recruit is not going to be snatching loot away from someone who has been here longer until they have accrued enough EP to be considered for loot. This would require them to attend multiple nights, kill multiple bosses, and be awarded EP. 

##Gear Points:
Gear points are what your EP is being measured against. In order to get a piece of loot you need to have the highest PR (priority) in the system. This is measured through EP/GP. Everyone starts with the same GP as a base. When you recieve a piece of gear, that gears gp is added to your gp and then used from there on out (with decay). 

The given GP for a piece of gear is based on how valuable that piece of gear is, that is to say:

GP = 0.483 x 2^(ilvl/100) x slot weight

Let's walk through that for two pieces of gear, a trinket and a wrist piece. Both of these pieces in the example are going to be item level 865. A trinket is going to provide a more significant boost on average than a wrist piece, so their slot weights are 1 and 0.5 respectively. Using the equation we see that:


0.483 x 2^(865/100) x 1 = 194 gp (trinket)
0.483 x 2^(865/100) x 0.5 = 97 gp (wrist)

If you were to win the trinket, your current gp would become current + 194, and the wrist it would become current + 97. 
It is important to remember that the GP of an item is only added to your score after the piece of loot is recieved, this way you are being evaluated on the current gear you possess. 

###Gear Point Decay
Like EP, GP also has a built in decay. This prevents you from sitting around not ever recieving loot, and it prevents the system from growing infinitely. Each week you current GP will be reduced by a certain amount (THIS IS GOOD FOR YOU). 

#Other stuff
##What about warforged/titanforged, gem sockets, and personal gear?
I am currently in the process of accounting for all of these different things.

###Warforged and Titanforged
Warforged and titanforged gear are going to affect the GP a piece of gear is worth by a small amount. If a normal piece of gear has a GP of 150, the warforged piece would be worth 170 and the titanforged piece would be worth 190. These values are subject to change. The take-away is that, yes, warforged and titanforged will be worth more to the system than normal gear. 

###Sockets
Just like with forged gear, sockets will add a value to the total GP a piece of gear is worth.

###The grand RNG Hierarchy
Normal > Warforged Normal > Socketed Normal > Titanforged > Socketed Warforged > Socketed Titanforged

###What about personal loot, loot recieved from pugs, mythic dungeons, ect.?
Singularity's stance on personal loot has always been: congrats on your gear it has no effect on anything. 
This will be changing with EPGP. Personal loot will effect your GP, but not you EP. You will still gain the same amount of EP as everyone else, but your GP will increase based on the item you recieve. (If its an upgrade)

EPGP will be concerned with loot recived IN RAID ONLY. This means that I don't want to hear about, nor do I care about, the gear you recieved in a dungeon, pug normal, lfr, cache, or wherever else it came from.  

##Why move away from KSK in the first place?
KSK is a great loot system for gearing small groups, or large groups on farm content. It is an absolute mess when it comes to gearing entire 20 man rosters at the begining of an expansion. While I enjoyed KSK's ease of use and simplicity, this system is going to be better in the long run. It allows us to reward and incentivize people for things we want to reward and incentivize. It also allows us to tweak who is getting gear if we decide that needs to happen (increasing EP gain for tanks and healers at the begingin of a tier would be an example). Overall while more complicated this system is going to provide a straight forward way for the raid team to be loot managed properly. 
