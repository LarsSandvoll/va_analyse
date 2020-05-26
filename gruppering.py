import xlrd
import sys


filterObjekt = {\
'1.Eldre_Støp_Jern_stor_diameter'  : '"DIAMETER" >= d AND ("MATERIAL" = \'SJ\' OR "MATERIAL" = \'SJK\'   OR "MATERIAL" = \'SJG\'  OR "MATERIAL" = \'SJK7\' OR "MATERIAL" = \'SJK9\') AND ("ANLEGGSAAR" < a AND "ANLEGGSAAR" > 1000)',\
'2.Eldre_Støp_Jern_liten_diameter' : '"DIAMETER" <  d AND ("MATERIAL" = \'SJ\' OR "MATERIAL" = \'SJK\'   OR "MATERIAL" = \'SJG\'  OR "MATERIAL" = \'SJK7\' OR "MATERIAL" = \'SJK9\') AND ("ANLEGGSAAR" < a AND "ANLEGGSAAR" > 1000)',\
'3.Eldre_Plastikk_stor_diameter'   : '"DIAMETER" >= d AND ("MATERIAL" = \'PE\' OR "MATERIAL" = \'PE100\' OR "MATERIAL" = \'PE32\' OR "MATERIAL" = \'PE50\' OR "MATERIAL" = \'PE80\' OR "MATERIAL" = \'PEH\' OR "MATERIAL" = \'PEL\' OR "MATERIAL" = \'PVC\') AND ("ANLEGGSAAR" < a AND "ANLEGGSAAR" > 1000)',\
'4.Eldre_Plastikk_liten_diameter'  : '"DIAMETER" <  d AND ("MATERIAL" = \'PE\' OR "MATERIAL" = \'PE100\' OR "MATERIAL" = \'PE32\' OR "MATERIAL" = \'PE50\' OR "MATERIAL" = \'PE80\' OR "MATERIAL" = \'PEH\' OR "MATERIAL" = \'PEL\' OR "MATERIAL" = \'PVC\') AND ("ANLEGGSAAR" < a AND "ANLEGGSAAR" > 1000)',\
'5.Nyere_Støp_Jern_stor_diameter'  : '"DIAMETER" >= d AND ("MATERIAL" = \'SJ\' OR "MATERIAL" = \'SJK\'   OR "MATERIAL" = \'SJG\'  OR "MATERIAL" = \'SJK7\' OR "MATERIAL" = \'SJK9\') AND ("ANLEGGSAAR" >= a)',\
'6.Nyere_Støp_Jern_liten_diameter' : '"DIAMETER" <  d AND ("MATERIAL" = \'SJ\' OR "MATERIAL" = \'SJK\'   OR "MATERIAL" = \'SJG\'  OR "MATERIAL" = \'SJK7\' OR "MATERIAL" = \'SJK9\') AND ("ANLEGGSAAR" >= a)',\
'7.Nyere_Plastikk_stor_diameter'   : '"DIAMETER" >= d AND ("MATERIAL" = \'PE\' OR "MATERIAL" = \'PE100\' OR "MATERIAL" = \'PE32\' OR "MATERIAL" = \'PE50\' OR "MATERIAL" = \'PE80\' OR "MATERIAL" = \'PEH\' OR "MATERIAL" = \'PEL\' OR "MATERIAL" = \'PVC\') AND ("ANLEGGSAAR" >= a)',\
'8.Nyere_Plastikk_liten_diameter'  : '"DIAMETER" <  d AND ("MATERIAL" = \'PE\' OR "MATERIAL" = \'PE100\' OR "MATERIAL" = \'PE32\' OR "MATERIAL" = \'PE50\' OR "MATERIAL" = \'PE80\' OR "MATERIAL" = \'PEH\' OR "MATERIAL" = \'PEL\' OR "MATERIAL" = \'PVC\') AND ("ANLEGGSAAR" >= a)',\
'9.Annet_material'                 : '("MATERIAL" = \'AAS\' OR "MATERIAL" = \'GAL\' OR "MATERIAL" = \'KOB\' OR "MATERIAL" = \'RDEL\' OR "MATERIAL" = \'ST\')'\
}

