import psutil

def ProcessDisplay():
    Border = "*"*50
    print(Border)
    print("Information of currently running process :")
    print(Border)

    for proc in psutil.process_iter():
        info = proc.as_dict(attrs=["pid","name","username"])
        info["vms"] = proc.memory_info().vms / (1024 * 1024)
        print(info)


def main():
    ProcessDisplay()



if __name__ == "__main__":
    main()