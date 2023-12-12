## Process Monitoring V 0.2

```
A mini application for show process monitoring
```

#### Colors Code (ANSI)

* RED       : \u001b[91m
* GREEN     : \u001b[92m
* ORANGE    : \u001b[93m
* BLUE      : \u001b[94m
* ROSE      : \u001b[95m
* CYAN      : \u001b[96m
* WHITE     : \u001b[97m

### default config.json
``` json
{
    "time_to_refresh": 5,
    "max_process": 10,
    "log_file": false,
    "color_keys": "\u001b[95m",
    "color_values": "\u001b[92m"
}
```

#### Compilation with pyinstaller
> pyinstaller --onefile --icon=ico.ico main.py