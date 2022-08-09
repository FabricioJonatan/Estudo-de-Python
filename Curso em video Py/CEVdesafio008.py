metro = float(input('Diga uma distância em metros : '))
km = metro / 1000
hm = metro / 100
dam = metro / 10
dm = metro * 10
cm = metro * 100
mm = metro * 1000

dm, cm, mm = int(dm), int(cm), int(mm)

print('Este é o tamanho deste comprimento ({}) em :'.format(metro))
print('{:.3f} km \n{:.2f} hm \n{} dam \n{} dm \n{} cm \n{} mm'.format(km, hm, dam, dm, cm, mm))