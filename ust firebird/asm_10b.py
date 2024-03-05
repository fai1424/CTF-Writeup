with open("/Users/lamhungfai/Documents/GitHub/CTF-Writeup/ust firebird/SDRSharp_20231113_160000Z_119100kHz副本.wav", "rb") as f:   

    ckID = f.read(4)
    cksize = f.read(4)
    WAVEID = f.read(4)

    ckID_ = f.read(4)
    cksize_ = f.read(4)
    wFormatTag = f.read(2)
    nChannels = f.read(2)
    nSamplesPerSec = f.read(4)
    nAvgBytesPerSec = f.read(4)
    nBlockAlign = f.read(2)
    wBitPerSample = f.read(2)

    ckID__ = f.read(4)
    cksize__ = f.read(4)

    print("ckID : %s"%ckID)
    print("cksize : %s"%cksize)
    print("WAVEID : %s"%WAVEID)
    print("=======")
    print("ckID : %s"%ckID_)
    print("cksize : %s"%cksize_)
    print("wFormatTag : %s"%wFormatTag)
    print("nChannels : %s"%nChannels)
    print("nSamplePerSec : %s"%nSamplesPerSec)
    print("nAvgBytesPerSec : %s"%nAvgBytesPerSec)
    print("nBlockAlign : %s"%nBlockAlign)
    print("wBitPerSample : %s"%wBitPerSample)
    print("=======")
    print("ckID : %s"%ckID__)
    print("cksize : %s"%cksize__)

    res = open("res.txt", "w", encoding="utf-8")
    while True:
        for i in range(8):
            break_f = 0
            data_raw = f.read(1)
            if not data_raw:
                break_f = 1
                break
            data = str(bin(int.from_bytes(data_raw, 'big') & 1)).split('b')[1]
            res.write(data)
        if(break_f==1):
            break
        res.write("\n")

    res.close()
    res_r = open("res.txt", "r")
    res_string = open("res_str.txt", "w", encoding="utf-8")
    for l in res_r:
        # print(chr(int(l,2)))

        try:
            res_string.write(l[7])
            # res_string.write(((l)))
#
        except:
            res_string.close()
    res_string.close()


    reada = open("res_str.txt","r")
    for l in reada:
        for i in range(len(l),8):
            print(chr(int(l[i:i+7])))