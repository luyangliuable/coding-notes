/**
 *   \file string-can-look-like-values.cs
 *   \brief A Documented file.
 *
 *  They can be explained by the fact that strings are immutable:
 * they cannot be changed after they are created.
 * Anything that appears to modify a string actually returns a new string object.
 *
 */

using System;

namespace StringTheException
{
    class Program
    {
        static void Main(string[] args)
        {
            // They can be explained by the fact that strings are immutable: they cannot be changed after they are created. Anything that appears to modify a string actually returns a new string object.

            string str1 = "immutable";
            string str2 = "immutable";

            Console.WriteLine(str1 == str2);

            Object obj1 = new Object();
            Object obj2 = new Object();

            Console.WriteLine(obj1 == obj2);
        }
    }
}
