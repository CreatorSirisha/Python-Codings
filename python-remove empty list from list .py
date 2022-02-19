test_list=[5,6,[],[],9]
print("the original list is :" + str(test_list))
res=[ele for ele in test_list if ele!=[]]
print("list after empty list removal:"+str(res))




