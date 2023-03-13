import subprocess


def process_exists(process_name):
    call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
    # use buildin check_output right away
    output = subprocess.check_output(call)
    # print(output)
    output = output.decode('latin-1')
    # check in last line for process name
    last_line = output.strip().split('\r\n')[-1]
    # print(last_line)
    # because Fail message could be translated
    return last_line.lower().startswith(process_name.lower())


# print(process_exists("chrome.exe"))
