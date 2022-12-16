#python标准包提供了简单的csv的读写
import csv

with open('csv_test.csv','r') as f:
    f_csv = csv.reader(f)
    name_list = list(f_csv)
    tamp_list = []
    for i in range(len(name_list)):
        tamp_list.append(name_list[i][0].split('\t'))

    print(tamp_list)
    print(tamp_list[0])
    print(tamp_list[1])


with open('csv_write.csv','w') as f:
    w_csv = csv.writer(f)
    w_csv.writerow(['id','hero','damage_caused'])
    w_csv.writerow(['ban_kai','venomancer',40000])
    w_csv.writerow(['general_ding','terror_blade',18000])
    big_list = [['weiren666','ember_spirit','20000'],
                ['lili','pudge','500000'],
                ['tenno_sun','juggernaut','0']]
    w_csv.writerows(big_list)