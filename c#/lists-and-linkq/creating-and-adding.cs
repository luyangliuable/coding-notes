/**
 *   \file creating-and-adding.cs
 *
 * You create a list using the new keyword, like you would create any other class. You specify the type of element inside angle brackets: < >. In this example, the list is named citiesList and it holds instances of the type string. *
 */

using System;
using System.Collections.Generic;

namespace LearnLists
{
    class Program
    {
        static void Main()
        {
            List<double> marathons = new List<double>();

            marathons.Add(144.07);
            marathons.Add(143.12);

            Console.WriteLine(marathons[1]);
        }
    }
}
