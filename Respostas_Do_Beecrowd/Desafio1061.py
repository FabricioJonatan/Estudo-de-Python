diaI = input().split()
horaI = input().split()
diaF = input().split()
horaF = input().split()

di, df = int(diaI[1]), int(diaF[1])
hi, mi, si = int(horaI[0]), int(horaI[2]), int(horaI[4])
hf, mf, sf = int(horaF[0]), int(horaF[2]), int(horaF[4])

minutoseg = 60
horaseg = minutoseg * 60
diaseg = horaseg * 24

inicio = si + mi * minutoseg + hi * horaseg + di * diaseg
fim = sf + mf * minutoseg + hf * horaseg + df * diaseg

if inicio < fim:
    tempo = fim - inicio
    dias = int(tempo/diaseg)
    tempo = tempo%diaseg
    horas = int(tempo/horaseg)
    tempo = tempo%horaseg
    minutos = int(tempo/minutoseg)
    tempo = tempo%minutoseg
    segundos = tempo

    print('{} dia(s)'.format(dias))
    print('{} hora(s)'.format(horas))
    print('{} minuto(s)'.format(minutos))
    print('{} segundo(s)'.format(segundos))