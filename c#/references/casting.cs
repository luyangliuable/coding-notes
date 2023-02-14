using System;

namespace LearnReferences
{
    class Program
    {
        static void Main(string[] args)
        {
            Dissertation diss = new Dissertation();
            Diary dy = new Diary();
      
            // This is upcasting and it can be done explicitly
            Book bdiss = diss;
            Book bdy = dy;

            // This is downcasting since Diary inherits from Book
            Diary a = (Diary) bdy;

        }
    }
}
