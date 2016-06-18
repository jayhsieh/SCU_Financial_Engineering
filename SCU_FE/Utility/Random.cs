using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Utility
{
    /// <summary>
    /// http://www.iro.umontreal.ca/~panneton/WELLRNG.html
    /// </summary>
    public class RandomWELL {
        private const int N = 16;
        private const uint M0 = 0x3F800000U;
        private const uint M1 = 0x007FFFFFU;
        private uint seed_ = 12345678;
        private int index_ = 0;
        private uint[] state_ = new uint[N] {   
            12345678, 277759943, 96845755, 1019000778, 861248694, 580794835, 399519109, 312451493,
            476862699, 301038016, 229543161, 1467734034, 307044411, 318946322, 857734790, 336374701};
        private byte[] bytes_ = new byte[4];
        /// <summary>
        /// generating a random seed
        /// </summary>
        /// <returns></returns>
        public int srand() {
            return (int)seed_;
        }
        /// <summary>
        /// given an initial random seed
        /// </summary>
        /// <param name="seed"></param>
        public void srand(int seed) {
            index_ = 0;
            seed_ = (uint)(seed & 0x7FFFFFFF);
            state_[0] = seed_;
            for (uint i = 1; i < N; ++i) {
                state_[i] = (1812433253 * (state_[i - 1] ^ (state_[i - 1] >> 30)) + i);
                state_[i] &= 0x7FFFFFFF;
            }
        }
        /// <summary>
        /// Upper closed 1 and lower opened 0 interval
        /// </summary>
        /// <returns>(0.0 1.0]</returns>
        public double frand() {
            uint t = rand_();
            t = M0 | (t & M1);
            bytes_[0] = (byte)((t >> 0) & 0xFF);
            bytes_[1] = (byte)((t >> 8) & 0xFF);
            bytes_[2] = (byte)((t >> 16) & 0xFF);
            bytes_[3] = (byte)((t >> 24) & 0xFF);
            return System.BitConverter.ToSingle(bytes_, 0) - 0.999999881f;
        }
        /// <summary>
        /// Upper opened 1 and lower closed 0 interval
        /// </summary>
        /// <returns>[0.0 1.0)</returns>
        public double frand2() {
            uint t = rand_();
            t = M0 | (t & M1);
            bytes_[0] = (byte)((t >> 0) & 0xFF);
            bytes_[1] = (byte)((t >> 8) & 0xFF);
            bytes_[2] = (byte)((t >> 16) & 0xFF);
            bytes_[3] = (byte)((t >> 24) & 0xFF);
            return System.BitConverter.ToSingle(bytes_, 0) - 1.0f;
        }
        /// <summary>
        /// 
        /// </summary>
        /// <returns></returns>
        public int rand() {
            return (int)(rand_() & 0x7FFFFFFF);
        }
        private uint rand_() {
            uint a, b, c, d;

            a = state_[index_];
            c = state_[(index_ + 13) & 15];
            b = a ^ c ^ (a << 16) ^ (c << 15);
            c = state_[(index_ + 9) & 15];
            c ^= c >> 11;
            a = state_[index_] = b ^ c;
            d = a ^ ((a << 5) & 0xDA442D24U);
            index_ = (index_ + 15) & 15;
            a = state_[index_];
            state_[index_] = a ^ b ^ d ^ (a << 2) ^ (b << 18) ^ (c << 28);
            return state_[index_];
        }
        /// <summary>
        /// uniform random generator 
        /// </summary>
        /// <param name="min">lower bound</param>
        /// <param name="max">upper bound</param>
        /// <returns></returns>
        public double Range(double min, double max) {
            return (min - max) * frand() + min;
        }
        /// <summary>
        /// uniform random generator 
        /// </summary>
        /// <param name="min">lower bound</param>
        /// <param name="max">upper bound</param>
        /// <returns></returns>
        public int Range(int min, int max) {
            return (int)((min - max) * frand2() + min);
        }
    }
    /// <summary>
    /// 
    /// </summary>
    public class Normal01{
        /// <summary>
        /// Marsaglia polar method
        /// </summary>
        /// <returns>Normal random generator</returns>
        public double NextGaussianDouble() {  
            double u, v, S;
            Random rnd = new Random(Guid.NewGuid().GetHashCode());
            do {
                u = 2.0 * rnd.NextDouble() - 1.0;
                v = 2.0 * rnd.NextDouble() - 1.0;
                S = u * u + v * v;
            }
            while (S >= 1.0 || S==0);
            
            double fac = Math.Sqrt(-2.0 * Math.Log(S) / S);
            return u * fac;
        }
        /// <summary>
        /// Box-Muller transform
        /// </summary> https://en.wikipedia.org/wiki/Box%E2%80%93Muller_transform
        /// <returns>Normal random generator</returns>
        public double NextGaussianDouble_Box_Muller() {
            const double Pi = 3.1415926;
            double u1, u2, R, theta, x1, x2;
            Random rnd = new Random(Guid.NewGuid().GetHashCode());
            u1 = rnd.NextDouble();
            u2 = rnd.NextDouble();
            R = Math.Sqrt(-2 * Math.Log(u1));
            theta = 2 * Pi * u2;
            x1 = R * Math.Cos(theta);
            x2 = R * Math.Sin(theta);

            return x1;
        }
    }
}
