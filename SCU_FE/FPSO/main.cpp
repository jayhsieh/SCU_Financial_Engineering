/*******************************************************************/
/*     filename : Fixed Paticle Swarm Optimization (FPSO)          */
/*     date     : 2012.10.03                                       */
/*******************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "pso_quality.h"

#define W        0.9		/* 自身權重參數	*/
#define C1       2.0		/* 經驗常數     */
#define C2       2.0		/* 整體經驗常數 */
#define DIM      2          /* 維度			*/
#define PCNT     30         /* 粒子數		*/
#define ITERATOR 10000      /* 迭代次數		*/

void main(void)
{
	unsigned i = ITERATOR;
    double  best_fv;                        /* 最佳適應值*/		//Max or Min 目標函數值
    double  *min_pos = Allocate1Dim(DIM);  	/* 維度最小值*/		//配置一維記憶體double arr[x]
    double  *max_pos = Allocate1Dim(DIM);  	/* 維度最大值*/		//配置一維記憶體double arr[x]
    double  *best_pos = Allocate1Dim(DIM);  /* 維度最佳值*/		//配置一維記憶體double arr[x]
    double  *max_v = Allocate1Dim(DIM);  	/* 速度限制  */		//配置一維記憶體double arr[x]
	clock_t t1, t2;
	t1 = clock();							//計時開始
	
// ----------------------------------------------------
    // 設定參數
    min_pos[0]=0.0   , max_pos[0]=10.0;
    min_pos[1]=0.0   , max_pos[1]=10.0;

    max_v[0] = 0.0006 * ( max_pos[0] - min_pos[0] );
    max_v[1] = 0.0006 * ( max_pos[1] - min_pos[1] );     

    SetParam(W, C1, C2, DIM, PCNT);			// 設置pso 相關參數
    SetSolRange(min_pos, max_pos, max_v);	// 設置pso 解空間相關參數
     
    //----------------------------------------------------
    //開始進行pso algorithm
     
    ParticleInit();                       	/* 初始化設定      */	// 粒子群初始化
    while(i--)                            	/* 開始進行迭代    */
		ParticleSwarm();                	/* 粒子移動與更新  */	// 各粒子開始移動
    GetOptimzation(best_pos, &best_fv);   	/* 取得最佳值      */	// 取得最優解

		for(i=0; i!=DIM; ++i)
			printf("#x%u = %10.7lf\n", i+1, best_pos[i]);

    printf("find best fitness : %.16e\n", best_fv);

	t2 = clock();							//計時結束
    printf("--- Total CPU time = %lf ---\n", (t2-t1)/(double)(CLOCKS_PER_SEC));
	system("pause");
    //----------------------------------------------------
    //最後釋放記憶體
    ParticleRelease();
    Release1Dim(min_pos);
    Release1Dim(max_pos);
    Release1Dim(best_pos);
}
