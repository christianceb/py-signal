import signal
import os


class Application:
    ctrl_c_once = False

    def __init__(self):
        signal.signal(signal.SIGINT, lambda signum, frame: self.ctrl_c(signum, frame))

        while True:
            try:
                what_you_want_to_do = input("Hit any key, But if you CTRL+C, something happens\n")

                if what_you_want_to_do == "SIGINT":
                    os.kill(os.getpid(), signal.SIGINT)
            except:
                ""  # Do nothing really. We need that right there because otherwise, python will just complain

    def ctrl_c(self, signum, frame):
        if self.ctrl_c_once:
            print("\nWell you did it again. Goodbye.\n")

            os.kill(os.getpid(), signal.SIGINT)

        print("\nIf you CTRL+C again, I might quit\n")

        self.ctrl_c_once = True


def main():
    Application()


if __name__ == '__main__':
    main()
