import matplotlib.pyplot as plt
import pandas as pd
 
Data = pd.read_csv('data 2.csv')

print('Limited iteration press 1')
print('Unlimited iteration press 2')
num =int(input('press: '))

plt.scatter(Data['X'], Data['Y'], marker='*', color='red')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('Linear Regression')

thita0= 50
thita1= 60
oThita0=0
oThita1=0
learningRate=0.001

df = pd.DataFrame(Data) 
x_list = df['X'].tolist()
y_list = df['Y'].tolist()
sum=0
j=0
for i in x_list:
     result= ((thita0+(thita1*i))-y_list[j])
     result=result*result
     j+=1
     sum=sum+result

cost_function=sum/(2*len(x_list))
print('cost_function= ',cost_function)


if (num==1):
    iteration=int(input('How many iteration want!'))
    
    for l in range(0,iteration):
        oThita0=thita0
        oThita1=thita1
        sum=0
        sum2= 0
        j=0
        result=0
        for i in x_list:
            result= ((thita0+(thita1*i))-y_list[j])
            result2=((thita0+(thita1*i))-y_list[j])*i
            j+=1
            sum=sum+result
            sum2=sum2+result
        thita0=(thita0-((learningRate*sum)/len(x_list)))
        thita1=(thita1-((learningRate*sum2)/len(x_list))) 
    
        sum=0
        j=0
        for i in x_list:
            result= ((thita0+(thita1*i))-y_list[j])
            result=result*result
            j+=1
            sum=sum+result
        
        cost_function1=sum/(2*len(x_list))
        print('cost_function1= ',cost_function1)
        if(cost_function1 < cost_function):
            flag=1
            cost_function=cost_function1  
        
        else:
            flag=2
            break
    if (flag==1):
        print ('Best Thita0= ', oThita0)
        print ('Best Thita1= ', oThita1)
    else:
        print ('Best Thita0= ', thita0)
        print ('Best Thita1= ', thita1)
    
    
if (num==2):    
    #for l in range(0,len(x_list)):
    while True:
        oThita0=thita0
        oThita1=thita1
        sum=0
        sum2= 0
        j=0
        result=0
        for i in x_list:
            result= ((thita0+(thita1*i))-y_list[j])
            result2=((thita0+(thita1*i))-y_list[j])*i
            j+=1
            sum=sum+result
            sum2=sum2+result2
        thita0=(thita0-((learningRate*sum)/len(x_list)))
        thita1=(thita1-((learningRate*sum2)/len(x_list))) 
    
        sum=0
        j=0
        for i in x_list:
            result= ((thita0+(thita1*i))-y_list[j])
            result=result*result
            j+=1
            sum=sum+result
        
        cost_function1=sum/(2*len(x_list))
        print('cost_function1= ',cost_function1)
        if(cost_function1 < cost_function):
            cost_function=cost_function1  
        
        else:
            break

    print ('Best Thita0= ', oThita0)
    print ('Best Thita1= ', oThita1)
#thita0 = 24.399952593923135
#thita1 = 7.6000105970017025
#print(thita0+thita1*8)
y_predicted_value=[]
for i in range(0, len(x_list), 1):
    y_predicted_value.append(thita0+thita1*x_list[i])
plt.plot(x_list, y_predicted_value)
plt.show()
     
          
        
  
    
    