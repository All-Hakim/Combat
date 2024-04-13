from Personnage import Personnage
from Magicien import Magicien
from RoiSorcier import RoiSorcier
from Combat import Combat

magicien = Magicien('LE Magicien')
roi = RoiSorcier('Le Roi Sorcier')
guerre = Combat(magicien,roi)
guerre.demarrerCombat()