"""
Task definitions and result types for the Islands API.

Tasks represent actions that can be performed on islanders (e.g. measuring
blood pressure, consuming food/drink). TaskResult holds the outcome of a
completed task as scraped from an islander's profile page.
"""
from typing import Final


class TaskResult:
    """Represents a completed task entry on an islander's profile."""

    def __init__(self, time: str, name: str, result: str):
        self._time = time
        self._name = name
        self._result = result

    def time(self) -> str:
        """Return the timestamp string of when the task was completed."""
        return self._time

    def name(self) -> str:
        """Return the display name of the task."""
        return self._name  # was incorrectly returning self._result

    def result(self) -> str:
        """Return the result/measurement value of the task."""
        return self._result

    def __repr__(self):
        return f'{self._name} @ {self._time} - ({self._result})'


class Task:
    """Represents a task that can be assigned to an islander."""

    def __init__(self, code: str):
        self._code = code

    def code(self) -> str:
        """Return the URL code used to submit this task."""
        return self._code


# ---------------------------------------------------------------------------
# Task Definitions
# ---------------------------------------------------------------------------

MEASURE_BLOOD_GLUCOSE: Final[Task] = Task('bloodglucose')
"""Measure blood glucose levels."""

MEASURE_BLOOD_PRESSURE: Final[Task] = Task('bloodpressure')
"""Measure blood pressure levels."""

CHOCOLATE_DARK_40: Final[Task] = Task('chocdark')
"""Consume 50g of 40% cocoa chocolate."""

CHOCOLATE_DARK_70: Final[Task] = Task('chocdark70')
"""Consume 50g of 70% cocoa chocolate."""

CHOCOLATE_DARK_85: Final[Task] = Task('chocdark85')
"""Consume 50g of 85% cocoa chocolate."""

CHOCOLATE_DARK_99: Final[Task] = Task('chocdark99')
"""Consume 50g of 99% cocoa chocolate."""

SIT_TEMP_NEG20: Final[Task] = Task('freezer')
"""Sit at -20°C for 10 minutes."""

SIT_TEMP_40: Final[Task] = Task('heat40')
"""Sit at 40°C for 10 minutes."""

SIT_TEMP_5: Final[Task] = Task('cold')
"""Sit at 5°C for 10 minutes."""

DRINK_WATER_250: Final[Task] = Task('water250')
"""Drink 250 ml of water."""

DRINK_WATER_60: Final[Task] = Task('water60')  # was a duplicate of DRINK_WATER_250
"""Drink 60 ml of water."""

EAT_FRIED_CHIPS: Final[Task] = Task('fries')
"""Eat 50g of fried chips."""

ENERGY_DRINK: Final[Task] = Task('energydrink')
"""Drink 250 mL of energy drink."""

# Survey
COMPLETE_QUESTIONNAIRE: Final[Task] = Task('questionnaire')
"""Complete questionnaire."""

# Documents
BIRTH_CERTIFICATE: Final[Task] = Task('birth')
"""Retrieve birth certificate."""
FOOD_DIARY: Final[Task] = Task('fooddiary')
"""Retrieve food diary."""
HYPNOGRAM: Final[Task] = Task('hypnogram')
"""Retrieve hypnogram."""
REPORT_CARD: Final[Task] = Task('reportcard')
"""Retrieve report card."""
TAX_RECORDS: Final[Task] = Task('taxrecords')
"""Retrieve tax records."""

# Physiology
AUDIOGRAM: Final[Task] = Task('audiogram')
"""Measure hearing via audiogram."""
BODY_TEMPERATURE: Final[Task] = Task('temperature')
"""Measure body temperature."""
HEAD_CIRCUMFERENCE: Final[Task] = Task('head')
"""Measure head circumference."""
HEIGHT: Final[Task] = Task('height')
"""Measure height."""
LIVER_SIZE: Final[Task] = Task('liver')
"""Measure liver size."""
OXIMETER: Final[Task] = Task('spo2')
"""Measure blood oxygen saturation via oximeter."""
OXYGEN_UPTAKE_SUBMAXIMAL: Final[Task] = Task('submax')
"""Measure submaximal oxygen uptake."""
PEAK_FLOW_METER: Final[Task] = Task('peakflow')
"""Measure peak expiratory flow."""
PERCEPTUAL_VOICE_EVALUATION: Final[Task] = Task('pve')
"""Perform perceptual voice evaluation."""
PRESSURE_PAIN_THRESHOLD_BICEPS: Final[Task] = Task('pptbiceps')
"""Measure pressure pain threshold at the biceps."""
PRESSURE_PAIN_THRESHOLD_TRAPEZIUS: Final[Task] = Task('ppttrapezius')
"""Measure pressure pain threshold at the trapezius."""
PULSE_METER: Final[Task] = Task('pulse')
"""Measure pulse rate."""
RESPIRATORY_RATE_2_MINS: Final[Task] = Task('breathing')
"""Measure respiratory rate over 2 minutes."""
SKIN_COLOURATION: Final[Task] = Task('skin')
"""Assess skin colouration."""
SLEEP_STAGE: Final[Task] = Task('sleep')
"""Assess current sleep stage."""
SPEECH_DISCRIMINATION_TEST: Final[Task] = Task('speechwords')
"""Perform speech discrimination test."""
SPEECH_INTELLIGIBILITY_INDEX_0DB: Final[Task] = Task('sii')
"""Measure speech intelligibility index at 0 dB."""
SPIROMETER: Final[Task] = Task('fev')
"""Measure forced expiratory volume via spirometer."""
VISUAL_ACUITY: Final[Task] = Task('visualacuity')
"""Measure visual acuity."""
VOCAL_FREQUENCY: Final[Task] = Task('vocalfreq')
"""Measure vocal frequency."""
WAIST_CIRCUMFERENCE: Final[Task] = Task('waist')
"""Measure waist circumference."""
WEIGHT: Final[Task] = Task('weight')
"""Measure body weight."""

# Blood Tests
BLOOD_ADRENALINE: Final[Task] = Task('bloodadrenaline')
"""Measure blood adrenaline levels."""
BLOOD_ALCOHOL: Final[Task] = Task('breathalyzer')
"""Measure blood alcohol via breathalyzer."""
BLOOD_APTT: Final[Task] = Task('aptt')
"""Measure activated partial thromboplastin time."""
BLOOD_CHOLESTEROL: Final[Task] = Task('cholesterol')
"""Measure blood cholesterol levels."""
BLOOD_CORTISOL: Final[Task] = Task('cortisol')
"""Measure blood cortisol levels."""
BLOOD_ENDORPHIN: Final[Task] = Task('endorphin')
"""Measure blood endorphin levels."""
BLOOD_ESTROGEN: Final[Task] = Task('estrogen')
"""Measure blood estrogen levels."""
BLOOD_GHRELIN: Final[Task] = Task('ghrelin')
"""Measure blood ghrelin levels."""
BLOOD_HEMATOCRIT: Final[Task] = Task('hematocrit')
"""Measure blood hematocrit."""
BLOOD_MAGNESIUM: Final[Task] = Task('bloodmg')
"""Measure blood magnesium levels."""
BLOOD_MELATONIN: Final[Task] = Task('melatonin')
"""Measure blood melatonin levels."""
BLOOD_OXYGEN: Final[Task] = Task('pao2')
"""Measure partial pressure of oxygen in blood."""
BLOOD_OXYTOCIN: Final[Task] = Task('oxytocin')
"""Measure blood oxytocin levels."""
BLOOD_POTASSIUM: Final[Task] = Task('potassium')
"""Measure blood potassium levels."""
BLOOD_SEROTONIN: Final[Task] = Task('serotonin')
"""Measure blood serotonin levels."""
BLOOD_SODIUM: Final[Task] = Task('sodium')
"""Measure blood sodium levels."""
BLOOD_TESTOSTERONE: Final[Task] = Task('testosterone')
"""Measure blood testosterone levels."""
BLOOD_TYPE: Final[Task] = Task('bloodtype')
"""Determine blood type."""
BLOOD_VITAMIN_D: Final[Task] = Task('vitd')
"""Measure blood vitamin D levels."""
CDZ_LYMPHOCYTE_COUNT: Final[Task] = Task('cdz')
"""Measure CDZ lymphocyte count."""
GENE_ARRAY_CHROMOSOME_A: Final[Task] = Task('genes1')
"""Perform gene array on chromosome A."""
GENE_ARRAY_CHROMOSOME_B: Final[Task] = Task('genes2')
"""Perform gene array on chromosome B."""
GENE_ARRAY_COMBINED: Final[Task] = Task('genes3')
"""Perform combined gene array."""
WHITE_BLOOD_CELL_COUNT: Final[Task] = Task('wbc')
"""Measure white blood cell count."""

# Mental Tasks
ATTENTION_TEST_10_MINS: Final[Task] = Task('attention')
"""Perform attention test for 10 minutes."""
CODE_TRANSMISSION_TEST_10_MINS: Final[Task] = Task('codetransmission')
"""Perform code transmission test for 10 minutes."""
COMPREHENSION_TEST_10_MINS: Final[Task] = Task('comprehension')
"""Perform comprehension test for 10 minutes."""
GROOVED_PEGBOARD_TEST: Final[Task] = Task('pegboard')
"""Perform grooved pegboard test."""
HAPPY_MEMORIES_1_MIN: Final[Task] = Task('happy')
"""Recall happy memories for 1 minute."""
IQ_TEST: Final[Task] = Task('iq')
"""Perform IQ test."""
MEMORY_GAME: Final[Task] = Task('memorygame')
"""Play memory game."""
MEMORY_TEST_CARDS: Final[Task] = Task('memorycards')
"""Perform memory test with cards."""
MEMORY_TEST_VOCABULARY: Final[Task] = Task('memoryvocab')
"""Perform memory test with vocabulary."""
MENTAL_ARITHMETIC_BASIC_4_MINS: Final[Task] = Task('mental')
"""Perform basic mental arithmetic for 4 minutes."""
MENTAL_ARITHMETIC_DIFFICULT_4_MINS: Final[Task] = Task('mentalhard')
"""Perform difficult mental arithmetic for 4 minutes."""
MINI_COG_TEST: Final[Task] = Task('minicog')
"""Perform mini-cog cognitive test."""
MONETARY_INCENTIVE: Final[Task] = Task('money')
"""Perform monetary incentive task."""
PERSONALITY_TEST: Final[Task] = Task('ocean')
"""Perform OCEAN personality test."""
PLAY_CHESS_BLACK: Final[Task] = Task('chessblack')
"""Play chess as black."""
PLAY_CHESS_WHITE: Final[Task] = Task('chesswhite')
"""Play chess as white."""
PROBLEM_SOLVING_BASIC_20_MINS: Final[Task] = Task('solving')
"""Perform basic problem solving for 20 minutes."""
PUZZLE_CUBE: Final[Task] = Task('puzzlecube')
"""Solve a puzzle cube."""
SAD_MEMORIES_1_MIN: Final[Task] = Task('sad')
"""Recall sad memories for 1 minute."""
STROOP_TEST_CONTROL: Final[Task] = Task('stroop1')
"""Perform Stroop test (control condition)."""
STROOP_TEST_INTERFERENCE: Final[Task] = Task('stroop2')
"""Perform Stroop test (interference condition)."""
TRIVIAL_PURSUIT_5_MINS: Final[Task] = Task('trivial')
"""Play trivial pursuit for 5 minutes."""
VIGILANCE_TEST: Final[Task] = Task('vigilance')
"""Perform vigilance test."""

# Exercise
ARM_CURL_TEST_30S: Final[Task] = Task('armcurl')
"""Perform arm curl test for 30 seconds."""
ARM_STRENGTH: Final[Task] = Task('armstrength')
"""Measure arm strength."""
BRISK_WALK_INDOORS_30_MINS: Final[Task] = Task('briskin30')
"""Brisk walk indoors for 30 minutes."""
BRISK_WALK_OUTDOORS_1KM: Final[Task] = Task('brisk1000')
"""Brisk walk outdoors for 1 km."""
BRISK_WALK_OUTDOORS_30_MINS: Final[Task] = Task('brisk30')
"""Brisk walk outdoors for 30 minutes."""
BUNGY_JUMP_25M: Final[Task] = Task('bungie25')
"""Perform a 25 m bungy jump."""
BUNGY_JUMP_50M: Final[Task] = Task('bungie50')
"""Perform a 50 m bungy jump."""
CLIMB_TREE_3_MINS: Final[Task] = Task('climbtree')
"""Climb a tree for 3 minutes."""
HIIT_20_MINS: Final[Task] = Task('hiit')
"""Perform high-intensity interval training for 20 minutes."""
HOP_OUTDOORS_100M: Final[Task] = Task('hop100')
"""Hop outdoors for 100 m."""
JOG_DOWNHILL_200M: Final[Task] = Task('jogdown')
"""Jog downhill for 200 m."""
JOG_ON_SPOT_1_MIN: Final[Task] = Task('jog')
"""Jog on the spot for 1 minute."""
JOG_OUTDOORS_30_MINS: Final[Task] = Task('jog30')
"""Jog outdoors for 30 minutes."""
JOG_UPHILL_200M: Final[Task] = Task('jogup')
"""Jog uphill for 200 m."""
JUMPING_30S: Final[Task] = Task('jumping')
"""Jump for 30 seconds."""
LIGHT_JOGGING_30_MINS: Final[Task] = Task('joglight30')
"""Light jog for 30 minutes."""
LIGHT_JOGGING_5_MINS: Final[Task] = Task('joglight')
"""Light jog for 5 minutes."""
MULTISTAGE_SHUTTLE_RUN_TEST: Final[Task] = Task('beep')
"""Perform multistage shuttle run (beep) test."""
RELAXING_WALK_INDOORS_60_MINS: Final[Task] = Task('walkin')
"""Relaxing walk indoors for 60 minutes."""
RELAXING_WALK_OUTDOORS_30_MINS: Final[Task] = Task('walk30')
"""Relaxing walk outdoors for 30 minutes."""
RELAXING_WALK_OUTDOORS_60_MINS: Final[Task] = Task('walk')
"""Relaxing walk outdoors for 60 minutes."""
RUN_INDOORS_1KM: Final[Task] = Task('runin1000')
"""Run indoors for 1 km."""
RUN_INDOORS_100M: Final[Task] = Task('runin100')
"""Run indoors for 100 m."""
RUN_INDOORS_30_MINS: Final[Task] = Task('runin30')
"""Run indoors for 30 minutes."""
RUN_INDOORS_5KM: Final[Task] = Task('runin5000')
"""Run indoors for 5 km."""
RUN_OUTDOORS_1KM: Final[Task] = Task('run1000')
"""Run outdoors for 1 km."""
RUN_OUTDOORS_100M: Final[Task] = Task('run100')
"""Run outdoors for 100 m."""
RUN_OUTDOORS_30_MINS: Final[Task] = Task('run30')
"""Run outdoors for 30 minutes."""
RUN_OUTDOORS_5KM: Final[Task] = Task('run5000')
"""Run outdoors for 5 km."""
RUN_OUTDOORS_5KM_WITH_HUSAAM: Final[Task] = Task('run5000f')
"""Run outdoors for 5 km with Husaam."""
STRENGTH_TRAINING_30_MINS: Final[Task] = Task('resistance')
"""Perform strength training for 30 minutes."""
STRETCHING_30_MINS: Final[Task] = Task('stretching30')
"""Perform stretching and holding for 30 minutes."""
STRETCHING_5_MINS: Final[Task] = Task('stretching')
"""Perform stretching and holding for 5 minutes."""
SWIM_FREESTYLE_1500M: Final[Task] = Task('freestyle1500')
"""Swim freestyle for 1500 m."""
SWIM_FREESTYLE_200M: Final[Task] = Task('freestyle200')
"""Swim freestyle for 200 m."""
SWIM_FREESTYLE_30_MINS: Final[Task] = Task('swim30')
"""Swim freestyle for 30 minutes."""
SWIM_FREESTYLE_50M: Final[Task] = Task('freestyle50')
"""Swim freestyle for 50 m."""
WALK_7M: Final[Task] = Task('walk7')
"""Walk 7 m."""
YOGA_30_MINS: Final[Task] = Task('yoga')
"""Perform yoga for 30 minutes."""

# Coordination
BALANCE_TEST_EYES_CLOSED: Final[Task] = Task('balance')
"""Perform balance test with eyes closed."""
BALANCE_TEST_EYES_OPEN: Final[Task] = Task('balanceopen')
"""Perform balance test with eyes open."""
BALL_BOUNCE_TEST_1_MIN: Final[Task] = Task('bounce')
"""Perform ball bounce test for 1 minute."""
CLAP_HANDS_1_MIN: Final[Task] = Task('clapping')
"""Clap hands for 1 minute."""
LIGHT_FLASH_TEST: Final[Task] = Task('lightbulb')
"""Perform light flash reaction test."""
RULER_TEST: Final[Task] = Task('ruler')
"""Perform ruler drop reaction test."""
TIMED_UP_AND_GO_TEST: Final[Task] = Task('tug')
"""Perform timed up and go test."""
TIMED_UP_AND_GO_TEST_COGNITIVE: Final[Task] = Task('tugc')
"""Perform timed up and go test (cognitive)."""
TIMED_UP_AND_GO_TEST_MANUAL: Final[Task] = Task('tugm')
"""Perform timed up and go test (manual)."""

# Alcoholic Drinks
BEER_LIGHT_250ML: Final[Task] = Task('lightbeer')
"""Drink 250 mL of light beer."""
BEER_REGULAR_250ML: Final[Task] = Task('regularbeer')
"""Drink 250 mL of regular beer."""
GUINNESS_250ML: Final[Task] = Task('guinness')
"""Drink 250 mL of Guinness."""
MAI_TAI_100ML: Final[Task] = Task('maitai')
"""Drink 100 mL of Mai Tai."""
RED_WINE_250ML: Final[Task] = Task('redwine')
"""Drink 250 mL of red wine."""
TEQUILA_30ML: Final[Task] = Task('tequila')
"""Drink 30 mL of tequila."""
VODKA_30ML: Final[Task] = Task('vodka')
"""Drink 30 mL of vodka."""
WHITE_WINE_250ML: Final[Task] = Task('whitewine')
"""Drink 250 mL of white wine."""

# Cold Drinks
APPLE_JUICE_250ML: Final[Task] = Task('applejuice')
"""Drink 250 mL of apple juice."""
BEER_NON_ALCOHOLIC_250ML: Final[Task] = Task('nabeer')
"""Drink 250 mL of non-alcoholic beer."""
COLA_CAFFEINATED_250ML: Final[Task] = Task('cola')
"""Drink 250 mL of caffeinated cola."""
COLA_CAFFEINE_FREE_250ML: Final[Task] = Task('coladecaf')
"""Drink 250 mL of caffeine-free cola."""
ENERGY_DRINK_CAFFEINE_FREE_250ML: Final[Task] = Task('energydrinkcf')
"""Drink 250 mL of caffeine-free energy drink."""
ENERGY_DRINK_CAFFEINE_FREE_SUGAR_FREE_250ML: Final[Task] = Task('energydrinkcfsf')
"""Drink 250 mL of caffeine-free sugar-free energy drink."""
ENERGY_DRINK_SUGAR_FREE_250ML: Final[Task] = Task('energydrinksf')
"""Drink 250 mL of sugar-free energy drink."""
ISOTONIC_DRINK_250ML: Final[Task] = Task('isotonic')
"""Drink 250 mL of isotonic drink."""
KAVA_250ML: Final[Task] = Task('kava')
"""Drink 250 mL of kava."""
LEMONADE_250ML: Final[Task] = Task('lemonade')
"""Drink 250 mL of lemonade."""
LEMONADE_SUGAR_FREE_250ML: Final[Task] = Task('lemonadesf')
"""Drink 250 mL of sugar-free lemonade."""
MILK_COLD_250ML: Final[Task] = Task('milkcold')
"""Drink 250 mL of cold milk."""
MONOSODIUM_GLUTAMATE_250ML: Final[Task] = Task('msg')
"""Drink 250 mL of monosodium glutamate solution."""
MUDDY_WATER_250ML: Final[Task] = Task('muddy')
"""Drink 250 mL of muddy water."""
NONALCOHOLIC_WHITE_WINE_250ML: Final[Task] = Task('nawine')
"""Drink 250 mL of non-alcoholic white wine."""
SALT_WATER_250ML: Final[Task] = Task('salt')
"""Drink 250 mL of salt water."""
SPORTS_DRINK_250ML: Final[Task] = Task('sports')
"""Drink 250 mL of sports drink."""
SPORTS_DRINK_CAFFEINATED_250ML: Final[Task] = Task('sportscaf')
"""Drink 250 mL of caffeinated sports drink."""
SUGAR_WATER_250ML: Final[Task] = Task('sugar')
"""Drink 250 mL of sugar water."""
VITAMIN_C_DRINK_250ML: Final[Task] = Task('vitc')
"""Drink 250 mL of vitamin C drink."""

# Hot Drinks
COFFEE_250ML: Final[Task] = Task('coffee')
"""Drink 250 mL of coffee."""
COFFEE_DECAFFEINATED_250ML: Final[Task] = Task('coffeedecaf')
"""Drink 250 mL of decaffeinated coffee."""
COFFEE_ESPRESSO_60ML: Final[Task] = Task('espresso')
"""Drink 60 mL of espresso."""
COFFEE_ESPRESSO_SUGAR_60ML: Final[Task] = Task('espressosugar')
"""Drink 60 mL of espresso with sugar."""
HONEY_DRINK_250ML: Final[Task] = Task('honeywater')
"""Drink 250 mL of honey drink."""
MILK_WARM_250ML: Final[Task] = Task('milkwarm')
"""Drink 250 mL of warm milk."""
TEA_250ML: Final[Task] = Task('tea')
"""Drink 250 mL of tea."""
TEA_GREEN_250ML: Final[Task] = Task('greentea')
"""Drink 250 mL of green tea."""
TEA_HERBAL_250ML: Final[Task] = Task('herbaltea')
"""Drink 250 mL of herbal tea."""

# Tablets
ASPIRIN_500MG: Final[Task] = Task('aspirin')
"""Take aspirin 500 mg."""
CAFFEINE_TABLET_100MG: Final[Task] = Task('caffeine')
"""Take caffeine tablet 100 mg."""
FISH_OIL_500MG: Final[Task] = Task('fishoil')
"""Take fish oil 500 mg."""
LACTOSE_TABLET: Final[Task] = Task('lactose')
"""Take lactose tablet."""
MAGNESIUM_TABLET_250MG: Final[Task] = Task('magnesium')
"""Take magnesium tablet 250 mg."""
NICOTINE_2MG: Final[Task] = Task('nicotine')
"""Take nicotine 2 mg."""
OLIVE_OIL_500MG: Final[Task] = Task('oliveoil')
"""Take olive oil 500 mg."""
PARACETAMOL_500MG: Final[Task] = Task('paracetemol')
"""Take paracetamol 500 mg."""
PSEUDOEPHEDRINE_30MG: Final[Task] = Task('pse')
"""Take pseudoephedrine 30 mg."""
SUGAR_TABLET: Final[Task] = Task('placebo')
"""Take sugar tablet (placebo)."""
VALERIAN_1G: Final[Task] = Task('valerian')
"""Take valerian 1 g."""
VITAMIN_D_50UG: Final[Task] = Task('vitamind')
"""Take vitamin D 50 µg."""

# Other Drugs
CHEW_DALPA_LEAVES_10_MINS: Final[Task] = Task('dalpa')
"""Chew dalpa leaves for 10 minutes."""
CHEW_GUM_10_MINS: Final[Task] = Task('chewinggum')
"""Chew gum for 10 minutes."""
CIGARETTE: Final[Task] = Task('cigarette')
"""Smoke a cigarette."""
HERBAL_CIGARETTE: Final[Task] = Task('herbal')
"""Smoke a herbal cigarette."""
MENTHOL_CIGARETTE: Final[Task] = Task('menthol')
"""Smoke a menthol cigarette."""
MENTHOL_INHALER: Final[Task] = Task('inhaler')
"""Use a menthol inhaler."""
NICOTINE_INHALER_2MG: Final[Task] = Task('inhalernicotine')
"""Use a nicotine inhaler 2 mg."""

# Environment
IMAGINE_PROFESSOR_5_MINS: Final[Task] = Task('professor')
"""Imagine being a professor for 5 minutes."""
IMMERSE_IN_FRESH_WATER_60_MINS: Final[Task] = Task('immersefresh')
"""Immerse in fresh water for 60 minutes."""
IMMERSE_IN_SALT_WATER_60_MINS: Final[Task] = Task('immersesalt')
"""Immerse in salt water for 60 minutes."""
NAP_15_MINS: Final[Task] = Task('nap15')
"""Take a 15 minute nap."""
NAP_30_MINS: Final[Task] = Task('nap')
"""Take a 30 minute nap."""
NAP_60_MINS: Final[Task] = Task('nap60')
"""Take a 60 minute nap."""
OXYGEN_15_PERCENT_10_MINS: Final[Task] = Task('oxygen15')
"""Breathe 15% oxygen for 10 minutes."""
OXYGEN_30_PERCENT_10_MINS: Final[Task] = Task('oxygen30')
"""Breathe 30% oxygen for 10 minutes."""
OXYGEN_35_PERCENT_10_MINS: Final[Task] = Task('oxygen35')
"""Breathe 35% oxygen for 10 minutes."""
OXYGEN_40_PERCENT_10_MINS: Final[Task] = Task('oxygen')
"""Breathe 40% oxygen for 10 minutes."""
READ_BOOK_30_MINS: Final[Task] = Task('book')
"""Read a book for 30 minutes."""
ROCKING_CHAIR_10_MINS: Final[Task] = Task('rocking')
"""Sit in a rocking chair for 10 minutes."""
SIT_10_MINS: Final[Task] = Task('sitting')
"""Sit for 10 minutes."""
SIT_30_MINS: Final[Task] = Task('sitting30')
"""Sit for 30 minutes."""
SIT_WITH_PET_CAT_10_MINS: Final[Task] = Task('petcat')
"""Sit with a pet cat for 10 minutes."""
SIT_WITH_PET_CROCODILE_10_MINS: Final[Task] = Task('petcroc')
"""Sit with a pet crocodile for 10 minutes."""
SIT_WITH_PET_DOG_10_MINS: Final[Task] = Task('petdog')
"""Sit with a pet dog for 10 minutes."""
SOCIALISING_WITH_HUSAAM_60_MINS: Final[Task] = Task('social')
"""Socialise with Husaam for 60 minutes."""
SUNBATHE_30_MINS: Final[Task] = Task('sunbathe')
"""Sunbathe for 30 minutes."""
SWEDISH_MASSAGE_10_MINS: Final[Task] = Task('massage10')
"""Receive a Swedish massage for 10 minutes."""
SWEDISH_MASSAGE_2_MINS: Final[Task] = Task('massage')
"""Receive a Swedish massage for 2 minutes."""
WATCH_TELEVISION_30_MINS: Final[Task] = Task('tv')
"""Watch television for 30 minutes."""
WATCH_TELEVISION_60_MINS: Final[Task] = Task('tv60')
"""Watch television for 60 minutes."""
WATER_SALINITY: Final[Task] = Task('salinity')
"""Measure water salinity."""

# Interventions
CHLORINE_TABLET_28_DAYS: Final[Task] = Task('chlorine')
"""Take chlorine tablet intervention for 28 days."""
GARDEN_PROJECT_14_DAYS: Final[Task] = Task('garden')
"""Participate in garden project for 14 days."""
HAND_WASHING_28_DAYS: Final[Task] = Task('hands')
"""Hand washing intervention for 28 days."""
HEALTHY_FOOD_14_DAYS: Final[Task] = Task('healthyfood')
"""Healthy food diet intervention for 14 days."""
KETOGENIC_DIET_14_DAYS: Final[Task] = Task('keto')
"""Ketogenic diet intervention for 14 days."""
REDUCE_ALCOHOL_14_DAYS: Final[Task] = Task('sobriety')
"""Reduce alcohol intake intervention for 14 days."""
SOCIAL_SPORTS_14_DAYS: Final[Task] = Task('socialsports')
"""Social sports intervention for 14 days."""
VEGETARIAN_DIET_14_DAYS: Final[Task] = Task('vegetarian')
"""Vegetarian diet intervention for 14 days."""
WATER_FILTRATION_28_DAYS: Final[Task] = Task('filter')
"""Water filtration intervention for 28 days."""

# Food
BANANA_100G: Final[Task] = Task('banana')
"""Eat 100 g of banana."""
BRAN_FLAKES_30G: Final[Task] = Task('branflakes')
"""Eat 30 g of bran flakes."""
CARROTS_100G: Final[Task] = Task('carrots')
"""Eat 100 g of carrots."""
CHOCOLATE_MILK_50G: Final[Task] = Task('chocmilk50')
"""Eat 50 g of milk chocolate."""
CHOCOLATE_WHITE_50G: Final[Task] = Task('chocwhite')
"""Eat 50 g of white chocolate."""
CORN_FLAKES_30G: Final[Task] = Task('cornflakes')
"""Eat 30 g of corn flakes."""
CREAM_CHEESE_50G: Final[Task] = Task('creamcheese')
"""Eat 50 g of cream cheese."""
LIQUORICE_50G: Final[Task] = Task('liquorice')
"""Eat 50 g of liquorice."""
LOLLIES_50G: Final[Task] = Task('lollies')
"""Eat 50 g of lollies."""
LOLLIES_SUGAR_FREE_50G: Final[Task] = Task('lolliessf')
"""Eat 50 g of sugar-free lollies."""
ORANGES_100G: Final[Task] = Task('oranges')
"""Eat 100 g of oranges."""
PEAR_100G: Final[Task] = Task('pear')
"""Eat 100 g of pear."""
SHIITAKE_MUSHROOMS_10G: Final[Task] = Task('shiitake')
"""Eat 10 g of shiitake mushrooms."""
WATERMELON_100G: Final[Task] = Task('watermelon')
"""Eat 100 g of watermelon."""
WHITE_BREAD_50G: Final[Task] = Task('bread')
"""Eat 50 g of white bread."""
WHITE_BUTTON_MUSHROOM_100G: Final[Task] = Task('button')
"""Eat 100 g of white button mushrooms."""

# Music
CLASSICAL_MUSIC_10_MINS: Final[Task] = Task('musicclassical')
"""Listen to classical music for 10 minutes."""
COUNTRY_MUSIC_10_MINS: Final[Task] = Task('musiccountry')
"""Listen to country music for 10 minutes."""
DANCE_MUSIC_10_MINS: Final[Task] = Task('musicdance')
"""Listen to dance music for 10 minutes."""
HEAVY_METAL_MUSIC_10_MINS: Final[Task] = Task('musicmetal')
"""Listen to heavy metal music for 10 minutes."""
PLAY_CELLO_10_MINS: Final[Task] = Task('cello')
"""Play cello for 10 minutes."""
PLAY_FLUTE_10_MINS: Final[Task] = Task('flute')
"""Play flute for 10 minutes."""
PLAY_PIANO_10_MINS: Final[Task] = Task('piano')
"""Play piano for 10 minutes."""

# Saliva Tests
SALIVARY_CORTISOL: Final[Task] = Task('cortisal')
"""Measure salivary cortisol."""

# Urine Tests
EMPTY_BLADDER: Final[Task] = Task('bladder')
"""Empty bladder."""
URINE_AMPHETAMINES: Final[Task] = Task('uamph')
"""Test urine for amphetamines."""
URINE_CREATININE: Final[Task] = Task('creatinine')
"""Measure urine creatinine."""
URINE_DOPAMINE: Final[Task] = Task('dopamine')
"""Measure urine dopamine."""
URINE_KETONES: Final[Task] = Task('uketone')
"""Measure urine ketones."""
URINE_PH: Final[Task] = Task('urineph')
"""Measure urine pH."""

# Miscellaneous
EXAMINE_WOUNDS: Final[Task] = Task('wound')
"""Examine wounds."""
HELIUM_500ML: Final[Task] = Task('helium')
"""Inhale 500 mL of helium."""
ROLL_20_DICE: Final[Task] = Task('dice20')
"""Roll 20 dice."""
ROLL_A_DIE: Final[Task] = Task('die')
"""Roll a die."""

__all__ = [name for name in globals() if not name.startswith('_')]
