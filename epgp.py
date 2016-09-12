'''
Alex Ring
Loot System for Singularity US
Update: 12/9/16

The EPGP formula for gear is as follows:
GP = 0.483 * 2^(ilvl/100) * slot mod

Slot mods:
Relic : 2
Trinkets: 1
Tier Head, Chest, Legs : 1.5
Tier Shoulder, Hands, cloak : 1
Normal Head, Chest, Legs : 1
Normal Shoulder, Hands, Waist, Feet: 0.75
Wrist, Neck, Back, Finger : 0.5

This formula results in gear that provides more stats being worth more
'''

def calcGP(itemName,itemLVL, itemSlot, tier):
	weight = 0
	if tier == 'y':
		if itemSlot == 'head':
			weight = 1.5
		elif itemSlot == 'chest':
			weight = 1.5
		elif itemSlot == 'shoulders':
			weight = 1
		elif itemSlot == 'back':
			weight = 1
		elif itemSlot == 'hands':
			weight = 1
		elif itemSlot == 'legs':
			weight = 1.5
	else:
		if itemSlot == 'relic':
			weight = 2
		elif itemSlot == 'head':
			weight = 1
		elif itemSlot == 'chest':
			weight = 1
		elif itemSlot == 'shoulders':
			weight = 0.75
		elif itemSlot == 'back':
			weight = 0.5
		elif itemSlot == 'hands':
			weight = 0.75
		elif itemSlot == 'legs':
			weight = 1
		elif itemSlot == 'neck':
			weight = 0.5
		elif itemSlot == 'wrist':
			weight = 0.5
		elif itemSlot == 'waist':
			weight = 0.75
		elif itemSlot == 'feet':
			weight = 0.75
		elif itemSlot == 'ring':
			weight = 0.5
		elif itemSlot == 'trinket':
			weight = 1.75


	gp = 0.483 * 2**(itemLVL/100) * weight
	gp = int(gp)
	warforgedGP = gp + 20
	sockGP = gp + 30
	titanforgedGP = gp + 40
	warSockGP = gp + 45
	titanSockGP = gp + 55

	gpWrite = itemName + ' GP:' + str(gp) + '\n'
	gpWarWrite = itemName + ' Warforged GP:' + str(warforgedGP) + '\n'
	gpSockWrite = itemName + ' Socketed GP:' + str(sockGP) + '\n'
	gpWarSockWrite = itemName + ' Warforged Socketed GP:' + str(warSockGP) + '\n'
	gpTitanWrite = itemName + ' Titanforged GP:' + str(titanforgedGP) + '\n'
	gpTitanSockWrite = itemName + ' Titanforged Socketed GP:' + str(titanSockGP) + '\n'
	with open('itemGP.txt', 'a') as myfile:
		myfile.write(gpWrite)
		myfile.write(gpWarWrite)
		myfile.write(gpSockWrite)
		myfile.write(gpWarSockWrite)
		myfile.write(gpTitanWrite)
		myfile.write(gpTitanSockWrite)
		myfile.write('\n')



def main():
	with open('itemGP.txt','a') as myfile:
		myfile.write('-------------------------------------------\n')
		myfile.write('EMERALD NIGHTMARE\n')
		myfile.write('-------------------------------------------\n')
		myfile.write('Nythendra \n')
		myfile.write('--------------------------\n')
	calcGP('Despoiled Dragonscale',865,'relic','n')
	calcGP('Preserved Worldseed',865,'relic','n')
	calcGP('Shaladrassil\'s Blossom',865,'relic','n')
	calcGP('Unwaking Slumber',865,'relic','n')
	calcGP('Greyed Dragonscale Coif',865,'head','n')
	calcGP('Ancient Dreamwoven Manle',865,'shoulders','n')
	calcGP('Insect-Etched Chestplate',865,'chest','n')
	calcGP('Wristclamps of Mad Dreams',865,'wrist','n')
	calcGP('Creeping String of Larva',865,'waist','n')
	calcGP('Lifeless Buckled Girdle',865,'waist','n')
	calcGP('Stained Maggot Squishers',865,'feet','n')
	calcGP('Grubby Silver Ring',865,'ring','n')
	calcGP('Ravaged Seed Pod',865,'trinket','n')
	calcGP('Swarming Plaguehive',865,'trinket','n')

	with open('itemGP.txt','a') as myfile:
		myfile.write('--------------------------\n')
		myfile.write('Elerethe Renferal\n')
		myfile.write('--------------------------\n')
	calcGP('Fel-bloated Venom Sac',865,'relic','n')
	calcGP('Scything Quill',865,'relic','n')
	calcGP('Shrieking Bloodstone',865,'relic','n')
	calcGP('Mask of Multitudinous Eyes',865,'head','n')
	calcGP('Venom-Fanged Barbute',865,'head','n')
	calcGP('Gossamer-Spun Greatcloak',865,'back','n')
	calcGP('Patient Ambusher\'s Hauberk',865,'chest','n')
	calcGP('Wristwraps of Broken Trust',865,'wrist','n')
	calcGP('Pliable Spider Sil Cinch',865,'waist','n')
	calcGP('Ragged Horroweave Legplates',865,'legs','n')
	calcGP('Storm-Battered Legplates',865,'legs','n')
	calcGP('Black Venom Sabatons',865,'feet','n')
	calcGP('Cocoon of Enforced Solitude',865,'trinket','n')
	calcGP('Twisiting Wind',865,'trinket','n')

	with open('itemGP.txt','a') as myfile:
		myfile.write('--------------------------\n')
		myfile.write('Il\'gynoth, Heart of Corruption\n')
		myfile.write('--------------------------\n')
	calcGP('Cube of Malice',865,'relic','n')
	calcGP('Gore-Drenched Fetish',865,'relic','n')
	calcGP('Radiating Metallic Shard',865,'relic','n')
	calcGP('Sloshing Core of Hatred',865,'relic','n')
	calcGP('Celestially Aligned Hood',865,'head','n')
	calcGP('Otherworldly Leather Mantle',865,'shoulders','n')
	calcGP('Pauldrons of Shifting Runes',865,'shoulders','n')
	calcGP('Cinch of Cosmic insignificance',865,'wrist','n')
	calcGP('Dreamsculptor\'s gloves',865,'hands','n')
	calcGP('Gauntlets of Malevolent Intent',865,'hands','n')
	calcGP('Waistplate of Nameless Horror',865,'waist','n')
	calcGP('Singular Chain Leggings',865,'legs','n')
	calcGP('Dreadful Cyclopean Signet',865,'ring','n')
	calcGP('Goblet of Nightmarish Ichor',865,'trinket','n')
	calcGP('Spontaneous Appendages',865,'trinket','n')
	calcGP('Wriggling Sinew',865,'trinket','n')

	with open('itemGP.txt','a') as myfile:
		myfile.write('--------------------------\n')
		myfile.write('Ursoc\n')
		myfile.write('--------------------------\n')
	calcGP('Bloodied Bear Fang',865,'relic','n')
	calcGP('Reverberating Femur',865,'relic','n')
	calcGP('Tuft of Ironfur',865,'relic','n')
	calcGP('Cursed Beartooth Necklace',865,'neck','n')
	calcGP('Matted Fur Pauldrons',865,'shoulders','n')
	calcGP('Scarred Ragefang Chestpiece',865,'chest','n')
	calcGP('Ragged Fur Wristwraps',865,'wrist','n')
	calcGP('Scored Ironclaw Sabatons',865,'wrist','n')
	calcGP('Primal Gauntlets of Rage',865,'hands','n')
	calcGP('Splotched Bloodfur Leggings',865,'legs','n')
	calcGP('Crimson Wool-Lined Slippers',865,'feet','n')
	calcGP('Trampling Warboots',865,'feet','n')
	calcGP('Blodthirsty Instinct',865,'trinket','n')
	calcGP('Heightened Senses',865,'trinket','n')
	calcGP('Unbridled Fury',865,'trinket','n')
	calcGP('Ursoc\'s Rending Paw',865,'trinket','n')

	with open('itemGP.txt','a') as myfile:
		myfile.write('--------------------------\n')
		myfile.write('Dragons of Nightmare\n')
		myfile.write('--------------------------\n')
	calcGP('Bioluminescent Mushroom',865,'relic','n')
	calcGP('Entrancing Stone',865,'relic','n')
	calcGP('Nightmare Engulfed Jewel',865,'relic','n')
	calcGP('Cowl of Fright',865,'head','n')
	calcGP('Dreamscale Inlaid Vestments',865,'chest','n')
	calcGP('Horror Inscribed Chestguard',865,'chest','n')
	calcGP('Dragonbone Wristclamps',865,'wrist','n')
	calcGP('Dragonspur Wristguards',865,'wrist','n')
	calcGP('Gauntlets of the Demented Mind',865,'hands','n')
	calcGP('Handwraps of Delusional Power',865,'hands','n')
	calcGP('Malignant Sabatons',865,'feet','n')
	calcGP('Mindrend Band',865,'ring','n')
	calcGP('Phantasmal Echo',865,'trinket','n')
	calcGP('Unstable Horrorslime',865,'trinket','n')
	calcGP('Vial of Nightmare Fog',865,'trinket','n')

	with open('itemGP.txt','a') as myfile:
		myfile.write('--------------------------\n')
		myfile.write('Cenarius\n')
		myfile.write('--------------------------\n')
	calcGP('Blessing of Cenarius',865,'relic','n')
	calcGP('Radiant Dragon Egg',865,'relic','n')
	calcGP('Uplifiting Emerald',865,'relic','n')
	calcGP('Crown of Steely Brambles',865,'head','n')
	calcGP('Mantle of Perpetual Bloom',865,'shoulders','n')
	calcGP('Throny Bramblemail Pauldrons',865,'shoulders','n')
	calcGP('Evergreen Vinewrap Drape',865,'back','n')
	calcGP('Tunic of the Grove keeper',865,'chest','n')
	calcGP('Fitted Ironbark Gauntlets',865,'hands','n')
	calcGP('Forest-Lord\'s Waistwrap',865,'waist','n')
	calcGP('Laughing Sister\'s Pouch-chain',865,'waist','n')
	calcGP('Cozy Dryad Hoof-Socks',865,'feet','n')
	calcGP('Hord of Cenarius',865,'trinket','n')
	calcGP('Nature\'s Call',865,'trinket','n')

	with open('itemGP.txt','a') as myfile:
		myfile.write('--------------------------\n')
		myfile.write('Xavius\n')
		myfile.write('--------------------------\n')
	calcGP('Azsharan Councillor\'s Clasp',865,'relic','n')
	calcGP('Crystallized Drop of Eternity',865,'relic','n')
	calcGP('Fragment of Eternal Spite',865,'relic','n')
	calcGP('Nightmarish Elm Branch',865,'relic','n')
	calcGP('Hood of Darkened Visions',865,'head','n')
	calcGP('Blackened Portalstone Necklace',865,'neck','n')
	calcGP('Midnight Herald\'s Pauldrons',865,'shoulders','n')
	calcGP('Maddening Robe of Secrets',865,'chest','n')
	calcGP('Manacles of the Nightmare Colassus',865,'wrist','n')
	calcGP('Eon-Tempered Waistplate',865,'waist','n')
	calcGP('Disjointed Linkage Leggings',865,'legs','n')
	calcGP('Repulsive Leathery Pants',865,'legs','n')
	calcGP('Boots of Endless Betrayal',865,'feet','n')
	calcGP('Twice-Warped Azsharan Signet',865,'ring','n')
	calcGP('Bough of Corruption',865,'trinket','n')
	calcGP('Grotesque Stattuette',865,'trinket','n')

main()


