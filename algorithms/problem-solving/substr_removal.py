def substr_removal(str):
    removal = True
    new = str

    while(removal):
        print(new)
        for i in range(len(new) - 1):
            if i+1 < len(new):
                if ( new[i] == 'A' and new[i+1] == 'B' ) or (new[i] == 'B' and new[i+1]=='B'):
                    if (i+2 > len(new) - 1):
                        new = new[0:i]
                        removal = True
                    else:
                        new = new[0:i]+new[i+2:len(new)]
                        removal = True

        removal = False

    return new

if __name__ == '__main__':
    print(substr_removal("BABBCDEFG"))
    # substr_removal("CEDAB")
