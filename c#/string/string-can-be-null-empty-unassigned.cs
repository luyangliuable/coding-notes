/**
 *   \file .cs
 *   \brief A Documented file.
 *
 * unassigned means that the programmer did not give the variable any input
 * null means that the programmer intentionally made the variable refer to no object
 * an empty string signifies a piece of text with zero characters. This is often used to represent a blank text field. It can be represented by "" or String.Empty
 */ 


using System;

namespace StringTheException
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter some input please: ");
            string input = Console.ReadLine();
      
            if (String.IsNullOrEmpty(input))
            {
                Console.WriteLine("You didn't enter anything!");
            }
            else
            {
                Console.WriteLine("Thank you for your submission!");
            }
     
        }
    }
}
