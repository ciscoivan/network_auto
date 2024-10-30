from nornir_handler.nornir_manager import get_nornir_onj_by_excel
from nornir_handler.config_tasks import backup_config_task
from nornir_utils.plugins.functions import print_result

if __name__ == '__main__':
    devs_nr = get_nornir_onj_by_excel('inventory2.xlsx')
    results = devs_nr.run(taskbackup_config_task)
    print_result(results)
