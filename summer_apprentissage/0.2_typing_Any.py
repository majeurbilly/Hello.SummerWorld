from typing import Any

mon_dict_01: dict[Any] = {"nom": "billy", "binaritée": 3}


print(mon_dict_01)


#--------------------------------------------

from typing import Any

mon_dict_02: dict[int, Any] = {"nom": "kelly", "binaritée": 8}  #dict[Any]


print(mon_dict_02 - mon_dict_01)
