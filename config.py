from cadCAD.configuration import append_configs
from cadCAD.configuration.utils import ep_time_step, config_sim
from cadCAD.engine import ExecutionMode, ExecutionContext, Executor
from cadCAD import configs
from cadCAD.configuration import append_configs
from cadCAD.configuration.utils import config_sim, access_block
from typing import Dict, List
import numpy as np
from sqlalchemy import create_engine
import pandas as pd
import json
import datetime
from decimal import Decimal
from datetime import timedelta
import matplotlib.pyplot as plt
import math
import datetime
from datetime import timedelta

# from genesis_states import genesis_states
# from functions import *
# from partial_state_update_block import partial_state_update_block


from cadCAD.configuration.utils import ep_time_step,config_sim, access_block
from cadCAD.configuration import append_configs
from tabulate import tabulate
from cadCAD.engine import ExecutionMode, ExecutionContext, Executor
from cadCAD import configs

from typing import Dict, List

from functions import *
from genesis_states import genesis_states
from partial_state_update_block import partial_state_update_block

#Internal
avg_200 = 200
avg_250 = 250
avg_300 = 300
avg_350 = 350
avg_400 = 400

record = 57
games = 160
seasons = 20
attempts = games * seasons - record
#print(attempts)
# games = 160
# seasons = 20
time_step_count = games * seasons
run_count = 2


# ------------------- RANDOM STATE SEED ------------------------------
seed = {
#    'z': np.random.RandomState(1)
}
#--------------EXOGENOUS STATE MECHANISM DICTIONARY--------------------
exogenous_states =     {
    "timestamp": set_time,
    }

#--------------ENVIRONMENTAL PROCESS DICTIONARY------------------------
env_processes = {
}
#----------------------SIMULATION RUN SETUP----------------------------
sim_config = config_sim(
    {
    "N": run_count,
    "T": range(time_step_count)
#     "M": g  # for parameter sweep
}
)

append_configs(
    sim_configs=sim_config,
    initial_state=genesis_states,
    seeds=seed,
    raw_exogenous_states= exogenous_states,
    env_processes=env_processes,
    partial_state_update_blocks=partial_state_update_block
)

exec_mode = ExecutionMode()

first_config = configs # only contains config1
single_proc_ctx = ExecutionContext(context=exec_mode.single_proc)
run1 = Executor(exec_context=single_proc_ctx, configs=first_config)
run1_raw_result, tensor_field = run1.execute()
result = pd.DataFrame(run1_raw_result)
print(result.head())
# return result