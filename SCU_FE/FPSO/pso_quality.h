/*******************************************************************/
/*     filename : pso_quality.h                                    */
/*     date     : 2012.10.03                                       */
/*******************************************************************/

#ifndef PSO_QUALITY_H
#define PSO_QUALITY_H
/////////////////////////////////////////////////////////////////////
double   fitness(double *x, int dim) ; /* 適應函式                 */

double** Allocate2Dim(int m, int n);   /* 配置double arr[m][n]     */
void     Release2Dim(double** ptr);    /* 釋放二維記憶體           */
double*  Allocate1Dim(int x);          /* 配置double arr[x]        */
void     Release1Dim(double* ptr);     /* 釋放一維記憶體           */

void   SetParam(                       /* 設置PSO 參數,配置記憶體  */
                 double w,             /* 自身權重參數w            */
                 double c1,            /* 經驗常數c1               */
                 double c2,            /* 整體經驗常數c2           */
                 unsigned dim,         /* 解空間之維度             */   
                 unsigned particle_cnt /* 粒子個數                 */
               );

void   SetSolRange(                    /* 設定解空間限制           */
                    double* min_pos,   /* 解空間最小限制           */
                    double* max_pos,   /* 解空間最大限制           */
                    double* max_v      /* 粒子移動最大速度限制     */
                  );

void ParticleInit();                   /* 粒子群初始化             */
void ParticleSwarm();                  /* 各粒子開始移動           */
void ParticleDisplay();                /* 顯示粒子詳細資訊         */

void GetOptimzation(                   /* 取得最優解               */
                     double* x,        /* 最優之解                 */
                     double* fitv      /* 最優解之適應值           */
					);            

void ParticleRelease();                /* 粒子釋放記憶體           */ 
/////////////////////////////////////////////////////////////////////
#endif
