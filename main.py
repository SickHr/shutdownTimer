import os
import time


def shutdown(timer):
    total_seconds = timer * 60

    for remaining_seconds in range(total_seconds, 0, -1):
        remaining_minutes, remaining_seconds_part = divmod(remaining_seconds, 60)
        remaining_hours, remaining_minutes = divmod(remaining_minutes, 60)
        print(
            f"\rRemaining time till shutdown: {remaining_hours:02d}:{remaining_minutes:02d}:{remaining_seconds_part:02d}",
            end="", flush=True)
        time.sleep(1)

    print("\nShutting down...")
    os.system("shutdown -s")


def main():
    while True:
        try:
            user_input = int(input("Enter the shutdown timer in minutes: "))
            if user_input <= 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    shutdown(user_input)


if __name__ == "__main__":
    main()
