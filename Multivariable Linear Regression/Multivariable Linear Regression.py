import matplotlib.pyplot as plt
import pandas as pd
 
Data = pd.read_csv('Data 2.csv')

print('Limited iteration press 1')
print('Unlimited iteration press 2')
num =int(input("Press: "))

thita0= 10
thita1= 20
thita2= 30
thita3= 40
thita4= 50
oThita0=0
oThita1= 0
oThita2= 0
oThita3= 0
oThita4= 0
learningRate=0.0000000001

df = pd.DataFrame(Data) 
x1_list = df['size(feet^2)(x1)'].tolist()
x2_list = df['# of bedrooms(x2)'].tolist()
x3_list = df['# of floors(x3)'].tolist()
x4_list = df['age of home(year)(x4)'].tolist()
y_list = df['price($)(y)'].tolist()



cost_value=[]
iteration_Number=[]
sum=0
j=0
for i in range(0,len(x1_list)):
     result= ((thita0+(thita1*x1_list[i])+(thita2*x2_list[i])+(thita3*x3_list[i])+(thita4*x4_list[i]))-y_list[j])
     result=result*result
     j+=1
     sum=sum+result

cost_function=sum/(2*len(x1_list))
cost_value.append(cost_function)
iteration_Number.append(1)
print('cost_function= ',cost_function)

x=1

if (num==1):
    iteration=int(input('How many iteration want!'))
    for l in range(0,iteration):
        x=x+1
        oThita0= thita0
        oThita1= thita1
        oThita2= thita2
        oThita3= thita3
        oThita4= thita4
        
        sum=0
        sum2=0
        sum3=0
        sum4=0
        sum5=0
        j=0
        result=0
        
        for i in range(0,len(x1_list)):
            result= ((thita0+(thita1*x1_list[i])+(thita2*x2_list[i])+(thita3*x3_list[i])+(thita4*x4_list[i]))-y_list[j])
            result2= ((thita0+(thita1*x1_list[i])+(thita2*x2_list[i])+(thita3*x3_list[i])+(thita4*x4_list[i]))-y_list[j])*x1_list[0]
            result3= ((thita0+(thita1*x1_list[i])+(thita2*x2_list[i])+(thita3*x3_list[i])+(thita4*x4_list[i]))-y_list[j])*x1_list[1]
            result4= ((thita0+(thita1*x1_list[i])+(thita2*x2_list[i])+(thita3*x3_list[i])+(thita4*x4_list[i]))-y_list[j])*x1_list[2]
            result5= ((thita0+(thita1*x1_list[i])+(thita2*x2_list[i])+(thita3*x3_list[i])+(thita4*x4_list[i]))-y_list[j])*x1_list[3]
            j+=1
            sum=sum+result
            sum2=sum2+result2
            sum3=sum2+result2
            sum4=sum2+result2
            sum5=sum2+result2
        thita0=(thita0-((learningRate*sum)/len(x1_list)))
        thita1=(thita1-((learningRate*sum2)/len(x1_list)))
        thita2=(thita0-((learningRate*sum3)/len(x1_list)))
        thita3=(thita1-((learningRate*sum4)/len(x1_list)))
        thita4=(thita1-((learningRate*sum5)/len(x1_list)))            
         
        
        sum=0
        j=0
        for i in range(0,len(x1_list)):
            result= ((thita0+(thita1*x1_list[i])+(thita2*x2_list[i])+(thita3*x3_list[i])+(thita4*x4_list[i]))-y_list[j])
            result=result*result
            j+=1
            sum=sum+result

        cost_function1=sum/(2*len(x1_list))
        cost_value.append(cost_function1)
        iteration_Number.append(x)
        print('cost_function1= ',cost_function1)
        if(cost_function1 < cost_function):
            flag=1
            cost_function=cost_function1  
        
        else:
            flag=2
            break
    if(flag==1):
        print ('Best Thita0= ', oThita0)
        print ('Best Thita1= ', oThita1)
        print ('Best Thita2= ', oThita2)
        print ('Best Thita3= ', oThita3)
        print ('Best Thita4= ', oThita4)
        
    else:
        print ('Best Thita0= ', thita0)
        print ('Best Thita1= ', thita1)
        print ('Best Thita2= ', thita2)
        print ('Best Thita3= ', thita3)
        print ('Best Thita4= ', thita4)
                

   

if (num==2):    
    
    while True:
        x=x+1
        oThita0= thita0
        oThita1= thita1
        oThita2= thita2
        oThita3= thita3
        oThita4= thita4
        
        sum=0
        sum2= 0
        sum3=0
        sum4=0
        sum5=0
        j=0
        result=0
        
        for i in range(0,len(x1_list)):
            result= ((thita0+(thita1*x1_list[i])+(thita2*x2_list[i])+(thita3*x3_list[i])+(thita4*x4_list[i]))-y_list[j])
            result2= ((thita0+(thita1*x1_list[i])+(thita2*x2_list[i])+(thita3*x3_list[i])+(thita4*x4_list[i]))-y_list[j])*x1_list[0]
            result3= ((thita0+(thita1*x1_list[i])+(thita2*x2_list[i])+(thita3*x3_list[i])+(thita4*x4_list[i]))-y_list[j])*x1_list[1]
            result4= ((thita0+(thita1*x1_list[i])+(thita2*x2_list[i])+(thita3*x3_list[i])+(thita4*x4_list[i]))-y_list[j])*x1_list[2]
            result5= ((thita0+(thita1*x1_list[i])+(thita2*x2_list[i])+(thita3*x3_list[i])+(thita4*x4_list[i]))-y_list[j])*x1_list[3]
            j+=1
            sum=sum+result
            sum2=sum2+result2
            sum3=sum2+result2
            sum4=sum2+result2
            sum5=sum2+result2
        thita0=(thita0-((learningRate*sum)/len(x1_list)))
        thita1=(thita1-((learningRate*sum2)/len(x1_list)))
        thita2=(thita0-((learningRate*sum3)/len(x1_list)))
        thita3=(thita1-((learningRate*sum4)/len(x1_list)))
        thita4=(thita1-((learningRate*sum5)/len(x1_list)))            
         
        
        sum=0
        j=0
        for i in range(0,len(x1_list)):
            result= ((thita0+(thita1*x1_list[i])+(thita2*x2_list[i])+(thita3*x3_list[i])+(thita4*x4_list[i]))-y_list[j])
            result=result*result
            j+=1
            sum=sum+result

        cost_function1=sum/(2*len(x1_list))
        cost_value.append(cost_function1)
        iteration_Number.append(x)
        print('cost_function1= ',cost_function1)
        if(cost_function1 < cost_function):
            cost_function=cost_function1  
        
        else:
            break

    print ('Best Thita0= ', oThita0)
    print ('Best Thita1= ', oThita1)
    print ('Best Thita2= ', oThita2)
    print ('Best Thita3= ', oThita3)
    print ('Best Thita4= ', oThita4)
    
#print(thita0+thita1*8)
plt.plot(iteration_Number, cost_value)
print(oThita0+oThita1*852+oThita2*2+oThita3*1+oThita4*36)
 
      
        
  
    
    