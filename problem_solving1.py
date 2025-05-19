import threading
import time

people = [
  {"first_name": "Jhon", "last_name": "Black", "age": 30},
  {"first_name": "Michael", "last_name": "Johnsson", "age": 13},
  {"first_name": "Mery", "last_name": "Hunter", "age": 60},
  {"first_name": "Chris", "last_name": "Williams", "age": 45},
]

class Person:
  people_count = 0
  
  def __init__(self, first_name, last_name, age):
    self.first_name = first_anme
    self.last_name = last_name
    self.age = age #corrected the "==" to "="
    self.id = self.increasecount()

 # This method should not be modified.
 def introduce(self):
   time.sleep(1)
   print(f"Hello, my first name is {self.first_name} and I am {self.age} years old."}

 @classmethod
 def increase_count(cls): # added the cls parameter 
   cls.people_count += 1
   return cls.people_count

def main():
  threads = []
    for p in people:
        x = Person(p["first_name"], p["last_name"], p["age"]) #changed the paramters as per the constructor decleration
        thread = threading.Thread(target=x.introduce)
        threads.append(thread)
    
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    # Print total only after all threads have finished
    print(f"Number of people created: {Person.people_count}") # pinting the number of people after threads is completed.

if __name__ == "__main__":  # main is declared correctly
    main()
