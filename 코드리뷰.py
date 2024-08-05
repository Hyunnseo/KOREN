#알고리즘을 위한 각 운전상황 정의

def left_detect(driver_data): #좌회전 정의, 파라미터는 운전 속성이 담긴 데이터프레임 
    left_ind=[] #좌회전 시작과 끝나는 인덱스를 담기 위한 리스트 생성 
    flag = 0 #좌회전 여부를 나타내는 변수 생성 
    uflag = 0 #좌회전 중 유턴 여부 나타내는 변수 생성

    for i in range(driver_data.shape[0]): 
        if (driver_data[i,4] > 70) & (driver_data[i,4] < 200): #driver_data[i,4](조향각) 이 70~200 사이면   
            flag = 1 #좌회전임 
        elif driver_data[i,4] > 300: #조향각 300초과는 
            flag =0
            uflag=1  #유턴임
        
        if (flag == 1) & (driver_data[i,4]<10) & (uflag==0): #좌회전 끝났을 때 
            flag =0
            left_ind.append(i) #해당 행의 인덱스를 리스트에 추가 
        if (uflag == 1) & (driver_data[i,4]<10): #유턴 끝났을 때 
            uflag=0 
            flag =0 

    return left_ind 

def right_detect(driver_data): #우회전 정의, 파라미터는 운전 속성이 담긴 데이터프레임 
    right_ind=[] #우회전 시작과 끝나는 인덱스를 담기 위한 리스트 생성 
    flag =0 #우회전 여부를 나타내는 변수 생성 
    uflag = 0 #우회전 중 유턴 여부 나타내는 변수 생성 ??우회전으로 유턴하는 상황이 없길바란다! 

    for i in range(driver_data.shape[0]): 
        if (driver_data[i,4] < -50) & (driver_data[i,4] > -200): #driver_data[i,4](조향각) 이 -50~-200 사이면   
            flag = 1 #우회전임 
        elif driver_data[i,4] < -360: #조향각 -360보다 더돌렸을 때  
            flag =0
            uflag=1  #유턴임
        
        if (flag == 1) & (driver_data[i,4] > -10) & (uflag==0): #우회전 끝났을 때 
            flag =0
            right_ind.append(i) #해당 행의 인덱스를 리스트에 추가 
        if (uflag == 1) & (driver_data[i,4]<10): #유턴 끝났을 때 
            uflag=0 
            flag =0 

    return right_ind 

def uturn_detect(driver_data): #유턴 정의, 파라미터는 운전 속성이 담긴 데이터프레임 
    uturn_ind=[] #유턴 시작과 끝나는 인덱스를 담기 위한 리스트 생성 
    flag =0 #유턴 여부를 나타내는 변수 생성 
    uflag = 0 #유턴 여부 나타내는 변수 생성 --필요없을 듯

    for i in range(driver_data.shape[0]): 
        if (driver_data[i,4] > 300):  #driver_data[i,4](조향각) 이 300이상 - 좌로 이빠이 
            flag = 1 #유턴 

        if (flag == 1) & (driver_data[i,4]) < 10 : #우회전 끝났을 때 
            flag =0
            uturn_ind.append(i) #해당 행의 인덱스를 리스트에 추가 

    return right_ind 
        

def start_detect(driver_data): #출발 정의, 파라미터는 운전 속성이 담긴 데이터프레임 
    start_ind=[] #출발상황 인덱스 
    flag =0 #출발여부 변수 생성  
    cnt = 0 #정지시간 체크하기 위함   

    for i in range(driver_data.shape[0]): 
        if (driver_data[i,4] < 15) & (driver_data[i,4] > -15 ): #driver_data[i,4](조향각) 이 -15~15 사이(직진)이면    
            if driver_data[i,2] == 0: # 차속 0
                cnt=cnt+1 #차속 0인 시간 
            if (cnt>=3) & (i+12 < driver_data.shape[0]): #cnt 3번동안 정지해있었고, i+12행 보다 행개수가 많을때?? 12가 왜나왔지
                if driver_data[i,2]>0:
                    start_ind.append(i+12) #출발 인덱스를 i+12로 추가 
                    cnt=0

    return start_ind 
        
def stop_detect(driver_data): #정지 정의, 파라미터는 운전 속성이 담긴 데이터프레임 
    stop_ind=[] #정지상황 인덱스 
    flag =0 #주행여부 변수 생성- 0이 정지 , 1이 주행   
    cnt = 0 #정지시간 체크 

    for i in range(driver_data.shape[0]): 
        if (driver_data[i,4] < 15) & (driver_data[i,4] > -15 ): #driver_data[i,4](조향각) 이 -15~15 사이(직진)이면    
            if driver_data[i,2] > 5: # 차속 5보다 클 때 
                flag = 1 #주행 중
            if (flag == 1) & (driver_data[i,2] == 0): #주행 중이었는데 차속이 0이 된 경우 
                cnt=cnt+1

            if cnt >= 2:  #cnt 2번동안 이상일때 
                stop_ind.append(i) #정지임
                cnt = 0
                flag = 0 #정지 
            
        else : 
            flag = 0 #
    return stop_ind 

def straight_detect(driver_data): #직진 정의, 파라미터는 운전 속성이 담긴 데이터프레임 
    straight_ind=[] #직진상황 인덱스 
    flag =0 #주행여부 변수 생성- 0이 정지 , 1이 주행   
    cnt = 0 #주행시간 체크 
    count = 0 
    for i in range(driver_data.shape[0]): 
        if (driver_data[i,4] < 15) & (driver_data[i,4] > -15 ): #driver_data[i,4](조향각) 이 -15~15 사이(직진)이면    
            if driver_data[i,2] > 5: # 차속 5보다 클 때 
                flag = 1 #주행 중
            else :  #차속 5이하로 떨어지면 
                count=count+1
                if count>2:
                    flag=0
                    count=0
                    cnt=0 
            if (flag == 1): #주행 중 
                cnt = cnt + 1
            
            if cnt >= 15:  #cnt 15번동안 지속
                straight_ind.append(i) #직진임
                cnt = 0
                flag = 0  
            
        else : 
            flag = 0 #
    return straight_ind 