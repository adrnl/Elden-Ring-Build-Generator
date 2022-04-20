import random
import WeaponLibrary


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
