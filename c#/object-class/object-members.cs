using System;

namespace TheObjectClass
{
    class Program
    {
        static void Main(string[] args)
        {
            Book b = new Book();      
            Diary d = new Diary(38);
            Random r = new Random();
            int i = 9;

            Object[] arr = new Object[] {b, d, r, i};

            foreach (Object item in arr) {
                Console.WriteLine(item.GetType());
            }
        }
    }
}
