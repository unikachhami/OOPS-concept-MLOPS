class coverbook:

    __id = 0
    def __init__(self):
         self.user_id = coverbook.__id
         coverbook.__id += 1
         self.user_name = 'unik'
         self.password = ''
         self.loggedin = False
        # self.menu()

    def get_name():
        return coverbook.user_id
    
    def set_name(value):
        coverbook.user_id= value

    def menu(self):
        user_input = input('''Welcome how eould you like to proceed:
                           1.Press 1 to signup
                           2.Press 2 to signin
                           3.Press 3 to write a post
                           4.Press 4 to meaasge a friend
                           5.Press any other key to exit
                           ''')
        
        if user_input =='1':
            self.signup()
            self.menu()
        elif user_input =='2':
            if self.user_name =='' and self.password=='':
                print('sign in first for further processing:')
                self.menu()
            self.signin()
        elif user_input=='3':
            self.post()
            
        elif user_input=='4':
            self.message()
        else:
            pass

    
    def signup(self):
       
        email = input('Enter your email:')
        password = input('Enter your password:')
        self.user_name = email
        self.password = password
        print('You successfully signed-up:')


    def signin(self):
        if self.user_name =='' and self.password =='':
            print('You have not signed up please kindly sign in:')

        else:
            user = input('Enter user name:')
            pwd = input('Enter your password:')

            if user == self.user_name and pwd == self.password:
                print('You signed up successfully:')
                self.loggedin ==True

            else:
                print('Please enter correct information:')
                self.menu()

    def post(self):
        if self.loggedin ==True:
           print('You can write a post:/n')
           user_post = input('Enter any information to post:')
        else:
            print('Please signup first to post any information:/n')
            self.menu()

    def message(self):
        print('Enter a message for your friend:')
obj = coverbook()

