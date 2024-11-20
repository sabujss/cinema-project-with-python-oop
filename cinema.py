class Star_Cinema:
    __hall_list=[]
    @classmethod
    def entry_hall(cls,hall):
        cls.__hall_list.append(hall)
        

class Hall(Star_Cinema):
    def __init__(self,rows,cols,_hall_no):
        self.seats={}
        self.show_list=[]
        self.rows=rows
        self.cols=cols
        self._hall_no=_hall_no
        Star_Cinema.entry_hall(self)
    
    def entry_show(self,_id,movie_name,time):
        self._id=_id
        self.movie_name=movie_name
        self.time=time
        show=(self._id,self.movie_name,self.time)
        self.show_list.append(show)

        seat=[]
        for i in range(self.rows):
            row=[0]*self.cols
            seat.append(row)
        self.seats[_id]=seat
    
    def book_seat(self,_id,seat_no):
        if _id not in self.seats:
            print(f'the movie with id:{_id} not exist')
            print("------------------------------")
            return
        seat=self.seats[_id]
        for row,col in seat_no:
            if row<0 or row>=self.rows or col<0 or col>=self.cols:
                print("invalid seat position")
                print("------------------------------")
                continue

            if seat[row][col]==1:
                print(f'the seat ({row+1},{col+1}) is already booked!!')
                print("------------------------------")
            else:
                seat[row][col]=1
                print(f'the seat ({row+1},{col+1}) successfully booked!!')
                print("------------------------------")
    
    def view_show_list(self):
        if not self.show_list:
            print("No shows running now")
            print("------------------------------")
            return

        print("shows running")
        print("------------------------------")
        for _id,movie_name,time in self.show_list:
            print(f'ID: {_id}, Movie: {movie_name}, Time: {time}')
        print("------------------------------") 

    def view_available_seats(self,_id):
        if _id not in self.seats:
            print(f'ID {_id} not exist!!')
            return
        print(f"available seat for ID {_id}")
        seat=self.seats[_id]
        for x in seat:
            print(" ".join(str(seat) for seat in x)) 
        print("------------------------------")       


cineplex=Hall(10,10,"Hall_1")
cineplex.entry_show("100","saalar","09:00am")
cineplex.entry_show("101","dangal","12:00pm")
cineplex.entry_show("102","jawaan","02:00pm")

run=True
while run:
    print("1. View all show today")
    print("2. View available seats")
    print("3. Book ticket")
    print("4. Exit")
    option=int(input("Enter Option: "))
    if option==1:
        cineplex.view_show_list()
    elif option==2:
        _id=input("Enter id: ")
        cineplex.view_available_seats(_id)
    elif option==3:
        _id=input("Enter id: ")
        row=int(input("Enter Row: "))
        col=int(input("Enter Col: "))
        seat_no=[(row-1,col-1)]
        cineplex.book_seat(_id,seat_no)
    else:
        break
    


        