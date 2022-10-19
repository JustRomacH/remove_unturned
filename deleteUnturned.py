import os
import shutil
import pathlib


class DelUnturned:
    def __init__(self) -> None:
        self.SYS = os.getenv("SystemDrive")
        self.userDir = pathlib.Path.home()
        self.startUpDir = f'{self.userDir}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup'

    def success(self) -> None:
        print("Дамой Unturned")

    def error(self) -> None:
        print("Не дамой Unturned :(")

    def deleteUnturned(self) -> None:
        try:
            shutil.rmtree(
                f"{self.SYS}\\Program Files (x86)\\Steam\\steamapps\\common\\unturned")
            self.success()
        except Exception as ex:
            print(repr(ex))
            self.error()


def main() -> None:
    delUnt = DelUnturned()
    delUnt.deleteUnturned()


if __name__ == "__main__":
    main()
