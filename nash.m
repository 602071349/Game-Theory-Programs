%If you want to run the programm,you need to download the tensor package
%from http://www.sandia.gov/~tgkolda/TensorToolbox/index-2.6.html
num1 = 2;
num2 = 2;
num3 = 2;

T1 = tensor(randi([-10,10],num1,num2,num3));
T2 = tensor(randi([-10,10],num1,num2,num3));
T3 = tensor(randi([-10,10],num1,num2,num3));

minimum = 100;

for a = 1:1000
    
    a;
    while 1
        s1 = randi([0,20],num1,1);
        if sum(s1) ~= 0
            s1 = s1 / sum(s1);
            break
        end
    end
    
    while 1
        s2 = randi([0,20],num2,1);
        if sum(s2) ~= 0
            s2 = s2 / sum(s2);
            break
        end
    end
    
    while 1
        s3 = randi([0,20],num3,1);
        if sum(s3) ~= 0
            s3 = s3 / sum(s3);
            break
        end
    end
    
    T1a = T1;
    T2a = permute(T2,[2 1 3]);
    T3a = permute(T3,[3 1 2]);
    
    T1a = ttv(T1a, s3, 3);
    T1a = ttv(T1a, s2, 2);
    
    T1a = double(T1a);
    max1 = max(T1a);
    RT1a = dot(transpose(s1), T1a);
    
    T2a = ttv(T2a, s3, 3);
    T2a = ttv(T2a, s1, 2);
    
    T2a = double(T2a);
    max2 = max(T2a);
    RT2a = dot(transpose(s2), T2a);
    
    T3a = ttv(T3a, s2, 3);
    T3a = ttv(T3a, s1, 2);
    
    T3a = double(T3a);
    max3 = max(T3a);
    RT3a = dot(transpose(s3), T3a);
    
    difference = sqrt((max1 - RT1a)^2 + (max2 - RT2a)^2 + (max3-RT3a)^2);
    
    if minimum > difference
        minimum = difference;
        strategy = [s1;s2;s3];
    
    if minimum == 0
        break
    end
    
    end
end

strategy;
minimum;


