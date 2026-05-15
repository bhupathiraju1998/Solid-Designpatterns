# Topic 1: Single Responsibility Principle (SRP) (Refined & Pure OOP)
# Concept: A class should have one and only one reason to change, meaning it should focus on a single, specific job


from abc import abstractmethod,ABC

# RESPONSIBILITY 1: Only holds and manages Page data
class Page:
    
    # STATIC METHOD: Belongs to the class itself, can be called without creating an object
    @staticmethod
    def is_valid_title(title: str) -> bool: # RETURN TYPE: explicitly returns a boolean
        return len(title) > 0 # Returns True if the title is not empty

    def __init__(self, title: str, content: str):
        self.__title = title # PRIVATE variable: double underscore hides it from the outside
        self.__content = content # PRIVATE variable: protects data from accidental changes

    # PUBLIC METHOD: Allows the outside world to safely read the private variable
    def get_title(self) -> str: 
        return self.__title # Returns the string safely

    # OVERLOADING (Python style): Using a default argument 'limit=None' to allow different ways to call this method
    def get_content(self, limit: int = None) -> str:
        if limit: # Check if the user provided a limit argument
            return self.__content[:limit] # Return only a shortened version of the content
        return self.__content # Otherwise, return the full content


# INTERFACE / ABSTRACT CLASS: A blueprint that forces other classes to follow a structure
class AbstractFormatter(ABC):
    
    @abstractmethod # ABSTRACT METHOD: Forces child classes to implement this exact method
    def format_page(self, page: Page) -> str: 
        pass # Empty body; it just sets the rule that a format_page method MUST exist


# RESPONSIBILITY 2: Only handles formatting (SRP in action!)
class JsonFormatter(AbstractFormatter):
    
    # OVERRIDING: We are replacing the empty abstract method with actual working code
    def format_page(self, page: Page) -> str: 
        t = page.get_title() # Uses public method to get private data
        c = page.get_content() # Uses public method to get private data
        return f'{{"title": "{t}", "content": "{c}"}}' # Creates and returns a JSON formatted string
# Practical Way to Use These Classes: Here is how you actually execute this code in a real application. Because everything is separated, it is highly flexible.
# 1. Use the STATIC METHOD to validate input before doing anything
if Page.is_valid_title("Home"):
    
    # 2. Create the Page object (Data logic)
    my_page = Page("Home", "Welcome to the new platform!")
    
    # 3. Create the Formatter object (Presentation logic)
    formatter = JsonFormatter()
    
    # 4. Use the Formatter on the Page 
    json_output = formatter.format_page(my_page)
    print(json_output) 
    
    # 5. Using the OVERLOADED method to just get the first 7 characters
    short_text = my_page.get_content(limit=7)
    print(short_text) 


# 1)2 things to learn  one is we use privitate variables because for it needs to update it need to undergo teh set of conidtion else suppose
# if a user updates the price like my_page.price = 900 it will get updated for that class so we will write a set_price funcaton and ther 
# we will write the validations

# 2) the use of abstract  now write jsonForamtter
# 3)abstract classes is still a calss we can have normal method and abstract method but we cannot crate a object using abstract and the main motto is to force chindren to implemtn the abstract methods if they use them 
# ----->
# so a class can follow multiple solid and mutiple patterns?

# Yes — absolutely.

# This is one of the biggest realizations in software architecture.

# A single class can:
# follow multiple SOLID principles
# participate in multiple design patterns
# serve multiple architectural roles

# at the SAME time.

# That is completely normal.

# Your Checkout Class Is Already Doing This
# 1. SRP (Single Responsibility Principle)

# Checkout only handles checkout orchestration.

# It does NOT:

# process cards
# call PayPal APIs
# validate bank accounts

# So it has one responsibility.

# 2. DIP (Dependency Inversion Principle)
# def __init__(self, payment_method: PaymentStrategy):

# Checkout depends on:

# PaymentStrategy

# (an abstraction)

# NOT on concrete classes like:

# CreditCardPayment

# That’s DIP.

# 3. OCP (Open/Closed Principle)

# You can add:

# StripePayment
# CryptoPayment
# ApplePayPayment

# without modifying Checkout.

# That’s OCP.

# 4. Strategy Pattern

# Checkout dynamically delegates payment behavior:

# payment_method.process_payment()

# That makes it the Context in Strategy Pattern.