using System;

namespace LearnReferences
{
    class Program
    {
        static void Main(string[] args)
        {
            Book book = null;

            Console.WriteLine($"{book}");

            Console.WriteLine(book == null);
        }
    }
}
