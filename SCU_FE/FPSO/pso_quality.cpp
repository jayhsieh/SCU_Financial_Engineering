/*******************************************************************/
/*     filename : pso_quality.cpp                                  */
/*     date     : 2012.10.03									   */
/*******************************************************************/
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>
#include "pso_quality.h"

//////////////////////////////////////////////////////////////////////////
//  macro 設定
/* 產生[0,1] 亂數*/
// #define RND() ((double) ((rand()<<15)|rand() )/( (RAND_MAX << 15) | RAND_MAX)) 
#define RND() ((double)rand()/RAND_MAX )
/* 產生[low,up] 亂數*/
#define random(low, up) ( ((up)-(low)) * RND()  + (low) )
/* 產生[-1,1] 亂數*/
#define RND1() (random(-1.0, 1.0)) 
//////////////////////////////////////////////////////////////////////////
// 靜態變數

static double w;
static double c1;
static double c2;

static unsigned  pcnt;         /* 粒子群個數                       */
static unsigned  dim;          /* 解空間維度                       */

static double **particle_pos;  /* 各粒子目前位置[pcnt][dim]         */
static double **particle_v;    /* 各粒子目前速度[pcnt][dim]         */
static double  *particle_fv;   /* 各粒子目前適應值[pcnt]            */
static double **pbest_pos;     /* 各粒子目前找到最佳位置[pcnt][dim] */
static double  *pbest_fv ;     /* 各粒子目前最佳適應值[pcnt]        */

static double  *gbest_pos;     /* 全域目前找到最佳位置[dim]         */
static double   gbest_fv;      /* 全域目前最佳適應值               */
static double *max_pos;        /* 各維度之最大值[dim]               */
static double *min_pos;        /* 各維度之最小值[dim]               */
static double *max_v  ;        /* 各維度最大速度限制[dim]           */

void ParticleDisplay()
{
     int i, j;
     for(i=0; i!=pcnt; ++i){
           for(j=0; j!=dim; ++j)
                printf("%+6.3lf(%+6.3lf) ", particle_pos[i][j],  particle_v[i][j]);
           printf("[%+10.5lf]\n",particle_fv[i]);
     }
}

//////////////////////////////////////////////////////////////////////////
// ------------------------------------------------------------------
// ******************************************************************
// 適應函式, De Jong, Goldberg
double fitness(double *x, int dim)
{
     int i;
     double SinMult=1.0, mult=1.0;

     for(i=0; i!=dim; ++i)
	 {
           mult*=x[i];
           SinMult*=sin(x[i]);
     }
     return sqrt(fabs(mult))*SinMult;
	 
}
// ******************************************************************
// ------------------------------------------------------------------
// 配置二維記憶體double arr[m][n]
double** Allocate2Dim(int m, int n)
{
     int i;
     double *trunk = (double*)malloc(sizeof(double)*m*n);
     double **p = (double**)malloc(sizeof(double*)*m);
     for(i=0; i<m; ++i){
           p[i]= trunk;
           trunk+=n;
     }
     return p;
}
// ------------------------------------------------------------------
// 釋放二維記憶體
void Release2Dim(double **ptr)
{
     free(*ptr), free(ptr);
}

// ------------------------------------------------------------------
// 配置一維記憶體double arr[x]
double*  Allocate1Dim(int x)
{
     return (double*)malloc(sizeof(double)*x);
}
// ------------------------------------------------------------------
// 配置一維記憶體
void Release1Dim(double* ptr)
{
     free(ptr);
}
// ------------------------------------------------------------------
// 設置pso 相關參數
void   SetParam( double _w,             /* 自身權重參數w         */
                 double _c1,            /* 經驗常數c1            */
                 double _c2,            /* 整體經驗常數c2        */
                 unsigned _dim,         /* 解空間之維度          */   
                 unsigned _particle_cnt /* 粒子個數              */
               )
{
     w=_w, c1=_c1, c2=_c2;
     dim=_dim, pcnt=_particle_cnt;

     // 配置相關記憶體空間
     particle_pos = Allocate2Dim(pcnt, dim); /* 各粒子目前位置        */
     particle_v   = Allocate2Dim(pcnt, dim); /* 各粒子目前速度        */
     particle_fv  = Allocate1Dim(pcnt);      /* 各粒子目前適應值      */
     pbest_pos    = Allocate2Dim(pcnt, dim); /* 各粒子目前找到最佳位置*/
     pbest_fv     = Allocate1Dim(pcnt);      /* 各粒子目前最佳適應值  */
     gbest_pos    = Allocate1Dim(dim);       /* 全域目前找到最佳位置  */
     max_pos      = Allocate1Dim(dim);       /* 各維度之最大值        */
     min_pos      = Allocate1Dim(dim);       /* 各維度之最小值        */
     max_v        = Allocate1Dim(dim);       /* 各維度最大速度限制    */
}

// ------------------------------------------------------------------
// 設置pso 解空間相關參數
void   SetSolRange(						/* 設定解空間限制        */
                    double* _min_pos,   /* 解空間最小限制        */
                    double* _max_pos,   /* 解空間最大限制        */
                    double* _max_v      /* 粒子移動最大速度限制  */
                  )
{
     memcpy( (void*)min_pos, (void*)_min_pos, dim*sizeof(double));
     memcpy( (void*)max_pos, (void*)_max_pos, dim*sizeof(double));
     memcpy( (void*)max_v  , (void*)_max_v  , dim*sizeof(double));
}
// ------------------------------------------------------------------
// 粒子群初始化
void ParticleInit()
{
     int i, j;

     srand((unsigned)time(NULL));
     for(i=0; i!=pcnt; ++i){
           for(j=0; j!=dim; ++j){
                /* 隨機產生各粒子位置*/
                particle_pos[i][j] = random(min_pos[j], max_pos[j]);
                /* 隨機產生各粒子速度*/
                particle_v[i][j]   = random(0.0, max_v[j]);
           }
           /* 計算各粒子適應值*/
           pbest_fv[i]=particle_fv[i] = fitness(particle_pos[i], dim);

           /* 更新全域最佳解*/
           if(i==0 || pbest_fv[i] > gbest_fv) {
                memcpy((void*)gbest_pos, (void*)pbest_pos[i], sizeof(double)*dim);
                gbest_fv = pbest_fv[i];
           }          
     }
}
// ------------------------------------------------------------------
// 各粒子開始移動
void ParticleSwarm()
{
     int i, j;
     double tmp;
     
     for(i=0; i!=pcnt; ++i){
           for(j=0; j!=dim; ++j){
                /* 更新各粒子速度*/
                particle_v[i][j] = \
                     w * particle_v[i][j] + \
                     c1 * RND1() * (pbest_pos[i][j]-particle_pos[i][j]) + \
                     c2 * RND1() * (gbest_pos[j]   -particle_pos[i][j]) ;

                /* 判斷速度是否超過上下界*/
                if(particle_v[i][j] > max_v[j]  ||
                     particle_v[i][j] < -max_v[j]) /* 重新產生一速度*/
                     particle_v[i][j] = random(0.0, max_v[j]);

                /* 更新各粒子位置*/
                particle_pos[i][j] += particle_v[i][j];

                /* 超過上下界，重新產生一新位置*/
                if(particle_pos[i][j] > max_pos[j] ||
                     particle_pos[i][j] < min_pos[j]
                     )
                     particle_pos[i][j] = random(min_pos[j], max_pos[j]);
           }
         /* 更新各粒子適應值*/
           tmp = particle_fv[i] = fitness(particle_pos[i], dim);
           /* 更新各粒子最佳適應值*/
           if(tmp > pbest_fv[i]) {
                pbest_fv[i] = tmp;
                memcpy((void*)pbest_pos[i], (void*)particle_pos[i], sizeof(double)*dim);
           }
           /* 更新全域最佳適應值 */
           if(tmp > gbest_fv) {
                gbest_fv = tmp;
                memcpy((void*)gbest_pos, (void*)particle_pos[i], sizeof(double)*dim);
           }
     }
}

// ------------------------------------------------------------------
// 取得最優解
void GetOptimzation(double *x, double *fitv)
{
     memcpy((void*)x, (void*)gbest_pos, sizeof(double)*dim);
     *fitv = gbest_fv;
}
// ------------------------------------------------------------------
// 粒子釋放記憶體
void ParticleRelease()
{
     Release2Dim(particle_pos);
     Release2Dim(particle_v);
     Release1Dim(particle_fv);
     Release2Dim(pbest_pos);
     Release1Dim(pbest_fv);
     Release1Dim(gbest_pos);
     Release1Dim(max_pos);
     Release1Dim(min_pos);
}                    
//////////////////////////////////////////////////////////////////////////
