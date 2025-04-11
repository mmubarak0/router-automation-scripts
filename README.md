Automation scripts for the Huawei B315s-936  

## Requirements:
- [huawei-lte-api](https://github.com/Salamek/huawei-lte-api)

### Tested on:  

```
Software version:  21.329.01.00.1006
Web UI version:    17.100.09.00.03
```

## Scripts included
- `send_ussd.py`: Send USSD codes to the modem.
- `remove_sms.py`: Remove annoying sms from inbox based on a query.
- `net_mode.py`: Change the network mode of the modem.
- `reboot.py`: Reboot the modem.

### Usage

example for sending a USSD code:

```bash
python3 send_ussd.py http://admin:PASSWORD@192.168.8.1 --ussd "*#100#"
```

example for removing sms:

```bash
python3 remove_sms.py http://admin:PASSWORD@192.168.8.1 --query "Your current Balance is"
```

example for changing the network mode:

```bash
python3 net_mode.py http://admin:PASSWORD@192.168.8.1 --mode "4G"
```

example for rebooting the modem:

```bash
python3 reboot.py http://admin:PASSWORD@192.168.8.1
```
