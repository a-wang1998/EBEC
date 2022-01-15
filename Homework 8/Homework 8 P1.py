################
# Author: Andrew Wang
# Date: 11/03/2019
# This programs that create a dictionary containing course numbers and room numbers of the rooms there the courses meet. 
#################
#Main function
def main():
    #Room number for each course
    room_num = {'CS101':'3004','CS102':'4501','CS103':'6755','NT110':'1244','CM241':'1411'}
    #Instructor for each course
    instructor = {'CS101':'Haynes','CS102':'Alvarado','CS103':'Rich','NT110':'Burke','CM241':'Lee'}
    #Meeting time for each course
    meet_time = {'CS101':'8:00 a.m.','CS102':'9:00 a.m.','CS103':'10:00 a.m.','NT110':'11:00 a.m.','CM241':'1:00 a.m.'}

    #Allows user to input course number
    course_num = str(input('Enter a course number: '))

    #If statement to print out the details of course
    if course_num in room_num:
        print('The details for course ' +course_num+ ' are:')
        print('Room: ' +room_num[course_num])
        print('Instructor: '+instructor[course_num])
        print('Time: '+meet_time[course_num])
        
    else:
        print(course_num+ ' is an invalid course number.')

#Calls main function
main()
