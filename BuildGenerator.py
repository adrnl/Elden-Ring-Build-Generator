import random
from dataclasses import dataclass


@dataclass
class Weapon:
    name: str
    str: int = 0
    dex: int = 0
    int: int = 0
    fai: int = 0
    arc: int = 0

dagger = Weapon('Dagger', 5, 9)
parryDagger = Weapon('Parrying Dagger', 5, 14)
misericorde = Weapon('Misericorde', 7, 12)
greatKnife = Weapon('Great Knife', 6, 12)
bloodstainedDagger = Weapon('Bloodstained Dagger', 9, 12)
erdsteelDagger = Weapon('Erdsteel Dagger', 7, 12, 0, 14)
wakizashi = Weapon('Wakizashi', 9, 13)
celebrantsSickle = Weapon('Celebrant\'s Sickle', 6, 11)
ivorySickle = Weapon('Ivory Sickle', 6, 11, 13)
crystalKnife = Weapon('Cystal Knife', 8, 12, 9)
scorpionsDagger = Weapon('Scorpion\'s Dagger', 6, 12)
cinqueda = Weapon('Cinqueda', 10, 10)
glintstoneKris = Weapon('Glinstone Kris', 5, 12, 16)
reduvia = Weapon('Reduvia', 5, 13, 0, 0, 13)
bladeOfCalling = Weapon('Blade of Calling', 6, 13, 0, 15)
blackKnife = Weapon('Black Knife', 8, 12, 0, 18)

meleeWeapons = {
    'Daggers': [
        dagger,
        parryDagger,
        misericorde,
        greatKnife,
        bloodstainedDagger,
        erdsteelDagger,
        wakizashi,
        celebrantsSickle,
        ivorySickle,
        crystalKnife,
        scorpionsDagger,
        cinqueda,
        glintstoneKris,
        reduvia,
        bladeOfCalling,
        blackKnife
    ],
}


meleeWeaponCategories = {
    'Dagger': [
        'Dagger',
        'Parrying Dagger',
        'Misericorde',
        'Great Knife',
        'Bloodstained Dagger',
        'Wakizashi',
        'Celebrant\'s Sickle',
        'Ivory Sickle',
        'Cystal Knife',
        'Scorpion\'s Dagger',
        'Cinqueda',
        'Glinstone Kris',
        'Reduvia',
        'Blade of Calling',
        'Black Knife'
    ],
    'Straight Sword': [
        'Short Sword',
        'Longsword',
        'Broadsword',
        'Weathered Straight Sword',
        'Lordsworn\'s Straight Sword',
        'Noble\'s Slender Sword',
        'Cane Sword',
        'Warhawk\'s Talon',
        'Lazuli Glintstone Sword',
        'Carian Knight\'s Sword',
        'Crystal Sword',
        'Rotten Crystal Sword',
        'Miquellan Knight\'s Sword',
        'Ornamental Straight Sword',
        'Golden Epitaph',
        'Sword of St. Trina',
        'Regalia of Eochaid',
        'Coded Sword',
        'Sword of Night and Flame'
    ],
    'great sword': [
        'Bastard Sword',
        'Claymore',
        'Iron Greatsword',
        'Lordsworn\'s Greatsword',
        'Knight\'s Greatsword',
        'Banished Knight\'s Greatsword',
        'Forked Greatsword',
        'Flamberge',
        'Gargoyle\'s Greatsword',
        'Gargoyle\'s Blackblade',
        'Inseperable Sword',
        'Sword of Milos',
        'Ordovis\'s Greatsword',
        'Alabster Lord\'s Sword',
        'Death\'s Poker',
        'Helphen\'s Steeple',
        'Blashphemous Blade',
        'Golden Order Greatsword',
        'Dark Moon Greatsword',
        'Sacred Relic Sword'
    ],
    'colossal sword': [
        'Zweihander',
        'Greatsword',
        'Watchdog\'s Greatsword',
        'Troll\'s Golden Sword',
        'Troll Knight\'s Sword',
        'Royal Greatsword',
        'Grafted Blade Greatsword',
        'Ruins Greatsword',
        'Starscourge Greatsword',
        'Godslayer\'s Greatsword',
        'Maliketh\'s Black Blade',

    ],
    'thrusting sword': [
        'Rapier',
        'Estoc',
        'Noble\'s Estoc',
        'Cleanrot Knight\'s Sword',
        'Rogier\'s Rapier',
        'Antspur Rapier',
        'Frozen Needle'
    ],
    'heavy thrusting sword': [
        'Great Epee',
        'Godskin Stitcher',
        'Bloody Helice',
        'Dragon King\'s Cragblade'
    ],
    'curved sword': [
        'Scimitar',
        'Falchion',
        'Shamshir',
        'Grossmesser',
        'Bandit\'s Curved Sword',
        'Shotel',
        'Scavenger\'s Curved Sword',
        'Mantis Blade',
        'Beastman\'s Curved Sword',
        'Flowing Curved Sword',
        'Serpent-God\'s Curved Sword',
        'Magma Blade',
        'Nox Flowing Sword',
        'Wing of Astel',
        'Eclipse Shotel'
    ],
    'curved greatsword': [
        'Dismounter',
        'Omen Cleaver',
        'Monk\'s Flameblade',
        'Beastman\'s Cleaver',
        'Bloodhound\'s Fang',
        'Onyx Lord\'s Greatsword',
        'Zamor Curved Sword',
        'Magma Wyrm\'s Scalesword',
        'Morgott\'s Cursed Sword'
    ],
    'katana': [
        'Uchigatana',
        'Nagakiba',
        'Serpentbone Blade',
        'Meteoric Ore Blade',
        'Moonveil',
        'Rivers of Blood',
        'Dragonscale Blade',
        'Hand of Melenia'
    ],
    'twinblade': [
        'Twinblade',
        'Twinned Knight Swords',
        'Godskin Peeler',
        'Gargoyle\'s Twinblade',
        'Gargoyle\'s Black Blades',
        'Eleonora\'s Poleblade'
    ],
    'axe': [
        'Hand Axe',
        'Forked Hatchet',
        'Battle Axe',
        'Warped Axe',
        'Jawbone Axe',
        'Iron Cleaver',
        'Highland Axe',
        'Celebrant\'s Cleaver',
        'Sacrificial Axe',
        'Icerind Hatchet',
        'Ripple Blade',
        'Stornhawk Axe',
        'Rosus\' Axe'
    ],
    'greataxe': [
        'Greataxe',
        'Crescent Moon Axe',
        'Longshaft Axe',
        'Executioner\'s Greataxe',
        'Great Omenkiller Cleaver',
        'Rusted Anchor',
        'Butchering Knife',
        'Gargoyle\'s Great Axe',
        'Gargoyle\'s Black Axe',
        'Winged Greathorn',
        'Axe of Godrick'
    ],
    'hammer': [
        'Club',
        'Curved Club',
        'Spiked Club',
        'Stone Club',
        'Mace',
        'Morning Star',
        'Warpick',
        'Monk\'s Flamemace',
        'Varre\'s Bouquet',
        'Envoy\'s Horn',
        'Nox Flowing Hammer',
        'Ringed Finger',
        'Scepter of the All-Knowing',
        'Marika\'s Hammer'
    ],
    'flail': [
        'Flail',
        'Nightrider Flail',
        'Chainlink Flail',
        'Family Heads',
        'Bastard\'s Stars'
    ],
    'great hammer': [
        'Large Club',
        'Curved Great Club',
        'Great Mace',
        'Pickaxe',
        'Brick Hammer',
        'Battle Hammer',
        'Rotten Battle Hammer',
        'Celebrant\'s Skull',
        'Great Stars',
        'Greathorn Hammer',
        'Envoy\'s Long Horn',
        'Cranial Vessel Candlestand',
        'Beastclaw Greathammer',
        'Devourer\'s Scepter'
    ],
    'colossal weapon': [
        'Duelist Greataxe',
        'Rotten Greataxe',
        'Golem\'s Halberd',
        'Giant-Crusher',
        'Prelate\'s Inferno Crozier',
        'Great Club',
        'Troll\'s Hammer',
        'Dragon Greatclaw',
        'Watchdog\'s Staff',
        'Staff of the Avatar',
        'Envoy\'s Greathorn',
        'Ghiza\'s Wheel',
        'Fallingstar Beast Jaw',
        'Axe of Godfrey'
    ],
    'spear': [
        'Short Spear',
        'Iron Spear',
        'Spear',
        'Partisan',
        'Pike',
        'Spiked Spear',
        'Cross-Naginata',
        'Clayman\'s Harpoon',
        'Celebrant\'s Rib-Snake',
        'Torchpole',
        'Inquisitor\'s Girandole',
        'Crystal Spear',
        'Rotten Crystal Spear',
        'Cleanrot Spear',
        'Death Ritual Spear',
        'Bolt of Gransax'
    ],
    'great spear': [
        'Lance',
        'Treespear',
        'Serpent-Hunter',
        'Siluria\'s Tree',
        'Vyke\'s War Spear',
        'Mohgwyn\'s Sacred Spear'
    ],
    'halberd': [
        'Halberd',
        'Banished Knight\'s Halberd',
        'Lucerne',
        'Glaive',
        'Vulgar Militia Shotel',
        'Vulgar Militia Saw'
        'Guardian\'s Swordspear',
        'Gargoyle\'s Halberd',
        'Gargoyle\'s Black Halberd',
        'Nightrider Glaive',
        'Pest\'s Glaive',
        'Ripple Crescent Halberd',
        'Golden Halberd',
        'Dragon Halberd',
        'Loretta\'s War Sickle',
        'Commander\'s Standard'
    ],
    'reaper': [
        'Scythe',
        'Grave Scythe',
        'Halo Scythe',
        'Winged Scythe'
    ],
    'whip': [
        'Whip',
        'Thorned Whip',
        'Urumi',
        'Hoslow\'s Petal Whip',
        'Magma Whip Candlestick',
        'Giant\'s Red Braid'
    ],
    'fist': [
        'Caestus',
        'Spiked Caestus',
        'Katar',
        'Iron Ball',
        'Star Fist',
        'Clinging Bone',
        'Veteran\'s Prosthesis',
        'Cipher Pata',
        'Grafted Dragon',
        'Hookclaws',
        'Bloodhound Claws',
        'Venemous Fang',
        'Raptor Talons'
    ],
}

rangedWeaponCategories = {
    'crossbow': [
        'Soldier\'s Crossbow',
        'Light Crossbow',
        'Heavy Crossbow',
        'Arbalest',
        'Crepus\'s Black-Key Crossbow',
        'Pulley Crossbow',
        'Full Moon Crossbow'
    ],
    'bow': [
        'Short Bow',
        'Composite Bow',
        'Red Branch Shortbow',
        'Misbegotten Shortbow',
        'Harp Bow',
        'Longbow',
        'Albinauric Bow',
        'Black Bow',
        'Pulley Bow',
        'Horn Bow',
        'Serpent Bow',
        'Erdtree Bow'
    ],
    'greatbow': [
        'Greatbow',
        'Golem Greatbow',
        'Erdtree Greatbow',
        'Lion Greatbow',
    ],
    'ballistae': [
        'Hand Ballista',
        'Jar Cannon'
    ]
}

secondaryWeaponCategories = {
    'torch': [
        'Torch',
        'Beast-Repellent Torch',
        'Steel-Wire Torch',
        'Sentry\'s Torch',
        'Ghostflame Torch',
        'St. Trina\'s Torch'
    ],
    'staff': [
        'Astrologer\'s Staff',
        'Glinstone Staff',
        'Academy Glintstone Staff',
        'Carian Regal Scepter',
        'Demi-Human Queen\'s Staff',
        'Digger\'s Staff',
        'Azur\'s Glintstone Staff',
        'Carian Glintstone Staff',
        'Staff of Loss',
        'Meteorite Staff',
        'Lusat\'s Glintstone Staff',
        'Crystal Staff',
        'Staff of the Guilty',
        'Prince of Death\'s Staff',
        'Carian Glintblade Staff',
        'Rotten Crystal Staff',
        'Gelmir Glintstone Staff',
        'Albinauric Staff'
    ],
    'sacred seal': [
        'Finger Seal',
        'Erdtree Seal',
        'Golden Order Seal',
        'Gravel Stone Seal',
        'Giant\'s Seal',
        'Godslayer\'s Seal',
        'Clawmark Seal',
        'Frenzied Flame Seal',
        'Dragon Communion Seal'
    ],
    'small shield': [
        'Buckler',
        'Perfumer\'s Shield',
        'Man-Serpent\'s Shield',
        'RICKETY Shield',
        'PILLORY Shield',
        'Shield of the Guilty',
        'Red Thorn Roundshield',
        'Scripture Wooden Shield',
        'Riveted Wooden Shield',
        'Blue-White Wooden Shield',
        'Rift Shield',
        'Iron Roundshield',
        'Gilded Iron Shield',
        'Ice Crest Shield',
        'Smoldering Shield',
        'Spiralhorn Shield',
        'Coil Shield',
    ],
    'medium shield': [
        'Kite Shield',
        'Marred Leather Shield',
        'Marred Wooden Shield',
        'Banished Knight\'s Shield',
        'Albinauric Shield',
        'Sun Realm Shield',
        'Silver Mirrorshield',
        'Round Shield',
        'Scorpion Kite Shield',
        'Twinbird Kite Shield',
        'Blue-Gold Kite Shield',
        'Brass Shield',
        'Great Turtle Shell',
        'Beastman\'s Jar-Shield',
        'Carian Knight\'s Shield',
        'Large Leather Shield',
        'Horse Crest Wooden Shield',
        'Candletree Wooden Shield',
        'Flame Crest Wooden Shield',
        'Hawk Crest Wooden Shield',
        'Beast Crest Heater Shield',
        'Red Crest Heater Shield',
        'Blue Crest Heater Shield',
        'Eclipse Crest Heater Shield',
        'Inverted Hawk Heater Shield',
        'Heater Shield',
        'Black Leather Shield',
    ],
    'great shield': [
        'Dragon Towershield',
        'Distinguished Greatshield',
        'Crucible Hornshield',
        'Dragonclaw Shield',
        'Briar Greatshield',
        'Erdtree Greatshield',
        'Golden Beast Crest Shield',
        'Jellyfish Shield',
        'Fingerprint Stone Shield',
        'Icon Shield',
        'One-Eyed Shield',
        'Visage Shield',
        'Spiked Palisade Shield',
        'Manor Towershield',
        'Crossed-Tree Towershield',
        'Inverted Hawk Towershield',
        'Ant\'s Skull Plate',
        'Redmane Greatshield',
        'Eclipse Crest Greatshield',
        'Cuckoo Greatshield',
        'Golden Greatshield',
        'Gilded Greatshield',
        'Haligtree Crest Greatshield',
        'Wooden Greatshield',
        'Lordsworn\'s Shield'
    ]
}

ashesOfWar = [
    'Ash of War: Repeating Thrust',
    'Ash of War: Unsheathe',
    'Ash of War: Quickstep',
    'Ash of War: Impaling Thrust',
    'Ash of War: Spinning Slash',
    'Ash of War: Sword Dance',
    'Ash of War: Beast\'s Roar',
    'Ash of War: Bloodhound\'s Step',
    'Ash of War: Double Slash',
    'Ash of War: Raptor of the Mists',
    'Ash of War: Piercing Fang',
    'Ash of War: Storm Blade',
    'Ash of War: Storm Stomp',
    'Ash of War: Storm Assault',
    'Ash of War: Stormcaller',
    'Ash of War: Determination',
    'Ash of War: Charge Forth',
    'Ash of War: Square Off',
    'Ash of War: Giant Hunt',
    'Ash of War: Vacuum Slice',
    'Ash of War: Spinning Strikes',
    'Ash of War: Royal Knight\'s Resolve',
    'Ash of War: Phantom Slash',
    'Ash of War: Lightning Slash',
    'Ash of War: Lightning Ram',
    'Ash of War: Thunderbolt',
    'Ash of War: Gravitas',
    'Ash of War: Glintstone Pebble',
    'Ash of War: Carian Greatsword',
    'Ash of War: Spinning Weapon',
    'Ash of War: Carian Grandeur',
    'Ash of War: Loretta\'s Slash',
    'Ash of War: Thops\'s Barrier',
    'Ash of War: Glintblade Phalanx',
    'Ash of War: Carian Retaliation',
    'Ash of War: Waves of Darkness',
    'Ash of War: Golden Vow',
    'Ash of War: Sacred Blade',
    'Ash of War: Sacred Order',
    'Ash of War: Shared Order',
    'Ash of War: Prayerful Strike',
    'Ash of War: Vow of the Indomitable',
    'Ash of War: Sacred Ring of Light',
    'Ash of War: Golden Slam',
    'Ash of War: Golden Land',
    'Ash of War: Golden Parry',
    'Ash of War: Holy Ground',
    'Ash of War: Stamp (Sweep)',
    'Ash of War: Stamp (Upward Cut)',
    'Ash of War: Kick',
    'Ash of War: Endure',
    'Ash of War: War Cry',
    'Ash of War: Wild Strikes',
    'Ash of War: Ground Slam',
    'Ash of War: Lion\'s Claw',
    'Ash of War: Hoarah Loux\'s Earthshaker',
    'Ash of War: Cragblade',
    'Ash of War: Barbaric Roar',
    'Ash of War: Troll\'s Roar',
    'Ash of War: Earthshaker',
    'Ash of War: Braggart\'s Roar',
    'Ash of War: Flaming Strike',
    'Ash of War: Eruption',
    'Ash of War: Flame of the Redmanes',
    'Ash of War: Prelate\'s Charge',
    'Ash of War: Black Flame Tornado',
    'Ash of War: Poison Moth Flight',
    'Ash of War: Poisonous Mist',
    'Ash of War: Hoarfrost Stomp',
    'Ash of War: Chilling Mist',
    'Ash of War: Ice Spear',
    'Ash of War: Bloody Slash',
    'Ash of War: Blood Blade',
    'Ash of War: Seppuku',
    'Ash of War: Blood Tax',
    'Ash of War: Spectral Lance',
    'Ash of War: Lifesteal Fist',
    'Ash of War: Assassin\'s Gambit',
    'Ash of War: White Shadow\'s Lure',
]


def generateBuild(ranged, powerstance):
    if ranged and powerstance:
        primaryOptions = rangedWeaponCategories['crossbow']
        weapon = random.choice(primaryOptions)
        return [weapon, weapon]

    elif ranged and not powerstance:
        offhand = random.randint(0, 1)
        if offhand == 0:
            primaryOptions = rangedWeaponCategories['greatbow']
            primaryOptions.extend(rangedWeaponCategories['ballistae'])
            weapon = random.choice(primaryOptions)
            return [weapon]

        elif offhand == 1:
            primaryOptions = rangedWeaponCategories['crossbow']
            secondaryWeaponTuple = random.choice(
                list(secondaryWeaponCategories.items())
            )
            secondaryOptions = secondaryWeaponTuple[1]
            primary = random.choice(primaryOptions)
            secondary = random.choice(secondaryOptions)
            return [primary, secondary]

    elif not ranged and powerstance:
        primaryWeaponTuple = random.choice(
            list(meleeWeaponCategories.items())
        )
        primaryOptions = primaryWeaponTuple[1]
        weapon = random.choice(primaryOptions)
        return [weapon, weapon]

    elif not ranged and not powerstance:
        offhand = random.randint(0, 1)
        if offhand == 0:
            weaponTuple = random.choice(
                list(meleeWeaponCategories.items())
            )
            weaponOptions = weaponTuple[1]
            weapon = random.choice(weaponOptions)
            return [weapon]

        elif offhand == 1:
            primaryWeaponTuple = random.choice(
                list(meleeWeaponCategories.items())
            )
            primaryOptions = primaryWeaponTuple[1]
            secondaryWeaponTuple = random.choice(
                list(secondaryWeaponCategories.items())
            )
            secondaryOptions = secondaryWeaponTuple[1]
            primary = random.choice(primaryOptions)
            secondary = random.choice(secondaryOptions)
            return [primary, secondary]


def main():
    print('Ranged Powerstance Build: {0}'.format(generateBuild(True, True)))
    print('Ranged Unpaired Build: {0}'.format(generateBuild(True, False)))
    print('Melee Powerstance Build: {0}'.format(generateBuild(False, True)))
    print('Melee Unpaired Build: {0}'.format(generateBuild(False, False)))

main()
