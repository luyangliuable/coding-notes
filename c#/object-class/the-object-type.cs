/**
 *   \file the-object-type.cs
 *   \brief Object type.
 *
 */

using System;

namespace TheObjectClass
{
    class Program
    {
        static void Main(string[] args)
        {
            Book bk = new Book();
            Object ok = bk;

            Diary dy = new Diary(38);
            Object oy = dy;
      
            int i = 9;
            Object o = i;

            i = 100;
            // i and o both doesn't still refer to the same number.
            Console.WriteLine($"{i}, {o}");


        }
    }
}
