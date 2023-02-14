/**
 *   \file polymorphism.cs
 *   \brief Diary inherits from Book class and overrids function Stringify hence polymorphism.
 *
 */
using System;

namespace LearnReferences
{
    class Program
    {
        static void Main(string[] args)
        {
            Book b1 = new Book();
            Book b2 = new Diary();
      
            Console.WriteLine($"{b1.Stringify()}");

            // Diary inherits from Book class and overrids function Stringify hence polymorphism
            Console.WriteLine($"{b2.Stringify()}");
        }
    }
}
