from nornir import InitNornir


# 需要安装pip install  nornir_table_inventory


def get_nornir_onj_by_excel(inventory_filename='inventory.xlsx', num_workers=50):
    runner = {
        "plugin": "threaded",
        "options": {
            "num_workers": num_workers,
        },
    }
    inventory = {
        "plugin": "ExcelInventory",
        "options": {
            "excel_file": inventory_filename,
        },
    }
    nr_obj = InitNornir(runner=runner, inventory=inventory)
    return nr_obj


if __name__ == '__main__':
    file = '../inventory2.xlsx'
    nr = get_nornir_onj_by_excel(file)
