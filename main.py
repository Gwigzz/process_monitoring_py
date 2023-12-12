#coding:utf-8
import time
import ctypes
import psutil
from setup import SetupManager

# Définition de la fonction SetConsoleTitleW
ctypes.windll.kernel32.SetConsoleTitleW.restype = ctypes.c_bool
ctypes.windll.kernel32.SetConsoleTitleW.argtypes = [ctypes.c_wchar_p]

setup           = SetupManager()
config          = setup.setup_config_json_file()

COLOR_KEYS     = config["color_keys"]
COLOR_VALUES   = config["color_values"]
RESET           = "\033[0m" # Reset the color


def set_console_title(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)

def get_top_processes():
    # Obtient une liste de tous les processus
    all_processes = [proc for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent'])]

    # Trie les processus par utilisation CPU décroissante
    top_cpu_processes = sorted(all_processes, key=lambda x: x.info['cpu_percent'], reverse=True)

    # Trie les processus par utilisation mémoire décroissante
    top_memory_processes = sorted(all_processes, key=lambda x: x.info['memory_percent'], reverse=True)

    return top_cpu_processes, top_memory_processes

def print_top_processes(processes, title):

    print(f'\nTop {title} Processes ({config["max_process"]}) :')

    print(COLOR_KEYS +"{:<10} {:<20} {:<15} {:<15}".format('PID', 'Name', 'CPU %', 'Memory %'))

    print("="*70 + RESET)

    for proc in processes[:int(config["max_process"])]:  # Affiche les 5 premiers processus
        print(COLOR_VALUES +"{:<10} {:<20} {:<15.2f} {:<15.2f}".format(
            proc.info['pid'], proc.info['name'], proc.info['cpu_percent'], proc.info['memory_percent']
            ) + RESET)
        setup.log_process_info(proc)

if __name__ == "__main__":

    set_console_title(f"ProMonito V {setup.APP_VERSION}")
    setup.create_log_file()

    while True:

        top_cpu_processes, top_memory_processes = get_top_processes()

        print_top_processes(top_cpu_processes, "CPU")
        print_top_processes(top_memory_processes, "Memory")

        time.sleep(int(config["time_to_refresh"]))
