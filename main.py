import sys

lang = {
    "russe":0.0529,
    "serbe":0.0643,
    "suedois":0.0644,
    "anglais":0.0667,
    "esperanto":0.0690,
    "grec":0.0691,
    "norvegien":0.0694,
    "danois":0.0707,
    "finnois":0.0737,
    "italien":0.0738,
    "portugais":0.0745,
    "arabe":0.0758,
    "allemand":0.0762,
    "hebreu":0.0768,
    "espagnol":0.0770,
    "francais":0.0772,
    "malaysien":0.0778,
}

def main():
    try:
        if sys.argv[1] == "-c":
            indicator(sys.argv[2])
    except:
        raise SystemExit

def indicator(text: str):
    try:
        plain  = "".join([x.upper() for x in text.split() if  x.isalpha()])
        N = len(plain)
        freqs = {}
        for i in plain:
            if i in freqs:
                freqs[i] += 1
            else:
                freqs[i] = 1
        print(freqs)
        fs = 0.0
        alpha = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
        for i in alpha:
            fs += freqs[i] * ( freqs[i] - 1 )
        IC = fs / (N * ( N - 1 ))
        closest(IC)
    except:
        raise SystemExit

def closest(v: float):
    try: 
        diff = float('inf')
        for key, value in lang.items():
            if diff > abs(v - value):
                diff = abs(v - value)
                x = key
        print(x)
    except:
        raise SystemExit

main()
