#coding:utf-8

import psutil
import time
import ctypes
from setup import SetupManager

# Définition de la fonction SetConsoleTitleW
ctypes.windll.kernel32.SetConsoleTitleW.restype = ctypes.c_bool
ctypes.windll.kernel32.SetConsoleTitleW.argtypes = [ctypes.c_wchar_p]

# COLORS CODE | ANSI d'échappement pour les couleurs |
# GREEN     : \u001b[92m
# ROSE      : \u001b[95m
# ORANGE    : \u001b[93m
# RED       : \u001b[91m

cfg = SetupManager()

_, COLOR_TXT = cfg.setup_config_json_file()
RESET = "\033[0m" # Reset the color

TIME_RESET ,_ = cfg.setup_config_json_file()

def set_console_title(title):
    # Appel à la fonction SetConsoleTitleW pour changer le titre de la fenêtre
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
    print(f"\nTop {title} Processes:")
    print("{:<10} {:<20} {:<15} {:<15}".format('PID', 'Name', 'CPU %', 'Memory %'))
    print("="*70)
    for proc in processes[:5]:  # Affiche les 5 premiers processus
        print(COLOR_TXT +"{:<10} {:<20} {:<15.2f} {:<15.2f}".format(
            proc.info['pid'], proc.info['name'], proc.info['cpu_percent'], proc.info['memory_percent']
            ) + RESET)
    print("______ Process Monitoring V 0.2 ______")

if __name__ == "__main__":

    set_console_title("ProMonito V.0.2")

    while True:

        top_cpu_processes, top_memory_processes = get_top_processes()

        print_top_processes(top_cpu_processes, "CPU")
        print_top_processes(top_memory_processes, "Memory")

        time.sleep(TIME_RESET)
