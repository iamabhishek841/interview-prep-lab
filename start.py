from pathlib import Path

ROOT = Path(__file__).parent


def show_menu() -> None:
    print("\nInterview Prep Lab")
    print("1. Foundation")
    print("2. DSA")
    print("3. LLD")
    print("4. Progress")
    print("5. Exit")


def main() -> None:
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            print(f"Open: {ROOT / 'foundation'}")
        elif choice == "2":
            print(f"Open: {ROOT / 'dsa'}")
        elif choice == "3":
            print(f"Open: {ROOT / 'lld'}")
        elif choice == "4":
            print((ROOT / 'progress.json').read_text(encoding='utf-8'))
        elif choice == "5":
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
