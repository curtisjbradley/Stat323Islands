from api import IslandsAPI
from api.tasks import  ENERGY_DRINK, ENERGY_DRINK_CAFFEINE_FREE_250ML, ENERGY_DRINK_SUGAR_FREE_250ML, ENERGY_DRINK_CAFFEINE_FREE_SUGAR_FREE_250ML, BLOOD_CORTISOL
import csv
from time import time_ns, sleep

from tqdm import tqdm

api = IslandsAPI()
treatments = {
    "REGULAR" : ENERGY_DRINK,
    "CAFFEINE_FREE" : ENERGY_DRINK_CAFFEINE_FREE_250ML,
    "SUGAR_FREE" : ENERGY_DRINK_SUGAR_FREE_250ML,
    "CAFFEINE_AND_SUGAR_FREE" : ENERGY_DRINK_CAFFEINE_FREE_SUGAR_FREE_250ML
}

with open('energy_drink_assignments.csv', newline='') as f:
    assignments = list(csv.DictReader(f))

for row in assignments:
    row['person_id'] = api.get_person_manager().get_person(row['person_id'])



def wait_with_progress(endtime_ms : float, description: str):#Create a progress bar until a time is complete
    start = time_ns() // 1_000_000
    total_duration = endtime_ms - start

    with tqdm(total=total_duration, unit="ms", desc=description) as pbar:
        last_elapsed = 0

        while (now := time_ns() // 1_000_000) < endtime_ms:
            elapsed = now - start
            if elapsed > last_elapsed:
                pbar.update(elapsed - last_elapsed)
                last_elapsed = elapsed
            sleep(0.1)

        if last_elapsed < total_duration:
            pbar.update(total_duration - last_elapsed)




def run_task(row, n):
    return row['person_id'].do_task(treatments[row[f'treatment_{n}']])


def run_treatment(n : int):
    tqdm.write("Starting Blood Cortisol Task")
    cortisol_results = [person_row['person_id'].do_task(BLOOD_CORTISOL) for person_row in tqdm(assignments)]
    wait_with_progress(max(r['end_time'] for r in cortisol_results if r), 'Waiting for Blood Cortisol')
    drink_results = [run_task(row, n) for row in tqdm(assignments)]
    wait_with_progress(max(r['end_time'] for r in drink_results if r), "Drinking Energy Drinks")
    wait_with_progress((time_ns() // 1_000_000) + 30 * 60 * 1000 , "Waiting for effect")
    cortisol_results = [person_row['person_id'].do_task(BLOOD_CORTISOL) for person_row in tqdm(assignments)]
    wait_with_progress(max(r['end_time'] for r in cortisol_results if r), 'Waiting for Blood Cortisol')



for i in range(1, len(treatments)+1):
    print("Running Treatment" , i)
    run_treatment(i)
    wait_with_progress((time_ns() // 1_000_000) + 4 * 60 * 60 * 1000 , "Waiting 4 hours for washout")

