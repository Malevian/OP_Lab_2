using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lab_3_cs
{
    class Program
    {
        static void Main(string[] args)
        {
            otherThings function = new otherThings();
            int amount = 0;
            Console.WriteLine("Press Ctrl+S+Enter to stop writing text");
            text_abstraction[] Text;

            Text = function.MoreText(ref amount);
            Console.WriteLine("\nThe texts:\n");
            function.output(Text);

            Console.WriteLine("\nWrite more text:");
            function.ExtendTheText(Text);

            Console.WriteLine("\nExtended texts:\n");
            function.output(Text);

            text_abstraction VowelsGod = function.TextWithTheLargestAmountOfVowels(Text);
            VowelsGod.outText();

            Console.ReadLine();
        }
    }
}
