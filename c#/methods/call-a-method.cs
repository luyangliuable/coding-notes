using System;

namespace CallAMethod
{
    class Program
    {
        static void Main(string[] args)
        {
            string msg = "Yabba dabba doo!";

            // Call method Math.min on any argument
            Math.Min(1, 2);

            string msg = "Phasellus at dui in ligula mollis ultricies.  ";
            Console.WriteLine(msg);

            // Get the first leteer of the msg string .
            Console.WriteLine( msg.Substring(0, 1) );
        }
    }
}
