import psutil


def gaseste_pid_radiocodedb():
    for proces in psutil.process_iter(["pid", "name"]):
        if proces.info["name"] == "RadioCodeDatabase v2.0.exe":
            return proces.info["pid"]
    return None
