import pandas as pd
import numpy as np
import seaborn as sns

from sklearn import __version__ as sklearn_version
from scipy import __version__ as scipy_version
from xgboost import __version__ as xgboost_version
from matplotlib import __version__ as matplotlib_version
from category_encoders import __version__ as category_encoders_version

from packaging import version

def pkg_version():
    print(
f""" Package version check
numpy: {np.__version__}
pandas: {pd.__version__}
sklearn: {sklearn_version}
matplotlib: {matplotlib_version}
seaborn: {sns.__version__}
scipy: {scipy_version}
xgboost: {xgboost_version}
category_encoders : {category_encoders_version}
"""
    )
    