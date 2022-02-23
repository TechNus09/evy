import os
import math
import asyncio
import discord as d
from discord.ext import commands
from discord.utils import get
import random
from datetime import date as dt
from urllib.request import Request, urlopen
import json
import nest_asyncio
import time
import aiohttp
from db_helper import createT

#from logs import members_log, members_list, unsorted_lb, skills_names_list, skills_xp_list


nest_asyncio.apply()

##############################################################################Bot_Resources######################################################################################

skill = ['','-mining', '-smithing', '-woodcutting', '-crafting', '-fishing', '-cooking']
skills = ['combat','mining', 'smithing', 'woodcutting', 'crafting', 'fishing', 'cooking','total']

guilds_combat = {}
guilds_mining = {}
guilds_smithing = {}
guilds_woodcutting = {}
guilds_crafting = {}
guilds_fishing = {}
guilds_cooking = {}

guilds_counter  = {'p1mp': 0,'IMMORTAL': 0, 'OWO': 0, 'EXP': 0, 'BRX': 0, 'RNG': 0, 'LAT': 0, 'KRG': 0, 'GGWP': 0, 'PVM': 0, 'DTF': 0, 'HSR': 0, 'FG': 0, 
                    'NS': 0, 'AOE': 0, 'NSFW': 0, 'DMG': 0, 'AXIAL': 0, 'PAK': 0, 'T62': 0, 'VLR': 0, 'RYU': 0, 'TI': 0, 'NSL': 0, '1HB': 0, 'FFA': 0,
                    'OG': 0, 'ORAZE': 0, 'BLITZ': 0, 'DTS': 0, 'SOLO': 0, 'BIG': 0, 'TRG': 0, 'CCCP': 0, 'TNT': 0, 'SOW': 0, 'PAPA': 0, 'TH': 0,
                    'EXC': 0, 'PHG': 0, 'SHORN': 0, 'TT': 0, 'UMBRA': 0, 'AK7': 0, 'GG': 0, 'LNH': 0, 'SLP': 0, 'DEAD': 0, 'TCK': 0, 'XP': 0, 
                    'VN': 0, 'XNW': 0, 'DARK': 0, 'FW': 0, 'DAVY': 0, 'DK': 0, 'II': 0, 'RW': 0, 'WG': 0, 'OL': 0, 'GOD': 0, 'YOUNG': 0, 'MAD': 0,
                    'ORDO': 0, 'LGN': 0, 'STEVE': 0, 'LOST': 0, 'LI': 0, 'GO': 0, 'LOLI': 0, 'PKMN': 0, 'GUN': 0, 'TAZ': 0, 'BH': 0, 'YT': 0,
                    'SYN': 0, 'NINJA': 0, 'ESP': 0, 'DR': 0, 'PK': 0, 'CW': 0, 'XD': 0, 'RS': 0, 'GOLEM': 0, 'IIAMA': 0, 'IL': 0, 'HANSA': 0, 'YAO': 
                    0, 'ST': 0, '6T9': 0, 'FLO': 0, 'SORRY': 0, 'AEVN': 0, 'MSA': 0, 'TROLL': 0, 'GW': 0, 'AROS': 0, 'GOKU': 0, 'YUZU': 0, 'GEAR': 0, 'IE': 0,
                    'WTH': 0, 'ACE': 0, 'RDS': 0, 'ROYAL': 0, 'KH': 0, 'FT': 0, 'TMG': 0, 'IY': 0, 'W3': 0, 'NEW': 0, 'TTT': 0, 'LT': 0, 'PW': 0,
                    'PAPPY': 0, '403': 0, 'KING': 0, 'FOX': 0, 'YSD': 0, 'NN': 0, 'MARIA': 0, 'OLD': 0, 'ROSE': 0, 'JESSA': 0, 'DAZZ': 0, 'SIR': 0,
                    'RP': 0, 'RSM': 0, '  ILY': 0, 'PWN': 0, 'IV': 0, 'VX': 0, 'ROBBY': 0, 'REN': 0, 'SNAKE': 0, 'GOUL': 0, 'FLOS': 0, 'LBX': 0,
                    'DN': 0, 'SG': 0, 'CUTE': 0, 'SUPER': 0, 'ETN': 0, 'BREAD': 0, 'YAMI': 0, 'GREEN': 0, 'VLOK': 0, 'CASH': 0, 'KAYN': 0, 'SV': 0,
                    'SIAPA': 0, 'KXNG': 0, 'ZERO': 0, 'DIMAS': 0, 'WHO': 0, 'TCM': 0, 'GLOW': 0, 'LDK': 0, 'LX': 0, 'KELLY': 0, 'JANG': 0, 'OLAZ': 0,
                    'THE': 0, 'DIPS': 0, 'GXB': 0, 'TITIT': 0, 'SMOL': 0, 'NEAL': 0, 'SOS': 0, 'FS': 0, 'R13': 0, 'WC2': 0, 'KENJI': 0, 
                    'AG': 0, 'ZIGG': 0, 'MFJ': 0, 'BLUE': 0, 'YAH': 0, 'BILL': 0, 'VAN': 0, 'SOY': 0, 'WAX': 0, 'FBI': 0, 'DUKE': 0, 'APEX': 0,
                    'OOPSY': 0, 'MEYO': 0, '666': 0, 'DADDY': 0, 'MINER': 0, 'NACHT': 0, 'EISA': 0, 'FRTK': 0, 'RRR': 0, 'FAJNA': 0, 'T2': 0,
                    'CFR': 0, 'ION': 0, 'MINI': 0, 'CAKE': 0, 'RANDO': 0, 'OLGA': 0, 'CAP': 0, 'CYCLO': 0, 'LE': 0, 'WAN': 0, 'LV': 0, 'YAN': 0,
                    'CP': 0, 'HMG': 0, 'RED': 0, 'BUZZ': 0, 'GR0': 0, 'A51': 0, 'ISMA': 0, 'THC': 0, 'C137': 0, 'LIAN': 0, 'RON': 0, 'NUB': 0, 'TNS': 0, 
                    'LUCKY': 0, 'SD': 0, 'QL': 0, 'EL': 0, 'DGG': 0, 'DEATH': 0, 'MELEE': 0, 'LQM': 0, 'RIVER': 0, 'KDA': 0, 'GODLY': 0, 'IG': 0, 
                    'AZURE': 0, 'ADNX': 0, 'AK47': 0, 'TETRA': 0, 'KVN': 0, 'BUD': 0, 'FAST': 0, 'CC': 0, 'HONEY': 0, 'YDS': 0, '63': 0, 'OMED': 0,
                    'PIXYZ': 0, 'KOA': 0, 'FROOT': 0, 'ANTI': 0, 'STILL': 0, 'YSO': 0, 'XPLOI': 0, 'BI': 0, 'MC': 0, 'IM': 0, 'LEMON': 0, 'MAOKI': 0,
                    'LEVEL': 0, 'MR': 0, 'THL': 0, 'SAD': 0, '1337': 0, 'ITCHY': 0, 'THOR': 0, 'ROTI': 0, 'WASON': 0, 'FLXW': 0, 'IT': 0, 'RAFA': 0,
                    'MAOU': 0, 'TEXAN': 0, 'HEDGE': 0, 'MLG': 0, 'ISC': 0, 'YOUR': 0, 'GOAT': 0, 'EA': 0, 'PRX': 0, 'OLY': 0, 'BLECK': 0, 'ADAM': 0,
                    'ERBO': 0, 'SZEPT': 0, 'BTW': 0, 'ENZA': 0, 'BL4CK': 0, 'GRB': 0, 'KYOU': 0, 'WORLD': 0, 'XDARK': 0, 'BR': 0, 'LUCAS': 0, 'XZ': 0,
                    'LIL': 0, 'ILI': 0, 'AI': 0, 'TOM': 0, 'CAPT': 0, 'MS': 0, 'LO': 0, 'BD': 0, 'FLOOR': 0, 'LOYAL': 0, 'TRULY': 0, 'AKUTO': 0,
                    'AKT': 0, 'TIGER': 0, 'VND': 0, 'SR': 0, 'GA': 0, 'DMN': 0, 'MANG': 0, 'GM': 0, 'WILL': 0, 'GOLD': 0, 'GK': 0, '808': 0,
                    'RICK': 0, 'ULTR': 0, 'KAMI': 0, 'QUAN': 0, 'FORST': 0, 'DWIKI': 0, 'LBCL': 0, 'EML': 0, 'HUONG': 0, 'AFK': 0, 'NO': 0,
                    'DUCKS': 0, 'XERRA': 0, 'THAT': 0, 'DJ': 0, 'TWO': 0}

guilds_counter_total  = {'p1mp': 0,'IMMORTAL': 0, 'OWO': 0, 'EXP': 0, 'BRX': 0, 'RNG': 0, 'LAT': 0, 'KRG': 0, 'GGWP': 0, 'PVM': 0, 'DTF': 0, 'HSR': 0, 'FG': 0, 
                        'NS': 0, 'AOE': 0, 'NSFW': 0, 'DMG': 0, 'AXIAL': 0, 'PAK': 0, 'T62': 0, 'VLR': 0, 'RYU': 0, 'TI': 0, 'NSL': 0, '1HB': 0, 'FFA': 0,
                        'OG': 0, 'ORAZE': 0, 'BLITZ': 0, 'DTS': 0, 'SOLO': 0, 'BIG': 0, 'TRG': 0, 'CCCP': 0, 'TNT': 0, 'SOW': 0, 'PAPA': 0, 'TH': 0,
                        'EXC': 0, 'PHG': 0, 'SHORN': 0, 'TT': 0, 'UMBRA': 0, 'AK7': 0, 'GG': 0, 'LNH': 0, 'SLP': 0, 'DEAD': 0, 'TCK': 0, 'XP': 0, 
                        'VN': 0, 'XNW': 0, 'DARK': 0, 'FW': 0, 'DAVY': 0, 'DK': 0, 'II': 0, 'RW': 0, 'WG': 0, 'OL': 0, 'GOD': 0, 'YOUNG': 0, 'MAD': 0,
                        'ORDO': 0, 'LGN': 0, 'STEVE': 0, 'LOST': 0, 'LI': 0, 'GO': 0, 'LOLI': 0, 'PKMN': 0, 'GUN': 0, 'TAZ': 0, 'BH': 0, 'YT': 0,
                        'SYN': 0, 'NINJA': 0, 'ESP': 0, 'DR': 0, 'PK': 0, 'CW': 0, 'XD': 0, 'RS': 0, 'GOLEM': 0, 'IIAMA': 0, 'IL': 0, 'HANSA': 0, 'YAO': 
                        0, 'ST': 0, '6T9': 0, 'FLO': 0, 'SORRY': 0, 'AEVN': 0, 'MSA': 0, 'TROLL': 0, 'GW': 0, 'AROS': 0, 'GOKU': 0, 'YUZU': 0, 'GEAR': 0, 'IE': 0,
                        'WTH': 0, 'ACE': 0, 'RDS': 0, 'ROYAL': 0, 'KH': 0, 'FT': 0, 'TMG': 0, 'IY': 0, 'W3': 0, 'NEW': 0, 'TTT': 0, 'LT': 0, 'PW': 0,
                        'PAPPY': 0, '403': 0, 'KING': 0, 'FOX': 0, 'YSD': 0, 'NN': 0, 'MARIA': 0, 'OLD': 0, 'ROSE': 0, 'JESSA': 0, 'DAZZ': 0, 'SIR': 0,
                        'RP': 0, 'RSM': 0, '  ILY': 0, 'PWN': 0, 'IV': 0, 'VX': 0, 'ROBBY': 0, 'REN': 0, 'SNAKE': 0, 'GOUL': 0, 'FLOS': 0, 'LBX': 0,
                        'DN': 0, 'SG': 0, 'CUTE': 0, 'SUPER': 0, 'ETN': 0, 'BREAD': 0, 'YAMI': 0, 'GREEN': 0, 'VLOK': 0, 'CASH': 0, 'KAYN': 0, 'SV': 0,
                        'SIAPA': 0, 'KXNG': 0, 'ZERO': 0, 'DIMAS': 0, 'WHO': 0, 'TCM': 0, 'GLOW': 0, 'LDK': 0, 'LX': 0, 'KELLY': 0, 'JANG': 0, 'OLAZ': 0,
                        'THE': 0, 'DIPS': 0, 'GXB': 0, 'TITIT': 0, 'SMOL': 0, 'NEAL': 0, 'SOS': 0, 'FS': 0, 'R13': 0, 'WC2': 0, 'KENJI': 0, 
                        'AG': 0, 'ZIGG': 0, 'MFJ': 0, 'BLUE': 0, 'YAH': 0, 'BILL': 0, 'VAN': 0, 'SOY': 0, 'WAX': 0, 'FBI': 0, 'DUKE': 0, 'APEX': 0,
                        'OOPSY': 0, 'MEYO': 0, '666': 0, 'DADDY': 0, 'MINER': 0, 'NACHT': 0, 'EISA': 0, 'FRTK': 0, 'RRR': 0, 'FAJNA': 0, 'T2': 0,
                        'CFR': 0, 'ION': 0, 'MINI': 0, 'CAKE': 0, 'RANDO': 0, 'OLGA': 0, 'CAP': 0, 'CYCLO': 0, 'LE': 0, 'WAN': 0, 'LV': 0, 'YAN': 0,
                        'CP': 0, 'HMG': 0, 'RED': 0, 'BUZZ': 0, 'GR0': 0, 'A51': 0, 'ISMA': 0, 'THC': 0, 'C137': 0, 'LIAN': 0, 'RON': 0, 'NUB': 0, 'TNS': 0, 
                        'LUCKY': 0, 'SD': 0, 'QL': 0, 'EL': 0, 'DGG': 0, 'DEATH': 0, 'MELEE': 0, 'LQM': 0, 'RIVER': 0, 'KDA': 0, 'GODLY': 0, 'IG': 0, 
                        'AZURE': 0, 'ADNX': 0, 'AK47': 0, 'TETRA': 0, 'KVN': 0, 'BUD': 0, 'FAST': 0, 'CC': 0, 'HONEY': 0, 'YDS': 0, '63': 0, 'OMED': 0,
                        'PIXYZ': 0, 'KOA': 0, 'FROOT': 0, 'ANTI': 0, 'STILL': 0, 'YSO': 0, 'XPLOI': 0, 'BI': 0, 'MC': 0, 'IM': 0, 'LEMON': 0, 'MAOKI': 0,
                        'LEVEL': 0, 'MR': 0, 'THL': 0, 'SAD': 0, '1337': 0, 'ITCHY': 0, 'THOR': 0, 'ROTI': 0, 'WASON': 0, 'FLXW': 0, 'IT': 0, 'RAFA': 0,
                        'MAOU': 0, 'TEXAN': 0, 'HEDGE': 0, 'MLG': 0, 'ISC': 0, 'YOUR': 0, 'GOAT': 0, 'EA': 0, 'PRX': 0, 'OLY': 0, 'BLECK': 0, 'ADAM': 0,
                        'ERBO': 0, 'SZEPT': 0, 'BTW': 0, 'ENZA': 0, 'BL4CK': 0, 'GRB': 0, 'KYOU': 0, 'WORLD': 0, 'XDARK': 0, 'BR': 0, 'LUCAS': 0, 'XZ': 0,
                        'LIL': 0, 'ILI': 0, 'AI': 0, 'TOM': 0, 'CAPT': 0, 'MS': 0, 'LO': 0, 'BD': 0, 'FLOOR': 0, 'LOYAL': 0, 'TRULY': 0, 'AKUTO': 0,
                        'AKT': 0, 'TIGER': 0, 'VND': 0, 'SR': 0, 'GA': 0, 'DMN': 0, 'MANG': 0, 'GM': 0, 'WILL': 0, 'GOLD': 0, 'GK': 0, '808': 0,
                        'RICK': 0, 'ULTR': 0, 'KAMI': 0, 'QUAN': 0, 'FORST': 0, 'DWIKI': 0, 'LBCL': 0, 'EML': 0, 'HUONG': 0, 'AFK': 0, 'NO': 0,
                        'DUCKS': 0, 'XERRA': 0, 'THAT': 0, 'DJ': 0, 'TWO': 0}

guilds_counter_int  = {'p1mp': 0,'IMMORTAL': 0, 'OWO': 0, 'EXP': 0, 'BRX': 0, 'RNG': 0, 'LAT': 0, 'KRG': 0, 'GGWP': 0, 'PVM': 0, 'DTF': 0, 'HSR': 0, 'FG': 0, 
                        'NS': 0, 'AOE': 0, 'NSFW': 0, 'DMG': 0, 'AXIAL': 0, 'PAK': 0, 'T62': 0, 'VLR': 0, 'RYU': 0, 'TI': 0, 'NSL': 0, '1HB': 0, 'FFA': 0,
                        'OG': 0, 'ORAZE': 0, 'BLITZ': 0, 'DTS': 0, 'SOLO': 0, 'BIG': 0, 'TRG': 0, 'CCCP': 0, 'TNT': 0, 'SOW': 0, 'PAPA': 0, 'TH': 0,
                        'EXC': 0, 'PHG': 0, 'SHORN': 0, 'TT': 0, 'UMBRA': 0, 'AK7': 0, 'GG': 0, 'LNH': 0, 'SLP': 0, 'DEAD': 0, 'TCK': 0, 'XP': 0, 
                        'VN': 0, 'XNW': 0, 'DARK': 0, 'FW': 0, 'DAVY': 0, 'DK': 0, 'II': 0, 'RW': 0, 'WG': 0, 'OL': 0, 'GOD': 0, 'YOUNG': 0, 'MAD': 0,
                        'ORDO': 0, 'LGN': 0, 'STEVE': 0, 'LOST': 0, 'LI': 0, 'GO': 0, 'LOLI': 0, 'PKMN': 0, 'GUN': 0, 'TAZ': 0, 'BH': 0, 'YT': 0,
                        'SYN': 0, 'NINJA': 0, 'ESP': 0, 'DR': 0, 'PK': 0, 'CW': 0, 'XD': 0, 'RS': 0, 'GOLEM': 0, 'IIAMA': 0, 'IL': 0, 'HANSA': 0, 'YAO': 0,
                        'ST': 0, '6T9': 0, 'FLO': 0, 'SORRY': 0, 'AEVN': 0, 'MSA': 0, 'TROLL': 0, 'GW': 0, 'AROS': 0, 'GOKU': 0, 'YUZU': 0, 'GEAR': 0, 'IE': 0,
                        'WTH': 0, 'ACE': 0, 'RDS': 0, 'ROYAL': 0, 'KH': 0, 'FT': 0, 'TMG': 0, 'IY': 0, 'W3': 0, 'NEW': 0, 'TTT': 0, 'LT': 0, 'PW': 0,
                        'PAPPY': 0, '403': 0, 'KING': 0, 'FOX': 0, 'YSD': 0, 'NN': 0, 'MARIA': 0, 'OLD': 0, 'ROSE': 0, 'JESSA': 0, 'DAZZ': 0, 'SIR': 0,
                        'RP': 0, 'RSM': 0, '  ILY': 0, 'PWN': 0, 'IV': 0, 'VX': 0, 'ROBBY': 0, 'REN': 0, 'SNAKE': 0, 'GOUL': 0, 'FLOS': 0, 'LBX': 0,
                        'DN': 0, 'SG': 0, 'CUTE': 0, 'SUPER': 0, 'ETN': 0, 'BREAD': 0, 'YAMI': 0, 'GREEN': 0, 'VLOK': 0, 'CASH': 0, 'KAYN': 0, 'SV': 0,
                        'SIAPA': 0, 'KXNG': 0, 'ZERO': 0, 'DIMAS': 0, 'WHO': 0, 'TCM': 0, 'GLOW': 0, 'LDK': 0, 'LX': 0, 'KELLY': 0, 'JANG': 0, 'OLAZ': 0,
                        'THE': 0, 'DIPS': 0, 'GXB': 0, 'TITIT': 0, 'SMOL': 0, 'NEAL': 0, 'SOS': 0, 'FS': 0, 'R13': 0, 'WC2': 0, 'KENJI': 0, 
                        'AG': 0, 'ZIGG': 0, 'MFJ': 0, 'BLUE': 0, 'YAH': 0, 'BILL': 0, 'VAN': 0, 'SOY': 0, 'WAX': 0, 'FBI': 0, 'DUKE': 0, 'APEX': 0,
                        'OOPSY': 0, 'MEYO': 0, '666': 0, 'DADDY': 0, 'MINER': 0, 'NACHT': 0, 'EISA': 0, 'FRTK': 0, 'RRR': 0, 'FAJNA': 0, 'T2': 0,
                        'CFR': 0, 'ION': 0, 'MINI': 0, 'CAKE': 0, 'RANDO': 0, 'OLGA': 0, 'CAP': 0, 'CYCLO': 0, 'LE': 0, 'WAN': 0, 'LV': 0, 'YAN': 0,
                        'CP': 0, 'HMG': 0, 'RED': 0, 'BUZZ': 0, 'GR0': 0, 'A51': 0, 'ISMA': 0, 'THC': 0, 'C137': 0, 'LIAN': 0, 'RON': 0, 'NUB': 0, 'TNS': 0, 
                        'LUCKY': 0, 'SD': 0, 'QL': 0, 'EL': 0, 'DGG': 0, 'DEATH': 0, 'MELEE': 0, 'LQM': 0, 'RIVER': 0, 'KDA': 0, 'GODLY': 0, 'IG': 0, 
                        'AZURE': 0, 'ADNX': 0, 'AK47': 0, 'TETRA': 0, 'KVN': 0, 'BUD': 0, 'FAST': 0, 'CC': 0, 'HONEY': 0, 'YDS': 0, '63': 0, 'OMED': 0,
                        'PIXYZ': 0, 'KOA': 0, 'FROOT': 0, 'ANTI': 0, 'STILL': 0, 'YSO': 0, 'XPLOI': 0, 'BI': 0, 'MC': 0, 'IM': 0, 'LEMON': 0, 'MAOKI': 0,
                        'LEVEL': 0, 'MR': 0, 'THL': 0, 'SAD': 0, '1337': 0, 'ITCHY': 0, 'THOR': 0, 'ROTI': 0, 'WASON': 0, 'FLXW': 0, 'IT': 0, 'RAFA': 0,
                        'MAOU': 0, 'TEXAN': 0, 'HEDGE': 0, 'MLG': 0, 'ISC': 0, 'YOUR': 0, 'GOAT': 0, 'EA': 0, 'PRX': 0, 'OLY': 0, 'BLECK': 0, 'ADAM': 0,
                        'ERBO': 0, 'SZEPT': 0, 'BTW': 0, 'ENZA': 0, 'BL4CK': 0, 'GRB': 0, 'KYOU': 0, 'WORLD': 0, 'XDARK': 0, 'BR': 0, 'LUCAS': 0, 'XZ': 0,
                        'LIL': 0, 'ILI': 0, 'AI': 0, 'TOM': 0, 'CAPT': 0, 'MS': 0, 'LO': 0, 'BD': 0, 'FLOOR': 0, 'LOYAL': 0, 'TRULY': 0, 'AKUTO': 0,
                        'AKT': 0, 'TIGER': 0, 'VND': 0, 'SR': 0, 'GA': 0, 'DMN': 0, 'MANG': 0, 'GM': 0, 'WILL': 0, 'GOLD': 0, 'GK': 0, '808': 0,
                        'RICK': 0, 'ULTR': 0, 'KAMI': 0, 'QUAN': 0, 'FORST': 0, 'DWIKI': 0, 'LBCL': 0, 'EML': 0, 'HUONG': 0, 'AFK': 0, 'NO': 0,
                        'DUCKS': 0, 'XERRA': 0, 'THAT': 0, 'DJ': 0, 'TWO': 0}

lvltab = [0,46,99,159,229,309,401,507,628,768,928,1112,1324,1567,1847,2168,2537,2961,3448,4008,4651,5389,6237,7212,8332,9618,11095,12792,14742,16982,19555,22510,25905,29805,34285,
39431,45342,52132,59932,68892,79184,91006,104586,120186,138106,158690,182335,209496,240696,276536,317705,364996,419319,481720,553400,635738,730320,838966,963768,1107128,1271805,
1460969,1678262,1927866,2214586,2543940,2922269,3356855,3856063,4429503,5088212,5844870,6714042,7712459,8859339,10176758,11690075,13428420,15425254,17719014,20353852,23380486,
26857176,30850844,35438364,40708040,46761308,53714688,61702024,70877064,81416417,93522954,107429714,123404386,141754466,162833172,187046247,214859767,246809111,283509271,325666684,
374092835,429719875,493618564,567018884,651333710,748186012,859440093,987237472,1134038112,1302667765,1496372370,1718880532,1974475291,2268076571,2605335878,2992745089,3437761413,
3948950932,4536153492,5210672106]

lvldef = [46, 53, 60, 70, 80, 92, 106, 121, 140, 160, 184, 212, 243, 280, 321, 369, 424, 487, 560, 643, 738, 848, 975, 1120, 1286, 1477, 1697, 1950, 2240, 2573, 2955, 3395, 3900, 
4480, 5146, 5911, 6790, 7800, 8960, 10292, 11822, 13580, 15600, 17920, 20584, 23645, 27161, 31200, 35840, 41169, 47291, 54323, 62401, 71680, 82338, 94582, 108646, 124802, 143360, 
164677, 189164, 217293, 249604, 286720, 329354, 378329, 434586, 499208, 573440, 658709, 756658, 869172, 998417, 1146880, 1317419, 1513317, 1738345, 1996834, 2293760, 2634838, 3026634, 
3476690, 3993668, 4587520, 5269676, 6053268, 6953380, 7987336, 9175040, 10539353, 12106537, 13906760, 15974672, 18350080, 21078706, 24213075, 27813520, 31949344, 36700160, 42157413, 
48426151, 55627040, 63898689, 73400320, 84314826, 96852302, 111254081, 127797379, 146800640, 168629653, 193704605, 222508162, 255594759, 293601280, 337259307, 387409211, 445016324, 
511189519, 587202560]
#######################################################
members_log= [
 {'member_name': 'OwO Harvey', 'combat_xp': 380951225 ,'mining_xp': 102287084, 'smithing_xp': 46043608,'woodcutting_xp': 20682077, 'crafting_xp': 4472966,'fishing_xp':  6118541, 'cooking_xp': 12300}
,{'member_name': 'OwO Cash Money', 'combat_xp': 0, 'mining_xp': 72217800, 'smithing_xp': 571649872, 'woodcutting_xp': 80374322, 'crafting_xp': 87208852, 'fishing_xp': 380975865, 'cooking_xp': 283624900}
,{'member_name': 'OwO Silent', 'combat_xp': 4536153492, 'mining_xp': 434930717, 'smithing_xp': 38297515, 'woodcutting_xp': 326025445, 'crafting_xp': 568024172, 'fishing_xp': 494397160, 'cooking_xp': 349145655}
,{'member_name': 'OwO TheDuck', 'combat_xp': 2480568998, 'mining_xp': 145858839, 'smithing_xp': 288239664, 'woodcutting_xp': 187076760, 'crafting_xp': 145225480, 'fishing_xp': 988740825, 'cooking_xp': 942283975}
,{'member_name': 'OwO Mirage', 'combat_xp': 1998833812, 'mining_xp': 45843639, 'smithing_xp': 37058503, 'woodcutting_xp': 42949750, 'crafting_xp': 28025409, 'fishing_xp': 120849670, 'cooking_xp': 9061805}
,{'member_name': 'OwO Thor', 'combat_xp': 1683161651, 'mining_xp': 146755113, 'smithing_xp': 71685688, 'woodcutting_xp': 153284740, 'crafting_xp': 82607529, 'fishing_xp': 72092275, 'cooking_xp': 84832115}
,{'member_name': 'OwO DaveDust', 'combat_xp': 1302727611, 'mining_xp': 39758525, 'smithing_xp': 35863055, 'woodcutting_xp': 54285760, 'crafting_xp': 42346404, 'fishing_xp': 360672865, 'cooking_xp': 305686845}
,{'member_name': 'OwO Tempy', 'combat_xp': 1283220108, 'mining_xp': 12184195, 'smithing_xp': 14432547, 'woodcutting_xp': 20410260, 'crafting_xp': 13887705, 'fishing_xp': 0, 'cooking_xp': 0}
,{'member_name': 'OwO Tantrid', 'combat_xp': 1194593053, 'mining_xp': 285136798, 'smithing_xp': 674936361, 'woodcutting_xp': 283527964, 'crafting_xp': 331371229, 'fishing_xp': 4536153492, 'cooking_xp': 4536153492}
,{'member_name': 'OwO Smith', 'combat_xp': 1184124500, 'mining_xp': 87527718, 'smithing_xp': 36477810, 'woodcutting_xp': 44205515, 'crafting_xp': 18187330, 'fishing_xp': 21304150, 'cooking_xp': 1319520}
,{'member_name': 'OwO Freaka', 'combat_xp': 1037575033, 'mining_xp': 171178150, 'smithing_xp': 325929952, 'woodcutting_xp': 246859245, 'crafting_xp': 215101770, 'fishing_xp': 615519105, 'cooking_xp': 434823380}
,{'member_name': 'OwO DirtyShots', 'combat_xp': 987237472, 'mining_xp': 667773401, 'smithing_xp': 342313218, 'woodcutting_xp': 511729755, 'crafting_xp': 289025531, 'fishing_xp': 862342950, 'cooking_xp': 519790370}
,{'member_name': 'OwO h0lka', 'combat_xp': 915011175, 'mining_xp': 43937350, 'smithing_xp': 46783385, 'woodcutting_xp': 123004482, 'crafting_xp': 38372381, 'fishing_xp': 567047225, 'cooking_xp': 374303670}
,{'member_name': 'OwO TheWitcher', 'combat_xp': 859440777, 'mining_xp': 170410056, 'smithing_xp': 117889730, 'woodcutting_xp': 196658670, 'crafting_xp': 299417602, 'fishing_xp': 1311420385, 'cooking_xp': 1013956155}
,{'member_name': 'OwO Krieger', 'combat_xp': 859440093, 'mining_xp': 4499904550, 'smithing_xp': 39305644, 'woodcutting_xp': 14778425, 'crafting_xp': 35439719, 'fishing_xp': 771023825, 'cooking_xp': 658520965}
,{'member_name': 'OwO Dryness', 'combat_xp': 859440093, 'mining_xp': 60431676, 'smithing_xp': 78275917, 'woodcutting_xp': 56538139, 'crafting_xp': 208574471, 'fishing_xp': 18982074, 'cooking_xp': 276996}
,{'member_name': 'OwO Salty', 'combat_xp': 848912823, 'mining_xp': 266909773, 'smithing_xp': 109159845, 'woodcutting_xp': 37271671, 'crafting_xp': 72269728, 'fishing_xp': 117001040, 'cooking_xp': 126911255}
,{'member_name': 'OwO TJ', 'combat_xp': 807088082, 'mining_xp': 98804362, 'smithing_xp': 54320853, 'woodcutting_xp': 149518275, 'crafting_xp': 290280079, 'fishing_xp': 267399720, 'cooking_xp': 229217490}
,{'member_name': 'OwO Spooniest', 'combat_xp': 779208393, 'mining_xp': 24384717, 'smithing_xp': 71219984, 'woodcutting_xp': 31048599, 'crafting_xp': 54306335, 'fishing_xp': 81602405, 'cooking_xp': 2124295}
,{'member_name': 'OwO DarkSecret', 'combat_xp': 703432955, 'mining_xp': 316161665, 'smithing_xp': 44280505, 'woodcutting_xp': 1147056874, 'crafting_xp': 92416285, 'fishing_xp': 1041853145, 'cooking_xp': 521915000}
,{'member_name': 'OwO Moist', 'combat_xp': 664036177, 'mining_xp': 77347705, 'smithing_xp': 36052130, 'woodcutting_xp': 49270465, 'crafting_xp': 4511019, 'fishing_xp': 131855, 'cooking_xp': 0}
,{'member_name': 'OwO Matt', 'combat_xp': 651348745, 'mining_xp': 411713601, 'smithing_xp': 311267451, 'woodcutting_xp': 2108016845, 'crafting_xp': 296289070, 'fishing_xp': 1068048830, 'cooking_xp': 296459105}
,{'member_name': 'OwO Aeonic', 'combat_xp': 603847678, 'mining_xp': 9310626, 'smithing_xp': 10870890, 'woodcutting_xp': 9393815, 'crafting_xp': 10975635, 'fishing_xp': 11355405, 'cooking_xp': 9272265}
,{'member_name': 'OwO Olive Yew', 'combat_xp': 592973660, 'mining_xp': 178915811, 'smithing_xp': 38585043, 'woodcutting_xp': 118541613, 'crafting_xp': 71008466, 'fishing_xp': 148462761, 'cooking_xp': 32376134}
,{'member_name': 'OwO KcAlex', 'combat_xp': 588527449, 'mining_xp': 12436562, 'smithing_xp': 36038091, 'woodcutting_xp': 42589920, 'crafting_xp': 22935718, 'fishing_xp': 0, 'cooking_xp': 300}
,{'member_name': 'OwO Messwithme', 'combat_xp': 567022637, 'mining_xp': 141772875, 'smithing_xp': 72005129, 'woodcutting_xp': 70881545, 'crafting_xp': 21765459, 'fishing_xp': 101868080, 'cooking_xp': 82980995}
,{'member_name': 'OwO CromacK', 'combat_xp': 509772893, 'mining_xp': 14245643, 'smithing_xp': 35688196, 'woodcutting_xp': 6901564, 'crafting_xp': 4673435, 'fishing_xp': 1813618, 'cooking_xp': 0}
,{'member_name': 'OwO Kreat', 'combat_xp': 494707606, 'mining_xp': 155072785, 'smithing_xp': 39826946, 'woodcutting_xp': 25095915, 'crafting_xp': 11983715, 'fishing_xp': 2244415, 'cooking_xp': 896038}
,{'member_name': 'OwO Cerez Jr', 'combat_xp': 439302748, 'mining_xp': 189314571, 'smithing_xp': 679630358, 'woodcutting_xp': 83015910, 'crafting_xp': 567078184, 'fishing_xp': 2297413410, 'cooking_xp': 1936958831}
,{'member_name': 'OwO DigiPope', 'combat_xp': 429723533, 'mining_xp': 33682480, 'smithing_xp': 44981244, 'woodcutting_xp': 46277305, 'crafting_xp': 38537640, 'fishing_xp': 125722205, 'cooking_xp': 110534310}
,{'member_name': 'OwO Roy Donk', 'combat_xp': 388919055, 'mining_xp': 20574375, 'smithing_xp': 36167460, 'woodcutting_xp': 9357260, 'crafting_xp': 27479794, 'fishing_xp': 8859935, 'cooking_xp': 0}
,{'member_name': 'OwO Maxxd', 'combat_xp': 385350722, 'mining_xp': 18315543, 'smithing_xp': 74751475, 'woodcutting_xp': 20958545, 'crafting_xp': 453369105, 'fishing_xp': 170191720, 'cooking_xp': 36719225}
,{'member_name': 'OwO Heartman', 'combat_xp': 374143480, 'mining_xp': 193841661, 'smithing_xp': 37292892, 'woodcutting_xp': 252102435, 'crafting_xp': 18219729, 'fishing_xp': 86910175, 'cooking_xp': 1164670}
,{'member_name': 'OwO MrBrisingr', 'combat_xp': 374092835, 'mining_xp': 9988395, 'smithing_xp': 5220915, 'woodcutting_xp': 50149300, 'crafting_xp': 20509603, 'fishing_xp': 78827610, 'cooking_xp': 73447640}
,{'member_name': 'OwO Yekzer', 'combat_xp': 374092835, 'mining_xp': 70974620, 'smithing_xp': 2638695736, 'woodcutting_xp': 70895257, 'crafting_xp': 1610781219, 'fishing_xp': 794134520, 'cooking_xp': 4501885}
,{'member_name': 'OwO Bucketss', 'combat_xp': 342392423, 'mining_xp': 5329230, 'smithing_xp': 114270310, 'woodcutting_xp': 7175805, 'crafting_xp': 17786971, 'fishing_xp': 2872325, 'cooking_xp': 9614430}
,{'member_name': 'OwO Crixal', 'combat_xp': 318804144, 'mining_xp': 16181067, 'smithing_xp': 36428348, 'woodcutting_xp': 28557512, 'crafting_xp': 28658408, 'fishing_xp': 11367641, 'cooking_xp': 861441}
,{'member_name': 'OwO Panda', 'combat_xp': 317333694, 'mining_xp': 283526958, 'smithing_xp': 283544071, 'woodcutting_xp': 293112912, 'crafting_xp': 283818557, 'fishing_xp': 299481955, 'cooking_xp': 283584860}
,{'member_name': 'OwO AnimeHDD', 'combat_xp': 308126090, 'mining_xp': 12797890, 'smithing_xp': 36492905, 'woodcutting_xp': 1189545, 'crafting_xp': 2440014, 'fishing_xp': 464830, 'cooking_xp': 337335}
,{'member_name': 'OwO RunPerge', 'combat_xp': 299145165, 'mining_xp': 17750437, 'smithing_xp': 35820106, 'woodcutting_xp': 16842165, 'crafting_xp': 554836, 'fishing_xp': 884120, 'cooking_xp': 105155}
,{'member_name': 'OwO TechNus09', 'combat_xp': 295469035, 'mining_xp': 74280443, 'smithing_xp': 47043361, 'woodcutting_xp': 133854001, 'crafting_xp': 70881395, 'fishing_xp': 83854421, 'cooking_xp': 82229449}
,{'member_name': 'OwO Titan', 'combat_xp': 289896159, 'mining_xp': 11365880, 'smithing_xp': 5391161, 'woodcutting_xp': 5616485, 'crafting_xp': 4197884, 'fishing_xp': 2940, 'cooking_xp': 260}
,{'member_name': 'OwO Mullet', 'combat_xp': 285391282, 'mining_xp': 0, 'smithing_xp': 0, 'woodcutting_xp': 575830, 'crafting_xp': 8175, 'fishing_xp': 0, 'cooking_xp': 0}
,{'member_name': 'OwO Yec', 'combat_xp': 283945565, 'mining_xp': 73952614, 'smithing_xp': 71447863, 'woodcutting_xp': 13471135, 'crafting_xp': 9727155, 'fishing_xp': 1480, 'cooking_xp': 600}
,{'member_name': 'OwO AcePar', 'combat_xp': 283518875, 'mining_xp': 56706684, 'smithing_xp': 36665501, 'woodcutting_xp': 5399014, 'crafting_xp': 17769520, 'fishing_xp': 7125150, 'cooking_xp': 1627285}
,{'member_name': 'OwO Rage', 'combat_xp': 270575983, 'mining_xp': 19249067, 'smithing_xp': 45219367, 'woodcutting_xp': 3028815, 'crafting_xp': 866155, 'fishing_xp': 1312027, 'cooking_xp': 109407}
,{'member_name': 'OwO Dzoga', 'combat_xp': 260924809, 'mining_xp': 6068244, 'smithing_xp': 6011502, 'woodcutting_xp': 3334895, 'crafting_xp': 2830952, 'fishing_xp': 82755, 'cooking_xp': 7560}
,{'member_name': 'OwO Skitter', 'combat_xp': 253075776, 'mining_xp': 4879880, 'smithing_xp': 5086185, 'woodcutting_xp': 6236370, 'crafting_xp': 3085949, 'fishing_xp': 0, 'cooking_xp': 0}
,{'member_name': 'OwO Cool Adam', 'combat_xp': 247373540, 'mining_xp': 60690388, 'smithing_xp': 35616093, 'woodcutting_xp': 32006820, 'crafting_xp': 22894466, 'fishing_xp': 178133165, 'cooking_xp': 71066815}
,{'member_name': 'OwO Jaf', 'combat_xp': 220515307, 'mining_xp': 32855285, 'smithing_xp': 11918715, 'woodcutting_xp': 17729235, 'crafting_xp': 9228623, 'fishing_xp': 17721730, 'cooking_xp': 37140}
,{'member_name': 'OwO Maddy', 'combat_xp': 216416629, 'mining_xp': 29009950, 'smithing_xp': 37032898, 'woodcutting_xp': 45025093, 'crafting_xp': 8217718, 'fishing_xp': 103135385, 'cooking_xp': 2410}
,{'member_name': 'OwO Hentai', 'combat_xp': 190593110, 'mining_xp': 15620943, 'smithing_xp': 12011087, 'woodcutting_xp': 2755105, 'crafting_xp': 3687784, 'fishing_xp': 6023785, 'cooking_xp': 811995}
,{'member_name': 'OwO Scarthach', 'combat_xp': 182120573, 'mining_xp': 9196558, 'smithing_xp': 4849684, 'woodcutting_xp': 10529405, 'crafting_xp': 570273, 'fishing_xp': 142145, 'cooking_xp': 0}
,{'member_name': 'OwO SAVYS', 'combat_xp': 176380744, 'mining_xp': 2441115, 'smithing_xp': 7426229, 'woodcutting_xp': 10182895, 'crafting_xp': 11631210, 'fishing_xp': 8495, 'cooking_xp': 520}
,{'member_name': 'OwO Bunkie', 'combat_xp': 172678675, 'mining_xp': 23790890, 'smithing_xp': 36857835, 'woodcutting_xp': 65625205, 'crafting_xp': 53661737, 'fishing_xp': 3728305, 'cooking_xp': 357380}
,{'member_name': 'OwO Senku', 'combat_xp': 153437055, 'mining_xp': 1540690, 'smithing_xp': 2238374, 'woodcutting_xp': 0, 'crafting_xp': 0, 'fishing_xp': 0, 'cooking_xp': 0}
,{'member_name': 'OwO Doony', 'combat_xp': 151975781, 'mining_xp': 0, 'smithing_xp': 4766684, 'woodcutting_xp': 90585, 'crafting_xp': 27126, 'fishing_xp': 0, 'cooking_xp': 0}
,{'member_name': 'OwO J Sins', 'combat_xp': 151568852, 'mining_xp': 3186736, 'smithing_xp': 4557622, 'woodcutting_xp': 333710, 'crafting_xp': 107231, 'fishing_xp': 2520, 'cooking_xp': 0}
,{'member_name': 'OwO PUZZLE', 'combat_xp': 148505016, 'mining_xp': 3992406, 'smithing_xp': 6183521, 'woodcutting_xp': 3775725, 'crafting_xp': 239629, 'fishing_xp': 21860, 'cooking_xp': 0}
,{'member_name': 'OwO Crusha', 'combat_xp': 147897427, 'mining_xp': 9784845, 'smithing_xp': 9752586, 'woodcutting_xp': 4869670, 'crafting_xp': 0, 'fishing_xp': 0, 'cooking_xp': 0}
,{'member_name': 'OwO John', 'combat_xp': 141754466, 'mining_xp': 7470352, 'smithing_xp': 4629371, 'woodcutting_xp': 157670050, 'crafting_xp': 6714233, 'fishing_xp': 126225, 'cooking_xp': 42490}
,{'member_name': 'OwO Dribbyl', 'combat_xp': 139998773, 'mining_xp': 4982770, 'smithing_xp': 2749452, 'woodcutting_xp': 3279390, 'crafting_xp': 916466, 'fishing_xp': 289334, 'cooking_xp': 0}
,{'member_name': 'OwO Pabs', 'combat_xp': 125968392, 'mining_xp': 36961382, 'smithing_xp': 73224824, 'woodcutting_xp': 37252625, 'crafting_xp': 17901626, 'fishing_xp': 70896074, 'cooking_xp': 70997780}
,{'member_name': 'OwO Chez', 'combat_xp': 124192749, 'mining_xp': 5615105, 'smithing_xp': 5620815, 'woodcutting_xp': 832270, 'crafting_xp': 526895, 'fishing_xp': 17145, 'cooking_xp': 6735}
,{'member_name': 'OwO Birb', 'combat_xp': 123419360, 'mining_xp': 18828698, 'smithing_xp': 10811748, 'woodcutting_xp': 28548235, 'crafting_xp': 7150639, 'fishing_xp': 1117020, 'cooking_xp': 338715}
,{'member_name': 'OwO DaddyShark', 'combat_xp': 116032361, 'mining_xp': 14274720, 'smithing_xp': 5171950, 'woodcutting_xp': 14077395, 'crafting_xp': 1609984, 'fishing_xp': 1205005, 'cooking_xp': 11660}
,{'member_name': 'OwO Xbl', 'combat_xp': 113372379, 'mining_xp': 16495791, 'smithing_xp': 5374281, 'woodcutting_xp': 6803390, 'crafting_xp': 1773503, 'fishing_xp': 3061515, 'cooking_xp': 0}
,{'member_name': 'OwO Gage', 'combat_xp': 112544628, 'mining_xp': 3748015, 'smithing_xp': 4802609, 'woodcutting_xp': 2777560, 'crafting_xp': 13195, 'fishing_xp': 0, 'cooking_xp': 0}
,{'member_name': 'OwO Avi', 'combat_xp': 108338199, 'mining_xp': 146579689, 'smithing_xp': 71215959, 'woodcutting_xp': 91479710, 'crafting_xp': 17757762, 'fishing_xp': 287940840, 'cooking_xp': 20363337}
,{'member_name': 'OwO l Derek l', 'combat_xp': 107529128, 'mining_xp': 10962230, 'smithing_xp': 5120211, 'woodcutting_xp': 5452785, 'crafting_xp': 4682380, 'fishing_xp': 10020070, 'cooking_xp': 2335640}
,{'member_name': 'OwO PeeterIV', 'combat_xp': 100058273, 'mining_xp': 5084010, 'smithing_xp': 3292287, 'woodcutting_xp': 3254040, 'crafting_xp': 1547415, 'fishing_xp': 507655, 'cooking_xp': 770}
,{'member_name': 'OwO Shadow', 'combat_xp': 92663806, 'mining_xp': 8729642, 'smithing_xp': 2389356, 'woodcutting_xp': 555985, 'crafting_xp': 19718, 'fishing_xp': 4432300, 'cooking_xp': 278070}
,{'member_name': 'OwO Schnee', 'combat_xp': 83090598, 'mining_xp': 14468875, 'smithing_xp': 6052183, 'woodcutting_xp': 3057745, 'crafting_xp': 421832, 'fishing_xp': 150125, 'cooking_xp': 180}
,{'member_name': 'OwO Buttcrack', 'combat_xp': 77035962, 'mining_xp': 1721454, 'smithing_xp': 6102324, 'woodcutting_xp': 1722895, 'crafting_xp': 461386, 'fishing_xp': 1530, 'cooking_xp': 590}
,{'member_name': 'OwO DummyThicc', 'combat_xp': 74034889, 'mining_xp': 6257964, 'smithing_xp': 4892240, 'woodcutting_xp': 816770, 'crafting_xp': 76813, 'fishing_xp': 0, 'cooking_xp': 773755}
,{'member_name': 'OwO Necrotic', 'combat_xp': 73501222, 'mining_xp': 32443416, 'smithing_xp': 19985521, 'woodcutting_xp': 97857950, 'crafting_xp': 5605001, 'fishing_xp': 1579270, 'cooking_xp': 285285}
,{'member_name': 'OwO Stoned', 'combat_xp': 71975295, 'mining_xp': 17719865, 'smithing_xp': 14993404, 'woodcutting_xp': 110385715, 'crafting_xp': 8868619, 'fishing_xp': 73600400, 'cooking_xp': 4447290}
,{'member_name': 'OwO Tzak', 'combat_xp': 63616298, 'mining_xp': 1092055, 'smithing_xp': 2355197, 'woodcutting_xp': 0, 'crafting_xp': 0, 'fishing_xp': 752015, 'cooking_xp': 150}
,{'member_name': 'OwO Kona', 'combat_xp': 63380181, 'mining_xp': 8399985, 'smithing_xp': 2877686, 'woodcutting_xp': 110710830, 'crafting_xp': 23704144, 'fishing_xp': 48590, 'cooking_xp': 630}
,{'member_name': 'OwO Glitchy', 'combat_xp': 58346783, 'mining_xp': 2646688, 'smithing_xp': 12324401, 'woodcutting_xp': 0, 'crafting_xp': 13244, 'fishing_xp': 56105, 'cooking_xp': 0}
,{'member_name': 'OwO Bighhhh', 'combat_xp': 57580647, 'mining_xp': 2894365, 'smithing_xp': 2484143, 'woodcutting_xp': 986220, 'crafting_xp': 161296, 'fishing_xp': 1214890, 'cooking_xp': 0}
,{'member_name': 'OwO White', 'combat_xp': 54076568, 'mining_xp': 5545070, 'smithing_xp': 4598558, 'woodcutting_xp': 4660140, 'crafting_xp': 3121791, 'fishing_xp': 405975, 'cooking_xp': 410685}
,{'member_name': 'OwO SeikoYuki', 'combat_xp': 46908281, 'mining_xp': 10445510, 'smithing_xp': 2424721, 'woodcutting_xp': 2289275, 'crafting_xp': 505647, 'fishing_xp': 0, 'cooking_xp': 0}
,{'member_name': 'OwO Mr Yusuf', 'combat_xp': 44477792, 'mining_xp': 4461648, 'smithing_xp': 4510058, 'woodcutting_xp': 503407, 'crafting_xp': 156639, 'fishing_xp': 219475, 'cooking_xp': 3390}
,{'member_name': 'OwO ryry', 'combat_xp': 40269886, 'mining_xp': 0, 'smithing_xp': 2282571, 'woodcutting_xp': 146980, 'crafting_xp': 44754, 'fishing_xp': 0, 'cooking_xp': 270}
,{'member_name': 'OwO Durps', 'combat_xp': 39814493, 'mining_xp': 0, 'smithing_xp': 0, 'woodcutting_xp': 0, 'crafting_xp': 0, 'fishing_xp': 0, 'cooking_xp': 0}
,{'member_name': 'OwO KaitoZezo', 'combat_xp': 38302811, 'mining_xp': 1230645, 'smithing_xp': 2415170, 'woodcutting_xp': 51485, 'crafting_xp': 9279, 'fishing_xp': 35460, 'cooking_xp': 380}
,{'member_name': 'OwO Bowl', 'combat_xp': 35438364, 'mining_xp': 12459674, 'smithing_xp': 4660272, 'woodcutting_xp': 4441035, 'crafting_xp': 2945475, 'fishing_xp': 965280, 'cooking_xp': 0}
,{'member_name': 'OwO Vick Vega', 'combat_xp': 28925941, 'mining_xp': 4801020, 'smithing_xp': 45726293, 'woodcutting_xp': 4663700, 'crafting_xp': 8928437, 'fishing_xp': 1657578, 'cooking_xp': 868738}
,{'member_name': 'OwO Doody', 'combat_xp': 28662628, 'mining_xp': 7314382, 'smithing_xp': 2292451, 'woodcutting_xp': 1512512, 'crafting_xp': 1116252, 'fishing_xp': 392490, 'cooking_xp': 277455}
,{'member_name': 'OwO Skaifox', 'combat_xp': 19993719, 'mining_xp': 89960510, 'smithing_xp': 83522374, 'woodcutting_xp': 6298441, 'crafting_xp': 1998198, 'fishing_xp': 0, 'cooking_xp': 0}
,{'member_name': 'OwO Aurora', 'combat_xp': 18595271, 'mining_xp': 812160, 'smithing_xp': 235267, 'woodcutting_xp': 2370175, 'crafting_xp': 584667, 'fishing_xp': 0, 'cooking_xp': 0}
,{'member_name': 'OwO Smiley', 'combat_xp': 17811922, 'mining_xp': 4556225, 'smithing_xp': 4614662, 'woodcutting_xp': 383145, 'crafting_xp': 93236, 'fishing_xp': 0, 'cooking_xp': 0}
,{'member_name': 'OwO Redro', 'combat_xp': 16367424, 'mining_xp': 2332950, 'smithing_xp': 2313729, 'woodcutting_xp': 779052, 'crafting_xp': 139429, 'fishing_xp': 69353, 'cooking_xp': 1100}
,{'member_name': 'OWO Sriddec', 'combat_xp': 11625931, 'mining_xp': 16299955, 'smithing_xp': 4733924, 'woodcutting_xp': 1743300, 'crafting_xp': 876592, 'fishing_xp': 44850, 'cooking_xp': 31660}
,{'member_name': 'OwO Bank', 'combat_xp': 10329562, 'mining_xp': 0, 'smithing_xp': 0, 'woodcutting_xp': 139725, 'crafting_xp': 0, 'fishing_xp': 13195, 'cooking_xp': 0}
,{'member_name': 'OwO CromacK Jr', 'combat_xp': 8291630, 'mining_xp': 0, 'smithing_xp': 0, 'woodcutting_xp': 0, 'crafting_xp': 0, 'fishing_xp': 0, 'cooking_xp': 0}
,{'member_name': 'OwO AJ', 'combat_xp': 7651894, 'mining_xp': 1346365, 'smithing_xp': 203211, 'woodcutting_xp': 1184716, 'crafting_xp': 1139869, 'fishing_xp': 2914380, 'cooking_xp': 1108766}
,{'member_name': 'OwO MessEh', 'combat_xp': 4950297, 'mining_xp': 0, 'smithing_xp': 0, 'woodcutting_xp': 0, 'crafting_xp': 0, 'fishing_xp': 0, 'cooking_xp': 0}
,{'member_name': 'OwO Zoidberg', 'combat_xp': 4699445, 'mining_xp': 11690900, 'smithing_xp': 11015178, 'woodcutting_xp': 142790, 'crafting_xp': 18923, 'fishing_xp': 3250, 'cooking_xp': 0}
,{'member_name': 'OwO Goat Bank', 'combat_xp': 4429503, 'mining_xp': 0, 'smithing_xp': 0, 'woodcutting_xp': 0, 'crafting_xp': 0, 'fishing_xp': 0, 'cooking_xp': 0}
,{'member_name': 'OwO GaRgAmEL', 'combat_xp': 3330713, 'mining_xp': 0, 'smithing_xp': 0, 'woodcutting_xp': 0, 'crafting_xp': 0, 'fishing_xp': 0, 'cooking_xp': 0}
,{'member_name': 'OwO Tasty', 'combat_xp': 0, 'mining_xp': 291887733, 'smithing_xp': 4572137, 'woodcutting_xp': 0, 'crafting_xp': 0, 'fishing_xp': 0, 'cooking_xp': 0}
,{'member_name': 'OwO Hnngh', 'combat_xp': 0, 'mining_xp': 196805671, 'smithing_xp': 13700032, 'woodcutting_xp': 206652414, 'crafting_xp': 14374325, 'fishing_xp': 0, 'cooking_xp': 0}
,{'member_name': 'OwO Lonely', 'combat_xp': 0, 'mining_xp': 1051140, 'smithing_xp': 1142029, 'woodcutting_xp': 0, 'crafting_xp': 0, 'fishing_xp': 0, 'cooking_xp': 0}
,{'member_name': 'OwO Fake User', 'combat_xp': 0, 'mining_xp': 457730, 'smithing_xp': 308077, 'woodcutting_xp': 98604, 'crafting_xp': 30939, 'fishing_xp': 669367, 'cooking_xp': 11218}
,{'member_name': 'OwO Life', 'combat_xp': 0, 'mining_xp': 0, 'smithing_xp': 0, 'woodcutting_xp': 523275, 'crafting_xp': 0, 'fishing_xp': 0, 'cooking_xp': 0}
,{'member_name': 'OwO Uncloud', 'combat_xp': 0, 'mining_xp': 0, 'smithing_xp': 0, 'woodcutting_xp': 309163, 'crafting_xp': 107675, 'fishing_xp': 0, 'cooking_xp': 0}
,{'member_name': 'OwO goout', 'combat_xp': 0, 'mining_xp': 0, 'smithing_xp': 0, 'woodcutting_xp': 176794, 'crafting_xp': 0, 'fishing_xp': 0, 'cooking_xp': 0}
,{'member_name': 'OwO tanttwat', 'combat_xp': 0, 'mining_xp': 0, 'smithing_xp': 0, 'woodcutting_xp': 41800, 'crafting_xp': 0, 'fishing_xp': 0, 'cooking_xp': 0}
,{'member_name': 'OwO The Hungry', 'combat_xp': 0, 'mining_xp': 0, 'smithing_xp': 0, 'woodcutting_xp': 0, 'crafting_xp': 11513, 'fishing_xp': 0, 'cooking_xp': 30}
,{'member_name': 'OwO Senpaii', 'combat_xp': 0, 'mining_xp': 0, 'smithing_xp': 0, 'woodcutting_xp': 0, 'crafting_xp': 0, 'fishing_xp': 39590, 'cooking_xp': 330}
,{'member_name': 'OwO Nightmare', 'combat_xp': 0, 'mining_xp': 0, 'smithing_xp': 0, 'woodcutting_xp': 0, 'crafting_xp': 0, 'fishing_xp': 1230, 'cooking_xp': 0}]

members_list = ['OwO Cash Money', 'OwO Silent', 'OwO TheDuck', 'OwO Mirage', 'OwO Thor', 'OwO DaveDust', 'OwO Tempy', 'OwO Tantrid', 'OwO Smith', 'OwO Freaka', 'OwO DirtyShots', 'OwO h0lka',
'OwO TheWitcher', 'OwO Krieger', 'OwO Dryness', 'OwO Salty', 'OwO TJ', 'OwO Spooniest', 'OwO DarkSecret', 'OwO Moist', 'OwO Matt', 'OwO Aeonic', 'OwO Olive Yew', 'OwO KcAlex',
'OwO Messwithme', 'OwO CromacK', 'OwO Kreat', 'OwO Cerez Jr', 'OwO DigiPope', 'OwO Roy Donk', 'OwO Maxxd', 'OwO Heartman', 'OwO MrBrisingr', 'OwO Yekzer', 'OwO Bucketss',
'OwO Crixal', 'OwO Panda', 'OwO AnimeHDD', 'OwO RunPerge', 'OwO TechNus09', 'OwO Titan', 'OwO Mullet', 'OwO Yec', 'OwO AcePar', 'OwO Rage', 'OwO Dzoga', 'OwO Skitter',
'OwO Cool Adam', 'OwO Jaf', 'OwO Maddy', 'OwO Hentai', 'OwO Scarthach', 'OwO SAVYS', 'OwO Bunkie', 'OwO Senku', 'OwO Doony', 'OwO J Sins', 'OwO PUZZLE', 'OwO Crusha',
'OwO John', 'OwO Dribbyl', 'OwO Pabs', 'OwO Chez', 'OwO Birb', 'OwO DaddyShark', 'OwO Xbl', 'OwO Gage', 'OwO Avi', 'OwO l Derek l', 'OwO PeeterIV', 'OwO Shadow', 'OwO Schnee',
'OwO Buttcrack', 'OwO DummyThicc', 'OwO Necrotic', 'OwO Stoned', 'OwO Tzak', 'OwO Kona', 'OwO Glitchy', 'OwO Bighhhh', 'OwO White', 'OwO SeikoYuki', 'OwO Mr Yusuf', 'OwO ryry',
'OwO Durps', 'OwO KaitoZezo', 'OwO Bowl', 'OwO Vick Vega', 'OwO Doody', 'OwO Skaifox', 'OwO Aurora', 'OwO Smiley', 'OwO Redro', 'OWO Sriddec', 'OwO Bank', 'OwO CromacK Jr', 'OwO AJ',
'OwO MessEh', 'OwO Zoidberg', 'OwO Goat Bank', 'OwO GaRgAmEL', 'OwO Tasty', 'OwO Hnngh', 'OwO Lonely', 'OwO Fake User', 'OwO Life', 'OwO Uncloud', 'OwO goout', 'OwO tanttwat',
'OwO The Hungry', 'OwO Senpaii', 'OwO Nightmare']

unsorted_lb = {'OwO Harvey': 0, 'OwO Cash Money': 0, 'OwO Silent': 0, 'OwO TheDuck': 0, 'OwO Mirage': 0, 'OwO Thor': 0, 'OwO DaveDust': 0, 'OwO Tempy': 0, 'OwO Tantrid': 0, 'OwO Smith': 0, 'OwO Freaka': 0, 'OwO DirtyShots': 0, 
'OwO h0lka': 0, 'OwO TheWitcher': 0, 'OwO Krieger': 0, 'OwO Dryness': 0, 'OwO Salty': 0, 'OwO TJ': 0, 'OwO Spooniest': 0, 'OwO DarkSecret': 0, 'OwO Moist': 0, 'OwO Matt': 0, 'OwO Aeonic': 0, 
'OwO Olive Yew': 0, 'OwO KcAlex': 0, 'OwO Messwithme': 0, 'OwO CromacK': 0, 'OwO Kreat': 0, 'OwO Cerez Jr': 0, 'OwO DigiPope': 0, 'OwO Roy Donk': 0, 'OwO Maxxd': 0, 'OwO Heartman': 0,
'OwO MrBrisingr': 0, 'OwO Yekzer': 0, 'OwO Bucketss': 0, 'OwO Crixal': 0, 'OwO Panda': 0, 'OwO AnimeHDD': 0, 'OwO RunPerge': 0, 'OwO TechNus09': 0, 'OwO Titan': 0, 'OwO Mullet': 0, 'OwO Yec': 0,
'OwO AcePar': 0, 'OwO Rage': 0, 'OwO Dzoga': 0, 'OwO Skitter': 0, 'OwO Cool Adam': 0, 'OwO Jaf': 0, 'OwO Maddy': 0, 'OwO Hentai': 0, 'OwO Scarthach': 0, 'OwO SAVYS': 0, 'OwO Bunkie': 0, 
'OwO Senku': 0, 'OwO Doony': 0, 'OwO J Sins': 0, 'OwO PUZZLE': 0, 'OwO Crusha': 0, 'OwO John': 0, 'OwO Dribbyl': 0, 'OwO Pabs': 0, 'OwO Chez': 0, 'OwO Birb': 0, 'OwO DaddyShark': 0, 'OwO Xbl': 0,
'OwO Gage': 0, 'OwO Avi': 0, 'OwO l Derek l': 0, 'OwO PeeterIV': 0, 'OwO Shadow': 0, 'OwO Schnee': 0, 'OwO Buttcrack': 0, 'OwO DummyThicc': 0, 'OwO Necrotic': 0, 'OwO Stoned': 0, 'OwO Tzak': 0,
'OwO Kona': 0, 'OwO Glitchy': 0, 'OwO Bighhhh': 0, 'OwO White': 0, 'OwO SeikoYuki': 0, 'OwO Mr Yusuf': 0, 'OwO ryry': 0, 'OwO Durps': 0, 'OwO KaitoZezo': 0, 'OwO Bowl': 0, 'OwO Vick Vega': 0, 
'OwO Doody': 0, 'OwO Skaifox': 0, 'OwO Aurora': 0, 'OwO Smiley': 0, 'OwO Redro': 0, 'OWO Sriddec': 0, 'OwO Bank': 0, 'OwO CromacK Jr': 0, 'OwO AJ': 0, 'OwO MessEh': 0, 'OwO Zoidberg': 0, 
'OwO Goat Bank': 0, 'OwO GaRgAmEL': 0, 'OwO Tasty': 0, 'OwO Hnngh': 0, 'OwO Lonely': 0, 'OwO Fake User': 0, 'OwO Life': 0, 'OwO Uncloud': 0, 'OwO goout': 0, 'OwO tanttwat': 0, 'OwO The Hungry': 0, 
'OwO Senpaii': 0, 'OwO Nightmare': 0}

skills_names_list = ['combat','mining','smithing','woodcutting','crafting','fishing','cooking']

skills_xp_list = ['combat_xp','mining_xp','smithing_xp','woodcutting_xp','crafting_xp','fishing_xp','cooking_xp']


###############################################################################################################################################################################







async def SearchEvent(skill_name):
    global members_log, members_list, unsorted_lb
    
    start = time.time()
    namelist = ['OwO Harvey','OwO Cash Money', 'OwO Silent', 'OwO TheDuck', 'OwO Mirage', 'OwO Thor', 'OwO DaveDust', 'OwO Tempy', 'OwO Tantrid', 'OwO Smith', 'OwO Freaka', 'OwO DirtyShots', 'OwO h0lka',
    'OwO TheWitcher', 'OwO Krieger', 'OwO Dryness', 'OwO Salty', 'OwO TJ', 'OwO Spooniest', 'OwO DarkSecret', 'OwO Moist', 'OwO Matt', 'OwO Aeonic', 'OwO Olive Yew', 'OwO KcAlex',
    'OwO Messwithme', 'OwO CromacK', 'OwO Kreat', 'OwO Cerez Jr', 'OwO DigiPope', 'OwO Roy Donk', 'OwO Maxxd', 'OwO Heartman', 'OwO MrBrisingr', 'OwO Yekzer', 'OwO Bucketss',
    'OwO Crixal', 'OwO Panda', 'OwO AnimeHDD', 'OwO RunPerge', 'OwO TechNus09', 'OwO Titan', 'OwO Mullet', 'OwO Yec', 'OwO AcePar', 'OwO Rage', 'OwO Dzoga', 'OwO Skitter',
    'OwO Cool Adam', 'OwO Jaf', 'OwO Maddy', 'OwO Hentai', 'OwO Scarthach', 'OwO SAVYS', 'OwO Bunkie', 'OwO Senku', 'OwO Doony', 'OwO J Sins', 'OwO PUZZLE', 'OwO Crusha',
    'OwO John', 'OwO Dribbyl', 'OwO Pabs', 'OwO Chez', 'OwO Birb', 'OwO DaddyShark', 'OwO Xbl', 'OwO Gage', 'OwO Avi', 'OwO l Derek l', 'OwO PeeterIV', 'OwO Shadow', 'OwO Schnee',
    'OwO Buttcrack', 'OwO DummyThicc', 'OwO Necrotic', 'OwO Stoned', 'OwO Tzak', 'OwO Kona', 'OwO Glitchy', 'OwO Bighhhh', 'OwO White', 'OwO SeikoYuki', 'OwO Mr Yusuf', 'OwO ryry',
    'OwO Durps', 'OwO KaitoZezo', 'OwO Bowl', 'OwO Vick Vega', 'OwO Doody', 'OwO Skaifox', 'OwO Aurora', 'OwO Smiley', 'OwO Redro', 'OWO Sriddec', 'OwO Bank', 'OwO CromacK Jr', 'OwO AJ',
    'OwO MessEh', 'OwO Zoidberg', 'OwO Goat Bank', 'OwO GaRgAmEL', 'OwO Tasty', 'OwO Hnngh', 'OwO Lonely', 'OwO Fake User', 'OwO Life', 'OwO Uncloud', 'OwO goout', 'OwO tanttwat',
    'OwO The Hungry', 'OwO Senpaii', 'OwO Nightmare']

    log_file = members_log
    skills_list = skills_names_list
    skills_xp = skills_xp_list
    sorted_lb ={}
    temp_dic = {}
    members_sorted = []
    unsortedl = {}
    skill_x = skills_list.index(skill_name)
    async with aiohttp.ClientSession() as session:
        
        to_do = get_tasks(session,skill[skill_x])
        responses = await asyncio.gather(*to_do)
        for response in responses:
            fdata = await response.json()
            for i in range(0,20):
                player_name = fdata[i]["name"]
                xp = fdata[i]["xp"]
                tag = player_name.split()[0]
                tag = tag.upper()
                if player_name in namelist :
                    name_order = namelist.index(player_name)
                    old_xp = log_file[name_order][skills_xp[skill_x]]
                    new_xp = xp
                    xp_diff = new_xp - old_xp
                    unsortedl[player_name] = xp_diff
                    continue
    temp_dic = {k: v for k, v in sorted(unsortedl.items(), key=lambda item: item[1],reverse=True)}
    members_sorted.clear()
    total_xp = 0
    for key, value in temp_dic.items():
        if value != 0 :
            total_xp += value
            test = key + " <> " + "{:,}".format(value)
            members_sorted.append(test)
        else:
            continue
    
    mini_list = []
    mini_list = members_sorted
    temp_dic = {}
    end = time.time()
    total_time = math.ceil(end - start)
    return mini_list, total_time, total_xp
###############################################################################################
players_xp = [{'member_name': 'OwO Maddy', 'mining_xp' : 29650310 , 'woodcutting_xp': 45425673 },
              {'member_name': 'OwO AJ', 'mining_xp' : 1359865 , 'woodcutting_xp': 1420576 }]
c_xp = ['mining_xp','woodcutting_xp']
async def competitionTotal() :
    start = time.time()
    names = ['OwO Maddy' ,'OwO AJ']
    c_skill =['-mining', '-woodcutting']
    sorted_lb = {}
    temp_dic = {}
    members_sorted = []
    unsortedl = {}
    
    
    for skill_x in range(2):
        async with aiohttp.ClientSession() as session :
            to_do = get_tasks(session, c_skill[skill_x])
            responses = await asyncio.gather(*to_do)
            for response in responses:
                fdata = await response.json()
                for i in range(0,20):
                    player_name = fdata[i]["name"]
                    xp = fdata[i]["xp"]
                    
                    
                    if player_name in names :
                        name_order = names.index(player_name)
                        old_xp = players_xp[name_order][c_xp[skill_x]]
                        new_xp = xp
                        xp_diff = new_xp - old_xp
                        if player_name in unsortedl:
                            unsortedl[player_name] += xp_diff
                        else:
                            unsortedl[player_name] = xp_diff
                        continue
    temp_dic = {k: v for k, v in sorted(unsortedl.items(), key=lambda item: item[1],reverse=True)}
    members_sorted.clear()
    total_xp = 0
    for key, value in temp_dic.items():
        total_xp += value
        test = key + " <> " + "{:,}".format(value)
        members_sorted.append(test)
        
    mini_list = []
    mini_list = members_sorted
    temp_dic = {}
    end = time.time()
    total_time = math.ceil(end - start)
    return mini_list, total_time, total_xp



async def competition(skill_name) :
    start = time.time()
    names = ['OwO Maddy' ,'OwO AJ']
    c_skill =['-mining', '-woodcutting']
    c_skill_n =['mining', 'woodcutting']
    temp_dic = {}
    members_sorted = []
    unsortedl = {}
    skill_x = c_skill_n.index(skill_name.lower())
    async with aiohttp.ClientSession() as session :
        to_do = get_tasks(session, c_skill[skill_x])
        responses = await asyncio.gather(*to_do)
        for response in responses:
            fdata = await response.json()
            for i in range(0,20):
                player_name = fdata[i]["name"]
                xp = fdata[i]["xp"]
                    
                    
                if player_name in names :
                    name_order = names.index(player_name)
                    old_xp = players_xp[name_order][c_xp[skill_x]]
                    new_xp = xp
                    xp_diff = new_xp - old_xp
                    unsortedl[player_name] = xp_diff
    temp_dic = {k: v for k, v in sorted(unsortedl.items(), key=lambda item: item[1],reverse=True)}
    members_sorted.clear()
    total_xp = 0
    for key, value in temp_dic.items():
        total_xp += value
        test = key + " <> " + "{:,}".format(value)
        members_sorted.append(test)

    mini_list = []
    mini_list = members_sorted
    temp_dic = {}
    end = time.time()
    total_time = math.ceil(end - start)
    return mini_list, total_time, total_xp


async def SearchEventTotal():
    global members_log, members_list, unsorted_lb
    
    start = time.time()
    namelist = ['OwO Harvey', 'OwO Cash Money', 'OwO Silent', 'OwO TheDuck', 'OwO Mirage', 'OwO Thor', 'OwO DaveDust', 'OwO Tempy', 'OwO Tantrid', 'OwO Smith', 'OwO Freaka', 'OwO DirtyShots', 'OwO h0lka',
    'OwO TheWitcher', 'OwO Krieger', 'OwO Dryness', 'OwO Salty', 'OwO TJ', 'OwO Spooniest', 'OwO DarkSecret', 'OwO Moist', 'OwO Matt', 'OwO Aeonic', 'OwO Olive Yew', 'OwO KcAlex',
    'OwO Messwithme', 'OwO CromacK', 'OwO Kreat', 'OwO Cerez Jr', 'OwO DigiPope', 'OwO Roy Donk', 'OwO Maxxd', 'OwO Heartman', 'OwO MrBrisingr', 'OwO Yekzer', 'OwO Bucketss',
    'OwO Crixal', 'OwO Panda', 'OwO AnimeHDD', 'OwO RunPerge', 'OwO TechNus09', 'OwO Titan', 'OwO Mullet', 'OwO Yec', 'OwO AcePar', 'OwO Rage', 'OwO Dzoga', 'OwO Skitter',
    'OwO Cool Adam', 'OwO Jaf', 'OwO Maddy', 'OwO Hentai', 'OwO Scarthach', 'OwO SAVYS', 'OwO Bunkie', 'OwO Senku', 'OwO Doony', 'OwO J Sins', 'OwO PUZZLE', 'OwO Crusha',
    'OwO John', 'OwO Dribbyl', 'OwO Pabs', 'OwO Chez', 'OwO Birb', 'OwO DaddyShark', 'OwO Xbl', 'OwO Gage', 'OwO Avi', 'OwO l Derek l', 'OwO PeeterIV', 'OwO Shadow', 'OwO Schnee',
    'OwO Buttcrack', 'OwO DummyThicc', 'OwO Necrotic', 'OwO Stoned', 'OwO Tzak', 'OwO Kona', 'OwO Glitchy', 'OwO Bighhhh', 'OwO White', 'OwO SeikoYuki', 'OwO Mr Yusuf', 'OwO ryry',
    'OwO Durps', 'OwO KaitoZezo', 'OwO Bowl', 'OwO Vick Vega', 'OwO Doody', 'OwO Skaifox', 'OwO Aurora', 'OwO Smiley', 'OwO Redro', 'OWO Sriddec', 'OwO Bank', 'OwO CromacK Jr', 'OwO AJ',
    'OwO MessEh', 'OwO Zoidberg', 'OwO Goat Bank', 'OwO GaRgAmEL', 'OwO Tasty', 'OwO Hnngh', 'OwO Lonely', 'OwO Fake User', 'OwO Life', 'OwO Uncloud', 'OwO goout', 'OwO tanttwat',
    'OwO The Hungry', 'OwO Senpaii', 'OwO Nightmare']

    log_file = members_log
    skills_list = skills_names_list
    skills_xp = skills_xp_list
    sorted_lb ={}
    temp_dic = {}
    members_sorted = []
    unsortedl = {}
    for skill_x in range(7):
        async with aiohttp.ClientSession() as session:
            
            to_do = get_tasks(session,skill[skill_x])
            responses = await asyncio.gather(*to_do)
            for response in responses:
                fdata = await response.json()
                for i in range(0,20):
                    player_name = fdata[i]["name"]
                    xp = fdata[i]["xp"]
                    tag = player_name.split()[0]
                    tag = tag.upper()
                    if player_name in namelist :
                        name_order = namelist.index(player_name)
                        old_xp = log_file[name_order][skills_xp[skill_x]]
                        new_xp = xp
                        xp_diff = new_xp - old_xp
                        if player_name in unsortedl:
                            unsortedl[player_name] += xp_diff
                        else:
                            unsortedl[player_name] = xp_diff
                        continue
    temp_dic = {k: v for k, v in sorted(unsortedl.items(), key=lambda item: item[1],reverse=True)}
    members_sorted.clear()
    total_xp = 0
    for key, value in temp_dic.items():
        if value != 0 :
            total_xp += value
            test = key + " <> " + "{:,}".format(value)
            members_sorted.append(test)
        else:
            continue
    mini_list = []
    mini_list = members_sorted
    temp_dic = {}
    end = time.time()
    total_time = math.ceil(end - start)
    return mini_list, total_time, total_xp

######################################################################Bot_Funtctions##################################################################################        
        
        
        
def ToZero(dicc):
    for key in dicc:
        dicc[key]=0  
    
    
    
    
def tabfill(xp): 
    if xp>4536153492:
        lvl=120
        a=100
    else :   
        lvl=0
        a=0
        for l in range(120):
            if (xp > lvltab[l]):
                lvl = l+1
                a = round((((xp- lvltab[l]) / lvldef[l])*100),2)
    if a == 100:
        a = 0
        lvl += 1
    return lvl, a

def DictToList (dictio,listo):
    listo.clear()
    for key, value in dictio.items():
        test = key + " -- " + "{:,}".format(value)
        listo.append(test)

def DictToList_alt (dictio):
    temporal = []
    for key, value in dictio.items():
        test = key + " -- " + "{:,}".format(value)
        temporal.append(test)
    return temporal

def ResetDict(diction):
    diction = diction.fromkeys(diction, 0)
    return diction

def SortDict (di):
    temp = {}
    temp.clear()
    temp = {k: v for k, v in sorted(di.items(), key=lambda item: item[1],reverse=True)}
    return temp

def rankk (rank):
    rank_text = "**rank#"+str(rank)+"**"
    return rank_text

def get_tasks(session,skill_name):
    tasks = []
    for k in range(0,3000):  
        url='https://www.curseofaros.com/highscores'
        tasks.append(asyncio.create_task(session.get(url+skill_name+'.json?p='+str(k))))
    return tasks
def get_tasks2(session,skill_name,limit):
    tasks = []
    for k in range(0,limit):  
        url='https://www.curseofaros.com/highscores'
        tasks.append(asyncio.create_task(session.get(url+skill_name+'.json?p='+str(k))))
    return tasks

def get_tasks3(session,skill_name):
    tasks = []
    for k in range(0,3000):  
        url='https://www.curseofaros.com/highscores'
        tasks.append((k,asyncio.create_task(session.get(url+skill_name+'.json?p='+str(k)))))
    return tasks

owo_members=[]
members_list=[]
skill_xp=['combat_xp','mining_xp','smithing_xp','woodcutting_xp','crafting_xp','fishing_xp','cooking_xp']

async def set_init():
    start = time.time()
    members_sorted = []
    guildreg = {}
    x=0
    for skill_name in skill :
        async with aiohttp.ClientSession() as session:
            to_do = get_tasks(session,skill_name)
            responses = await asyncio.gather(*to_do)
            for response in responses:
                fdata = await response.json()
                for i in range(0,20):
                    member_templete={'member_name':'name_expml' ,'combat_xp':0 ,'mining_xp':0 ,'smithing_xp':0 ,'woodcutting_xp':0 ,'crafting_xp':0 ,'fishing_xp':0 ,'cooking_xp':0 }
                    player_name = fdata[i]["name"]
                    xp = fdata[i]["xp"]
                    tag = player_name.split()[0]
                    tag = tag.upper()
                    
                    if tag == 'OWO':
                        if player_name in members_list :
                            order = members_list.index(player_name)
                            owo_members[order][skill_xp[x]]=xp
                            continue
                        else:
                            members_list.append(player_name)
                            owo_member_temp=member_templete
                            owo_member_temp['member_name']=player_name
                            owo_member_temp[skill_xp[x]]=xp
                            owo_members.append(owo_member_temp)
                            continue
        x=x+1 
    end = time.time()
    total_time = end - start
    return owo_members, total_time


##############################################################################
#get guild members rankings in a certain skill (20000)    
async def searchtag(skill_name,guildtag):
    start = time.time()
    members_sorted = []
    guildreg_names = {}
    guildreg_ranks = {}
    async with aiohttp.ClientSession() as session:
        to_do = get_tasks(session,skill_name)
        responses = await asyncio.gather(*to_do)
        for response in responses:
            fdata = await response.json()
            for i in range(0,20): 
                #check names get rank
                #player_rank = 20 * k + i + 1
                player_name = fdata[i]["name"]
                xp = fdata[i]["xp"]
                tag = player_name.split()[0]
                tag = tag.upper()
                if tag == guildtag.upper():
                    if player_name in guildreg_names :
                        continue
                    else:
                        guildreg_names[player_name]=xp
                        #guildreg_ranks[player_name]=player_rank
                        continue
    temp_dic = {k: v for k, v in sorted(guildreg_names.items(), key=lambda item: item[1],reverse=True)}
    members_sorted.clear()
    for key, value in temp_dic.items():
        test = key + " -- " + "{:,}".format(value) +"\n [Lv."+str(tabfill(value)[0])+" ("+str(tabfill(value)[1])+"%)]"
        members_sorted.append(test)
    mini_list = []
    for i in range(len(members_sorted)):
        mini_list.append(members_sorted[i])
    members_sorted.clear()
    temp_dic = {}
    end = time.time()
    total_time = end - start
    #print(mini_list)
    #print(total_time)
    return mini_list, total_time

#get guilds members rankings in total xp (20000)
async def searchtagtotal(guildtag):
    start = time.time()
    members_sorted = []
    guildreg = {}
    
    for skill_name in skill :
        async with aiohttp.ClientSession() as session:
            to_do = get_tasks(session,skill_name)
            responses = await asyncio.gather(*to_do)
            for response in responses:
                fdata = await response.json()
                for i in range(0,20): 
                    #check names get rank
                    #player_rank = 20 * k + i + 1
                    player_name = fdata[i]["name"]
                    xp = fdata[i]["xp"]
                    tag = player_name.split()[0]
                    tag = tag.upper()
                    
                    if tag == guildtag.upper():
                        if player_name in guildreg :
                            guildreg[player_name]+=xp
                            continue
                        else:
                            guildreg[player_name]=xp
                            continue
    temp_dic = {k: v for k, v in sorted(guildreg.items(), key=lambda item: item[1],reverse=True)}
    members_sorted.clear()
    for key, value in temp_dic.items():
        test = key + " -- " + "{:,}".format(value)
        members_sorted.append(test)
    mini_list = []
    for i in range(len(members_sorted)):
        mini_list.append(members_sorted[i])
    members_sorted.clear()
    temp_dic = {}
    end = time.time()
    total_time = end - start
    return mini_list, total_time

#get guilds ranking in a certain skill (5000)
async def search(skill_name):
    start = time.time()
    list_guilds_stred = []
    d_test = ResetDict(guilds_counter_int)
    async with aiohttp.ClientSession() as session:
        to_do = get_tasks(session,skill_name)
        responses = await asyncio.gather(*to_do)
        for response in responses:
            fdata = await response.json()
            for i in range(0,20): 
                #check names get rank
                player_name = fdata[i]["name"]
                xp = fdata[i]["xp"]
                tag = player_name.split()[0]
                tag = tag.upper()
                
                if tag in d_test :
                    d_test[tag] += xp
                elif "Immortal" in player_name :
                    d_test["IMMORTAL"] += xp
                else :                
                    continue
            
    temp_guilds = {k: v for k, v in sorted(d_test.items(), key=lambda item: item[1],reverse=True)}
    
    DictToList(temp_guilds,list_guilds_stred)
    
    mini_list = []
    for i in range(len(list_guilds_stred)):
        mini_list.append(list_guilds_stred[i])
    list_guilds_stred.clear()
    temp_guilds = ResetDict(guilds_counter_int)
    end = time.time()
    total_time = end - start
    return mini_list , total_time
    
    
#get guilds ranking in total xp (5000)
async def searchTotal():
    start = time.time()
    list_guilds_total_stred = []
    dd_test = ResetDict(guilds_counter_int)
    for skill_name in skill:
        async with aiohttp.ClientSession() as session:
            to_do = get_tasks(session,skill_name)
            responses = await asyncio.gather(*to_do)
            for response in responses:
                fdata = await response.json()
                for i in range(0,20): 
                    #check names
                    player_name = fdata[i]["name"]
                    xp = fdata[i]["xp"]
                    tag = player_name.split()[0]
                    tag = tag.upper()
                    
                    if tag in dd_test :
                        dd_test[tag] += xp
                    elif "Immortal" in player_name :
                        dd_test["IMMORTAL"] += xp
                    else :                
                        continue
            
    temp_guilds = {k: v for k, v in sorted(dd_test.items(), key=lambda item: item[1],reverse=True)}
    
    DictToList(temp_guilds,list_guilds_total_stred)
        
    mini_list = []
    for i in range(len(list_guilds_total_stred)):
            mini_list.append(list_guilds_total_stred[i])
    list_guilds_total_stred.clear()
    temp_guilds = ResetDict(guilds_counter_int)
    end = time.time()
    total_time = end - start
    return mini_list, total_time


#get guilds overall ranking (20000)
async def LeaderBoard():
    start = time.time()
    all_xp = ResetDict(guilds_counter_int)
    skill_0 = ResetDict(guilds_counter_int)
    skill_1 = ResetDict(guilds_counter_int)
    skill_2 = ResetDict(guilds_counter_int)
    skill_3 = ResetDict(guilds_counter_int)
    skill_4 = ResetDict(guilds_counter_int)
    skill_5 = ResetDict(guilds_counter_int)
    skill_6 = ResetDict(guilds_counter_int)
    skills_dict_list = [skill_0,skill_1,skill_2,skill_3,skill_4,skill_5,skill_6,all_xp]

    list_empty = []
    list_empty.clear()
    list_0 = list_empty
    list_1 = list_empty
    list_2 = list_empty
    list_3 = list_empty
    list_4 = list_empty
    list_5 = list_empty
    list_6 = list_empty
    list_all = list_empty
    list_lists = [list_0, list_1, list_2, list_3, list_4, list_5, list_6, list_all ]
    m=0
    for skill_name in skill:
        async with aiohttp.ClientSession() as session:
            to_do = get_tasks(session,skill_name)
            responses = await asyncio.gather(*to_do)
            for response in responses:
                fdata = await response.json()
                for i in range(0,20): 
                    player_name = fdata[i]["name"]
                    xp = fdata[i]["xp"]
                    tag = player_name.split()[0]
                    tag = tag.upper()
                    n = player_name.lower()
                    
                    if tag in skills_dict_list[m] :
                        skills_dict_list[m][tag] += xp
                        all_xp[tag] += xp
                    elif "immortal" in n :
                        skills_dict_list[m]["IMMORTAL"] += xp
                        all_xp["IMMORTAL"] += xp
                    else :                
                        continue
        m +=1
        
    for j in range(0,8):
        tempo = SortDict(skills_dict_list[j])
        list_lists[j] = DictToList_alt(tempo)
        tempo.clear()
        
    end = time.time()
    total_time = end - start
    return list_lists ,total_time
#show members counts and lists of a certain guild in a certain range (rnk)
async def SearchMembers(guildtag,rnk):
    start = time.time()
    members_names = []
    limit = (rnk // 20) +1
    for skill_name in skill:
        async with aiohttp.ClientSession() as session:
            to_do = get_tasks2(session,skill_name,limit)
            responses = await asyncio.gather(*to_do)
            for response in responses:
                fdata = await response.json()
            for i in range(0,20): 
                player_name = fdata[i]["name"]
                tag = player_name.split()[0]
                tag = tag.upper()
                if tag == guildtag.upper():
                    if player_name in members_names :
                        continue
                    else:
                        members_names.append(player_name)
                        continue
    end = time.time()
    total_time = end - start
    return members_names, total_time

#############################################################################Bot_Main_Code##############################################################################


bot = commands.Bot(command_prefix='!')

bot.remove_command("help")
bot.remove_command("date")
bot.remove_command('random')
@bot.event
async def on_ready():
    print('Logging in as {0.user}'.format(bot))
    await bot.change_presence(activity=d.Activity(type=d.ActivityType.watching, name="LeaderBoard"))

@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(bot.latency * 1000)}ms")

    
@bot.command()
async def log(ctx):
    l = createT()
    if l :
        await ctx.send("table created")
    else:
        await ctx.send("error")

@bot.command()
async def hello(ctx):
    username = str(ctx.author).split('#')[0]
    await ctx.send(f"Hello {username}!")

@bot.command()
async def wussup(ctx):
    username = str(ctx.author).split('#')[0]
    await ctx.send(f"Nothing much, hbu {username} ?")

@bot.command()
async def bye(ctx):
    username = str(ctx.author).split('#')[0]
    await ctx.send(f"See you later {username}!")

@bot.command(name="OwO",aliases=["owo","Owo","oWo"])
async def OwO(ctx):
    await ctx.send(f"Numba Wan !!")

@bot.command(name='dc',aliases=['disconnect','logout'])
async def dc(ctx):
    await bot.logout()

@bot.command()
async def date(ctx):
    d1 = dt.today().strftime("%d/%m/%Y")
    await ctx.send(f'Today is : {d1}')


@bot.command()
async def getlist(ctx):
    await ctx.send('getting init members xp')
    list = set_init()
    a = asyncio.run(list)
    members_xp_list = a[0]
    time_taken = a[1]
    for i in range(len(members_xp_list)):
        await ctx.send(members_xp_list[i])
    await ctx.send(f'time taken {time_taken}')

#########
@bot.command()
async def comp(ctx,skill_name = 'total'):
    c_ranks = [":first_place:",":second_place:"]
    skill_n_l = skills_names_list
    if skill_name.lower() in skill_n_l:
        skill_name_c = skill_name.capitalize()
        fetch_msg1 = await ctx.send(f"Fetching {skill_name_c} Data ...")
        a = asyncio.run(competition(skill_name))
        lb_list = a[0]
        time_taken = a[1]
        total_xp = a[2]
        total_xp_txt =  "{:,}".format(total_xp)
        lb = ""

        await fetch_msg1.delete()

        c_embed = d.Embed(title= f"{skill_name_c}" , color=0x6600ff)
        for player in range(2):
            c_embed.add_field(name=f"{c_ranks[player]} place :", value= lb_list[player], inline=False)          
        c_embed.add_field(name= "\u200b" ,value=  f"Total Xp : {total_xp_txt}", inline=False)
        c_embed.set_footer(text= f"Time Taken : {time_taken} seconds.")
        await ctx.send(embed=c_embed)

    elif skill_name.lower() == 'total' :
        fetch_msg2 = await ctx.send(f"Fetching Total Xp Data ...")
        a = asyncio.run(competitionTotal())
        lb_list = a[0]
        time_taken = a[1]
        total_xp = a[2]
        total_xp_txt =  "{:,}".format(total_xp)
        lb = ""
        
        await fetch_msg2.delete()
        
        c_embed = d.Embed(title= "Total Xp" , color=0x6600ff)
        for player in range(2):
            c_embed.add_field(name=f"{c_ranks[player]} place :", value= lb_list[player], inline=False)          
        c_embed.add_field(name= "\u200b" ,value=  f"Total Xp : {total_xp_txt}", inline=False)
        c_embed.set_footer(text= f"Time Taken : {time_taken} seconds.")
        await ctx.send(embed=c_embed)
        
    else:
        await ctx.send("Unkown Skill Or Wrong Spelling, Please Use From :")
        await ctx.send("total <=> mining <=> woodcutting")
#########

@bot.command()
async def event(ctx,skill_n):
    skill_name = skill_n.lower()
    skill_n_l = skills_names_list
    if skill_name in skill_n_l:
        skill_name_c = skill_name.capitalize()
        fetch_msg1 = await ctx.send(f"Fetching {skill_name_c} Data ...")
        a = asyncio.run(SearchEvent(skill_name))
        lb_list = a[0]
        time_taken = a[1]
        total_xp = a[2]
        total_xp_txt =  "{:,}".format(total_xp)
        lb1 = ""
        lb2 = ""
        lb_size = len(lb_list)
        await fetch_msg1.delete()
        await ctx.send(f"{skill_name_c} LeaderBoard")
        for player in range(lb_size // 2):
            lb1 = lb1 + "Rank#"+str(player+1) +'\n'+ lb_list[player] + '\n'
        await ctx.send(lb1)

        for player in range((lb_size//2)+1,lb_size):
            lb2 = lb2 + "Rank#"+str(player+1) +'\n'+ lb_list[player] + '\n'
        await ctx.send(lb2)

        await ctx.send(f"Total Xp : {total_xp_txt} \n Time Taken : {time_taken} seconds.")
    elif skill_name == 'total' :
        fetch_msg2 = await ctx.send(f"Fetching Total Xp Data ...")
        a = asyncio.run(SearchEventTotal())
        lb_list = a[0]
        time_taken = a[1]
        total_xp = a[2]
        total_xp_txt =  "{:,}".format(total_xp)
        lb1 = ""
        lb2 = ""
        lb_size = len(lb_list)
        await fetch_msg2.delete()
        await ctx.send("Total Xp LeaderBoard")
        for player in range(lb_size // 2):
            lb1 = lb1 + "Rank#"+str(player+1) +'\n'+ lb_list[player] + '\n'
        await ctx.send(lb1)

        for player in range((lb_size//2)+1,lb_size):
            lb2 = lb2 + "Rank#"+str(player+1) +'\n'+ lb_list[player] + '\n'
        await ctx.send(lb2)

        await ctx.send(f"Total Xp : {total_xp_txt} \n Time Taken : {time_taken} seconds.")
    else:
        await ctx.send("Unkown Skill Or Wrong Spelling, Please Use From :")
        await ctx.send("total <=> combat <=> mining <=> smithing <=> woodcutting <=> crafting <=> fishing <=> cooking")
@event.error
async def on_command_error(ctx,error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("No Skill Specified ,Please Enter One From :")
        await ctx.send("total <=> combat <=> mining <=> smithing <=> woodcutting <=> crafting <=> fishing <=> cooking")


@bot.command()
async def lb(ctx,test1,test2,xp):
    global unsorted_lb
    test = test1 + ' ' + test2
    dic = {str(test):int(xp)}
    unsorted_lb |= dic 
    msg = f'{test} been added'
    await ctx.send(msg)
@bot.command()
async def show(ctx):
    global unsorted_lb
    lb = []
    DictToList(unsorted_lb,lb)
    lb1 = ""
    lb2 = ""
    lb_size = len(lb)
    await ctx.send(f"LeaderBoard")
    for player in range(lb_size // 2):
        lb1 = lb1 + "Rank#"+str(player+1) +'\n'+ lb[player] + '\n'
    await ctx.send(lb1)

    for player in range((lb_size//2)+1,lb_size):
        lb2 = lb2 + "Rank#"+str(player+1) +'\n'+ lb[player] + '\n'
    await ctx.send(lb2)



@bot.command(name='combat',aliases=['melee','sw','silent'])
async def combat(ctx,rank="25"):
    if ((int(rank)<=0) or (int(rank)>25)):
        await ctx.send("Ranks must be between 1 and 25")
    else:
        await ctx.send("Fetching Combat Data ... ")
        combatlb_srch = search("")
        a = asyncio.run(combatlb_srch)
        test_list_1 = a[0]
        time_taken = a[1]
        cmd_time = int(time_taken) 
        embedVar1 = d.Embed(title="Top Guilds: Combat (60,000)", color=0x669999)
        for i in range(int(rank)):
            embedVar1.add_field(name=rankk(i+1), value= test_list_1[i] , inline=False)
        embedVar1.set_footer(text="time taken : "+str(cmd_time)+" seconds.")
        await ctx.send(embed=embedVar1)
        test_list_1.clear()

@bot.command(name='mining',aliases=['mine','rocky','pick','krieger'])
async def mining(ctx,rank="25"):
    if ((int(rank)<=0) or (int(rank)>25)):
        await ctx.send("Ranks must be between 1 and 25")
    else:
        await ctx.send("Fetching Mining Data ... ")
        mininglb_srch = search("-mining")
        a = asyncio.run(mininglb_srch)
        test_list_2 = a[0]
        time_taken = a[1]
        cmd_time = int(time_taken) 
        embedVar2 = d.Embed(title="Top Guilds: Mining (60,000)", color=0x333300)
        for i in range(int(rank)):
            embedVar2.add_field(name=rankk(i+1), value= test_list_2[i] , inline=False)
        embedVar2.set_footer(text="time taken : "+str(cmd_time)+" seconds.")
        await ctx.send(embed=embedVar2)
        test_list_2.clear()

@bot.command(name='smithing',aliases=['smith','ember','hammer'])
async def smithing(ctx,rank="25"):
    if ((int(rank)<=0) or (int(rank)>25)):
        await ctx.send("Ranks must be between 1 and 25")
    else:
        await ctx.send("Fetching Smithing Data ... ")
        smithinglb_srch = search("-smithing")
        a = asyncio.run(smithinglb_srch)
        test_list_3 = a[0]
        time_taken = a[1]
        cmd_time = int(time_taken) 
        embedVar3 = d.Embed(title="Top Guilds: Smithing (60,000)", color=0xff0000)
        for i in range(int(rank)):
            embedVar3.add_field(name=rankk(i+1), value= test_list_3[i] , inline=False)
        embedVar3.set_footer(text="time taken : "+str(cmd_time)+" seconds.")
        await ctx.send(embed=embedVar3)
        test_list_3.clear()

@bot.command(name='woodcutting',aliases=['wc','pecker','axe','matt'])
async def woodcutting(ctx,rank="25"):
    if ((int(rank)<=0) or (int(rank)>25)):
        await ctx.send("Ranks must be between 1 and 25")
    else:
        await ctx.send("Fetching Woodcutting Data ... ")
        woodcuttinglb_srch = search("-woodcutting")
        a = asyncio.run(woodcuttinglb_srch)
        test_list_4 = a[0]
        time_taken = a[1]
        cmd_time = int(time_taken) 
        embedVar4 = d.Embed(title="Top Guilds: Woodcutting (60,000)", color=0x00cc00)
        for i in range(int(rank)):
            embedVar4.add_field(name=rankk(i+1), value= test_list_4[i] , inline=False)
        embedVar4.set_footer(text="time taken : "+str(cmd_time)+" seconds.")
        await ctx.send(embed=embedVar4)
        test_list_4.clear()

@bot.command(name='crafting',aliases=['craft','woody','yekzer'])
async def crafting(ctx,rank="25"):
    if ((int(rank)<=0) or (int(rank)>25)):
        await ctx.send("Ranks must be between 1 and 25")
    else:
        await ctx.send("Fetching Crafting Data ... ")
        craftinglb_srch = search("-crafting")
        a = asyncio.run(craftinglb_srch)
        test_list_5 = a[0]
        time_taken = a[1]
        cmd_time = int(time_taken) 
        embedVar5 = d.Embed(title="Top Guilds: Crafting (60,000)", color=0x996633)
        for i in range(int(rank)):
            embedVar5.add_field(name=rankk(i+1), value= test_list_5[i] , inline=False)
        embedVar5.set_footer(text="time taken : "+str(cmd_time)+" seconds.")
        await ctx.send(embed=embedVar5)
        test_list_5.clear()

@bot.command(name='fishing',aliases=['fish','tantrid','tant'])
async def fishing(ctx,rank="25"):
    if ((int(rank)<=0) or (int(rank)>25)):
        await ctx.send("Ranks must be between 1 and 25")
    else:
        await ctx.send("Fetching Fishing Data ... ")
        fishinglb_srch = search("-fishing")
        a = asyncio.run(fishinglb_srch)
        test_list_6 = a[0]
        time_taken = a[1]
        cmd_time = int(time_taken) 
        embedVar6 = d.Embed(title="Top Guilds: Fishing (60,000)", color=0x0066ff)
        for i in range(int(rank)):
            embedVar6.add_field(name=rankk(i+1), value= test_list_6[i] , inline=False)
        embedVar6.set_footer(text="time taken : "+str(cmd_time)+" seconds.")
        await ctx.send(embed=embedVar6)
        test_list_6.clear()

@bot.command(name='cooking',aliases=['cook','food'])
async def cooking(ctx,rank="25"):
    if ((int(rank)<=0) or (int(rank)>25)):
        await ctx.send("Ranks must be between 1 and 25")
    else:
        await ctx.send("Fetching Cooking Data ... ")
        cookinglb_srch = search("-cooking")
        a = asyncio.run(cookinglb_srch)
        test_list_7 = a[0]
        time_taken = a[1]
        cmd_time = int(time_taken) 
        embedVar7 = d.Embed(title="Top Guilds: Cooking (60,000)", color=0x800000)
        for i in range(int(rank)):
            embedVar7.add_field(name=rankk(i+1), value= test_list_7[i] , inline=False)
        embedVar7.set_footer(text="time taken : "+str(cmd_time)+" seconds.")
        await ctx.send(embed=embedVar7)
        test_list_7.clear()

@bot.command(name='total',aliases=['totalxp'])
async def total(ctx,rank='25'):
    if ((int(rank)<=0) or (int(rank)>25)):
        await ctx.send("Ranks must be between 1 and 25")
    else:
        await ctx.send("Fetching Data ... ")
        totallb_srch = searchTotal()
        a = asyncio.run(totallb_srch)
        test_list_0 = a[0]
        time_taken = a[1]
        cmd_time = int(time_taken) 
        embedVar0 = d.Embed(title="Top Guilds: Total XP (60,000)", color=0x6600ff)
        for i in range(int(rank)):
            embedVar0.add_field(name=rankk(i+1), value= test_list_0[i] , inline=False)
        embedVar0.set_footer(text="time taken : "+str(cmd_time)+" seconds.")
        await ctx.send(embed=embedVar0)
        test_list_0.clear()
        
@bot.command()
async def test(ctx):
    embedVar = d.Embed(title="TEST", color=0x6600ff)
    embedVar.add_field(name="test", value= "testtesttest" , inline=False)
                        
    embedVarr = d.Embed(title="TEST1", color=0x6600ff)
    embedVarr.add_field(name="test1", value= "testtesttest1" , inline=False)
                    
    await ctx.send(embed=embedVar)
    await ctx.send(embed=embedVarr)

@bot.command(name='all',aliases=['overall','ranking'])
async def all(ctx):
    mining = get(ctx.guild.emojis, name="mining")
    wc = get(ctx.guild.emojis, name="woodcutting")
    fishing = get(ctx.guild.emojis, name="fishing")
    smithing = get(ctx.guild.emojis, name="smithing")
    crafting = get(ctx.guild.emojis, name="crafting")
    cooking = get(ctx.guild.emojis, name="cooking")
    combat = get(ctx.guild.emojis, name="combat")
    
    field_header = [f' {mining} Top Guilds Mining \n',f' {wc} Top Guilds Woodcutting\n',f' {fishing} Top Guilds Fishing\n',f' {smithing} Top Guilds Smithing\n',
                        f' {crafting} Top Guilds Crafting\n',f' {cooking} Top Guilds Cooking\n',f' {combat} Top Guilds Combat\n',"Top Guilds Total XP\n"]
    await ctx.send("Fetching Data ... ")
    embedVar1 = d.Embed(title="Top Guilds (60,000)", color=0x669999)
    
    alllb_srch = LeaderBoard()
    a = asyncio.run(alllb_srch)
    listed = a[0]
    time_taken = a[1]
    cmd_time = int(time_taken) 
    wierd_order = [1,3,5,2,4,6,0,7]
    for i in range(8) :
        msg = ""
        for j in range(10):
            msg = msg + rankk(j+1) + ' ' + listed[wierd_order[i]][j]+'\n'
        embedVar1.add_field(name= field_header[i], value= msg , inline=True)
    embedVar1.set_footer(text="time taken : "+str(cmd_time)+" seconds.")
    await ctx.send(embed=embedVar1)
    listed.clear()



@bot.command(name='guildlb',aliases=['glb','guildboard'])
async def guildlb(ctx,skill_name,guildtag):
    guild_name = guildtag.upper()
    await ctx.send(f"Getting {guild_name}'s {skill_name} Leaderboard ... ")
    x = skills.index(skill_name.lower())

    guildlb_srch = searchtag(skill[x],guildtag)
    #loop = asyncio.get_event_loop()
    #future = await asyncio.ensure_future(guildlb_srch)
    #a = loop.run_until_complete(future)
    a = asyncio.run(guildlb_srch)
    test_list_8 = a[0]
    
    tag = guildtag.upper()
    time_taken = a[1]
    cmd_time = int(time_taken) 

    guildlb_msg = f"Top "+tag+": "+skill_name.capitalize()+"(60,000)"
    embedVar = d.Embed(title= guildlb_msg , color=0x0066ff)
    embedVar.add_field(name="Skillers count", value= str(len(test_list_8)) , inline=False)
    await ctx.send(embed=embedVar)
    
    counter_int = len(test_list_8)
    embeds_int = math.ceil(counter_int / 15)
    fields_int = embeds_int
    

    embed0 = d.Embed(title="\u200b", color=0x6600ff)
    embed1 = d.Embed(title="\u200b", color=0x6600ff)
    embed2 = d.Embed(title="\u200b", color=0x6600ff)
    embed3 = d.Embed(title="\u200b", color=0x6600ff)
    embed4 = d.Embed(title="\u200b", color=0x6600ff)
    embed5 = d.Embed(title="\u200b", color=0x6600ff)
    embed6 = d.Embed(title="\u200b", color=0x6600ff)
    embed7 = d.Embed(title="\u200b", color=0x6600ff)
    embed8 = d.Embed(title="\u200b", color=0x6600ff)
    embed9 = d.Embed(title="\u200b", color=0x6600ff)
    embed10 = d.Embed(title="\u200b", color=0x6600ff)
    embed11 = d.Embed(title="\u200b", color=0x6600ff)
    embed12 = d.Embed(title="\u200b", color=0x6600ff)
    embed13 = d.Embed(title="\u200b", color=0x6600ff)
    embed14 = d.Embed(title="\u200b", color=0x6600ff)
    embed15 = d.Embed(title="\u200b", color=0x6600ff)
    embed16 = d.Embed(title="\u200b", color=0x6600ff)
    embed17 = d.Embed(title="\u200b", color=0x6600ff)
    embeds_list = [embed0,embed1,embed2,embed3,embed4,embed5,embed6,embed7,embed8,embed9,embed10,embed11,embed12,embed13,embed14,embed15,embed16,embed17]
    
    members_msg0 = ""
    
    for i in range(embeds_int):
        members_msg0 = ""
        loop_list = []
        for j in range(fields_int):
            loop_list.append(j*15)
        loop_list.append(counter_int)
        
        for k in range(loop_list[i],loop_list[i+1]):
            members_msg0 = members_msg0 + rankk(k+1) + "\n" + test_list_8[k] + '\n'
        embeds_list[i].add_field(name='\u200b', value= members_msg0 , inline=False)
        members_msg0=""
        if i == embeds_int-1:
            embeds_list[i].set_footer(text="time taken : "+str(cmd_time)+" seconds.")
        await ctx.send(embed=embeds_list[i])
    test_list_8.clear()    












"""@bot.command()
async def event(ctx):

    await ctx.send(f"Getting Combat Grinders Leaderboard ... ")
    results_list = []
    results_list = CombatEvent()
    temp_msg = ""
    for i in range(len(results_list)-1):
        temp_msg = temp_msg + results_list[i] + '\n'
    await ctx.send(f"{temp_msg}")
    temp_msg0 = "Total Guild Gained Xp"+' -- '+"{:,}".format(results_list[len(results_list)-1])
    await ctx.send(f"{temp_msg0}")
    results_list.clear()"""


    
@bot.command(name='guildlbT',aliases=['glbt','guildranks'])
async def guildlbT(ctx,guildtag):
    guild_name = guildtag.upper()
    await ctx.send(f"Getting {guild_name}'s Leaderboard ... ")
    

    guildlbT_srch = searchtagtotal(guildtag)
    #loop = asyncio.get_event_loop()
    #future = await asyncio.ensure_future(guildlb_srch)
    #a = loop.run_until_complete(future)
    temp_result_T = asyncio.run(guildlbT_srch)
    test_list_10 = temp_result_T[0]


    tag = guildtag.upper()
    time_taken = temp_result_T[1]
    time_take = int(time_taken) 

    guildlb_msg = f"Top "+tag+": "+"[Total XP](60,000)"
    embedVar = d.Embed(title= guildlb_msg , color=0x0066ff)
    embedVar.add_field(name="Players Count", value= str(len(test_list_10)) , inline=False)
    await ctx.send(embed=embedVar)
    
    counter_int = len(test_list_10)
    embeds_int = math.ceil(counter_int / 15)
    fields_int = embeds_int
    
    embed0 = d.Embed(title="\u200b", color=0x6600ff)
    embed1 = d.Embed(title="\u200b", color=0x6600ff)
    embed2 = d.Embed(title="\u200b", color=0x6600ff)
    embed3 = d.Embed(title="\u200b", color=0x6600ff)
    embed4 = d.Embed(title="\u200b", color=0x6600ff)
    embed5 = d.Embed(title="\u200b", color=0x6600ff)
    embed6 = d.Embed(title="\u200b", color=0x6600ff)
    embed7 = d.Embed(title="\u200b", color=0x6600ff)
    embed8 = d.Embed(title="\u200b", color=0x6600ff)
    embed9 = d.Embed(title="\u200b", color=0x6600ff)
    embed10 = d.Embed(title="\u200b", color=0x6600ff)
    embed11 = d.Embed(title="\u200b", color=0x6600ff)
    embed12 = d.Embed(title="\u200b", color=0x6600ff)
    embed13 = d.Embed(title="\u200b", color=0x6600ff)
    embed14 = d.Embed(title="\u200b", color=0x6600ff)
    embed15 = d.Embed(title="\u200b", color=0x6600ff)
    embed16 = d.Embed(title="\u200b", color=0x6600ff)
    embed17 = d.Embed(title="\u200b", color=0x6600ff)
    embeds_list = [embed0,embed1,embed2,embed3,embed4,embed5,embed6,embed7,embed8,embed9,embed10,embed11,embed12,embed13,embed14,embed15,embed16,embed17]
    
    members_msg0 = ""
    
    for i in range(embeds_int):
        members_msg0 = ""
        loop_list = []
        for j in range(embeds_int):
            loop_list.append(j*15)
        loop_list.append(counter_int)
        
        for k in range(loop_list[i],loop_list[i+1]):
            members_msg0 = members_msg0 + rankk(k+1) + "\n" + test_list_10[k] + '\n'
        embeds_list[i].add_field(name='\u200b', value= members_msg0 , inline=False)
        members_msg0=""
        if i == embeds_int-1:
            embeds_list[i].set_footer(text="time taken : "+str(time_take)+" seconds.")
        await ctx.send(embed=embeds_list[i])
    test_list_10.clear()                  




    
@bot.command(name="guildcount",aliases=['gc','count','howmany','hm'])
async def guildcount(ctx,guildtag,rank):
    guild_name = guildtag.upper()
    await ctx.send(f"Countings {guild_name}'s members")
    count_srch = SearchMembers(guild_name,int(rank))
    a = asyncio.run(count_srch)
    y = a[0]
    time_taken = a[1]
    cmd_time = int(time_taken)
    counter_int = len(y)
    counter_msg = f"{guild_name}'s Members at Top {rank}"
    embedVar8 = d.Embed(title= counter_msg , color=0x0066ff)
    embedVar8.add_field(name="Count", value= str(counter_int) , inline=False)
    await ctx.send(embed=embedVar8)
    members_msg = ""
    members_msg0 = ""
    ###############################Guilds_Less_Than_65_members###############################################
    if (counter_int<=65):
        if (guild_name == "OWO"):
            embed = d.Embed(title="Legends", inline=False)
        else:
            embed = d.Embed(title="Members", inline=False)
        for i in range(counter_int):
            members_msg = members_msg + y[i] + '\n'
        embed.add_field(name="\u200b", value= members_msg , inline=False)
        embed.set_footer(text="time taken : "+str(cmd_time)+" seconds.")
        await ctx.send(embed=embed)      
    ###############################Guilds_Between_65_And_325_members###############################################
    elif ((counter_int>65) and (counter_int<325)):
        fields_int =  math.ceil(counter_int / 65)
        loop_list = []
        for i in range(fields_int):
            loop_list.append(i*65)
        loop_list.append(counter_int)
        if (guild_name == "OWO"):
            embed = d.Embed(title="Legends", inline=False)
        else:
            embed = d.Embed(title="Members", inline=False)
            
        for i in range(fields_int):
            for j in range(loop_list[i],loop_list[i+1]):
                members_msg0 = members_msg0 + y[j] + '\n'
            embed.add_field(name='\u200b', value= members_msg0 , inline=False)
            if i == fields_int-1:
                embed.set_footer(text="time taken : "+str(cmd_time)+" seconds.")
            members_msg0=""
            await ctx.send(embed=embed)
    ##################################Guilds_Between_325_And_1625_members############################################
    elif ((counter_int>=325) and (counter_int<1625)):
        embed0 = d.Embed(title="\u200b", color=0x6600ff)
        embed1 = d.Embed(title="\u200b", color=0x6600ff)
        embed2 = d.Embed(title="\u200b", color=0x6600ff)
        embed3 = d.Embed(title="\u200b", color=0x6600ff)
        embed4 = d.Embed(title="\u200b", color=0x6600ff)
        embed5 = d.Embed(title="\u200b", color=0x6600ff)
        embed6 = d.Embed(title="\u200b", color=0x6600ff)
        embed7 = d.Embed(title="\u200b", color=0x6600ff)
        embed8 = d.Embed(title="\u200b", color=0x6600ff)
        embed9 = d.Embed(title="\u200b", color=0x6600ff)
        embed10 = d.Embed(title="\u200b", color=0x6600ff)
        embed11 = d.Embed(title="\u200b", color=0x6600ff)
        embed12 = d.Embed(title="\u200b", color=0x6600ff)
        embed13 = d.Embed(title="\u200b", color=0x6600ff)
        embed14 = d.Embed(title="\u200b", color=0x6600ff)
        embed15 = d.Embed(title="\u200b", color=0x6600ff)

        embeds_list = [embed0,embed1,embed2,embed3,embed4,embed5,embed6,embed7,embed8,embed9,embed10,embed11,embed12,embed13,embed14,embed15]
        exf = math.ceil(counter_int / 65)
        embeds_int = exf
        fields_int = exf

        if (guild_name == "OWO"):
            embed = d.Embed(title="Legends", inline=False)
            embed.add_field(name="\u200b",value="\u200b")
        else:
            embed = d.Embed(title="Members", inline=False)
            embed.add_field(name="\u200b",value="\u200b")
        await ctx.send(embed=embed)

        for i in range(embeds_int):
            loop_list = []
            embeds_list[i] = d.Embed(title="\u200b", inline=False)
            for j in range(fields_int):
                loop_list.append(j*65)
            loop_list.append(counter_int)
                
            for k in range(loop_list[i],loop_list[(i)+1]):
                members_msg0 = members_msg0 + y[k] + '\n'
            embeds_list[i].add_field(name='\u200b', value= members_msg0 , inline=False)
            members_msg0=""
            await ctx.send(embed=embeds_list[i])
    y.clear()








@bot.command(name='help',aliases=['help?','helpme','commands?','command?','cmd'])
async def help(ctx):
    embedVar9 = d.Embed(title="Guilds Commands", color=0x669999)
    embedVar9.add_field(name="-----skills ranking-----", value= "!{Skill's Command} {How Many Guilds to Display(max 25)}" , inline=False)
    embedVar9.add_field(name="!combat or !melee or !sw", value= "Show Top Guilds in Combat (From Top 60,000 players)" , inline=False)
    embedVar9.add_field(name="!mining or !mine or !pick or !rocky or !krieger", value= "Show Top Guilds in Mining (From Top 60,000 players)" , inline=False)
    embedVar9.add_field(name="!smithing or !smith or !hammer or !ember", value= "Show Top Guilds in Smithing (From Top 60,000 players)" , inline=False)
    embedVar9.add_field(name="!woodcutting or !wc or !pecker or !matt", value= "Show Top Guilds in Woodcutting (From Top 60,000 players)" , inline=False)
    embedVar9.add_field(name="!crafting or !craft or !woody or !yekzer", value= "Show Top Guilds in Crafting (From Top 60,000 players)" , inline=False)
    embedVar9.add_field(name="!fishing or !fish or !tantrid or !tant", value= "Show Top Guilds in Fishing (From Top 60,000 players)" , inline=False)
    embedVar9.add_field(name="!cooking or !cook or !food", value= "Show Top Guilds in Cooking (From Top 60,000 players)" , inline=False)
    embedVar9.add_field(name="!total or !totalxp", value= "Show Top Guilds in Total XP (From Top 60,000 players)" , inline=False)
    embedVar9.add_field(name="!all or !overall or !ranking", value= "Show an Overall Leaderboard (From Top 60,000 players)" , inline=False)
    embedVar9.add_field(name="!guildlb or !glb or !guildboard", value= "Show The Leaderboard of a Guild in a Skill (From Top 60,000 players)\n !guildlb {skill name} {guild tag}" , inline=False)
    embedVar9.add_field(name="!guildlbT or !glbT or !guildboardT", value= "Show The Leaderboard of a Guild in Total XP (From Top 60,000 players)\n !guildlbT {guild tag}" , inline=False)
    embedVar9.add_field(name="!guildcount or !gc or !count or !howmany or !hm", value= "Show The Members of a Guilds in a Certain Range \n !counter {guild tag} {Search Range}" , inline=False)
    embedVar9.add_field(name="!date", value= "Show Today Date" , inline=False)
    embedVar9.add_field(name="!help or !help? or !helpme or !commands?", value= "Show  This Menu" , inline=False)
    embedVar9.add_field(name="!test", value= "Test The Current Command In Developement" , inline=False)
    embedVar9.add_field(name="!ping", value= "Show The Bot ping" , inline=False)
    embedVar9.add_field(name="!dc or !disconnect or !logout", value= "Disconnect The Bot For a While To Reset Himself" , inline=False)
    embedVar9.add_field(name="!hello , !wussup , !bye", value= "Interract With The Bot" , inline=False)
    await ctx.send(embed=embedVar9)   



bot.run(os.getenv('TOKEN'))

