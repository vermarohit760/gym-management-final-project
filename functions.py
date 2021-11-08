import re
class super_user:
    member_dict={}
    def __init__(self,name,age,gender,mobile_number,email,bmi,duration,password):
        self.name=name
        self.gender=gender
        self.age=age
        self.email=email
        self.mobile_number=mobile_number
        self.bmi=bmi
        self.duration=duration
        self.password=password
        super_user.member_dict[mobile_number]={}
        super_user.member_dict[mobile_number]['Name']=name
        super_user.member_dict[mobile_number]['Gender']=gender
        super_user.member_dict[mobile_number]['Age']=age
        super_user.member_dict[mobile_number]['Email']=email
        super_user.member_dict[mobile_number]['Mobile number']=mobile_number
        super_user.member_dict[mobile_number]['BMI']=bmi
        super_user.member_dict[mobile_number]['Duration']=duration
        super_user.member_dict[mobile_number]['Password']=password
        
class workout_regimen:
    regimen={}
    range_list=[]
    def __init__(self,bmi_lower,bmi_upper,mon,tue,wed,thur,fri,sat,sun):
        self.mon=mon
        self.tue=tue
        self.wed=wed
        self.thur=thur
        self.fri=fri
        self.sat=sat
        self.sun=sun
        workout_regimen.range_list.append(bmi_lower)
        workout_regimen.range_list.append(bmi_upper)
        workout_regimen.regimen[(bmi_lower,bmi_upper)]={}
        workout_regimen.regimen[(bmi_lower,bmi_upper)]['monday']=mon
        workout_regimen.regimen[(bmi_lower,bmi_upper)]['tuesday']=tue
        workout_regimen.regimen[(bmi_lower,bmi_upper)]['wednesday']=wed
        workout_regimen.regimen[(bmi_lower,bmi_upper)]['thursday']=thur
        workout_regimen.regimen[(bmi_lower,bmi_upper)]['friday']=fri
        workout_regimen.regimen[(bmi_lower,bmi_upper)]['saturday']=sat
        workout_regimen.regimen[(bmi_lower,bmi_upper)]['sunday']=sun
def create_member():
    print('Enter the name:- ')
    name=input()
    print('Enter the Age:- ')
    while True:
        try:
            age=int(input())
            break
        except:
            print('Please enter the correct age :')
    print('Enter the Gender (M,F,T):- ')
    while True:
        gender=input()
        gender_list=['M','F','T']
        if gender in gender_list:
            break
        else:
            print('Please enter the correct Gender :')
    print('Enter the Mobile Number:- ')
    while True:
        try:
            mobile_number=int(input())
            break
        except:
            print('Please enter the correct Mobile Number :')
    print('Enter the email:- ')
    while True:
        email=input()
        pattern = '^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$'
        if(re.search(pattern, email)):
            break
        else:
            print('Enter the Valid Email id ')
    print('Enter the BMI 0 to ',max(workout_regimen.range_list),':-')
    while True:
        try:
            bmi=float(input())
            assert bmi>0 and bmi<=max(workout_regimen.range_list)
            break
        except:
            print('Please enter the correct Body Mass Index (BMI) :')
    print('Enter Membership duration in months (1,3,6,12) :- ')
    while True:
        try:
            duration=int(input())
            duration_list=[1,3,6,12]
            if duration in duration_list:
                break
        except:
            print('Please enter the correct Membership Duration :')
    print('Create password for the member:- ')
    password=input()
    print('New Member Registered')
    
    member=super_user(name,age,gender,mobile_number,email,bmi,duration,password)
    
def view_member():
    print('Enter the Member Mobile Number to view details of member: -')
    while True:
        try:
            mobile_number=int(input())
            break
        except:
            print('Please enter the correct Mobile Number :')
    if mobile_number in super_user.member_dict.keys():
        print('Name                           : ',super_user.member_dict[mobile_number]['Name'])
        print('Age                            : ',super_user.member_dict[mobile_number]['Age'])
        print('Gender                         : ',super_user.member_dict[mobile_number]['Gender'])
        print('Mobile Number                  : ',super_user.member_dict[mobile_number]['Mobile number'])
        print('Email                          : ',super_user.member_dict[mobile_number]['Email'])
        print('Body Mass Index(BMI)           : ',super_user.member_dict[mobile_number]['BMI'])
        print('Membership duration in Months  : ',super_user.member_dict[mobile_number]['Duration'])
        print('Password                       : ',super_user.member_dict[mobile_number]['Password'])
    else:
        print('Entered Mobile Number is not registered--')
        
def delete_member():
    print('Enter the Member Mobile Number to delete details of member: -')
    while True:
        try:
            mobile_number=int(input())
            break
        except:
            print('Please enter the correct Mobile Number :')
            
    if mobile_number in super_user.member_dict.keys():
        super_user.member_dict.pop(mobile_number)
        print('Member deleted successfully')
    else:
        print('Entered Mobile Number is not registered--')
        
def update_member():
    print('Enter the Member Mobile Number to update details of member: -')
    while True:
        try:
            mobile_number=int(input())
            break
        except:
            print('Please enter the correct Mobile Number :')
    if mobile_number in super_user.member_dict.keys():
        print('Enter Membership duration to extend in months (1,3,6,12) , 0 to revoke membership :- ')
        while True:
            try:
                duration=int(input())
                duration_list=[0,1,3,6,12]
                if duration in duration_list:
                    break
            except:
                print('Please enter the correct Membership Duration :')
        super_user.member_dict[mobile_number]['Duration']=super_user.member_dict[mobile_number]['Duration']+duration
        while True:
            if duration==0:
                super_user.member_dict.pop(mobile_number)
                break
            else:
                print('Enter the name:- ')
                name=input()
                super_user.member_dict[mobile_number]['Name']=name
                print('Enter the Age:- ')
                while True:
                    try:
                        age=int(input())
                        break
                    except:
                        print('Please enter the correct age :')
                super_user.member_dict[mobile_number]['Age']=age
                print('Enter the Gender (M,F,T):- ')
                while True:
                    gender=input()
                    gender_list=['M','F','T']
                    if gender in gender_list:
                        break
                    else:
                        print('Please enter the correct Gender :')
                super_user.member_dict[mobile_number]['Gender']=gender
                print('Enter the email:- ')
                while True:
                    email=input()
                    pattern = '^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$'
                    if(re.search(pattern, email)):
                        break
                    else:
                        print('Enter the Valid Email id ')
                super_user.member_dict[mobile_number]['Email']=email
                print('Enter the BMI 0 to ',max(workout_regimen.range_list),':-')
                while True:
                    try:
                        bmi=float(input())
                        assert bmi>0 and bmi<=max(workout_regimen.range_list)
                        break
                    except:
                        print('Please enter the correct Body Mass Index (BMI) :')
                super_user.member_dict[mobile_number]['BMI']=bmi
                print('Create password for the member:- ')
                password=input()
                super_user.member_dict[mobile_number]['Password']=password
                print('Member details updated successfully')
                break
    else:
        print('Entered Mobile Number Is not Registered')
        
def work_regimen():
        workout=workout_regimen(0,18.5,'Chest','Biceps','Rest','Back','Triceps','Rest','Rest')
        workout=workout_regimen(18.5,25,'Chest','Biceps','Cardio/Abs','Back','Triceps','Legs','Rest')
        workout=workout_regimen(25,30,'Chest','Biceps','Cardio/Abs','Back','Triceps','Legs','Cardio')
        workout=workout_regimen(30,35,'Chest','Biceps','Cardio','Back','Triceps','Cardio','Cardio')
        
def create_regimen():
    print('Enter the lower limit of BMI range:-')
    while True:
        try:
            bmi_lower=int(input())
            break
        except:
            print('Please enter the correct Body Mass Index (BMI) lower limit :') 
    print('Enter the upper limit of BMI range:-')
    while True:
        try:
            bmi_upper=int(input())
            break
        except:
            print('Please enter the correct Body Mass Index (BMI) upper limit :')
    if bmi_lower>35:
        print('Enter workout for monday :')
        mon=input()
        print('Enter workout for tuesday :')
        tue=input()
        print('Enter workout for wednesday :')
        wed=input()
        print('Enter workout for thursday :')
        thur=input()
        print('Enter workout for friday :')
        fri=input()
        print('Enter workout for saturday :')
        sat=input()
        print('Enter workout for sunday :')
        sun=input()
        workout=workout_regimen(bmi_lower,bmi_upper,mon,tue,wed,thur,fri,sat,sun)
        print('Workout Regimen created successfully')
    else:
        print('The work regimen is already created')
    
def view_regimen():
    print('Enter the Body Mass Index (BMI): ')
    while True:
          try:
              Bmi=float(input())
              break
          except:
              print('Please Enter correct BMI')
    if Bmi<=max(workout_regimen.range_list) and Bmi>=min(workout_regimen.range_list):
        for k in workout_regimen.regimen.keys():
              if Bmi>k[0] and Bmi<=k[1]:
                  print('Monday    : ',workout_regimen.regimen[k]['monday'])
                  print('Tuesday   : ',workout_regimen.regimen[k]['tuesday'])
                  print('Wednesday : ',workout_regimen.regimen[k]['wednesday'])
                  print('Thursday  : ',workout_regimen.regimen[k]['thursday'])
                  print('Friday    : ',workout_regimen.regimen[k]['friday'])
                  print('Saturday  : ',workout_regimen.regimen[k]['saturday'])
                  print('Sunday    : ',workout_regimen.regimen[k]['sunday'])
    else:
          print('Workout regime for given BMI is yet to be created')
def delete_regimen():
    print('Choose workout regimen to be deleted',list(workout_regimen.regimen.keys()))
    print('Lower limit of range :')
    while True:
        try:
            lower=float(input())
            break
        except:
            print('Enter input in numbers')
    print('Upper limit of range :')
    while True:
        try:
            upper=float(input())
            break
        except:
            print('Enter input in numbers')
    if lower in workout_regimen.range_list and upper in workout_regimen.range_list:
        for i in list(workout_regimen.regimen.keys()):
            if lower==i[0] and upper==i[1]:
                workout_regimen.regimen.pop(i)
                workout_regimen.range_list.remove(lower)
                workout_regimen.range_list.remove(upper)
                print('Workout Regimen deleted successfully')
    else:
        print('This Range is NOT DEFINED for this work regimen')
          
def update_regimen():
    print('Choose workout regimen to be updated',list(workout_regimen.regimen.keys()))
    print('Lower limit of range :')
    while True:
        try:
            lower=float(input())
            break
        except:
            print('Enter input in numbers')
    print('Upper limit of range')
    while True:
        try:
            upper=float(input())
            break
        except:
            print('Enter input in numbers')
    if lower in workout_regimen.range_list and upper in workout_regimen.range_list:
        print('Enter workout for monday :')
        mon=input()
        workout_regimen.regimen[(lower,upper)]['monday']=mon
        print('Enter workout for tuesday :')
        tue=input()
        workout_regimen.regimen[(lower,upper)]['tuesday']=tue
        print('Enter workout for wednesday :')
        wed=input()
        workout_regimen.regimen[(lower,upper)]['wednesday']=wed
        print('Enter workout for thursday :')
        thur=input()
        workout_regimen.regimen[(lower,upper)]['thursday']=thur
        print('Enter workout for friday :')
        fri=input()
        workout_regimen.regimen[(lower,upper)]['friday']=fri
        print('Enter workout for saturday :')
        sat=input()
        workout_regimen.regimen[(lower,upper)]['saturday']=sat
        print('Enter workout for sunday :')
        sun=input()
        workout_regimen.regimen[(lower,upper)]['sunday']=sun
          
        workout=workout_regimen(lower,upper,mon,tue,wed,thur,fri,sat,sun)
        print('workout regimen updated successfully')
    
    else:
        print('This Range is NOT DEFINED for this workout regimen')
          
def view_my_regimen(mobile_number):
    Bm_index=super_user.member_dict[mobile_number]['BMI']
    for k in workout_regimen.regimen.keys():
        if Bm_index>k[0] and Bm_index<=k[1]:
            print('Monday    : ',workout_regimen.regimen[k]['monday'])
            print('Tuesday   : ',workout_regimen.regimen[k]['tuesday'])
            print('Wednesday : ',workout_regimen.regimen[k]['wednesday'])
            print('Thursday  : ',workout_regimen.regimen[k]['thursday'])
            print('Friday    : ',workout_regimen.regimen[k]['friday'])
            print('Saturday  : ',workout_regimen.regimen[k]['saturday'])
            print('Sunday    : ',workout_regimen.regimen[k]['sunday'])
          
def view_my_profile(mobile_number):
    print('Name                           : ',super_user.member_dict[mobile_number]['Name'])
    print('Age                            : ',super_user.member_dict[mobile_number]['Age'])
    print('Gender                         : ',super_user.member_dict[mobile_number]['Gender'])
    print('Mobile Number                  : ',super_user.member_dict[mobile_number]['Mobile number'])
    print('Email                          : ',super_user.member_dict[mobile_number]['Email'])
    print('Body Mass Index(BMI)           : ',super_user.member_dict[mobile_number]['BMI'])
    print('Membership duration in Months  : ',super_user.member_dict[mobile_number]['Duration'])
    print('Password                       : ',super_user.member_dict[mobile_number]['Password'])
          
def update_profile(mobile_number):
    print('Enter the name:- ')
    name=input()
    super_user.member_dict[mobile_number]['Name']=name
    print('Enter the Age:- ')
    while True:
        try:
            age=int(input())
            break
        except:
            print('Please enter the correct age :')
    super_user.member_dict[mobile_number]['Age']=age
    print('Enter the Gender (M,F,T):- ')
    while True:
        gender=input()
        gender_list=['M','F','T']
        if gender in gender_list:
            break
        else:
            print('Please enter the correct Gender :')
    super_user.member_dict[mobile_number]['Gender']=gender
    print('Enter the email:- ')
    while True:
        email=input()
        pattern = '^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$'
        if(re.search(pattern, email)):
            break
        else:
            print('Enter the Valid Email id ')
    super_user.member_dict[mobile_number]['Email']=email
    print('Enter the BMI from 0 to ',max(workout_regimen.range_list),':-')
    while True:
        try:
            bmi=float(input())
            assert bmi>0 and bmi<=max(workout_regimen.range_list)
            break
        except:
            print('Please enter the correct Body Mass Index (BMI) :')
    super_user.member_dict[mobile_number]['BMI']=bmi
    print('Create password for the member:- ')
    password=input()
    super_user.member_dict[mobile_number]['Password']=password
    print('Details updated successfully')
          
def SUPER_USER():
    print('HELLOOOOOO Super User.... Please select one option from given list:---')
    while True:
        try:
            print('1. Create Member')
            print('2. View Member')
            print('3. Delete Member')
            print('4. Update Member')
            print('5. Create Regimen')
            print('6. View Regimen')
            print('7. Delete Regimen')
            print('8. Update Regimen')
            print('9. Logout')
            n=int(input())
            if n==1:
                create_member()
            elif n==2:
                view_member()
            elif n==3:
                delete_member()
            elif n==4:
                update_member()
            elif n==5:
                create_regimen()
            elif n==6:
                view_regimen()
            elif n==7:
                delete_regimen()
            elif n==8:
                update_regimen()
            elif n==9:
                print('Logging Out')
                break
            assert n>=1 and n<=9
        except:
            print('Something went wrong, please select correct option')
def MEMBER():
    print('Please enter LOGIN credential')
    print('Enter your mobile number')
    while True:
        try:
            mobile_number=int(input())
            break
        except:
            print('Enter correct mobile number')
    if mobile_number in super_user.member_dict.keys():
        print('Enter your Password:')
        user_password=input()
        if super_user.member_dict[mobile_number]['Password']==user_password:
            print('HELLOOOOOO Member.... Please select one option from given list:---')
            while True:
                try:
                    print('1. View My Regimen')
                    print('2. View My Profile')
                    print('3. Update Profile')
                    print('4. Logout')
                    m=int(input())
                    if m==1:
                        view_my_regimen(mobile_number)
                    elif m==2:
                        view_my_profile(mobile_number)
                    elif m==3:
                        update_profile(mobile_number)
                    elif m==4:
                        print('Logging OUT')
                        break
                    assert m>=1 and m<=4
                except:
                    print('Something went wrong, please select correct option')
                    
        else:     
            print('Login Credential did not match')
    else:
        print('This mobile number is not registered')
    
def option():
    while True:
        try:
            print('Select User Type')
            print('1. Super User')
            print('2. Member')
            print('3. Exit')
            user= int(input())
            if user==1:
                SUPER_USER()
            elif user==2:
                MEMBER()
            elif user==3:
                print('Happy Gyming.... VISIT SOON')
                break
            assert user>=1 and user<=3
        except:
            print('Something went wrong . Please select CORRECT option')
    
          
