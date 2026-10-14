def main():
    print("===================================")
    print(" Network Troubleshooting Assistant")
    print("===================================")
    print("This program helps diagnose common")
    print("internet connection problems.")
    print()

    results = troubleshoot_network()
    display_results(results)


def ask_yes_no(question):
    while True:
        answer = input(question + " (yes/no): ").lower().strip()

        if answer == "yes" or answer == "no":
            return answer
        else:
            print("Please enter yes or no.")


def troubleshoot_network():
    results = []

    print("\nLet's check your network connection.")

    internet = ask_yes_no("Can you access the internet?")

    if internet == "yes":
            results.append("Internet connection is working.")
            results.append("Recommendation: No internet fix is needed.")
    else:
        results.append("Internet connection is not working.")

        devices = ask_yes_no("Can other devices connect?")

        if devices == "yes":
            results.append("The problem may be with your computer.")
            results.append("Recommendation: Restart your computer and check Wi-Fi.")
        else:
            results.append("The problem may be with your router or modem.")
            results.append("Recommendation: Restart your router and modem.")

    return results


def display_results(results):
    print("\n========== TROUBLESHOOTING REPORT ==========")

    for item in results:
        print("- " + item)

    print("============================================")
    print("Thank you for using the assistant!")
if __name__== "__main__":
    main()
