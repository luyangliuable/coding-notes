using System;

namespace LearnReferences
{
    class Program
    {
        static void Main(string[] args)
        {
            Diary dy1 = new Diary(5);
            Diary dy2 = dy1;
            dy2.Flip();
            Console.WriteLine($"{dy1.CurrentPage}, {dy2.CurrentPage}");
        }
    }
}
