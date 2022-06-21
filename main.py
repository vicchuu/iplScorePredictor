import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import pandas as ps
matplotlib.rcParams["figure.figsize"] = (20,10)


complete_org_dataset = ps.read_csv("Bengaluru_House_Data.csv")
print(complete_org_dataset.head())
