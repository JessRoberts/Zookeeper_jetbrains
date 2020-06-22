group1 = int(input())
group1_rem = group1 % 2
group2 = int(input())
group2_rem = group2 % 2
group3 = int(input())
group3_rem = group3 % 2
desk1 = group1 // 2 + group1_rem
desk2 = group2 // 2 + group2_rem
desk3 = group3 // 2 + group3_rem

print(desk1 + desk2 + desk3)
