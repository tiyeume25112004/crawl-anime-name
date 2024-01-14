def prRed(skk): 
    print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): 
    print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): 
    print("\033[93m {}\033[00m" .format(skk))
def prLightPurple(skk): 
    print("\033[94m {}\033[00m" .format(skk))
def prPurple(skk): 
    print("\033[95m {}\033[00m" .format(skk))
def prCyan(skk): 
    print(f"\033[96m {skk}\033[00m")
def prLightGray(skk): 
    print("\033[97m {}\033[00m" .format(skk))


def prBlack(skk): 
    print("\033[98m {}\033[00m" .format(skk))

def banners():
    banner = """
    _____        _____                    _ 
    |  __ \      / ____|                  | |
    | |__) |   _| |     _ __ __ ___      _| |
    |  ___/ | | | |    | '__/ _` \ \ /\ / / |
    | |   | |_| | |____| | | (_| |\ V  V /| |
    |_|    \__, |\_____|_|  \__,_| \_/\_/ |_|
            __/ |                            
        ______|___/__ ______                    
        |______|______|______|                   
        collection of kon                     
    """
    prRed(banner)

