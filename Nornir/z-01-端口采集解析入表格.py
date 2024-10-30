from nornir_handler.all_intf_2_excel import interfaces2excel
from nornir_handler.interface_taUss import interfaces_colllect_task
from nornir_handler.nornir_manager import get_nornir_onj_by_excel

if __name__ == '__main__':
    devs_nr = get_nornir_onj_by_excel('inventory2.xlsx')
    results = devs_nr.run(task=interfaces_colllect_task)
    interfaces2excel(results)
