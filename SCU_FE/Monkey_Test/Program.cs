using Utility;
using System.IO;
using System;
using Simulation;
namespace Monkey_Test {
    class Program {
        static void Main(string[] args) {
            RandomWELL rnd = new RandomWELL();
            Normal01 n01 = new Normal01();
            Random qqq = new Random();
            FileStream rndWELL = new FileStream("random_WELL.txt", System.IO.FileMode.OpenOrCreate);
            StreamWriter bw = new StreamWriter(rndWELL);
            
            for (int i = 0; i < 256 * 256; i++) {
                bw.WriteLine(n01.NextGaussianDouble_Box_Muller());
                //Console.WriteLine(rnd.frand2());
            }
            bw.Flush();
            bw.Close();
        }

        static void Main_111(string[] args) {
            Heston hh = new Heston();
            hh.HestonMC(100, 100, 0, 1, 0, 2, 0.01, 0, 0.1, 0.01, 5000);   
        }
    }
}
