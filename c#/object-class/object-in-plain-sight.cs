using System;

/**
*   \file Diary.cs
*   \brief A Documented file.
*
*/
namespace TheObjectClass
{
    class Diary : Book, IFlippable
    {
        public int CurrentPage
        { get; set; }

        public Diary(int page = 0) : base()
        {
            CurrentPage = page;
        }
    
        public Diary(int page, string author, string title) : base(author, title)
        {
            CurrentPage = page;
        }

        public void Flip()
        {
            CurrentPage++;
        }

        public override string ToString() {
            return "Surprise!";
        }

        public string SpillSecret()
        {
            return "OMG kerry loves kris <3";
        }

        public override string Stringify() 
        {
            return "This is a Diary object!";
        }
    }
}


/**
 *   \file Program.cs
 *   \brief A Documented file.
 *
 */


namespace TheObjectClass
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine($"{new Diary()}");
        }
    }
}
