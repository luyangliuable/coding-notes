using System;

namespace UsingOut
{
    class Program
    {
        static void Main(string[] args)
        {
            bool result;
            string returned_value;

            Whisper("random", out returned_value);

            Console.WriteLine(returned_value);
        }    

        static string Whisper(string param1, out bool ret1)
        {
            ret1 = true;
            return param1.ToLower();
        }
    }
}
