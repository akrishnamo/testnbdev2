# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/01_anvilcode.ipynb.

# %% auto 0
__all__ = ['get_now_date2']

# %% ../nbs/01_anvilcode.ipynb 4
import datetime
import anvil.server



# %% ../nbs/01_anvilcode.ipynb 6
@anvil.server.callable
def get_now_date2():
  return "Ananth says  UTC time is " + str(datetime.datetime.today())
