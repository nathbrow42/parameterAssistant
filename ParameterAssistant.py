
import webbrowser

class serverSite:
    def __init__(self, serverNum, accountNum):
        self.serverNum = serverNum
        self.accountNum = accountNum
        self.url = "https://" + serverNum + ".serviceassistant.com/" + str(accountNum)

    def getUrl(self):
        return self.url

def getAccountNum():
    accountNum = input("Account number: ")
    print("You entered: ", accountNum)
    yesOrNo = input("Is this Correct? (Y/N): ")
    if yesOrNo != "Y" or yesOrNo != "y":
        while yesOrNo != "Y" or yesOrNo != "N" or yesOrNo != "y" or yesOrNo != "n":
            if yesOrNo == "Y" or yesOrNo == "y":
                break
            elif yesOrNo == "N" or yesOrNo == "n":
                accountNum = input("Account number: ")
                print("You entered: ", accountNum)
                yesOrNo = input("Is this Correct? (Y/N): ")
            else:
                yesOrNo = input("(Y/N): ")
    return accountNum


def main():
    
    accountNum = getAccountNum()

    server1a = serverSite("1a",accountNum)
    server1b = serverSite("1b",accountNum)
    server1c = serverSite("1c",accountNum)
    server1d = serverSite("1d",accountNum)
    server1e = serverSite("1e",accountNum)
    server1f = serverSite("1f",accountNum)
    server1g = serverSite("1g",accountNum)
    server1h = serverSite("1h",accountNum)

    webbrowser.open_new_tab(server1a.getUrl())
    webbrowser.open_new_tab(server1b.getUrl())
    webbrowser.open_new_tab(server1c.getUrl())
    webbrowser.open_new_tab(server1d.getUrl())
    webbrowser.open_new_tab(server1e.getUrl())
    webbrowser.open_new_tab(server1f.getUrl())
    webbrowser.open_new_tab(server1g.getUrl())
    webbrowser.open_new_tab(server1h.getUrl())

    return

if __name__ == '__main__': main()

        
