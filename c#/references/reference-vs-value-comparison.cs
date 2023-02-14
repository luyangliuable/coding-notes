using System;

namespace LearnReferences
{
    class Program
    {
        static void Main(string[] args)
        {
            Book b1 = new Book();
            Book b2 = b1;
            Console.WriteLine(b1 == b2);
        }
    }
}
