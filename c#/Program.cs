// See https://aka.ms/new-console-template for more information

using System;

namespace dotnet_sample
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            Console.WriteLine("Goodbye World!");

            string fooFs = string.Format("Check Check, {0} {1}, {0} {1:0.0}", 1, 2);
            Console.WriteLine(fooFs);

            List<int> intList = new List<int>() {1, 1, 1};
            intList[0] = 12;
            intList.Add(121);

            for (int i = 0; i < intList.Capacity; i++) {
              Console.WriteLine(intList[i]);
            }

            Console.WriteLine('\n');
            foreach (int w in intList) {
              Console.WriteLine(w);
            }

            int tryInt;
            if (int.TryParse("12318239", out tryInt)) // Function is boolean
                Console.WriteLine(tryInt); 

            int.Parse("12318239");
            
            // int numberString = tryInt.ToString();
            Another.sayHi();

            Another.IterateAndPrint(intList);


            var another = new Another();
            another.checkPhoneBook("Luyang");

        }
    }
}

class Another {

      private Dictionary<string, string> phonebook = new Dictionary<string, string>() {
          {
          "Sarah", "212 555 5555"
          }, {
          "Luyang", "0481820218"
          } // Add some entries to the phone book
      };

      public Another() {
        Console.WriteLine("Another");
      }

      public static void sayHi() {
        Console.WriteLine("Hi");
      }

      public static void IterateAndPrint<T>(T toPrint) where T: IEnumerable<int>
      {
          // We can iterate, since T is a IEnumerable
          foreach (var item in toPrint)
              // Item is an int
              Console.WriteLine(item.ToString());
      }      

      public void checkPhoneBook(string name) {
        string number;
        if (this.phonebook.TryGetValue(name, out number)) 
        {
            // Use percentage
            Console.WriteLine(number);
        }
      }
}
