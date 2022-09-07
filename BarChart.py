import matplotlib.pyplot as plt
plt.figure(figsize=(7,5))

name=["Alim","Dana","UyghurJan","Ildana","Camal"]
scores=[75,88,95,80,53]
scores2=[85,78,93,90,78]
positions=[0,1,2,3,4]
positions2=[.3,1.3,2.3,3.3,4.3]
positions3=[0.15,1.15,2.15,3.15,4.15]



plt.bar(positions,scores, width=0.3, color="g")
plt.bar(positions2,scores2,width=0.3)

plt.title("Latest test scores")
plt.xticks(positions3,name)

plt.show()
