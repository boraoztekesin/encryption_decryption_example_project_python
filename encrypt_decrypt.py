import sys
import os
try:
    assert len(sys.argv) == 5, "Parameter number error"
    assert sys.argv[1] == "enc" or sys.argv[1] == "dec", "Undefined parameter error"
    valids_plain = ["A", "B", "C", "D", "E", "G", "F", "H", "I", "J", "K", "L", "M", "N", "O", "P", "R", "S", "T",
                    "Q", "U", "V", "W", "X", "Y", "Z", " "]
    valids_cipher = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ","]
    valids_key = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", ","]
    if sys.argv[1] == "enc":
        assert "key" in sys.argv[2], "Key file could not be found."
        assert ".txt" in sys.argv[2], "Key file could not be read."
        assert "plain" in sys.argv[3], "Input file could not be found."
        assert ".txt" in sys.argv[3], "Input file could not be read."
        f = open(sys.argv[2], "r")
        plain = open(sys.argv[3], "r")
        out_enc = open(sys.argv[4], "w")
        assert os.path.getsize(sys.argv[2]) != 0, "Key file is empty."
        assert os.path.getsize(sys.argv[3]) != 0, "Input file is empty."
        asdasd = plain.read()
        for i in asdasd:
            assert i.upper() in valids_plain, "Assertion Error : Invalid characters in input file."
        evetttttt=f.readlines()
        vkey=[]
        for i in evetttttt:
            vkey.append(i.strip("\n"))
        for i in vkey:
            for j in i:
                assert j in valids_key, "AssertionError : Invalid character in key file."






        hehheee = asdasd.upper()
        inp = []
        for i in range(len(hehheee)):
            inp.append(hehheee[i])
        liste = []
        liste2 = []
        for i in inp:
            if i == "A":
                liste.append(1)
            if i == "B":
                liste.append(2)
            if i == "C":
                liste.append(3)
            if i == "D":
                liste.append(4)
            if i == "E":
                liste.append(5)
            if i == "F":
                liste.append(6)
            if i == "G":
                liste.append(7)
            if i == "H":
                liste.append(8)
            if i == "I":
                liste.append(9)
            if i == "J":
                liste.append(10)
            if i == "K":
                liste.append(11)
            if i == "L":
                liste.append(12)
            if i == "M":
                liste.append(13)
            if i == "N":
                liste.append(14)
            if i == "O":
                liste.append(15)
            if i == "P":
                liste.append(16)
            if i == "Q":
                liste.append(17)
            if i == "R":
                liste.append(18)
            if i == "S":
                liste.append(19)
            if i == "T":
                liste.append(20)
            if i == "U":
                liste.append(21)
            if i == "V":
                liste.append(22)
            if i == "W":
                liste.append(23)
            if i == "X":
                liste.append(24)
            if i == "Y":
                liste.append(25)
            if i == "Z":
                liste.append(26)
            if i == " ":
                liste.append(27)

        b = []
        a = []
        for x in evetttttt:
            b.append([x.strip("\n")])
        print(b)
        for i in b:
            for j in i:
                a.append(j.split(","))
        print(a)
        a2 = []
        for i in a:
            for j in i:
                a2.append(int(j))
        print(a2)

        x = 0
        for i in a2:
            x += 1

        if x == 4:
            a = [[a2[0], a2[1]], [a2[2], a2[3]]]
            print(a)
            counter = 0
            print(liste)
            if len(inp) % 2 != 0:
                liste.append(27)
            for i in range(int(len(liste) / 2)):
                liste2.append([[liste[0 + counter]], [liste[1 + counter]]])
                counter += 2
            print(liste2)
            newwwkeeee = []
            for x in liste2:
                matrix1 = a
                matrix2 = x
                result = [[0], [0]]
                for i in range(len(matrix1)):
                    for j in range(len(matrix2[0])):
                        for k in range(len(matrix2)):
                            result[i][j] += matrix1[i][k] * matrix2[k][j]
                newwwkeeee.append(result)
            print(newwwkeeee)
            list3 = []
            for i in newwwkeeee:
                for j in i:
                    for k in j:
                        list3.append(k)
            print(list3)
            for i in list3:
                    out_enc.write(str(i))
                    out_enc.write(",")

        if x == 9:
            a = [[a2[0], a2[1], a2[2]], [a2[3], a2[4], a2[5]], [a2[6], a2[7], a2[8]]]
            counter = 0
            print(liste)
            if len(inp) % 3 == 2:
                liste.append(27)
            if len(inp) % 3 == 1:
                liste.append(27)
                liste.append(27)
            for i in range(int(len(liste) / 3)):
                liste2.append([[liste[0 + counter]], [liste[1 + counter]], [liste[2 + counter]]])
                counter += 3
            print(liste2)
            newwwkeeee = []
            for x in liste2:
                matrix1 = a
                matrix2 = x
                result = [[0], [0], [0]]
                for i in range(len(matrix1)):
                    for j in range(len(matrix2[0])):
                        for k in range(len(matrix2)):
                            result[i][j] += matrix1[i][k] * matrix2[k][j]
                newwwkeeee.append(result)
            print(newwwkeeee)
            list3 = []
            for i in newwwkeeee:
                for j in i:
                    for k in j:
                        list3.append(k)
            print(list3)
            for i in list3:
                    out_enc.write(str(i))
                    out_enc.write(",")
        if x == 16:
            a = [[a2[0], a2[1], a2[2], a2[3]], [a2[4], a2[5], a2[6], a2[7]], [a2[8], a2[9], a2[10], a2[11]],
                 [a2[12], a2[13], a2[14], a2[15]]]
            counter = 0
            print(liste)
            if len(inp) % 4 == 3:
                liste.append(27)
            if len(inp) % 4 == 2:
                liste.append(27)
                liste.append(27)
            if len(inp) % 4 == 1:
                liste.append(27)
                liste.append(27)
                liste.append(27)
            for i in range(int(len(liste) / 4)):
                liste2.append([[liste[0 + counter]], [liste[1 + counter]], [liste[2 + counter]], [liste[3 + counter]]])
                counter += 4
            print(liste2)
            newwwkeeee = []
            for x in liste2:
                matrix1 = a
                matrix2 = x
                result = [[0], [0], [0], [0]]
                for i in range(len(matrix1)):
                    for j in range(len(matrix2[0])):
                        for k in range(len(matrix2)):
                            result[i][j] += matrix1[i][k] * matrix2[k][j]
                newwwkeeee.append(result)
            print(newwwkeeee)
            list3 = []
            for i in newwwkeeee:
                for j in i:
                    for k in j:
                        list3.append(k)
            print(list3)
            for i in list3:
                    out_enc.write(str(i))
                    out_enc.write(",")





    # deccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

    elif sys.argv[1] == "dec":
        assert "key" in sys.argv[2], "Key file could not be found."
        assert ".txt" in sys.argv[2], "Key file could not be read."
        assert "cipher" in sys.argv[3], "Input file could not be found."
        assert ".txt" in sys.argv[3], "Input file could not be read."
        f = open(sys.argv[2], "r")
        cipher = open(sys.argv[3], "r")
        out_dec = open(sys.argv[4], "w")

        assert os.path.getsize(sys.argv[2]) != 0, "Key file is empty."
        assert os.path.getsize(sys.argv[3]) != 0, "Input file is empty."
        vkey = []
        ewwwww = f.readlines()
        for i in ewwwww:
            vkey.append(i.strip("\n"))
        for i in vkey:
            for j in i:
                assert j in valids_key, "AssertionError : Invalid character in key file."
        cip = cipher.read()
        for i in cip:
            assert i in valids_cipher, "Assertion Error : Invalid characters in input file."

        cipke = cip.split(",")
        b = []
        cipp = []

        for i in cipke:
            cipp.append(int(i))

        b = []
        a = []
        for x in ewwwww:
            b.append([x.strip("\n")])
        for i in b:
            for j in i:
                a.append(j.split(","))

        a2 = []
        for i in a:
            for j in i:
                a2.append(int(j))
        print(a2)
        x = 0
        for i in a2:
            x += 1

        if x == 4:
            a = [[a2[0], a2[1]], [a2[2], a2[3]]]
            print(a)
            print("NASIL DA BURDAYIM", a)
            a[0][1] = a[0][1] * (-1)
            a[1][0] = a[1][0] * (-1)


            def detA():
                return (round(1 / (int(a[0][0]) * int(a[1][1]) - int(a[0][1]) * int(a[1][0]))))


            x = a[0][0]
            a[0][0] = a[1][1]
            a[1][1] = x
            a[0][0] * detA()
            a[0][1] * detA()
            a[1][0] * detA()
            a[1][1] * detA()
            print("TAK DYE", a)
            cipherx = []
            lastlist = []
            counter = 0
            for i in range(int(len(cipp) / 2)):
                cipherx.append([[cipp[0 + counter]], [cipp[1 + counter]]])
                counter += 2
            print(cipherx)
            for x in cipherx:
                matrix1 = a
                matrix2 = x
                result = [[0], [0]]
                for i in range(len(matrix1)):
                    for j in range(len(matrix2[0])):
                        for k in range(len(matrix2)):
                            result[i][j] += matrix1[i][k] * matrix2[k][j]
                lastlist.append(result)
            print(lastlist)
            declist = []
            for j in lastlist:
                for k in j:
                    for i in k:
                        if i == 1:
                            declist.append("A")
                        if i == 2:
                            declist.append("B")
                        if i == 3:
                            declist.append("C")
                        if i == 4:
                            declist.append("D")
                        if i == 5:
                            declist.append("E")
                        if i == 6:
                            declist.append("F")
                        if i == 7:
                            declist.append("G")
                        if i == 8:
                            declist.append("H")
                        if i == 9:
                            declist.append("I")
                        if i == 10:
                            declist.append("J")
                        if i == 11:
                            declist.append("K")
                        if i == 12:
                            declist.append("L")
                        if i == 13:
                            declist.append("M")
                        if i == 14:
                            declist.append("N")
                        if i == 15:
                            declist.append("O")
                        if i == 16:
                            declist.append("P")
                        if i == 17:
                            declist.append("Q")
                        if i == 18:
                            declist.append("R")
                        if i == 19:
                            declist.append("S")
                        if i == 20:
                            declist.append("T")
                        if i == 21:
                            declist.append("U")
                        if i == 22:
                            declist.append("V")
                        if i == 23:
                            declist.append("W")
                        if i == 24:
                            declist.append("X")
                        if i == 25:
                            declist.append("Y")
                        if i == 26:
                            declist.append("Z")
                        if i == 27:
                            declist.append(" ")
            print(declist)
            for i in declist:
                out_dec.write(i)
        # 3X333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        if x == 9:
            a = [[a2[0], a2[1], a2[2]], [a2[3], a2[4], a2[5]], [a2[6], a2[7], a2[8]]]
            print(a)



            def deletion(rx, ry, c, t=0):
                fac = (ry[c] - t) / rx[c]
                for i in range(len(ry)):
                    ry[i] -= fac * rx[i]


            def g(a):
                for i in range(len(a)):
                    if a[i][i] == 0:
                        for j in range(i + 1, len(a)):
                            if a[i][j] != 0:
                                a[i], a[j] = a[j], a[i]
                                break
                        else:
                            return -1
                    for j in range(i + 1, len(a)):
                        deletion(a[i], a[j], i)
                for i in range(len(a) - 1, -1, -1):
                    for j in range(i - 1, -1, -1):
                        deletion(a[i], a[j], i)
                for i in range(len(a)):
                    deletion(a[i], a[i], i, t=1)
                return a


            def inverse(a):
                h = [[] for _ in a]
                for i, r in enumerate(a):
                    assert len(r) == len(a)
                    h[i].extend(r + [0] * i + [1] + [0] * (len(a) - i - 1))
                g(h)
                listerr = []
                for i in range(len(h)):
                    listerr.append(h[i][len(h[i]) // 2:])
                return listerr


            cipherx = []
            newlist = []
            counter = 0
            for i in range(int(len(cipp) / 3)):
                cipherx.append([[cipp[0 + counter]], [cipp[1 + counter]], [cipp[2 + counter]]])
                counter += 3

            print("cipherx", cipherx)
            for x in cipherx:
                matrix1 = inverse(a)
                matrix2 = x
                result = [[0], [0], [0]]
                for i in range(len(matrix1)):
                    for j in range(len(matrix2[0])):
                        for k in range(len(matrix2)):
                            result[i][j] += matrix1[i][k] * matrix2[k][j]
                newlist.append(result)
            print("newlistt", newlist)
            declist = []
            for j in newlist:
                for k in j:
                    for i in k:
                        if i == 1:
                            declist.append("A")
                        if i == 2:
                            declist.append("B")
                        if i == 3:
                            declist.append("C")
                        if i == 4:
                            declist.append("D")
                        if i == 5:
                            declist.append("E")
                        if i == 6:
                            declist.append("F")
                        if i == 7:
                            declist.append("G")
                        if i == 8:
                            declist.append("H")
                        if i == 9:
                            declist.append("I")
                        if i == 10:
                            declist.append("J")
                        if i == 11:
                            declist.append("K")
                        if i == 12:
                            declist.append("L")
                        if i == 13:
                            declist.append("M")
                        if i == 14:
                            declist.append("N")
                        if i == 15:
                            declist.append("O")
                        if i == 16:
                            declist.append("P")
                        if i == 17:
                            declist.append("Q")
                        if i == 18:
                            declist.append("R")
                        if i == 19:
                            declist.append("S")
                        if i == 20:
                            declist.append("T")
                        if i == 21:
                            declist.append("U")
                        if i == 22:
                            declist.append("V")
                        if i == 23:
                            declist.append("W")
                        if i == 24:
                            declist.append("X")
                        if i == 25:
                            declist.append("Y")
                        if i == 26:
                            declist.append("Z")
                        if i == 27:
                            declist.append(" ")
            print(declist)
            for i in declist:
                out_dec.write(i)
        if x == 16:
            a = [[a2[0], a2[1], a2[2], a2[3]], [a2[4], a2[5], a2[6], a2[7]], [a2[8], a2[9], a2[10], a2[11]],
                 [a2[12], a2[13], a2[14], a2[15]]]
            print(a)
            newlist = []


            def deletion(rx, ry, c, t=0):
                fac = (ry[c] - t) / rx[c]
                for i in range(len(ry)):
                    ry[i] -= fac * rx[i]


            def g(a):
                for i in range(len(a)):
                    if a[i][i] == 0:
                        for j in range(i + 1, len(a)):
                            if a[i][j] != 0:
                                a[i], a[j] = a[j], a[i]
                                break
                        else:
                            return -1
                    for j in range(i + 1, len(a)):
                        deletion(a[i], a[j], i)
                for i in range(len(a) - 1, -1, -1):
                    for j in range(i - 1, -1, -1):
                        deletion(a[i], a[j], i)
                for i in range(len(a)):
                    deletion(a[i], a[i], i, t=1)
                return a


            def inverse(a):
                h = [[] for _ in a]
                for i, r in enumerate(a):
                    assert len(r) == len(a)
                    h[i].extend(r + [0] * i + [1] + [0] * (len(a) - i - 1))
                g(h)
                listerr = []
                for i in range(len(h)):
                    listerr.append(h[i][len(h[i]) // 2:])
                return listerr


            cipherx = []
            counter = 0
            for i in range(int(len(cipp) / 4)):
                cipherx.append([[cipp[0 + counter]], [cipp[1 + counter]], [cipp[2 + counter]], [cipp[3 + counter]]])
                counter += 4

            print("cipherx", cipherx)
            for x in cipherx:
                matrix1 = inverse(a)
                matrix2 = x
                result = [[0], [0], [0], [0]]
                for i in range(len(matrix1)):
                    for j in range(len(matrix2[0])):
                        for k in range(len(matrix2)):
                            result[i][j] += matrix1[i][k] * matrix2[k][j]
                newlist.append(result)
            print("newlistt", newlist)
            declist = []
            for j in newlist:
                for k in j:
                    for i in k:
                        if i == 1:
                            declist.append("A")
                        if i == 2:
                            declist.append("B")
                        if i == 3:
                            declist.append("C")
                        if i == 4:
                            declist.append("D")
                        if i == 5:
                            declist.append("E")
                        if i == 6:
                            declist.append("F")
                        if i == 7:
                            declist.append("G")
                        if i == 8:
                            declist.append("H")
                        if i == 9:
                            declist.append("I")
                        if i == 10:
                            declist.append("J")
                        if i == 11:
                            declist.append("K")
                        if i == 12:
                            declist.append("L")
                        if i == 13:
                            declist.append("M")
                        if i == 14:
                            declist.append("N")
                        if i == 15:
                            declist.append("O")
                        if i == 16:
                            declist.append("P")
                        if i == 17:
                            declist.append("Q")
                        if i == 18:
                            declist.append("R")
                        if i == 19:
                            declist.append("S")
                        if i == 20:
                            declist.append("T")
                        if i == 21:
                            declist.append("U")
                        if i == 22:
                            declist.append("V")
                        if i == 23:
                            declist.append("W")
                        if i == 24:
                            declist.append("X")
                        if i == 25:
                            declist.append("Y")
                        if i == 26:
                            declist.append("Z")
                        if i == 27:
                            declist.append(" ")
            print(declist)
            for i in declist:
                out_dec.write(i)
except AssertionError as msg:
    print(msg)
