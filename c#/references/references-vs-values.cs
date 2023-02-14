using System;

namespace LearnReferences
{
    class Program
    {
        static void Main(string[] args)
        {
            Book bookLocation = new Book();
            Book sameBookLocation = bookLocation;
            bool falseValue = false;
            bool anotherFalseValue = falseValue;
            falseValue = true;
            Console.WriteLine($"{falseValue}, {anotherFalseValue}");
        }
    }
}
