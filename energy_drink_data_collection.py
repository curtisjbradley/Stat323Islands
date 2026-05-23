from api import IslandsAPI
from api.tasks import  ENERGY_DRINK, ENERGY_DRINK_CAFFEINE_FREE_250ML, ENERGY_DRINK_SUGAR_FREE_250ML, ENERGY_DRINK_CAFFEINE_FREE_SUGAR_FREE_250ML, BLOOD_CORTISOL
import pandas as pd
from time import time_ns,sleep

from tqdm import tqdm

tqdm.pandas()
tqdm()

api = IslandsAPI()
treatments = {
    "REGULAR" : ENERGY_DRINK,
    "CAFFEINE_FREE" : ENERGY_DRINK_CAFFEINE_FREE_250ML,
    "SUGAR_FREE" : ENERGY_DRINK_SUGAR_FREE_250ML,
    "CAFFEINE_AND_SUGAR_FREE" : ENERGY_DRINK_CAFFEINE_FREE_SUGAR_FREE_250ML
}


assignments = pd.read_csv('energy_drink_assignments.csv')


assignments['person_id'] = assignments['person_id'].map(lambda x: api.get_person_manager().get_person(x))



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


def  run_treatment(n : int):
    tqdm.pandas(desc="Starting Blood Cortisol Task")
    blood_cortisol_task  = assignments['person_id'].progress_apply(lambda person: person.do_task(BLOOD_CORTISOL)).apply(pd.Series) #Have every person measure their blood glucose levels
    wait_with_progress(blood_cortisol_task['end_time'].max(), 'Waiting for Blood Cortisol')
    wait_times = assignments.progress_apply(lambda row: run_task(row,n), axis=1)
    wait_with_progress(wait_times['end_time'].max(), "Drinking Energy Drinks")
    wait_with_progress((time_ns() // 1_000_000) + 30 * 60 * 1000 , "Waiting for effect")
    blood_cortisol_task  = assignments['person_id'].progress_apply(lambda person: person.do_task(BLOOD_CORTISOL)).apply(pd.Series) #Have every person measure their blood glucose levels
    wait_with_progress(blood_cortisol_task['end_time'].max(), 'Waiting for Blood Cortisol')



for i in range(1, len(treatments)+1):
    print("Running Treatment" , i)
    run_treatment(i)
    wait_with_progress((time_ns() // 1_000_000) + 4 * 60 * 60 * 1000 , "Waiting 4 hours for washout")

