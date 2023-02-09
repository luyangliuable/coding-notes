/**
 *   \file getting-input.cs
 *   \brief The file gets an input from the user.
 *
 *  Asked the user about the age and repeat a line,
 *
 */

using System;

namespace GettingInput
{
    class Program
    {
        static void Main()
        {
            // Asked the user about the age and repeat a line,
            Console.WriteLine("How old are you?");
            string input = Console.ReadLine();
            Console.WriteLine($"You are {input} years old!");
        }
    }
}
